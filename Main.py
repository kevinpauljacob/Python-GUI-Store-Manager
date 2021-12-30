import sqlite3
import os
import random
import sys
sys.path.append("C:/Final Project/Project/")
sys.path.append("C:/Final Project/Project/")
from tkinter import *
import tkinter.messagebox as MessageBox
import tkinter.scrolledtext as scrolledtext

# Database Connection
con = sqlite3.connect(r"C:/Final Project/Database/store.db")
cur = con.cursor()

# Credentials
username = str("user") 
password = str("passwrd")
  
class LoginPage:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.loginframe=LabelFrame(master, width=1200, height=700, bg='steelblue')
        self.loginframe.pack(padx=0, pady=0)
        self.welcome_label = Label(self.loginframe, text="The Reader's Odyssey:Login", bg='steelblue', fg='white', font=('Courier 25 bold'))
        self.welcome_label.place(x=350, y=170)
        self.username_label = Label(self.loginframe, text="Username", bg='steelblue', fg='white', font=('Courier 15 bold'))
        self.username_label.place(x=460, y=240)
        self.username_entry = Entry(self.loginframe, text="", bg='white', fg='steelblue', font=('Courier 12 bold'))
        self.username_entry.place(x=570, y=242)  
        self.username_entry.focus()
        self.username_entry.bind('<Down>',lambda a: down1(1))
        self.username_entry.bind('<Up>',lambda a: up1(2))
        self.loginButton = Button(self.loginframe, text="Login", width=23, bg='white', fg='steelblue', font=('Courier 12 bold'), command=self.trylogin)
        self.loginButton.place(x=500, y=350)
        self.master.bind("<Return>", self.trylogin)

        def down1(x):
            self.password_entry.focus_set()
        def up1(x):
            self.username_entry.focus_set()

        self.password_label = Label(self.loginframe,text="Password", bg='steelblue', fg='white', font=('Courier 15 bold'))
        self.password_label.place(x=460, y=280)  
        self.password_entry = Entry(self.loginframe, text="", show='*', bg='white', fg='steelblue', font=('Courier 12 bold'))
        self.password_entry.place(x=570, y=282)
        self.password_entry.bind('<Down>',lambda a: down1(1))
        self.password_entry.bind('<Up>',lambda a: up1(2))



        self.choiceframe=LabelFrame(master, width=1200, height=700, bg='steelblue')
        
            
        self.dbmsButton = Button(self.choiceframe, text="Open Database System", width=23, bg='white', fg='steelblue', font=('Courier 12 bold'), command=self.call_Dbms)
        self.dbmsButton.place(x=480, y=230)
        self.billingButton = Button(self.choiceframe, text="Open Billing System", width=23, bg='white', fg='steelblue', font=('Courier 12 bold'), command=self.call_BillingSystem)
        self.billingButton.place(x=480, y=280
                                 )

    def call_BillingSystem(self):
            import BillingSystem
            
    def call_Dbms(self):
            import Dbms 
             
    def trylogin(self, *args, **kwargs): 
        if username == self.username_entry.get() and password == self.password_entry.get():
            MessageBox.showinfo("Login Status", "Login Successfull")
            self.loginframe.place(x=1000000,y=100000000)
            self.choiceframe.pack(padx=0, pady=0)
                
        else:
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            MessageBox.showinfo("Error", "Incorrect Username or Password")
        

        
            

		
root = Tk()
alpha = LoginPage(root)
root.geometry("1200x580+30+30")
root.resizable(False, False)
root.title("The Reader's Odyssey: Main Program")
root.configure(bg="steelblue")
root.mainloop()
