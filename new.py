
import imp
import json
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
from select import select
from tkinter import *
from turtle import heading, left, width
from tkinter import ttk
import requests
from email.mime import image
from tkinter import *
from tkinter import font
from PIL import ImageTk,Image
import tkintermapview
import customtkinter
from tkintermapview import TkinterMapView
import customtkinter
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.messagebox import showinfo
from tkinter import PhotoImage
from PIL import ImageTk
from tkcalendar import*

import time
from datetime import date
import datetime
import glob
import os , sys
import codecs
import ctypes, sys
import pyautogui
import win32com.shell.shell as shell
import subprocess
import csv
import schedule
import sqlite3
from sqlite3 import Error
import customtkinter  
from tkinter import messagebox
from ftplib import FTP 
import psutil
import serial
import mysql.connector


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
w = customtkinter.CTk()
w.geometry('1080x720')
w.configure(bg='white')#12c4c0')
w.resizable(0,0)
w.title(' SFMTechnologies-Drive Test')
w.iconbitmap('sfm.ico')

global img,img5,img4,img3,img2,button_help,button_user,button_stat,button_trajet,button_mission,button_home,img1,f1
img=PhotoImage(file='sfm-removebg-preview.gif')
img5=PhotoImage(file='search (1).png')
img4=PhotoImage(file='profile.png')
img3=PhotoImage(file='notification.png')
img2=PhotoImage(file='logout.png')
button_help=PhotoImage(file='help.png')
button_user=PhotoImage(file='userr.png')
button_stat=PhotoImage(file='statistiques.png')
button_trajet=PhotoImage(file='route.png')
button_mission=PhotoImage(file='mission.png')
button_home=PhotoImage(file='home.png')
img1=PhotoImage(file='user (1) (1).png')
f1=Frame(w,width=200,height=1000,bg='#6C8CB4')
#interface accueil
def accueil():
               
                #frame right
                f1.place(x=0,y=0)
                
                f5=Frame(w,width=2000,height=1000,bg='white')
                f5.place(x=200,y=70)
                #button accueil
                
                Button(f1,border=0,image=button_home,bg='#6C8CB4',activebackground='#6C8CB4',command=accueil).place(x=10,y=200)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='A C C U E I L',fg='white',command=accueil).place(x=70,y=200)
                #button mission
                
                Button(f1,border=0,image=button_mission,bg='#6C8CB4',activebackground='#6C8CB4',command=mission).place(x=10,y=300)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='M I S S I O N',fg='white',command=mission).place(x=70,y=300)

                #button trajet

                
                Button(f1,border=0,image=button_trajet,bg='#6C8CB4',activebackground='#6C8CB4',command=trajet).place(x=10,y=400)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='T R A J E T',fg='white',command=trajet).place(x=70,y=400)


                #button stats

                
                Button(f1,border=0,image=button_stat,bg='#6C8CB4',activebackground='#6C8CB4').place(x=10,y=600)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='S T A T S',fg='white').place(x=70,y=600)

                #button profil

                
                Button(f1,border=0,image=button_user,bg='#6C8CB4',activebackground='#6C8CB4',command=profil).place(x=10,y=500)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='P R O F I L',fg='white',command=profil).place(x=70,y=500)

                #button help        

              
                Button(f1,border=0,image=button_help,bg='#6C8CB4',activebackground='#6C8CB4').place(x=10,y=700)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='H E L P',fg='white').place(x=70,y=700)    

                #LOGOUT
               
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='LOG OUT',fg='white').place(x=50,y=830)
                Button(f1,image=img2,border=0,bg='#6C8CB4',activebackground='#6C8CB4').place(x=130,y=830)

                
                Label(w,image=img3,border=0,bg='white').place(x=1300,y=15)

                
                Label(w,image=img4,border=0,bg='white').place(x=1250,y=15)  

                
                Label(w,image=img5,border=0,bg='white').place(x=230,y=25)      

                #BOX FIND
                my_entry=Entry(w,font=('Arial',10),fg='#6C8CB4',width=50,border=2)
                my_entry.place(x=290,y=25)

                #img=PhotoImage(file='sfm-removebg-preview.gif')
                Label(f1,image=img,border=0,bg='#6C8CB4').place(x=40,y=30)
                
    
