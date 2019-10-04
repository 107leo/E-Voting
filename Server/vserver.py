import socket
import time
import cx_Oracle as cx
ff=""
curr_time=time.ctime()
curr_hour=int(curr_time[14:16])
#print(curr_time[10:19],curr_hour)
#print(curr_hour+5)
def se():
    TCP_IP = '192.168.43.177'
    TCP_PORT = 5005
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(2)
    conn, addr = s.accept()
    #print ('Connection address:', addr)
    data=""
    data = conn.recv(BUFFER_SIZE)
    a=str(data.decode())
    l=a.split(" ")
    ff=l[0]
    dd=l[1]

    #print(a,l)
    #def validate(username,password):
    con = cx.connect('MN7', 'MN7', 'MN7')
    cursor_s_user_info=con.cursor()
    cursor_s_user_info.execute("select count(*) from s_user_info where "
                                   "(user_name =:u AND password =:p AND status = 'no')",
                                   {'u': ff, 'p': dd})

    cnt = (cursor_s_user_info.fetchone())
    count=int(cnt[0])
    #print(ff,dd,count)
    curr_time1 = time.ctime()
    curr_hour1 = int(curr_time[14:16])
    #if count == 1:

            #return 2
        #else
            #return 0






    #print(ff , len(ff) , dd , len(dd))
    #print("received data:", a)
   # if curr_hour1<curr_hour:
    if count==1:

            msg="yes".encode()
            conn.send(bytearray(msg))  # echo
            conn.close()
    else:
            msg="no".encode()
            conn.send(bytearray(msg))
            conn.close()


while 1:
    se()