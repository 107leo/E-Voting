from tkinter import *
import time
#import LoginPage
import VotingPage
import SignupPage
import messenger_client
import vclient
from tkinter import messagebox
import cx_Oracle as cx
import a_server

#import socket
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.bind((my_host, my_port))
    #sock.listen(10)
my_port = 5552
my_host = "192.168.43.83"
active=True
m=0

    # my_port = 5556
receiver = messenger_client.Receiver(my_host, my_port)
#receiver.daemon=False
#receiver.start()
#receiver.do_run=
con = cx.connect('kp', 'kp', 'ORCL')
cursor_c_party_info = con.cursor()

#stmt1 = "create table c_party_info (party_id number(3), party_name varchar(20),votes number(10))"
#cursor_c_party_info.execute(stmt1)
#con.commit()
def main():


    # server_host = input("server host: ")
    # server_port = int(input("server port: "))

    server_host = "192.168.43.177"
    server_port = 5555
    final_vote=""


    def log():
        root.destroy()
        #LoginPage.main()

        root1 = Tk()
        root1.title("Login")
        root1.geometry("1600x8000")

        '''Tops = Frame(root1, width=1600, relief=SUNKEN)
        Tops.grid()

        f1 = Frame(root1, width=800, height=700, relief=SUNKEN)
        f1.grid()'''

        def VPage():
            user = e.get()
            pas = f.get()
            #print(user, pas)

            if vclient.validate(user, pas) == "yes":
                root1.destroy()
                #a_server.getuser(user)
                #VotingPage.main()
                def sel1():
                    def home():
                        root3.destroy()
                        main()

                    a_server.getuser(user)
                    root2.destroy()
                    root3 = Tk()
                    root3.title("SUBMIT")
                    root3.config(background='purple4')
                    root3.geometry("1600x8000")

                    # print(var.get(),"sfvfsvfv")
                    selection = "You Have Voted For " + var.get()
                    messenger_client.my_vote =var.get()
                    usernam= str(var.get())
                    label3 = Label(root3, bg='purple4', font=('arial', 16, 'bold'))

                    label3.config(text=selection, bg='purple4')
                    label3.pack()

                    label4 = Label(root3, bg='purple4', font=('arial', 16, 'bold'), text="Thanks for Voting ")
                    label4.pack()

                    homebutton = Button(root3, text="Go To Home Page", activebackground="LightBlue", relief="raised",
                                        font=('arial', 16, 'bold'), bd=10, bg="MediumPurple1",command=home)
                    homebutton.pack(side=LEFT)
                    #receiver.start()
                    sender = messenger_client.Sender(server_host, usernam, server_port, my_host, my_port)
                    sender.start()
                    #sender.keepRunning= False
                    #messenger_client.Sender.run()



                    stmt2 ="UPDATE c_party_info SET votes = (votes+1) where party_name = :n"
                    cursor_c_party_info.execute(stmt2,{'n':usernam})
                    con.commit()

                    #confirmbutton = Button(root2, text="Confirm", activebackground="LightBlue", relief="raised",
                     #                        font=('arial', 16, 'bold'), bd=10, bg="MediumPurple1")
                    #confirmbutton.pack(side=LEFT)


                root2 = Tk()
                root2.title("VOTING")
                root2.config(background='purple4')
                root2.geometry("1600x8000")
                var = StringVar()

                r1 = Radiobutton(root2, text="Bhartiya Janta Party ", font=('arial', 20, 'bold'), variable=var,
                                 value="BJP", bg='purple4', command=sel1)
                r1.place(x=500,y=200)

                r2 = Radiobutton(root2, text="Aam Aadmi Party", font=('arial', 20, 'bold'), variable=var, value="AAP",
                                 bg='purple4', command=sel1)
                r2.place(x=500,y=300)

                r3 = Radiobutton(root2, text="Congress", font=('arial', 20, 'bold'), variable=var, value="CONGRESS",
                                 bg='purple4', command=sel1)
                r3.place(x=500,y=400)

                r4 = Radiobutton(root2, text="Shivsena", font=('arial', 20, 'bold'), variable=var, value="SHIVSENA",
                                 bg='purple4', command=sel1)
                r4.place(x=500,y=500)

                r5 = Radiobutton(root2, text="MNS", font=('arial', 20, 'bold'), variable=var, value="MNS", bg='purple4',
                                 command=sel1)
                r5.place(x=500,y=600)

                root2.mainloop()

            else:
                messagebox.showinfo("ERROR", "Either username or password is invalid. Please try again.")

        # ****************************      LOGIN PAGE       *******************************

        label1 = Label(root1, text="LOGIN", bd='8', font=('helvetica', 50, 'bold'))
        label1.place(x=580,y=0)

        a = Label(root1, font=('arial', 16, 'bold'), text="USERNAME", bd='8')
        a.place(x=500,y=100)

        b = Label(root1, font=('arial', 16, 'bold'), text="PASSWORD", bd='8')
        b.place(x=500,y=150)

        username = StringVar()
        password = StringVar()

        e = Entry(root1, font=('arial', 16, 'bold'), textvariable=username, insertwidth=6, bg="MediumPurple1", bd=10)
        e.place(x=650,y=100)

        f = Entry(root1, font=('arial', 16, 'bold'), show="*", textvariable=password, insertwidth=4, bg="MediumPurple1",
                  bd=10)
        f.place(x=650,y=150)

        LoginButton = Button(root1, font=('arial', 16, 'bold'), text="Login", activebackground="LightBlue",
                             relief="raised", command=VPage, bd=10, bg="MediumPurple1")
        LoginButton.place(x=600,y=250)

        root.mainloop()

    def sign():
        root.destroy()
        SignupPage.main()

    def dispresult():
        time.sleep(1)
        root.destroy()
        time.sleep(1)
        L=[]
        tempp=""
        stm="select votes from c_party_info "
        data=cursor_c_party_info.execute(stm)
        for i in data:
            te=str(i)
            ss=""
            for k in te:
                if k!="(" and k!=")" and k!="," and k!=" ":
                    ss=ss+k
            L.append(int(ss))
        #print(L)



        root5 = Tk()
        root5.title("RESULT")
        root5.geometry("1600x8000")
        Tops = Frame(root5, width=1600, relief=SUNKEN)
        Tops.grid()

        f1 = Frame(root5, width=800, height=700, relief=SUNKEN)
        f1.grid()
        label1 = Label(Tops, text="RESULTS", bd='8', font=('helvetica', 50, 'bold'))
        label1.grid(row=0, column=0)

        a = Label(f1, font=('arial', 16, 'bold'), text="BJP    "+str(L[0]), bd='8')
        a.grid(row=5, column=10, sticky=E)

        b = Label(f1, font=('arial', 16, 'bold'), text="CONGRESS    "+str(L[1]), bd='8')
        b.grid(row=6, column=10, sticky=E)

        c = Label(f1, font=('arial', 16, 'bold'), text="AAP    "+str(L[2]), bd='8')
        c.grid(row=7, column=10, sticky=E)

        d = Label(f1, font=('arial', 16, 'bold'), text="SHIVSENA    "+str(L[3]), bd='8')
        d.grid(row=9, column=10, sticky=E)

        e= Label(f1, font=('arial', 16, 'bold'), text="MNS    "+str(L[4]), bd='8')
        e.grid(row=10, column=10, sticky=E)






    root = Tk()
    root.title("E-Voting")

    root.geometry("1600x8000")

    label1 = Label(root, text="E-VOTING", bd='8', font=('helvetica', 50, 'bold'))
    label1.place(x=500,y=0)

    loginbutton = Button(root, font=('arial', 16, 'bold'), text="Login", activebackground="LightBlue",
                         relief="raised", command=log, bd=10, bg="MediumPurple1")
    loginbutton.place(x=600,y=200)

    resultbutton = Button(root, font=('arial', 16, 'bold'),text="Result",command=dispresult, activebackground="LightBlue", relief="raised", bd=10, bg="MediumPurple1")
    resultbutton.place(x=600,y=300)

    root.mainloop()

if __name__ == '__main__':
    main()