def query_com1():
    conn=mysql.connector.connect(host="localhost",username="root",password="",database="stage")
    cur=conn.cursor()
    cur.execute("SELECT * FROM form")
    list5 = cur.fetchall()
    cur.close()
    conn.close()
    
    output6=''
    for x in list5:
	    output6 = x[0]
    
    return(output6)
    
#Detection   
def detection():
    
	output6=query_com1()
	com_det="com"+output6
	#now = datetime.now()
	#current_time_action = now.strftime("%H:%M:%S")
	battery = psutil.sensors_battery()
	cpu_level = psutil.cpu_percent()
	memorie_lev=psutil.virtual_memory().percent
	secteur_status=psutil.sensors_battery().power_plugged
	bat_level=battery.percent
	erreur =pyautogui.locateCenterOnScreen('img/gns3.png',confidence=0.7)
	erreur1 =pyautogui.locateCenterOnScreen('img/gps_des.png',confidence=0.7)
	erreur2 =pyautogui.locateCenterOnScreen('img/no_devv.png',confidence=0.7)
	erreur3 =pyautogui.locateCenterOnScreen('img/no_dev2.png',confidence=0.7)
	dev_des=pyautogui.locateCenterOnScreen('img/dev_des.png',confidence=0.7)
	#no_device_1=pyautogui.locateCenterOnScreen('img/dev_l.png')
	#no_device_2=pyautogui.locateCenterOnScreen('img/dev_lec.png')

	send = serial.Serial(com_det,115200)
	if erreur is not None :
		send.write('b'.encode())
	elif bat_level < 98 and secteur_status == False:
		send.write('d'.encode())	
	elif erreur2 is not None :
		send.write('c'.encode())
	elif erreur1 is not None :
		send.write('i'.encode())
	elif cpu_level > 80:
		send.write('e'.encode())	
	elif memorie_lev > 90:
		send.write('f'.encode())		
	else :
		send.write('a'.encode())	


#create table
def tableau():
                my_tree=ttk.Treeview(w)
                my_tree['columns']=("N°","Nom de mission","Trajet","Date","Technologie","Test")
                
                my_tree.column("#0",width=0,minwidth=0,anchor=CENTER)
                my_tree.column("N°",anchor=CENTER,width=30)
                my_tree.column("Nom de mission",anchor=CENTER,width=200)
                my_tree.column("Trajet",anchor=CENTER,width=250)
                my_tree.column("Date",anchor=CENTER,width=250)
                my_tree.column("Technologie",anchor=CENTER,width=100)
                my_tree.column("Test",anchor=CENTER,width=100)
                
                my_tree.heading("N°",text="N°",anchor=CENTER)
                my_tree.heading("Nom de mission",text="Nom de mission",anchor=CENTER)
                my_tree.heading("Trajet",text="Trajet",anchor=CENTER)
                my_tree.heading("Date",text="Date",anchor=CENTER)
                my_tree.heading("Technologie",text="Technologie",anchor=CENTER)
                my_tree.heading("Test",text="Test",anchor=CENTER)
                
                for i in range(1,2):
                    my_tree.insert(parent='',index=i,iid=i,text='',values=(i,"Litter mission","rue hedi chaker, tunis","20/11/2022","3G","Voix"))
                my_tree.place(y=200,x=300)
                
                
                def selected():
                    for selected_item in my_tree.selection():
                        item = my_tree.item(selected_item)
                        record = item['values']
                        # show a message
                        ch=record[2]
                        print(ch)
                        trajet(ch)
                        my_tree.destroy()
                def start_mission():
                    for selected_item in my_tree.selection():
                        item = my_tree.item(selected_item)
                        record = item['values']
                        print(record)
                        query_com1()
                        detection()
                        schedule.every(1).seconds.do(detection)	
                        while 1 :
	                        schedule.run_pending()
	                        time.sleep(1)
                        if(detection):
                            #envoie des données
                            pass
                global mybutton   
                mybutton=Button(w,text="Voir trajet",command=selected,padx=40).place(x=500,y=600)
                #Button start
                mybuttonstart=Button(w,text="Start",padx=40,command=start_mission).place(x=900,y=600)
                
                
