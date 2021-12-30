# Import and Database Connection=======================================================================================================================================
from tkinter import *
import sqlite3
import tkinter.messagebox as MessageBox
import tkinter.scrolledtext as scrolledtext
import datetime
import math
import random
import os
import time
con = sqlite3.connect(r"C:/Final Project/Database/store.db")
cur = con.cursor()
# Date and Time=================================================================================================================================================================
date = datetime.datetime.now().date()
time_string = datetime.datetime.now().time()
# Temporary List Sessions==============================================================================================================================================
bookslst = []
bookprc = []
bookqty = []
bookid = []

# Labels List==========================================================================================================================================================
labelslst = []

# Class================================================================================================================================================================
class Application:
    def __init__(self, master, *args, **kwargs):

        self.master = master
        global date
        # Frames=======================================================================================================================================================
        self.left = Frame(master, width=425, height=768, bg='white')
        self.left.pack(side=LEFT)
        self.right = Frame(master, width=860, height=768, bg='steelblue')
        self.right.pack(side=RIGHT)

        # Headers======================================================================================================================================================
        self.heading = Label(self.left, text="The Reader's Odyssey", font=('courier 25 bold'), bg='white', fg='black')
        self.heading.place(x=10, y=0)
        self.ldate = Label(self.right, text="Today's Date: " + str(date), font=('courier 16 bold'), bg='steelblue', fg='white')
        self.ldate.place(x=447, y=10)

        # Invoice Table================================================================================================================================================
        self.tbook =Label(self.right, text="Products", font=('courier 18 bold'), bg='steelblue', fg='white')
        self.tbook.place(x=5, y=60)
        self.tqty =Label(self.right, text="Quantity", font=('courier 18 bold'), bg='steelblue', fg='white')
        self.tqty.place(x=475, y=60)
        self.tamount =Label(self.right, text="Amount", font=('courier 18 bold'), bg='steelblue', fg='white')
        self.tamount.place(x=650, y=60)

        # Logs ScrolledText
        self.st = scrolledtext.ScrolledText(self.right, width=62, height=19, bg='steelblue', fg='white', font=('courier 15 bold'))
        self.st.place(x=5, y=100)

        # Labels=======================================================================================================================================================
        self.lbid = Label(self.left, text="Book-ID:", font=('courier 18 bold'), bg='white', fg='black')
        self.lbid.place(x=0, y=60)
        # for down arrow key
        def down2(x):
            self.echange.focus_set()
        self.ebid = Entry(self.left, width=14, font=('courier 15 bold'), bg='steelblue', fg='white')
        self.ebid.place(x=130, y=63)
        self.ebid.focus()
        self.ebid.bind('<Down>',lambda a: down2(1))

        # Search Button================================================================================================================================================
        self.btn_search = Button(self.left, text="Search", width=12, height=1,font=('courier 10 bold'), bg='steelblue', fg='white', command=self.search)
        self.btn_search.place(x=305, y=62)

        # Book Details=================================================================================================================================================       self.bookname = Label(self.left, text="", font=('courier 27 bold'), bg='white', fg='steelblue')
        self.bookname = Label(self.left, text="", font=('courier 15 bold'), bg='white', fg='steelblue')
        self.bookname.place(x=0, y=110)
        self.bprice = Label(self.left, text="", font=('courier 15 bold'), bg='white', fg='steelblue')
        self.bprice.place(x=0, y=130)

        # Total Label==================================================================================================================================================
        self.ltotal = Label(self.right, text="", font=('courier 25 bold'), bg='steelblue', fg='white')
        self.ltotal.place(x=5, y=542)

        # Binding Functions============================================================================================================================================
        self.master.bind("<Return>", self.search)
        self.master.bind("<Prior>", self.atc)
        self.master.bind("<space>", self.bill)
        self.master.bind("<Next>", self.change)
    
