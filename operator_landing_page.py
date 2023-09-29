import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

def operator_landing():
    registerScreen=Toplevel(win)

    registerScreen.title("Registered Here")

    bg_frame = Image.open('images/background1.png')

    photo = ImageTk.PhotoImage(bg_frame)

    bg_panel = Label(registerScreen, image=photo)

    bg_panel.image = photo

    bg_panel.pack(fill='both', expand='yes')

 

 

    reg_frame = Frame(registerScreen, bg='#d4d4ff', width=950, height=600)

    reg_frame.place(x=200, y=70)

 

    label = Label(reg_frame, text="Registration Here",width=20,fg="blue",font=("bold", 20))

    label.place(x=90,y=53)

 