#interface mission
def mission():
                
                f1.place(x=0,y=0)
                
                #button accueil
                
                Button(f1,border=0,image=button_home,bg='#6C8CB4',activebackground='#6C8CB4',command=accueil).place(x=10,y=200)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='A C C U E I L',fg='white',command=accueil).place(x=70,y=200)
                #button mission
                
                Button(f1,border=0,image=button_mission,bg='#6C8CB4',activebackground='#6C8CB4',command=mission).place(x=10,y=300)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='M I S S I O N',fg='white',command=mission).place(x=70,y=300)

                #button trajet

                
                Button(f1,border=0,image=button_trajet,bg='#6C8CB4',activebackground='#6C8CB4',command=trajet).place(x=10,y=400)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='T R A J E T',fg='white',command=trajet).place(x=70,y=400)


                #button stats

                
                Button(f1,border=0,image=button_stat,bg='#6C8CB4',activebackground='#6C8CB4').place(x=10,y=600)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='S T A T S',fg='white').place(x=70,y=600)

                #button profil

                
                Button(f1,border=0,image=button_user,bg='#6C8CB4',activebackground='#6C8CB4',command=profil).place(x=10,y=500)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='P R O F I L',fg='white',command=profil).place(x=70,y=500)

                #button help        

                
                Button(f1,border=0,image=button_help,bg='#6C8CB4',activebackground='#6C8CB4').place(x=10,y=700)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='H E L P',fg='white').place(x=70,y=700)    

                #LOGOUT
               
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='LOG OUT',fg='white').place(x=50,y=830)
                Button(f1,image=img2,border=0,bg='#6C8CB4',activebackground='#6C8CB4').place(x=130,y=830)

                
                Label(w,image=img3,border=0,bg='white').place(x=1300,y=15)

                
                Label(w,image=img4,border=0,bg='white').place(x=1250,y=15)  

                
                Label(w,image=img5,border=0,bg='white').place(x=230,y=25)      

                #BOX FIND
                my_entry=Entry(w,font=('Arial',10),fg='#6C8CB4',width=50,border=2)
                my_entry.place(x=290,y=25)
                
                
                Label(f1,image=img,border=0,bg='#6C8CB4').place(x=40,y=30)

                f5=Frame(w,width=2000,height=1000,bg='white')
                f5.place(x=200,y=70)
                global l2
                l2=Label(f5,text='Mission Drive Test',fg='black',bg='white')
                l2.config(font=('Arial',20))
                l2.place(x=480,y=15)
                tableau()
                
                
                
