import socket
import time
import cx_Oracle as cx
cnt=0
con = cx.connect('kp', 'kp', 'ORCL')
cursor_c_party_info = con.cursor()

while True:
    TCP_IP = '192.168.43.177'
    TCP_PORT = 5009
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


    #MESSAGE =username+" "+password
    MESSAGE="send data"
    s.send(bytearray(MESSAGE.encode()))
    #time.sleep(10)

    data = s.recv(BUFFER_SIZE).decode()

    dataa=str(data).split(",")
    t=dataa[0]
    u=dataa[4]
    v1=int(t[1:])
    v2=int(dataa[1])
    v3=int(dataa[2])
    v4=int(dataa[3])
    v5=int(u[:-1])
    #print(v1,v2,v3,v4,v5)
    #print ("received data:", data)
    s.close()
    cnt+=1
    print(cnt)
    stmt1="UPDATE c_party_info set votes =:m where PARTY_ID =1"
    cursor_c_party_info.execute(stmt1, {'m': v1})
    con.commit()

    stmt2 = "UPDATE c_party_info set votes =:m where PARTY_ID =2"
    cursor_c_party_info.execute(stmt2, {'m': v2})
    con.commit()

    stmt3 = "UPDATE c_party_info set votes =:m where PARTY_ID =3"
    cursor_c_party_info.execute(stmt3, {'m': v3})
    con.commit()

    stmt4 = "UPDATE c_party_info set votes =:m where PARTY_ID =4"
    cursor_c_party_info.execute(stmt4, {'m': v4})
    con.commit()

    stmt5 = "UPDATE c_party_info set votes =:m where PARTY_ID =5"
    cursor_c_party_info.execute(stmt5, {'m': v5})
    con.commit()

    time.sleep(6)