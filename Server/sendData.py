import socket
import time
import cx_Oracle as cx
cnt=0
while True:
    TCP_IP = '192.168.43.177'
    TCP_PORT = 5009
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(2)
    conn, addr = s.accept()
    print ('Connection address:', addr)
    #data=""
    data = conn.recv(BUFFER_SIZE)
    #a=str(data.decode())
    #l=a.split(" ")
    #ff=l[0]
    #@dd=l[1]

    #print(a,l)
    #def validate(username,password):
    con = cx.connect('MN7', 'MN7', 'MN7')
    cursor_s_user_info=con.cursor()
    cursor_s_user_info.execute("select votes from s_party_info ",)


    cnt = (cursor_s_user_info.fetchall())
    #count=int(cnt[0])
    #print(cnt)
    age=[]
    for agee in cnt:
        aa = str(agee)
        #print(aa)
        b=""
        for i in range(len(aa)):
            #print(aa[i])
            if aa[i]!="(" and aa[i]!=")" and aa[i]!="," and aa[i]!=" ":
                b=b+aa[i]
        #b = aa[1] + aa[2]
        #print(b)
        age.append(int(b))
    #print(age)
    p=str(age)
    count=p.encode()
    conn.send(bytearray(count))  # echo
    conn.close()

    #print(ff,dd,count)

    #if count == 1:

            #return 2
        #else
            #return 0
   # cnt += 1
    #time.sleep(2)


