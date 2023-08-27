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


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark


# Add tkdesigner to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
try:
    from tkdesigner.designer import Designer
except ModuleNotFoundError:
    raise RuntimeError("Couldn't add tkdesigner to the PATH.")


# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

# Required in order to add data files to Windows executable
path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)

output_path = ""

###### lien sfm #####
def know_more_clicked(event):
    instructions = (
        "https://www.sfmtechnologies.com/")
    webbrowser.open_new_tab(instructions)
    
#######
def make_label(master, x, y, h, w, *args, **kwargs):
    f = tk.Frame(master, height=h, width=w)
    f.pack_propagate(0)  # don't shrink
    f.place(x=x, y=y)

    label = tk.Label(f, *args, **kwargs)
    label.pack(fill=tk.BOTH, expand=1)

    return label


######## Login #########
def login():
    username=user.get()
    password=pas.get()
    
    if not username and not password:
            tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Username and Password.")
    elif not password:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Username.")
    elif not password:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Password.")
    
    else :
       
        reqUrl = "http://192.168.137.109:5000/user"

        headersList = {
         "Accept": "/",
         "Content-Type": "application/json"
         }
        payload = json.dumps({
        "username":username,
        "password":password
         })

        response = requests.request("GET", reqUrl, data=payload, headers=headersList)
        res=response.json()
        print(res)
        if(res!={'accept':False}):
            window.destroy()
            customtkinter.set_appearance_mode("System")
            customtkinter.set_default_color_theme("blue")
            w = customtkinter.CTk()
            w.geometry('1080x720')
            w.configure(bg='white')#12c4c0')
            w.resizable(0,0)
            w.title(' SFMTechnologies-Drive Test')
            w.iconbitmap('sfm.ico')
            
            
            #functions 
            
            
            #interface mission
            def mission():

                f2=Frame(w,width=900,height=455,bg='white')
                f2.place(x=0,y=45)
                l2=Label(f2,text='Mission Drive Test',fg='black',bg='white')
                l2.config(font=('Arial',20))
                l2.place(x=400,y=5)
                my_tree=ttk.Treeview(w)
                my_tree['columns']=("N°","Nom de mission","Trajet","Date","Technologie","Test")
                
                my_tree.column("#0",width=0,minwidth=0,anchor=CENTER)
                my_tree.column("N°",anchor=CENTER,width=50)
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
                
                for i in range(1,len(res['nom_miss'])+1):
                    my_tree.insert(parent='',index=i,iid=i,text='',values=(i,res['nom_miss'][i-1],res['trajet'][i-1],res['dates'][i-1],res['technologie'][i-1],res['test'][i-1]))
                my_tree.pack(pady=150,padx=10)
                
                
                def selected():
                    for selected_item in my_tree.selection():
                        item = my_tree.item(selected_item)
                        record = item['values']
                        # show a message
                        ch=record[2]
                        print(ch)
                        trajet(ch)
                        my_tree.destroy()
                        mybutton.destroy()
                global mybutton   
                mybutton=Button(w,text="Voir trajet",command=selected,padx=40).pack()
                
            
            
            #interface trajet   
            def trajet(ch):
                
                f2=Frame(w,width=900,height=455,bg='white')
                f2.place(x=0,y=45)
                l2=Label(f2,text=' Votre trajet',fg='#323335',bg='white')
                l2.config(font=('Arial',20))
                l2.place(x=300,y=10)
                my_lablel=LabelFrame(w)
                my_lablel.pack(pady=5)
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
                
                


            # interface historique

            def historique():
                
                f2=Frame(w,width=900,height=455,bg='white')
                f2.place(x=0,y=45)
                l2=Label(f2,text=' test',fg='#323335',bg='white')
                l2.config(font=('Arial',20))
                l2.place(x=500,y=10)
            
            # navbar
            global f1
            #frame right
            f1=Frame(w,width=200,height=1000,bg='#6C8CB4')
            f1.place(x=0,y=0)

            #frame left
            global f2
            f2=Frame(w,width=300,height=600,bg='#EBF4FF',padx=10)
            f2.place(x=1080,y=70)
            
            global f3
            f3=Frame(w,width=300,height=150,bg='#EBF4FF',padx=10)
            f3.place(x=1080,y=700)

            img3=PhotoImage(file='notification.png')
            Label(w,image=img3,border=0,bg='white').place(x=1300,y=15)

            img4=PhotoImage(file='profile.png')
            Label(w,image=img4,border=0,bg='white').place(x=1250,y=15)  

            img5=PhotoImage(file='search (1).png')
            Label(w,image=img5,border=0,bg='white').place(x=230,y=25)      

            #BOX FIND
            my_entry=Entry(w,font=('Arial',10),fg='#6C8CB4',width=50,border=2)
            my_entry.place(x=290,y=25)
            
            #button mission
            button_mission=PhotoImage(file='mission.png')
            Button(f1,border=0,image=button_mission,bg='#6C8CB4',activebackground='#6C8CB4',command=mission).place(x=10,y=200)
            Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='M I S S I O N',fg='white',command=mission).place(x=70,y=200)

            #button trajet

            button_trajet=PhotoImage(file='route.png')
            Button(f1,border=0,image=button_trajet,bg='#6C8CB4',activebackground='#6C8CB4',command=trajet).place(x=10,y=300)
            Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='T R A J E T',fg='white',command=trajet).place(x=70,y=300)


            #button stats

            button_stat=PhotoImage(file='statistiques.png')
            Button(f1,border=0,image=button_stat,bg='#6C8CB4',activebackground='#6C8CB4',command=historique).place(x=10,y=400)
            Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='S T A T S',fg='white',command=historique).place(x=70,y=400)

            #button setting

            button_sett=PhotoImage(file='settings.png')
            Button(f1,border=0,image=button_sett,bg='#6C8CB4',activebackground='#6C8CB4').place(x=10,y=500)
            Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='S E T T I N G',fg='white').place(x=70,y=500)

            #button help        

            button_help=PhotoImage(file='help.png')
            Button(f1,border=0,image=button_help,bg='#6C8CB4',activebackground='#6C8CB4').place(x=10,y=600)
            Button(f1,border=0,bg='#6C8CB4',activebackground='#6C8CB4',text='H E L P',fg='white').place(x=70,y=600)


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

            img=PhotoImage(file='sfm (1) (1).gif')
            Label(w,image=img,border=0,bg='white').place(x=550,y=50)
            w.mainloop()

              
            


