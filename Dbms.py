from tkinter import *
import sqlite3
import tkinter.messagebox as MessageBox
import tkinter.scrolledtext as scrolledtext

# Database Connection
con = sqlite3.connect(r"C:/Final Project/Database/store.db")
cur = con.cursor()

class Database:
    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.heading = Label(master, text="The Reader's Odyssey DBMS", font=('Courier 25 bold'), bg="steelblue", fg="black")
        self.heading.place(x=20, y=5)

        result = cur.execute("SELECT Max(bid) from inventory")
        for r in result:
            bid = r[0]
            
        # Labels
        self.lbname = Label(master, text="Book Name", font=('Courier 16 bold'), bg="steelblue", fg="white")
        self.lbname.place(x=10, y=62)
        self.lbauthor = Label(master, text="Author Name", font=('Courier 16 bold'), bg="steelblue", fg="white")
        self.lbauthor.place(x=10, y=107)
        self.lbstock = Label(master, text="Stock", font=('Courier 16 bold'), bg="steelblue", fg="white")
        self.lbstock.place(x=10, y=153)
        self.lbcp = Label(master, text="Cost Price", font=('Courier 16 bold'), bg="steelblue", fg="white")
        self.lbcp.place(x=10, y=199)
        self.lbsp = Label(master, text="Selling Price", font=('Courier 16 bold'), bg="steelblue", fg="white")
        self.lbsp.place(x=10, y=249)
        self.ltotalbcp = Label(master, text="Total C.Price", font=('Courier 16 bold'), bg="steelblue", fg="white")
        self.ltotalbcp.place(x=10, y=299)
        self.ltotalbsp = Label(master, text="Total S.Price", font=('Courier 16 bold'), bg="steelblue", fg="white")
        self.ltotalbsp.place(x=10, y=349)
        self.lbpub = Label(master, text="Publisher", font=('Courier 16 bold'), bg="steelblue", fg="white")
        self.lbpub.place(x=10, y=398)
        self.lbpub_tel = Label(master, text="Publisher Ph.No.", font=('Courier 16 bold'), bg="steelblue", fg="white")
        self.lbpub_tel.place(x=10, y=448)
        self.lbid = Label(master, text="BookID", font=('Courier 16 bold'), bg="steelblue", fg="white")
        self.lbid.place(x=10, y=498)

        # Label Entries
        # for down arrow key
        def down1(x):
            self.ebauthor.focus_set()

        def down2(x):
            self.ebstock.focus_set()

        def down3(x):
            self.ebcp.focus_set()

        def down4(x):
            self.ebsp.focus_set()

        def down5(x):
            self.etotalbcp.focus_set()

        def down6(x):
            self.etotalbsp.focus_set()

        def down7(x):
            self.ebpub.focus_set()

        def down8(x):
            self.ebpub_tel.focus_set()

        def down9(x):
            self.ebid.focus_set()

        def down10(x):
            self.ebname.focus_set()
 
        # for up arrow key
        def up1(x):
            self.ebid.focus_set()

        def up2(x):
            self.ebname.focus_set()
    
        def up3(x):
            self.ebauthor.focus_set()

        def up4(x):
            self.ebstock.focus_set()

        def up5(x):
            self.ebcp.focus_set()

        def up6(x):
            self.ebsp.focus_set()

        def up7(x):
            self.etotalbcp.focus_set()

        def up8(x):
            self.etotalbsp.focus_set()

        def up9(x):
            self.ebpub.focus_set()

        def up10(x):
            self.ebpub_tel.focus_set()

        self.ebname = Entry(master, width=20, font=('Courier 18 bold'))
        self.ebname.place(x=230, y=61)
        self.ebname.focus_set()
        self.ebname.bind('<Down>',lambda a: down1(1))
        self.ebname.bind('<Up>',lambda a: up1(2))
        
        self.ebauthor = Entry(master, width=20, font=('Courier 18 bold'))
        self.ebauthor.place(x=230, y=107)
        self.ebauthor.bind('<Down>',lambda a: down2(1))
        self.ebauthor.bind('<Up>',lambda a: up2(2))
        
        self.ebstock = Entry(master, width=20, font=('Courier 18 bold'))
        self.ebstock.place(x=230, y=153)
        self.ebstock.bind('<Down>',lambda a: down3(1))
        self.ebstock.bind('<Up>',lambda a: up3(2))
        
        self.ebcp = Entry(master, width=20, font=('Courier 18 bold'))
        self.ebcp.place(x=230, y=200)
        self.ebcp.bind('<Down>',lambda a: down4(1))
        self.ebcp.bind('<Up>',lambda a: up4(2))
        
        self.ebsp = Entry(master, width=20, font=('Courier 18 bold'))
        self.ebsp.place(x=230, y=250)
        self.ebsp.bind('<Down>',lambda a: down5(1))
        self.ebsp.bind('<Up>',lambda a: up5(2))
        
        self.etotalbcp= Entry(master, width=20, font=('Courier 18 bold'))
        self.etotalbcp.place(x=230, y=300)
        self.etotalbcp.bind('<Down>',lambda a: down6(1))
        self.etotalbcp.bind('<Up>',lambda a: up6(2))
        
        self.etotalbsp = Entry(master, width=20, font=('Courier 18 bold'))
        self.etotalbsp.place(x=230, y=350)
        self.etotalbsp.bind('<Down>',lambda a: down7(1))
        self.etotalbsp.bind('<Up>',lambda a: up7(2))
        
        self.ebpub = Entry(master, width=20, font=('Courier 18 bold'))
        self.ebpub.place(x=230, y=398)
        self.ebpub.bind('<Down>',lambda a: down8(1))
        self.ebpub.bind('<Up>',lambda a: up8(2))
        
        self.ebpub_tel = Entry(master, width=20, font=('Courier 18 bold'))
        self.ebpub_tel.place(x=230, y=448)
        self.ebpub_tel.bind('<Down>',lambda a: down9(1))
        self.ebpub_tel.bind('<Up>',lambda a: up9(2))
        
        self.ebid = Entry(master, width=20, font=('Courier 18 bold'))
        self.ebid.place(x=230, y=496)
        self.ebid.bind('<Down>',lambda a: down10(1))
        self.ebid.bind('<Up>',lambda a: up10(2))

        # Feature Buttons
        self.btn_add = Button(master, text="Add", font=('Courier 10 bold'), width=15, height=2, bg='white', fg='steelblue', command=self.get_items)
        self.btn_add.place(x=1058, y=100)
        self.btn_delete = Button(master, text="Delete", font=('Courier 10 bold'), width=15, height=2, bg='red', fg='white', command=self.delete)
        self.btn_delete.place(x=1058, y=455)
        self.btn_update = Button(master, text="Update", font=('Courier 10 bold'), width=15, height=2, bg='white', fg='steelblue', command=self.update)
        self.btn_update.place(x=1058, y=270)
        self.btn_search = Button(master, text="Search", font=('Courier 10 bold'), width=15, height=2, bg='white', fg='steelblue', command=self.search)
        self.btn_search.place(x=1058, y=360)
        self.btn_clear = Button(master, text="Clear", font=('Courier 10 bold'), width=15, height=2, bg='white', fg='steelblue', command=self.clear_all)
        self.btn_clear.place(x=1058, y=185) 

        # Logs ScrolledText
        self.st = scrolledtext.ScrolledText(master, width=50, height=23, bg='white', fg='black', font=('courier 13 bold'))
        self.st.place(x=520, y=63)
        self.st.insert(END, "BookID has reached upto: " + str(bid))  


    def get_items(self, *args, **kwargs):

        # Main Entries
        self.bname = self.ebname.get()
        self.bauthor = self.ebauthor.get()
        self.bstock = self.ebstock.get()
        self.bcp = self.ebcp.get()
        self.bsp = self.ebsp.get()
        self.bpub = self.ebpub.get()
        self.bpub_tel = self.ebpub_tel.get()

        # Custom Entries
        self.totalbcp = float(self.bcp) * float(self.bstock)
        self.totalbsp = float(self.bsp) * float(self.bstock)
        self.profit = float(self.totalbsp - self.totalbcp)
        
        if self.bname == '' or self.bauthor == '' or self.bstock == '' or self.bcp == '' or self.bsp == '':
            MessageBox.showinfo("Error", "All entries are required.")
        else:
            sql = "INSERT INTO inventory (bname, bauthor, bstock, bcp, bsp, totalbcp, totalbsp, profit, bpub, bpub_telno ) VALUES(?,?,?,?,?,?,?,?,?,?)"
            cur.execute(sql, (self.bname, self.bauthor, self.bstock, self.bcp, self.bsp, self.totalbcp, self.totalbsp, self.profit, self.bpub, self.bpub_tel))
            con.commit()
            # ScrollBox Insert
            self.st.insert(END, "\n\nAdded " + str(self.bname) + " to the database with BookID:" + str(self.ebid.get())) 
            self.ebname.delete(0, END)
            self.ebauthor.delete(0, END)
            self.ebstock.delete(0, END)
            self.ebcp.delete(0, END)
            self.ebsp.delete(0, END)
            self.etotalbcp.delete(0, END)
            self.etotalbsp.delete(0, END)
            self.ebpub.delete(0, END)
            self.ebpub_tel.delete(0, END)
            self.ebid.delete(0, END)
            MessageBox.showinfo("Insert Status", "Inserted Successfully");
            


    def delete(self, *args, **kwargs):
        
        # Deleting Values from Database
        if(self.ebid.get() == ""):
            MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
        else:
            cur.execute("DELETE FROM inventory WHERE bid='"+ self.ebid.get() +"'")
            con.commit() 
            self.ebid.delete(0, END)
            self.ebname.delete(0, END)
            self.ebauthor.delete(0, END)
            self.ebstock.delete(0, END)
            self.ebcp.delete(0, END)
            self.ebsp.delete(0, END)
            self.etotalbcp.delete(0, END)
            self.etotalbsp.delete(0, END)
            self.ebpub.delete(0, END)
            self.ebpub_tel.delete(0, END)
            self.ebid.delete(0, END)
            MessageBox.showinfo("Delete Status", "Deleted Successfully");
            


    def update(self, *args, **kwargs):
        
        # Getting Updated Values
        self.u1 = self.ebname.get()
        self.u2 = self.ebauthor.get() 
        self.u3 = self.ebstock.get()
        self.u4 = self.ebcp.get()
        self.u5 = self.ebsp.get()
        self.u6 = self.etotalbcp.get()
        self.u7 = self.etotalbsp.get()
        self.u8 = self.ebpub.get()
        self.u9 = self.ebpub_tel.get()
        query_1 = "UPDATE inventory SET bname=?, bauthor=?, bstock=?, bcp=?, bsp=?, totalbcp=?, totalbsp=?, bpub=?, bpub_telno=? WHERE bid=?"
        cur.execute(query_1, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.u9, self.ebid.get()))
        con.commit()
        MessageBox.showinfo("Success", "Updated Database Succesfully")


    def search(self, *args, **kwargs):

        # Retrieving Values
        query_2 = "SELECT * FROM inventory WHERE bid=?"
        result = cur.execute(query_2, (self.ebid.get(),))
        for r in result:
            self.n1 = r[1] #bname
            self.n2 = r[2] #bauthor
            self.n3 = r[3] #bstock
            self.n4 = r[4] #bcp
            self.n5 = r[5] #bsp
            self.n6 = r[6] #totalbcp
            self.n7 = r[7] #totalbsp
            self.n8 = r[8] #profit
            self.n9 = r[9] #bpub
            self.n10 = r[10] #bpub_tel
        con.commit()
        # Inserting Entries to Update
        self.ebname.delete(0, END)
        self.ebname.insert(0,  str(self.n1))
        self.ebauthor.delete(0, END)
        self.ebauthor.insert(0,  str(self.n2))
        self.ebstock.delete(0, END)
        self.ebstock.insert(0,  str(self.n3))
        self.ebcp.delete(0, END)
        self.ebcp.insert(0,  str(self.n4))
        self.ebsp.delete(0, END)
        self.ebsp.insert(0,  str(self.n5))
        self.ebpub.delete(0, END)
        self.ebpub.insert(0,  str(self.n9)) 
        self.ebpub_tel.delete(0, END)
        self.ebpub_tel.insert(0,  str(self.n10))
        self.etotalbcp.delete(0, END)
        self.etotalbcp.insert(0,  str(self.n6))
        self.etotalbsp.delete(0, END)
        self.etotalbsp.insert(0,  str(self.n7))


    def clear_all(self, *args, **kwargs):
        self.ebname.delete(0, END)
        self.ebauthor.delete(0, END)
        self.ebstock.delete(0, END)
        self.ebcp.delete(0, END)
        self.ebsp.delete(0, END)
        self.etotalbcp.delete(0, END)
        self.etotalbsp.delete(0, END)
        self.ebpub.delete(0, END)
        self.ebpub_tel.delete(0, END)
        self.ebid.delete(0, END)

root = Tk()
alpha = Database(root)
root.geometry('1200x580+30+30')
root.configure(bg="steelblue")
root.title("Database Management System")
root.mainloop()
                           
        
