from tkinter import *
from tkinter import font
from PIL import ImageTk,Image
import tkintermapview
import customtkinter
from tkintermapview import TkinterMapView
import json
from msilib.schema import PatchPackage
import webbrowser
import re
import sys
import os
import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox
import tkinter.filedialog
from pathlib import Path
from cProfile import label
from turtle import heading, left, width
from tkinter import ttk
import requests
from tkinter.messagebox import showinfo



customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
w = customtkinter.CTk()
w.geometry('690x400')
w.configure(bg='#323335')#12c4c0')
w.resizable(0,0)
w.title(' SFMTechnologies-Drive Test')
w.iconbitmap('sfm.ico')


def default_Mission():
                f2=Frame(w,width=900,height=455,bg='white')
                f2.place(x=0,y=45)
                l2=Label(f2,fg='#323335',bg='white')
                l2.config(font=('Arial',50))
                l2.place(x=380,y=150)
                img=PhotoImage(file='sfm (1).gif')
                Label(w,image=img,border=0,bg='white').place(x=10,y=10)
                
                #delete navbar
                def dele():
                    f1.destroy()
                    img1 = ImageTk.PhotoImage(Image.open("open.png"))
                    b2=Button(w,image=img1,
                           border=0,command=navbar,
                           bg='white',
                           activebackground='white')
                    b2.place(x=5,y=8)

             
                
                # navbar
                def navbar():
                    
                    global f1
                    f1=Frame(w,width=250,height=720,bg='#323335')
                    f1.place(x=0,y=0)
                    #les buttons
                    def bttn(x,y,text,bcolor,fcolor,cmd):
                        myButton1 = Button(f1,text=text,
                                   width=42,
                                   height=2,
                                   fg='white',
                                   border=0,
                                   bg=fcolor,
                                   activeforeground='white',
                                   activebackground=bcolor,            
                                    command=cmd)
                        myButton1.place(x=x,y=y)

                    bttn(-60,200,'M I S S I O N','#323335','#323335',mission)
                    bttn(-60,250,'T R A J E T','#323335','#323335',trajet)
                    bttn(-60,300,'H I S T O R I Q U E','#323335','#323335',historique)

                
                    img1 = ImageTk.PhotoImage(Image.open("x-circle.png"))
                    global b1
                    b1=Button(w,image=img1,
                           border=0,
                           bg='white',command=dele,
                           activebackground='white')
                    b1.place(x=5,y=8)
                
                
                navbar()
                # affiche nom chauffeur
                l3=Label(f2,text='Nom de chauffeur :',fg='#323335',bg='white')
                l3.config(font=('Arial-BoldMT',15))
                l3.place(x=300,y=150)
                
                nom=Entry(w,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))

                nom.place(x=530,y=200)
                nom.insert(0,'saoudi aya')
                
                
                #affiche Numéro carte CIN
                l4=Label(f2,text='Numéro Carte Identité de chauffeur :',fg='#323335',bg='white')
         
                l4.config(font=('Arial-BoldMT',15))
                l4.place(x=300,y=200)
                
                cin=Entry(w,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))

                cin.place(x=720,y=250)
                cin.insert(0,'14500953')
                #affiche si il est admin ou nom
                #test()




