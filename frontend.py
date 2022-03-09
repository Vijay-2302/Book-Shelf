from tkinter import *
from backend import Database

database=Database()

window=Tk()
window.title(string="Book Shelf")

selected_tuple=()

class book_operation():

    def __init__(self,lst):
        self.lst=lst
    
    def get_selected_tuple(self,event):
        global selected_tuple 
        try:
            index=lst.curselection()[0]   
            selected_tuple=lst.get(index)
            e1.delete(0,END)
            e1.insert(END,selected_tuple[1])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[2])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[3])
            e4.delete(0,END)
            e4.insert(END,selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.lst.delete(0,END)
        for row in database.view():
            self.lst.insert(END,row)

    def search_command(self):
        self.lst.delete(0,END)
        for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
            self.lst.insert(END,row)

    def insert_command(self):
        database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        self.lst.delete(0,END)
        self.lst.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

    def update_command(self):
        database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

    def delete_command(self):
        database.delete(selected_tuple[0])



lb1=Label(window,text="Title")
lb1.grid(row=0,column=0)

lb2=Label(window,text="Author")
lb2.grid(row=0,column=2)

lb3=Label(window,text="Year")
lb3.grid(row=1,column=0)

lb4=Label(window,text="ISBN")
lb4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

lst=Listbox(window,height=6,width=40)
lst.grid(row=2,column=0,rowspan=6,columnspan=2)

obj=book_operation(lst)
lst.bind('<<ListboxSelect>>',obj.get_selected_tuple)

sc=Scrollbar(window)
sc.grid(row=2,column=2,rowspan=6)

lst.configure(yscrollcommand=sc.set)
sc.configure(command=lst.yview)

b1=Button(window,text="View all",width=12,command=obj.view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry",width=12,command=obj.search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=12,command=obj.insert_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,command=obj.update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12,command=obj.delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()