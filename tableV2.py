#from tabulate import tabulate
##import numpy as np
##import pandas as pd
##table_date=[['Name','Age','Job'],
##            ['Mike','22','Programmer'],
##            ['Jane','24','Teacher'],
##            ]
##print(tabulate(table_date,headers="firstrow",tablefmt="fancy_grid",showindex="always"))
##
##
#
#
#from prettytable import PrettyTable
#from tkinter import *
#
#win=Tk()
#
#t=Text(win)#Inside text widget we would put our table
#
#x=PrettyTable()
#
#x.field_names = ['Name of mission','Route','Date','Technology','Test']
#
#for i in range(1,6):
#        x.add_row(["saoudi","aya","22/12/2022","3G","Voix"])
##x.add_row(["Adelaide", 1295, 1158259, 600.5])
##x.add_row(["Brisbane", 5905, 1857594, 1146.4])
##x.add_row(["Darwin", 112, 120900, 1714.7])
##x.add_row(["Hobart", 1357, 205556, 619.5])
##x.add_row(["Sydney", 2058, 4336374, 1214.8])
##x.add_row(["Melbourne", 1566, 3806092, 646.9])
##x.add_row(["Perth", 5386, 1554769, 869.4])
#
#t.insert(INSERT,x)#Inserting table in text widget
#t.pack()
#
#win.mainloop()
#
#
#
#
#
#
#"""
#table_data=[['Name of mission','Route','Date','Technology','Test']]
#print(tabulate(table_data,headers="firstrow",tablefmt="fancy_grid",showindex="always"))
#for i in range(1,6):
#        table_data.insert(["saoudi","aya","22/12/2022","3G","Voix"])
#"""
#
#
#
#
#
##table = Table(w, ["N°", "Name of mission", "Route","Date","Technology","Test"], column_minwidths=[None, None, None,None,None,None],header_background='#ffffff',header_foreground='black',bordercolor='black',scroll_horizontally=None,scroll_vertically=None)
##                table.pack(padx=10,pady=50)
##                table.place(x=300,y=120)
##                for i in range(1,6):
##                        table.insert_row([i,"saoudi",know_more,"22/12/2022","3G","Voix"])
#

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

w = tk.Tk()
w.title('Treeview demo')
w.geometry('620x200')

tree = ttk.Treeview(w, selectmode ='browse')
  
tree.grid(row=1,column=1,padx=20,pady=20)
# number of columns
tree["columns"] = ("1", "2", "3","4","5","6")
  
# Defining heading
tree['show'] = 'headings'
  
# width of columns and alignment 
tree.column("1", width = 80, anchor ='c')
tree.column("2", width = 80, anchor ='c')
tree.column("3", width = 80, anchor ='c')
tree.column("4", width = 80, anchor ='c')
tree.column("5", width = 80, anchor ='c')
tree.column("6", width = 80, anchor ='c')

  
# Headings  
# respective columns
tree.heading("1", text ="id")
tree.heading("2", text ="Nom de mission")
tree.heading("3", text ="Trajet")
tree.heading("4", text ="Date")  
tree.heading("5", text ="Technologie")
tree.heading("5", text ="Test")


# getting data from MySQL student table 
for dt in range(1,5): 
    tree.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt,"saoudi","abou ala","21/2/2022","3G","voix"))


def item_selected(event):
                    for selected_item in tree.selection():
                        item = tree.item(selected_item)
                        record = item['values']
                        # show a message
                        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)
                
tree.grid(row=0, column=0, sticky='nsew')
w.mainloop()               


"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

# define columns
columns = ('first_name', 'last_name', 'email')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')

# generate sample data
contacts = []
for n in range(1, 100):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# add data to the treeview
for contact in contacts:
    tree.insert('', tk.END, values=contact)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()

"""
add_frame=Frame(w)
                add_frame.pack()
                
                di=Label(add_frame,text="Id")
                di.grid(row=0,column=0)
                
                nm=Label(add_frame,text="Nom de mission")
                nm.grid(row=0,column=1)
                
                tr=Label(add_frame,text="Trajet")
                tr.grid(row=0,column=2)
                
                da=Label(add_frame,text="Date")
                da.grid(row=0,column=3)
                
                tc=Label(add_frame,text="Technologie")
                tc.grid(row=0,column=4)
                
                te=Label(add_frame,text="Test")
                te.grid(row=0,column=5)
                
                
                id_box=Entry(add_frame)
                id_box.grid(row=1,column=0)
                
                name_box=Entry(add_frame)
                name_box.grid(row=1,column=1)
                
                trajet_box=Entry(add_frame)
                trajet_box.grid(row=1,column=2)
                
                date_box=Entry(add_frame)
                date_box.grid(row=1,column=3)
                
                tech_box=Entry(add_frame)
                tech_box.grid(row=1,column=4)
                
                test_box=Entry(add_frame)
                test_box.grid(row=1,column=5)
                
                
                
                
table = Table(w, ["N°", "Name of mission", "Route","Date","Technology","Test"], column_minwidths=[None, None, None,None,None,None],header_background='#ffffff',header_foreground='black',bordercolor='black',scroll_horizontally=None,scroll_vertically=None)
                table.pack(padx=10,pady=50)
                table.place(x=300,y=120)
for i in range(1,len(res['nom_miss'])+1):
                        table.insert_row([i,res['nom_miss'][i-1],res['trajet'][i-1],res['dates'][i-1],res['technologie'][i-1],res['test'][i-1]])