from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox
import re
import cx_Oracle as cx
import matplotlib.pyplot as py
import numpy as np

con = cx.connect('MN7','MN7','MN7')
cursor_s_user_info = con.cursor()

root = Tk()
root.title("SERVER DATA")
root.geometry("1600x8000")
root.config(background='black')

def main():
    def result():
        root2 = Tk()
        root2.title("RESULTS")
        root2.geometry("1600x8000")
        root2.config(background='gainsboro')

    def analysis():
        def age():
            age2 = np.array(age)
            groups=[0,20,40,60,80,100]
            py.hist(age2 , groups , color='r',edgecolor='black')
            py.title("VOTER AGE ANAYLSIS")
            py.xlabel("AGE GROUPS")
            py.ylabel("NUMBER OF VOTERS")
            py.show()

        def gender():
            sub = py.subplot()
            barwidth = 4
            py.bar(1, malecount, align='center', edgecolor='black')
            py.bar(2, femalecount, align='center', edgecolor='black')
            py.title("VOTER GENDER ANAYLSIS")

            #sub.set_xticks(barwidth/2)
            sub.set_xticklabels(('MALE','FEMALE'))
            py.xlabel("GENDER")
            py.ylabel("TOTAL COUNT")
            py.show()

        def city_votes():

            stmt3 = "select DISTINCT count(*),city from s_user_info  group by city"
            cursor_s_user_info.execute(stmt3)
            totalList = cursor_s_user_info.fetchall()
            print(totalList)
            newTotalList = []

            for agee in totalList:
                aa = agee
                bb = ""
                for m in range(len(aa)):
                    if aa[m] != "(" and aa[m] != ")" and aa[m] != ",":
                        if isinstance(aa[m], int):
                            bb = bb + str(aa[m]) + ':'
                        else:
                            bb = bb + str(aa[m])
                newTotalList.append(bb)
                newTotalList.append(',')

            # print(newTotalList)
            new_totalstr = ''.join(newTotalList)
            # print('this is new string')
            # print(new_totalstr)

            tNewList = re.findall(r"[\w']+", new_totalstr)
            print('this is new total list')
            print(tNewList)

            totalcount = []
            totalcity = []

            for i in range(len(tNewList)):
                if (i % 2) == 0:
                    totalcount.append(int(tNewList[i]))
                else:
                    totalcity.append(tNewList[i])
            print('totalcount')
            print(totalcount)

            stmt4 = "select DISTINCT count(*),city from s_user_info where status='yes'  group by city"
            cursor_s_user_info.execute(stmt4)
            votedList = cursor_s_user_info.fetchall()
            print(votedList)
            newVotedList = []

            for agee in votedList:
                aa = agee
                bb = ""
                for m in range(len(aa)):
                    if aa[m] != "(" and aa[m] != ")" and aa[m] != ",":
                        if isinstance(aa[m], int):
                            bb = bb + str(aa[m]) + ':'
                        else:
                            bb = bb + str(aa[m])
                newVotedList.append(bb)
                newVotedList.append(',')

            # print(newFemaleList)
            new_vstr = ''.join(newVotedList)
            # print('this is new string')
            # print(new_fstr)

            vNewList = re.findall(r"[\w']+", new_vstr)
            print('this is new new voted list')
            print(vNewList)

            votedcount = []
            for i in range(9):
                votedcount.append(0)
            votedcity = []
            votedcount_count = 0

            for i in range(len(vNewList)):
                if (i % 2) == 0:
                    votedcount[votedcount_count] = (int(vNewList[i]))
                    votedcount_count += 1
                else:
                    votedcity.append(vNewList[i])
                    votedcount_count += 1
            print('femalecount')
            print(votedcount)
            # print(malecity)

            fig = py.figure()
            ax = fig.add_subplot(111)

            ## the data
            N = 9

            ## necessary variables
            ind = np.arange(N)  # the x locations for the groups
            width = 0.35  # the width of the bars

            ## the bars
            rects1 = ax.bar(ind, totalcount, width,
                            color='black',

                            error_kw=dict(elinewidth=2, ecolor='red'))

            rects2 = ax.bar(ind + width, votedcount, width,
                            color='red',

                            error_kw=dict(elinewidth=2, ecolor='black'))

            # axes and labels
            ax.set_xlim(-width, len(ind) + width)
            ax.set_ylim(0, 5)
            ax.set_ylabel('Vote Count')
            ax.set_title('Votes by City and Gender')
            xTickMarks = "CITY NAME"
            ax.set_xticks(ind + width)
            xtickNames = ax.set_xticklabels(xTickMarks)

            ## add a legend
            ax.legend((rects1[0], rects2[0]), ('Total People', 'People who voted'))

            py.show()

        def city():
            #  ******** GETTING MALE DATA  ********************

            stmt1 = "select DISTINCT count(*),city from s_user_info where gender ='male' group by city"
            cursor_s_user_info.execute(stmt1)
            maleList = cursor_s_user_info.fetchall()
            # print(maleList)
            newMaleList = []

            for agee in maleList:
                aa = agee
                bb = ""
                for m in range(len(aa)):
                    if aa[m] != "(" and aa[m] != ")" and aa[m] != ",":
                        if isinstance(aa[m], int):
                            bb = bb + str(aa[m]) + ':'
                        else:
                            bb = bb + str(aa[m])
                newMaleList.append(bb)
                newMaleList.append(',')

            # print(newMaleList)
            new_mstr = ''.join(newMaleList)
            # print('this is new string')
            # print(new_mstr)

            mNewList = re.findall(r"[\w']+", new_mstr)
            print('this is new male list')
            print(mNewList)

            malecount = []
            malecity = []

            for i in range(len(mNewList)):
                if (i % 2) == 0:
                    malecount.append(int(mNewList[i]))
                else:
                    malecity.append(mNewList[i])
            print('malecount')
            print(malecount)
            # print(malecity)

            #  ******** GETTING FEMALE DATA  ********************

            stmt2 = "select DISTINCT count(*),city from s_user_info where gender ='female' group by city"
            cursor_s_user_info.execute(stmt2)
            femaleList = cursor_s_user_info.fetchall()
            print('this is female list')
            print(femaleList)
            newFemaleList = []

            for agee in femaleList:
                aa = agee
                bb = ""
                for m in range(len(aa)):
                    if aa[m] != "(" and aa[m] != ")" and aa[m] != ",":
                        if isinstance(aa[m], int):
                            bb = bb + str(aa[m]) + ':'
                        else:
                            bb = bb + str(aa[m])
                newFemaleList.append(bb)
                newFemaleList.append(',')

            # print(newFemaleList)
            new_fstr = ''.join(newFemaleList)
            # print('this is new string')
            # print(new_fstr)

            fNewList = re.findall(r"[\w']+", new_fstr)
            print('this is new new female list')
            print(fNewList)

            femalecount = []
            femalecity = []

            for i in range(len(fNewList)):
                if (i % 2) == 0:
                    femalecount.append(int(fNewList[i]))
                else:
                    femalecity.append(fNewList[i])
            print('femalecount')
            print(femalecount)
            # print(malecity)

            fig = py.figure()
            ax = fig.add_subplot(111)


            N = 9



            ## necessary variables
            ind = np.arange(N)  # the x locations for the groups
            width = 0.35  # the width of the bars

            ## the bars
            rects1 = ax.bar(ind, malecount, width,
                            color='black',

                            error_kw=dict(elinewidth=2, ecolor='red'))

            rects2 = ax.bar(ind + width, femalecount, width,
                            color='red',

                            error_kw=dict(elinewidth=2, ecolor='black'))

            # axes and labels
            ax.set_xlim(-width, len(ind) + width)
            ax.set_ylim(0, 5)
            ax.set_ylabel('Vote Count')
            ax.set_title('Votes by City and Gender')
            xTickMarks = [malecity]
            ax.set_xticks(ind + width)
            xtickNames = ax.set_xticklabels(xTickMarks)

            ## add a legend
            ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
            py.show()


        root2 = Tk()
        root2.title("ANALYSIS")
        root2.geometry("1600x8000")

        agebutton = Button(root2, font=('arial', 16, 'bold'), text="AGE ANAYLSIS", activebackground="LightBlue",
                              relief="raised", bd=10, bg="MediumPurple1", command=age)
        agebutton.place(x=570, y=200)

        genderbutton = Button(root2, font=('arial', 16, 'bold'), text="GENDER ANALYSIS", activebackground="LightBlue",
                              relief="raised", bd=10, bg="MediumPurple1", command=gender)
        genderbutton.place(x=570, y=300)

        citybutton = Button(root2, font=('arial', 16, 'bold'), text="CITY-GENDER ANALYSIS", activebackground="LightBlue",
                              relief="raised", bd=10, bg="MediumPurple1", command=city)
        citybutton.place(x=570, y=400)

        city_votesbutton = Button(root2, font=('arial', 16, 'bold'), text="CITY-VOTES ANALYSIS", activebackground="LightBlue",
                            relief="raised", bd=10, bg="MediumPurple1", command=city_votes)
        city_votesbutton.place(x=570, y=500)

        db = cx.connect('MN7','MN7','MN7')
        cursor = db.cursor()

        age = []
        gender = []
        city = []
        status= []

        ag=cursor.execute("select age from s_user_info")
        a=cursor.fetchall()
        dum=[]
        for agee in a:
            aa=str(agee)
            b=aa[1]+aa[2]
            age.append(int(b))




        print(age)

        cursor.execute("select gender from s_user_info")
        ab = cursor.fetchall()

        dum=[]
        for agee in ab:
            aa = agee
            bb = ""
            for m in range(len(aa)):
                if aa[m] != "(" and aa[m]!=")" and aa[m]!=",":
                    bb = bb+aa[m]
            gender.append(bb)

        print(gender)

        malecount = 0
        femalecount = 0

        for i in gender:
            if i=="male":
                malecount+= 1
            else :
                femalecount += 1

        print(malecount)
        print(femalecount)


        db.close()


        #print(age)
    def signup():

        def confirm():
            username1 = userentry.get()
            print(username1)

            password1 = passentry.get()
            print(password1)

            age = ageentry.get()
            print(age)

            city = cityentry.get()
            print(city)

            gender = genderentry.get()
            print(gender)
            status="no"
            stment1="INSERT into s_user_info values(:a,:b,:x,:c,:d,:e)"
            cursor_s_user_info.execute(stment1, {'a':username1 , 'b':password1,'x':status,'c':age,'d':gender,'e':city})
            con.commit()


            root1.destroy()

            messagebox.showinfo("SUCCESS", "SIGNUP SUCCESSFULL")
            main()

        root1 = Tk()
        root1.title("SIGNUP PAGE")
        root1.geometry("1600x8000")

        label1 = Label(root1, text="SIGNUP", bd='8', font=('helvetica', 50, 'bold'))
        label1.place(x=520,y=0)

        userlabel = Label(root1, font=('arial', 16, 'bold'), text="USERNAME", bd='8')
        userlabel.place(x=400,y=200)

        passlabel = Label(root1, font=('arial', 16, 'bold'), text="PASSWORD", bd='8')
        passlabel.place(x=400,y=250)

        agelabel = Label(root1, font=('arial', 16, 'bold'), text="AGE", bd='8')
        agelabel.place(x=400, y=300)

        citylabel = Label(root1, font=('arial', 16, 'bold'), text="CITY", bd='8')
        citylabel.place(x=400, y=350)

        genderlabel = Label(root1, font=('arial', 16, 'bold'), text="GENDER", bd='8')
        genderlabel.place(x=400, y=400)

        username = StringVar()
        password = StringVar()
        age = StringVar()
        city = StringVar()
        gender = StringVar()

        userentry = Entry(root1, font=('arial', 16, 'bold'), textvariable=username, insertwidth=6, bg="MediumPurple1", bd=10)
        userentry.place(x=600,y=200)

        passentry = Entry(root1, font=('arial', 16, 'bold'),show="*", textvariable=password, insertwidth=4, bg="MediumPurple1",bd=10)
        passentry.place(x=600,y=250)

        ageentry = Entry(root1, font=('arial', 16, 'bold'), textvariable=age, insertwidth=6, bg="MediumPurple1",bd=10)
        ageentry.place(x=600, y=300)

        cityentry = Entry(root1, font=('arial', 16, 'bold'), textvariable=city, insertwidth=4,bg="MediumPurple1", bd=10)
        cityentry.place(x=600, y=350)

        genderentry = Entry(root1, font=('arial', 16, 'bold'), textvariable=gender, insertwidth=4, bg="MediumPurple1",
                          bd=10)
        genderentry.place(x=600, y=400)


        submitbutton = Button(root1, font=('arial', 16, 'bold'), text="Submit", activebackground="LightBlue",
                              relief="raised", bd=10, bg="MediumPurple1", command=confirm)
        submitbutton.place(x=570, y=520)

    photo = ImageTk.PhotoImage(Image.open('fpage.png'))
    label1 = Label(root, image=photo)

    label1.place(x=250, y=0)

    signupbutton = Button(root, font=('arial', 16, 'bold'), text="SignUp", activebackground="LightBlue",
                      relief="raised", bd=10, bg="royalblue1", command=signup)
    signupbutton.place_configure(x=650, y=650)

    analysisbutton = Button(root, font=('arial', 16, 'bold'), text="Anaylsis", activebackground="LightBlue",
                      relief="raised", bd=10, bg="royalblue1", command=analysis)
    analysisbutton.place_configure(x=800, y=650)

    resultbutton = Button(root, font=('arial', 16, 'bold'), text="Result", activebackground="LightBlue",
                          relief="raised", bd=10, bg="royalblue1", command=result)
    resultbutton.place_configure(x=725, y=725)

    root.mainloop()


main()