# Search===============================================================================================================================================================
    def search(self, *args, **kwargs):
        self.get_bid = self.ebid.get()
        # Retrieving Details===========================================================================================================================================
        query = "SELECT * FROM inventory WHERE bid=?"
        result = cur.execute(query, (self.get_bid, ))
        for self.r in result:
            self.get_bid = self.r[0]
            self.get_bname = self.r[1]
            self.get_bprice = self.r[5]
            self.get_bstock = self.r[3]
        self.bookname.configure(text="Book's Name: " + str(self.get_bname))
        self.bprice.configure(text="Price: Rs. " + str(self.get_bprice))

        # Quantity & Discount Labels & Entry=========================================================================================================================== 
        # for down arrow key
        def down1(x):
            self.echange.focus_set()
        # for up arrow key
        def up1(x):
            self.eqty.focus_set()
        self.lqty = Label(self.left, text="Quantity:", font=('courier 18 bold'), bg='white')
        self.lqty.place(x=0, y=190)
        self.ldiscount = Label(self.left, text="Discount:", font=('courier 18 bold'), bg='white')
        self.ldiscount.place(x=0, y=260)
        self.eqty = Entry(self.left, width=14, font=('courier 15 bold'), bg='steelblue', fg='white')
        self.eqty.place(x=130, y=195)
        self.eqty.focus_set()
        self.eqty.bind('<Down>',lambda a: down1(1))
        self.eqty.bind('<Up>',lambda a: up1(2))
        self.ediscount = Entry(self.left, width=14, font=('courier 15 bold'), bg='steelblue', fg='white')
        self.ediscount.place(x=130, y=265)
        self.ediscount.insert(END, 0)

        # Add To Cart Button===========================================================================================================================================
        self.btn_atc = Button(self.left, text="Add To Cart", width=12, height=1, bg='steelblue', fg='white',font=('courier 10 bold'), command=self.atc)
        self.btn_atc.place(x=305, y=194)

        # Change Label & Entry========================================================================================================================================= 
        self.lchange = Label(self.left, text="Given Amount:", font=('courier 18 bold'), bg='white')
        self.lchange.place(x=0, y=440)
        self.echange = Entry(self.left, width=18, font=('courier 15 bold'), bg='steelblue', fg='white')
        self.echange.place(x=192, y=440)
        self.echange.bind('<Down>',lambda a: down1(1))
        self.echange.bind('<Up>',lambda a: up1(2))

        # Change Button================================================================================================================================================
        self.btn_change = Button(self.left, text="Calculate Change", width=21, height=1, bg='steelblue', fg='white',font=('courier 12 bold'), command=self.change)
        self.btn_change.place(x=192, y=500)

        # Bill Button==================================================================================================================================================
        self.btn_bill = Button(self.left, text="Generate Bill", width=60, height=2, bg='red', fg='white', command=self.bill)
        self.btn_bill.place(x=0, y=540)

# AddToCart============================================================================================================================================================
    def atc(self, *args, **kwargs):
        global bookslst
        global bookprc
        global bookqty
        global bookid
        global labelslst
        self.vqty = int(self.eqty.get())
        if self.vqty > int(self.get_bstock):
            MessageBox.showinfo("Error", "Not that many products in our inventory.")
        else:
            # Calculating Price========================================================================================================================================
            self.fprice = (float(self.vqty) * float(self.get_bprice)) - (float(self.ediscount.get()))
            bookslst.append(self.get_bname)
            bookprc.append(self.fprice)
            bookqty.append(self.vqty)
            bookid.append(self.get_bid)
        
            self.x_index = 0
            self.y_index = 10
            self.counter = 0
            for self.p in bookslst:
                self.tempname = Label(self.st, text=str(bookslst[self.counter]), font=('courier 18 bold'), bg='steelblue', fg='white')
                self.tempname.place(x=5, y=self.y_index)
                labelslst.append(self.tempname)

                self.tempqt = Label(self.st, text=str(bookqty[self.counter]), font=('courier 18 bold'), bg='steelblue', fg='white')
                self.tempqt.place(x=525, y=self.y_index)
                labelslst.append(self.tempqt)
                
                self.tempprice = Label(self.st, text=str(bookprc[self.counter]), font=('courier 18 bold'), bg='steelblue', fg='white')
                self.tempprice.place(x=650, y=self.y_index)
                labelslst.append(self.tempprice)

                self.y_index += 40
                self.counter += 1

                # Total Configuration==================================================================================================================================
                self.ltotal.configure(text="Total: Rs." + str(sum(bookprc)))

                # Delete===============================================================================================================================================
                self.lqty.place_forget()
                self.eqty.place_forget()
                self.ldiscount.place_forget()
                self.ediscount.place_forget()
                self.bookname.configure(text="")
                self.bprice.configure(text="")
                self.btn_atc.destroy()

                # Autofocus Id=========================================================================================================================================
                self.ebid.focus()
                self.ebid.delete(0, END)
                