#interface login
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
window = customtkinter.CTk()
logo = tk.PhotoImage(file=ASSETS_PATH / "sfm.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title(" SFMTechnologies-Drive Test")
window.geometry("980x480")
window.configure(bg="#3A7FF6")
canvas = tk.Canvas(
    window, bg="#3A7FF6", height=600, width=800,
    bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
f2=Frame(window,width=600,height=600,bg='white')
f2.place(x=650,y=0)

#Box user
my_image=PhotoImage(file=ASSETS_PATH / "TextBox_Bg.png")
Label(f2,image=my_image,border=0,bg='white').place(x=100,y=230)

#Box Pass
my_image2=PhotoImage(file=ASSETS_PATH / "TextBox_Bg.png")
Label(f2,image=my_image2,border=0,bg='white').place(x=100,y=400)

#Img SFM
img=PhotoImage(file='sfm (1) (1).gif')
Label(f2,image=img,border=0,bg='white').place(x=240,y=5)

#User
user = tk.Entry(f2,bd=0, bg="#F6F7F9", highlightthickness=0,fg='black',font=('Arial',12))
user.place(x=120.0, y=240, width=300.0, height=40)
user.focus()

#Pass
pas = tk.Entry(f2,bd=0, bg="#F6F7F9", highlightthickness=0,font=('Arial',12),show='*')
pas.place(x=120.0, y=410, width=300.0, height=40)
pas.focus()



Label(f2,text="Nom d'utilisateur",
    font=("Arial-BoldMT", int(13.0)), anchor="w",fg='#271E79',bg='white').place(x=120,y=190)

Label(f2,text="Mot de passe",
    font=("Arial-BoldMT", int(13.0)), anchor="w",fg='#271E79',bg='white').place(x=120,y=360)

title = tk.Label(
    text="  Bienvenue dans SFMTechnologies-Drive Test", bg="#3A7FF6",
    fg="white", font=("Arial-BoldMT", int(15)))
title.place(x=10.0, y=100.0)


info_text = tk.Label(
    text="Make your drive test\n Funny Game ",
    bg="#3A7FF6", fg="white", justify="center",anchor=CENTER,
    font=("Arial", int(25.0)))

info_text.place(x=90.0, y=250.0)

know_more = tk.Label(
    text="\nCliquer ici pour plus d'information",
    bg="#3A7FF6", fg="white", cursor="hand2",font=("Arial", int(12.0)))
know_more.place(x=40, y=450)
know_more.bind('<Button-1>', know_more_clicked)

button_image=PhotoImage(file='7f2caf68-cdc3-4dd3-a8b3-3f553f9084b1-removebg-preview.png')
Button(f2,border=0,image=button_image,command=login).place(x=190,y=510)

window.resizable(False, False)
window.mainloop()
