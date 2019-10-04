import socket
import cx_Oracle as cx
def main():
    TCP_IP = '192.168.43.177'
    TCP_PORT = 5006
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(2)
    conn, addr = s.accept()
    data = ""
    data = conn.recv(BUFFER_SIZE)
    a = str(data.decode())
    #print(a)
    con = cx.connect('MN7', 'MN7', 'MN7')
    cursor_s_user_info = con.cursor()
    stmt2 = "UPDATE s_user_info SET status='yes' where user_name= :u"
    cursor_s_user_info.execute(stmt2, {'u':a})
    con.commit()
    conn.close()

while 1:
    main()