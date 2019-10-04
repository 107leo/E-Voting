import socket
import threading
import node_server
import cx_Oracle as cx
import time
con = cx.connect('kp', 'kp', 'ORCL')
cursor_c_party_info = con.cursor()

ENCODING = 'utf-8'
my_vote=""

def setglobal(c):
    counter=c
    return counter

class Receiver(threading.Thread):

    def __init__(self, my_host, my_port):
        threading.Thread.__init__(self, name="messenger_receiver")
        self.host = my_host
        self.port = my_port



    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock.bind((self.host, self.port))
        sock.listen(10)
        #rncounter = 0
        #print("above while")
        while True :
                #if counter==1:
            #print("fdsvdsvdsvdsvfsvsv")
            connection, client_address = sock.accept()
            try:
                    full_message = ""
                    while True :

                            print("fsdds")
                            data = connection.recv(16)
                            full_message = full_message + data.decode(ENCODING)
                            if not data :
                                #if self.active==True:
                                    #print("counter " ,counter)

                                    #print(full_message.strip() , len(full_message))

                                    L=full_message.split(":")
                                    op=str(L[0])
                                    #print(op)
                                    #addToDB(op)

                                    node_server.blockchain.add(node_server.Block(op.strip()))

                                    stmt2 = "UPDATE c_party_info SET votes = (votes+1) where party_name = :n"
                                    cursor_c_party_info.execute(stmt2, {'n': op})
                                    con.commit()
                                    break
                                    #self.active=False
                                    #StoppableThread.stop()


                                    #counter+=1
                                    #keepRunning=False
                                    #self.daemon=True
                                #else:
                                 #   pass
                                    #break
                                #else:
                                 #   self.__Thread__stop()
                         #   counter+=1
                    #counter += 1
            finally:
                    #counter+=1
                    connection.shutdown(2)
                    connection.close()
            #else:
             #   counter+=1
        #print("mbnm")


    def run(self):

        self.listen()






class Sender(threading.Thread):

    def __init__(self, server_host,user_name, server_port,  local_host, local_port):
        threading.Thread.__init__(self, name="messenger_sender")
        self.host = server_host
        self.port = server_port
        self.user_name = user_name

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        s.sendall("connect_request|{}|{}|{}".format(user_name,local_host, local_port).encode(ENCODING))
        s.shutdown(2)
        s.close()

    def run(self):
        #counter=0
        #while counter==0:

            #message = input("Enter the name of the party")
            #mess="fvfdgfddf"
            #node_server.blockchain.mine(node_server.Block(message))
            #print("jnsdcndsc")
            node_server.blockchain.add(node_server.Block(my_vote))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            s.sendall("from:{}|{}".format(self.user_name,my_vote).encode(ENCODING))
            s.shutdown(1)
            s.close()
            #counter+=1
            #while node_server.blockchain.head!=None:
             #   print(node_server.blockchain.head)
              #  node_server.blockchain.head=node_server.blockchain.head.next


def mmain():
    #my_host = input("host: ")
    #my_port = int(input("port: "))
    my_port = 5551
    my_host = "192.168.43.224"
    #my_port = 5556
    receiver = Receiver(my_host, my_port)
    #server_host = input("server host: ")
    #server_port = int(input("server port: "))

    server_host = "192.168.1.209"
    server_port = 5555

    user_name = " "
#password=input("Enter your password: ")
#party=input("Enter the name of the party :")
    #myvote=input("enter the name of the party")
    sender = Sender(server_host, server_port, user_name, my_host, my_port)
#treads = [receiver.start(), sender.start()]


#if __name__ == '__main__':
 #   main()