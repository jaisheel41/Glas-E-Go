import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
'''
# ////////////////////////// ids of databases /////////////////////////////

operator_id=IntVar()
bike_id=IntVar()

# ////////////////////////// operator variables ////////////////////////////
operator_nameVar=StringVar()
operator_surnameVar=StringVar()
operator_addressVar=StringVar()
operator_emailVar=StringVar()
operator_passportnoVar=StringVar()
contactVar=StringVar()
operator_bankaccountVar=StringVar()
operator_workinghoursVar=StringVar()
operator_shiftVar=StringVar()
operator_allowancesVar=StringVar()
operator_managerVar=StringVar()

# //////////////////////////// bike details variables /////////////////////////////////

bike_biketypeVar=StringVar()
bike_nameVar=StringVar()
bike_model=StringVar()
bike_location=StringVar()
bike_isavailable=BooleanVar()
bike_isservicing=BooleanVar()
bike_ischarged=BooleanVar()
'''
# =====================================================================================
# ================================== Remove this later on =============================
# =====================================================================================
'''
win = tk.Tk()
win.geometry('1166x718')
win.resizable(0,0)
win.state('zoomed')
win.title('Login Page')
'''
# =====================================================================================

def operator_landing(win):
    registerScreen=Toplevel(win)
    registerScreen.title("Operator Landing Page")

    bg_frame = Image.open('images/operator_bg.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(registerScreen, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')
    reg_frame = Frame(registerScreen, bg='#ffe16b', width=950, height=600)
    reg_frame.place(x=200, y=70)
    label = Label(reg_frame, text="Bike Tracking",width=20,fg="blue",font=("bold", 20))
    label.place(x=90,y=53)

'''

def mainActivity():
    bg_frame = Image.open('images/background1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(win, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')


    Button(win,text="Have no Accout! Create one",bg="red",fg="white",font=("bold",10), command=operator_landing).place(x=60,y=170)

 
'''