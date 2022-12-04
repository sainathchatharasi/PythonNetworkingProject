#Authors DB_implementation : Chatharasi sainath, Siyyadri megha shyam
#Author Login page : Naidu Rupasree

from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time
class DB_Access:
    def __init__(self):
        #connecting to the database
        self.db = mysql.connector.connect(host="localhost",user="root",password="admin",database="demo1")
        self.mycur = self.db.cursor()


    #destroy() in the code base is used to destroy the window
    def error_destroy(self):
        err.destroy()

    def succ_destroy(self):
        succ.destroy()
        root1.destroy()

    #error message pop-up box design
    def error(self):
        global err
        err = Toplevel(root1)
        err.title("Error")
        err.geometry("200x100")
        Label(err,text="All fields are required..",fg="red",font="bold").pack()
        Label(err,text="").pack()
        Button(err,text="Ok",bg="grey",width=8,height=1,command=self.error_destroy).pack()

    #success message pop-up box design
    def success(self):
        global succ
        succ = Toplevel(root1)
        succ.title("Success")
        succ.geometry("200x100")
        Label(succ, text="Registration successful...", fg="green", font="bold").pack()
        Label(succ, text="").pack()
        Button(succ, text="Ok", bg="grey", width=8, height=1, command=self.succ_destroy).pack()

    def register_user(self):
        username_info = username.get()
        password_info = password.get()
        if username_info == "":
            error()
        elif password_info == "":
            error()
        else:
            Time = time.localtime()
            T = time.asctime(Time)
            sql = "insert into login values(%s,%s,%s)"
            t = (username_info, password_info,T)
            self.mycur.execute(sql, t)
            self.db.commit()
            Label(root1, text="").pack()
            time.sleep(0.50)
            self.success()



    def registration(self):
        global root1
        root1 = Toplevel(root)
        root1.title("Registration Portal")
        root1.geometry("300x250")
        global username
        global password
        Label(root1,text="Register your account",bg="grey",fg="black",font="bold",width=300).pack()
        username = StringVar()
        password = StringVar()
        Label(root1,text="").pack()
        Label(root1,text="Username :",font="bold").pack()
        Entry(root1,textvariable=username).pack()
        Label(root1, text="").pack()
        Label(root1, text="Password :").pack()
        Entry(root1, textvariable=password,show="*").pack()
        Label(root1, text="").pack()
        Button(root1,text="Register",bg="red",command=self.register_user).pack()

    def login(self):
        global root2
        root2 = Toplevel(root)
        root2.title("Log-In Portal")
        root2.geometry("300x300")
        global username_varify
        global password_varify
        Label(root2, text="Log-In Portal", bg="grey", fg="black", font="bold",width=300).pack()
        username_varify = StringVar()
        password_varify = StringVar()
        Label(root2, text="").pack()
        Label(root2, text="Username :", font="bold").pack()
        Entry(root2, textvariable=username_varify).pack()
        Label(root2, text="").pack()
        Label(root2, text="Password :").pack()
        Entry(root2, textvariable=password_varify, show="*").pack()
        Label(root2, text="").pack()
        Button(root2, text="Log-In", bg="red",command=self.login_varify).pack()
        Label(root2, text="")

    def logg_destroy(self):
        logg.destroy()
        root2.destroy()

    def fail_destroy(self):
        fail.destroy()

    def logged(self):
        global logg
        logg = Toplevel(root2)
        logg.title("Welcome")
        logg.geometry("200x100")
        Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
        Label(logg, text="").pack()
        Button(logg, text="Log-Out", bg="grey", width=8, height=1, command=self.logg_destroy).pack()


    def failed(self):
        global fail
        fail = Toplevel(root2)
        fail.title("Invalid")
        fail.geometry("200x100")
        Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
        Label(fail, text="").pack()
        Button(fail, text="Ok", bg="grey", width=8, height=1, command=self.fail_destroy).pack()


    def login_varify(self):
        user_varify = username_varify.get()
        pas_varify = password_varify.get()
        sql = "select * from login where user = %s and password = %s"
        self.mycur.execute(sql,[(user_varify),(pas_varify)])
        results = self.mycur.fetchall()
        if results:
            for i in results:
                self.logged()
                break
        else:
            self.failed()


    def main_screen(self):
        global root
        root = Tk()
        root.title("Log-IN Portal")
        root.geometry("300x300")
        Label(root,text="Welcome to Log-In Protal",font="bold",bg="grey",fg="black",width=300).pack()
        Label(root,text="").pack()
        Button(root,text="Log-IN",width="8",height="1",bg="red",font="bold",command=self.login).pack()
        Label(root,text="").pack()
        Button(root, text="Registration",height="1",width="15",bg="red",font="bold",command=self.registration).pack()
        Label(root,text="").pack()
        Label(root,text="").pack()
        root.mainloop()
    
    
    
DB = DB_Access()
DB.main_screen()