#interface trajet   
def trajet(ch=""):
                
                f1.place(x=0,y=0)
                #button accueil
                
                Button(f1,border=0,image=button_home,bg='#6C8CB4',activebackground='#6C8CB4',command=accueil).place(x=10,y=200)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='A C C U E I L',fg='white',command=accueil).place(x=70,y=200)
                #button mission
                
                Button(f1,border=0,image=button_mission,bg='#6C8CB4',activebackground='#6C8CB4',command=mission).place(x=10,y=300)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='M I S S I O N',fg='white',command=mission).place(x=70,y=300)

                #button trajet

                
                Button(f1,border=0,image=button_trajet,bg='#6C8CB4',activebackground='#6C8CB4',command=trajet).place(x=10,y=400)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='T R A J E T',fg='white',command=trajet).place(x=70,y=400)


                #button stats

               
                Button(f1,border=0,image=button_stat,bg='#6C8CB4',activebackground='#6C8CB4').place(x=10,y=600)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='S T A T S',fg='white').place(x=70,y=600)

                #button profil

                
                Button(f1,border=0,image=button_user,bg='#6C8CB4',activebackground='#6C8CB4',command=profil).place(x=10,y=500)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='P R O F I L',fg='white',command=profil).place(x=70,y=500)

                #button help        

                
                Button(f1,border=0,image=button_help,bg='#6C8CB4',activebackground='#6C8CB4').place(x=10,y=700)
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='H E L P',fg='white').place(x=70,y=700)    

                #LOGOUT
                
                Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='LOG OUT',fg='white').place(x=50,y=830)
                Button(f1,image=img2,border=0,bg='#6C8CB4',activebackground='#6C8CB4').place(x=130,y=830)

                
                Label(w,image=img3,border=0,bg='white').place(x=1300,y=15)

               
                Label(w,image=img4,border=0,bg='white').place(x=1250,y=15)  

                
                Label(w,image=img5,border=0,bg='white').place(x=230,y=25)      

                #BOX FIND
                my_entry=Entry(w,font=('Arial',10),fg='#6C8CB4',width=50,border=2)
                my_entry.place(x=290,y=25)
                
                Label(f1,image=img,border=0,bg='#6C8CB4').place(x=40,y=30)
                
                f6=Frame(w,width=2000,height=1000,bg='white')
                f6.place(x=200,y=70)
                global l1
                l1=Label(f6,text='Trajet',fg='black',bg='white')
                l1.config(font=('Arial',20))
                l1.place(x=480,y=15)
                
                global my_lablel
                my_lablel=LabelFrame(w)
                my_lablel.pack(pady=150,padx=100)
                global map_widget
                map_widget=tkintermapview.TkinterMapView(my_lablel,width=900,height=500,corner_radius=0)
                map_widget.pack(pady=0)
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
                
                

#interface profil
def profil():
    
    #ajout frame f wost
    f5=Frame(w,width=2000,height=1000,bg='white')
    f5.place(x=200,y=70)
    #frame center
    f2=Frame(w,width=950,height=600,bg='#EBF4FF',padx=10)
    f2.place(x=300,y=150)
    
    f=Frame(f2,width=3,height=100,bg='black')
    f.place(x=200,y=80)
    
    #f3=Frame(w,width=300,height=150,bg='#EBF4FF',padx=10)
    #f3.place(x=1080,y=700)                

    # affiche nom chauffeur
    
    Label(f2,image=img1,border=0,bg='#EBF4FF').place(x=80,y=80)
    
    nom=Entry(f2,width=25,fg='#6C8CB4',border=0,bg='#EBF4FF',font=('Arial',11))
    nom.place(x=80,y=200)
    nom.insert(0,'Saoudi Aya')

    #affiche Mail
    l4=Label(f2,text='Email :',fg='#6C8CB4',bg='#EBF4FF')
    l4.config(font=('Arial-BoldMT',12))
    l4.place(x=250,y=50)

    cin=Entry(f2,width=25,fg='black',border=0,bg='#EBF4FF',font=('Arial',11))
    cin.place(x=250,y=100)
    cin.insert(0,'saoudiaya@gmail.com')

    #adresse chauffaur
    l4=Label(f2,text='Adresse :',fg='#6C8CB4',bg='#EBF4FF')
    l4.config(font=('Arial-BoldMT',12))
    l4.place(x=250,y=150)

    cin=Entry(f2,width=25,fg='black',border=0,bg='#EBF4FF',font=('Arial',11))
    cin.place(x=250,y=200)
    cin.insert(0,'17, rue hedi chaker')  
    
    #téléphone chauffaur
    l4=Label(f2,text='N° Téléphone :',fg='#6C8CB4',bg='#EBF4FF')
    l4.config(font=('Arial-BoldMT',11))
    l4.place(x=250,y=250)

    cin=Entry(f2,width=25,fg='black',border=0,bg='#EBF4FF',font=('Arial',11))
    cin.place(x=250,y=300)
    cin.insert(0,'29446211')  
   
# navbar

#frame right
f1.place(x=0,y=0)

#button accueil

Button(f1,border=0,image=button_home,bg='#6C8CB4',activebackground='#6C8CB4',command=accueil).place(x=10,y=200)
Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='A C C U E I L',fg='white',command=accueil).place(x=70,y=200)
#button mission

