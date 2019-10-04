import socket
#import gui.py

def validate(username , password):

    TCP_IP = '192.168.43.177'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    data=" "
#hand= open("demo.csv")
#hand=input("sf")
#print(hand)
#while data!="bye":
#userid=input("Enter your id")
#password=input("Enter your password")


    MESSAGE =username+" "+password

    s.send(bytearray(MESSAGE.encode()))
    data = s.recv(BUFFER_SIZE).decode()

    #print ("received data:", data)
    s.close()

    return data
#u=input()
#v=input()
#print(str(validate(u,v)))