# Change===============================================================================================================================================================
    def change(self, *args, **kwargs):
        # Getting Amount to be given===================================================================================================================================
        self.amount_given = float(self.echange.get())
        self.our_total = float(sum(bookprc))

        self.to_give = self.amount_given - self.our_total


        # Change Amount Label==========================================================================================================================================
        self.c_amount = Label(self.left, text="Change:Rs." + str(self.to_give), font=('courier 15 bold'), fg='red', bg='white')
        self.c_amount.place(x=0 , y=500)

    def bill(self, *args, **kwargs):
        global date
        global time_string
        # Creating Bill File===========================================================================================================================================
        directory = "C:/Final Project/Invoice/" + str(date) + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Bill Template================================================================================================================================================
        company = "\t\t\t\tThe Reader's Odyssey Pvt. Ltd.\n"
        address = "\t\t\t\tChennai, TamilNadu\n"
        phone = "\t\t\t\t9988776655\n"
        sample = "\t\t\t\tInvoice\n"
        dt = "\t\t\t\t" + str(date) + "\n"
        time = "\t\t\t\t" + str(time_string)
        table_header = "\n\n\t\t\t------------------------------------------\n\t\t\tSN.\tBooks\t\tQty\t\tAmount\n\t\t\t------------------------------------------"
        final = company + address + phone + sample + dt + time + "\n" + table_header

        # Opening File=================================================================================================================================================
        file_name = str(directory) + str(random.randrange(5000, 10000)) + ".rtf"
        f = open(file_name, 'w')
        f.write(final)
        
        # Dynamics=====================================================================================================================================================
        r = 1
        i = 0
        for t in bookslst:
            f.write("\n\t\t\t" + str(r) + "\t" + str(bookslst[i] + ".......")[:7] + "\t\t" + str(bookqty[i]) + "\t\t" + str(bookprc[i]))
            i += 1
            r += 1
        f.write("\n\n\t\t\tTotal: Rs. " + str(sum(bookprc)))
        f.write("\n\t\t\tThanks for Visiting.")
        os.startfile(file_name, "print")
        f.close()
        
        # Dcreasing Stock==============================================================================================================================================
        self.x = 0

        initial = "SELECT * FROM inventory WHERE  bid=?"
        result = cur.execute(initial, (bookid[self.x], ))
        
        for i in bookslst:
            for r in result:
                self.old_stock = r[3]
            self.new_bstock = int(self.old_stock) - int(bookqty[self.x])

            # Updating Stock===========================================================================================================================================
            sql = "UPDATE inventory SET bstock=? WHERE bid=?"
            cur.execute(sql, (self.new_bstock, bookid[self.x]))
            con.commit()

            # Inserting into Transactions Table
            sql2 = "INSERT INTO transactions (bname, bqty, amount, date) VALUES (?,?,?,?)"
            cur.execute(sql2, (bookslst[self.x], bookqty[self.x], bookprc[self.x], date))
            con.commit()
            
            self.x += 1

        for a in labelslst:
            a.destroy()

        # Delete=======================================================================================================================================================
        del(bookslst[:])
        del(bookid[:])
        del(bookqty[:])
        del(bookprc[:])

        self.ltotal.configure(text="")
        self.c_amount.configure(text="")
        self.echange.delete(0, END)
        self.ebid.focus()
        MessageBox.showinfo("Success", "Done everything smoothly")
        
                
root = Tk()
beta = Application(root)
root.geometry("1200x580+30+30")
root.configure(bg="darkslategrey")
root.title("Billing System")
root.mainloop()