Button(f1,border=0,image=button_mission,bg='#6C8CB4',activebackground='#6C8CB4',command=mission).place(x=10,y=300)
Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='M I S S I O N',fg='white',command=mission).place(x=70,y=300)

#button trajet


Button(f1,border=0,image=button_trajet,bg='#6C8CB4',activebackground='#6C8CB4',command=trajet).place(x=10,y=400)
Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='T R A J E T',fg='white',command=trajet).place(x=70,y=400)


#button stats


Button(f1,border=0,image=button_stat,bg='#6C8CB4',activebackground='#6C8CB4').place(x=10,y=600)
Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='S T A T S',fg='white').place(x=70,y=600)

#button profil


Button(f1,border=0,image=button_user,bg='#6C8CB4',activebackground='#6C8CB4',command=profil).place(x=10,y=500)
Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='P R O F I L',fg='white',command=profil).place(x=70,y=500)

#button help        


Button(f1,border=0,image=button_help,bg='#6C8CB4',activebackground='#6C8CB4').place(x=10,y=700)
Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='H E L P',fg='white').place(x=70,y=700)    
 
#LOGOUT

Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='LOG OUT',fg='white').place(x=50,y=830)
Button(f1,image=img2,border=0,bg='#6C8CB4',activebackground='#6C8CB4').place(x=130,y=830)
     

Label(w,image=img3,border=0,bg='white').place(x=1300,y=15)
Button(w,border=0,image=img4,bg='white',activebackground='white',command=profil).place(x=1250,y=15)
Label(w,image=img5,border=0,bg='white').place(x=230,y=25)      
    
#BOX FIND
my_entry=Entry(w,font=('Arial',10),fg='#6C8CB4',width=50,border=2)
my_entry.place(x=290,y=25)

Label(f1,image=img,border=0,bg='#6C8CB4').place(x=40,y=30)

w.mainloop()

"""
#frame left
f2=Frame(w,width=300,height=600,bg='#EBF4FF',padx=10)
f2.place(x=1080,y=70)

f3=Frame(w,width=300,height=150,bg='#EBF4FF',padx=10)
f3.place(x=1080,y=700)                
         
# affiche nom chauffeur
img1=PhotoImage(file='user (1) (1).png')
Label(f2,image=img1,border=0,bg='#EBF4FF').place(x=80,y=50)
                
nom=Entry(f2,width=25,fg='#6C8CB4',border=0,bg='#EBF4FF',font=('Arial',11))
nom.place(x=80,y=170)
nom.insert(0,'Saoudi Aya')

#affiche Mail
l4=Label(f2,text='Email :',fg='#6C8CB4',bg='#EBF4FF')
l4.config(font=('Arial-BoldMT',12))
l4.place(x=10,y=250)

cin=Entry(f2,width=25,fg='black',border=0,bg='#EBF4FF',font=('Arial',11))
cin.place(x=10,y=302)
cin.insert(0,'saoudiaya@gmail.com')
                
#adresse chauffaur
l4=Label(f2,text='Adresse :',fg='#6C8CB4',bg='#EBF4FF')
l4.config(font=('Arial-BoldMT',12))
l4.place(x=10,y=350)

cin=Entry(f2,width=25,fg='black',border=0,bg='#EBF4FF',font=('Arial',11))
cin.place(x=10,y=395)
cin.insert(0,'17, rue hedi chaker')  
 
#téléphone chauffaur
l4=Label(f2,text='N° Téléphone :',fg='#6C8CB4',bg='#EBF4FF')
l4.config(font=('Arial-BoldMT',11))
l4.place(x=10,y=450)

cin=Entry(f2,width=25,fg='black',border=0,bg='#EBF4FF',font=('Arial',11))
cin.place(x=10,y=490)
cin.insert(0,'29446211')  

#LOGOUT
img2=PhotoImage(file='logout.png')
Button(f3,image=img2,border=0,bg='#EBF4FF',activebackground='#EBF4FF').place(x=200,y=50)

#Button start
button_image=PhotoImage(file='bouton-start.png')
Button(f3,border=0,image=button_image,bg='#EBF4FF',activebackground='#EBF4FF').place(x=50,y=35)
"""