def mission():
                f1.destroy()
                f2=Frame(w,width=900,height=455,bg='white')
                f2.place(x=0,y=45)
                l2=Label(f2,text='Mission Drive Test',fg='black',bg='white')
                l2.config(font=('Arial',20))
                l2.place(x=350,y=5)
                
                my_tree=ttk.Treeview(w)
                my_tree['columns']=("Id","Nom de mission","Trajet","Date","Technologie","Test")
                
                my_tree.column("#0",width=0,minwidth=0,anchor=CENTER)
                my_tree.column("Id",anchor=CENTER,width=50)
                my_tree.column("Nom de mission",anchor=W,width=150)
                my_tree.column("Trajet",anchor=W,width=150)
                my_tree.column("Date",anchor=W,width=120)
                my_tree.column("Technologie",anchor=W,width=120)
                my_tree.column("Test",anchor=W,width=120)
                
                my_tree.heading("Id",text="Id",anchor=CENTER)
                my_tree.heading("Nom de mission",text="Nom de mission",anchor=CENTER)
                my_tree.heading("Trajet",text="Trajet",anchor=CENTER)
                my_tree.heading("Date",text="Date",anchor=CENTER)
                my_tree.heading("Technologie",text="Technologie",anchor=CENTER)
                my_tree.heading("Test",text="Test",anchor=CENTER)
                
                for i in range(1,4):
                    my_tree.insert(parent='',index=i,iid=i,text='',values=(i,"saoudi","rue hedi chaker, tunis","20/02/2022","3G","Voix"))
                    
                my_tree.pack(pady=90,padx=10)
                
                
                def selected():
                    for selected_item in my_tree.selection():
                        item = my_tree.item(selected_item)
                        record = item['values']
                        # show a message
                        ch=record[2]
                        print(ch)
                        trajet(ch)
                        my_tree.destroy()
                    
                
                Button(w,text="Voir trajet",command=selected).pack()
                
                """
                table = Table(w, ["N°", "Name of mission", "Route","Date","Technology","Test"], column_minwidths=[None, None, None,None,None,None],header_background='#ffffff',header_foreground='black',bordercolor='black',scroll_horizontally=None,scroll_vertically=None)
                table.pack(padx=10,pady=50)
                table.place(x=300,y=120)
                for i in range(1,6):
                        table.insert_row([i,"saoudi","rue abou alaa","22/12/2022","3G","Voix"])
                """
                #toggle_win()


def trajet(ch):
                f1.destroy()
                f2=Frame(w,width=900,height=455,bg='white')
                f2.place(x=0,y=45)
                l2=Label(f2,text=' Votre trajet',fg='#323335',bg='white')
                l2.config(font=('Arial',20))
                l2.place(x=500,y=10)
                my_lablel=LabelFrame(w)
                my_lablel.pack(pady=20)
                map_widget=tkintermapview.TkinterMapView(my_lablel,width=800,height=380,corner_radius=0)
                map_widget.pack()
                #set coordinates
                #map_widget.set_position(36.8063666,10.1813795)
                #map_widget.set_address("81 Av. Hédi Chaker, Tunis 1002")
                #set a zoom lavel
                map_widget.set_zoom(20)
                # set current widget position by address
                marker_1 = map_widget.set_address(ch, marker=True)

                print(marker_1.position, marker_1.text)  # get position and text

                marker_1.set_text("Votre trajet")  # set new text
                # marker_1.set_position(48.860381, 2.338594)  # change position
                # marker_1.delete()
                def lookup():
                    marker_2=map_widget.set_address(my_entry.get())
                    print(marker_2.position, marker_2.text) 
                    marker_2.set_text("Votre distination")
                    my_slider.config(value=9)

                def slide(e):
                    map_widget.set_zoom(my_slider.get())



                my_frame=LabelFrame(w)
                my_frame.pack(pady=10)
                my_entry=Entry(my_frame,font=("Arial",10))
                my_entry.grid(row=0,column=0,pady=20,padx=10)

                my_button=Button(my_frame,text="Search",font=("Arial",10),command=lookup)
                my_button.grid(row=0,column=1,padx=10)

                my_slider=ttk.Scale(my_frame,from_=4,to=20,orient=HORIZONTAL,command=slide,value=20,length=220)
                my_slider.grid(row=0,column=2,padx=10)
               

def historique():
                f1.destroy()
                f2=Frame(w,width=900,height=455,bg='white')
                f2.place(x=0,y=45)
                l2=Label(f2,text=' Historique',fg='#323335',bg='white')
                l2.config(font=('Arial',20))
                l2.place(x=500,y=10)
            

default_Mission()
w.mainloop()



