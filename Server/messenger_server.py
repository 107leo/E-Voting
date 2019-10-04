import socket
import threading
import repository
#import vserver
import node_server
import cx_Oracle as cx


ENCODING = 'utf-8'


class Receiver(threading.Thread):
    def __init__(self, my_host, my_port, queue, users):
        threading.Thread.__init__(self, name="messenger_receiver")
        self.host = my_host
        self.port = my_port
        self.queue = queue
        self.users = users

    def resolve_message(self, message):
        if "connect_request" in message:
            #print("connect request received")
            arr = message.split("|")
            if len(arr) == 4:
                user_name = arr[1]
                user_host = arr[2]
                user_port = arr[3]
                #print("adding user: {}, {}, {}".format(user_name, user_host, user_port))
                self.users.add_user(user_name, user_host, user_port)

               # print("invalid connect request...")
        elif "from:" in message:
            #print("received message... starting queueing process")
            arr = message.split("|")
            if len(arr) == 2:
                sender_name = arr[0].replace("from:", "")
                #print("adding message from {} to queue".format(sender_name))
                message_text = arr[1]
                self.queue.add_message(sender_name, message_text)

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,  1)
        sock.bind((self.host, self.port))
        sock.listen(2)
        party_name=""
        counter = 0
        while True:

            connection, client_address = sock.accept()
           # print("connection received from {}".format(str(client_address)))
            try:
                full_message = ""
                while True:
                    data = connection.recv(16)
                    full_message = full_message + data.decode(ENCODING)
                      #  full_message=str(data.decode(ENCODING))

                    if not data:
                        #print("received message: [{}]".format(full_message))
                        self.resolve_message(full_message.strip())
                        L=full_message.split("|")
                        party_name = str(L[1])
                        print(party_name)
                        break

            finally:

                #print("exchange finished. closing connection")

                if counter==1:
                    con = cx.connect('MN7', 'MN7', 'MN7')
                    cursor_s_user_info = con.cursor()

                    stmt = "UPDATE s_party_info SET votes = (votes + 1) WHERE party_name= :n"

                    cursor_s_user_info.execute(stmt, {'n': party_name})
                    #cursor_s_user_info.execute(stmt2,{'u':repository.getUsername()})
                    con.commit()
                    node_server.blockchain.add(node_server.Block(party_name))

                    counter =0
                else:
                    counter += 1
                connection.shutdown(2)
                connection.close()




class Sender(threading.Thread):

    def __init__(self, queue, users):
        threading.Thread.__init__(self, name="messenger_sender")
        self.queue = queue
        self.users = users

    def send(self, message, host, port):
        #print("sending message {} to {}".format(message, str((host, port))))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            s.sendall(message.encode(ENCODING))
        finally:
            #print("message has been sent. closing connection")
            s.shutdown(2)
            s.close()

    def run(self):
        while True:
            if self.queue.messages_waiting():
                #print("there are messages on queue. popping one")
                message = self.queue.pop_message()
                users = self.users.all_users()
                for user in users:
                    if user.get("name") != message.get("sender"):
                        self.send("{}: {}".format(message.get("sender"), message.get("message")), user.get("host"), user.get("port"))


def main():
    queue = repository.Queue()
    users = repository.Users()
    #host = input("host: ")
    #port = int(input("port: "))
    host = "192.168.43.177"
    port = 5555
    receiver = Receiver(host, port, queue, users)
    sender = Sender(queue, users)
    #threads = [receiver.start(), sender.start()]
    receiver.start()
    sender.start()

if __name__ == '__main__':
    main()