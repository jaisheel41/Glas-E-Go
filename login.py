import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from operator_landing_page import operator_landing

win = tk.Tk()
win.geometry('1166x718')
win.resizable(0,0)
win.state('zoomed')
win.title('Login Page')


# //////////////////// ids for primary and foreign keys //////////////////////////////////
customer_id=IntVar()
operator_id=IntVar()
manager_id=IntVar()

# ///////////////////////// customer data variables ///////////////////////////////////

customer_nameVar=StringVar()
customer_surnameVar=StringVar()
customer_emailVar=StringVar()
customer_passVar=StringVar()
customer_genderVar = IntVar()
customer_contact_number=StringVar()

# //////////////////////// oerator data variables ///////////////////////////

oprtator_name=StringVar()
operator_surname=StringVar()
operator_address=StringVar()
operator_email=StringVar()
operator_passport_no=StringVar()
operator_contact_no=StringVar()
operator_bank_account=StringVar()
operator_work_hrs=StringVar()
operator_shift=StringVar()
operator_allownces=StringVar()
operator_manager_id=StringVar()

# ========================================================================
# ============ method to add user register data in database ========================================
# ========================================================================

def addNewCustomer():
    name=customer_nameVar.get()
    surname=customer_surnameVar.get()
    email=customer_emailVar.get()
    password=customer_passVar.get()
    gender=customer_genderVar.get()
    conn = sqlite3.connect('StudentDatabase.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER_TABLE
                   (CUSTOMER_NAME TEXT, CUSTOMER_SURNAME TEXT,CUSTOMER_GENDER TEXT, CUSTOMER_EMAIL TEXT,CUSTOMER_PASSWORD TEXT)''')
    count=cursor.execute('''INSERT INTO CUSTOMER_TABLE
                         (CUSTOMER_ID INTEGER PRIMARY KEY, CUSTOMER_NAME , CUSTOMER_SURNAME ,CUSTOMER_GENDER , CUSTOMER_EMAIL ,CUSTOMER_PASSWORD )
                         VALUES(id,?,?,?,?,?)''',
                         (name, surname, gender,email,password))
    if(cursor.rowcount>0):
        print ("Signup Done")
        operator_landing_page.operator_landing()
    else:
        print ("Signup Error")
    conn.commit()

# ========================================================================
# ============ method to perform login ========================================
# ========================================================================

def loginNow():
    email=customer_emailVar.get()
    password=customer_passVar.get()
    conn = sqlite3.connect('StudentDatabase.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('Select * from CUSTOMER_TABLE Where Email=? AND Password=?',(email,password))
    if cursor.fetchone() is not None:
        print ("Welcome")
    else:
        print ("Login failed")

    conn.commit()

# ========================================================================
# ============ register page ========================================
# ========================================================================

def registerWindow():
    registerScreen=Toplevel(win)
    registerScreen.title("Registration Here")

    bg_frame = Image.open('images/background1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(registerScreen, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')
   
    reg_frame = Frame(registerScreen, bg='#d4d4ff', width=950, height=600)
    reg_frame.place(x=200, y=70)
   
    label = Label(reg_frame, text="Registration Here",width=20,fg="blue",font=("bold", 20))
    label.place(x=90,y=53)

    nameLabel = Label(reg_frame, text="Name",width=20,font=("bold", 10))
    nameLabel.place(x=90,y=130)

    nameEntery = Entry(reg_frame,textvar=customer_nameVar)
    nameEntery.place(x=260,y=130)

    surnameLabel = Label(reg_frame, text="Surname",width=20,font=("bold", 10))
    surnameLabel.place(x=90,y=160)

    surnameEntery = Entry(reg_frame,textvar=customer_surnameVar)
    surnameEntery.place(x=260,y=160)

    genderLabel = Label(reg_frame, text="Gender",width=20,font=("bold", 10))
    genderLabel.place(x=90,y=190)

    Radiobutton(reg_frame, text="Male",padx = 5, variable=customer_genderVar, value=1).place(x=260,y=188)
    Radiobutton(reg_frame, text="Female",padx = 20, variable=customer_genderVar, value=2).place(x=320,y=188)

    emailLabel = Label(reg_frame, text="Email",width=20,font=("bold", 10))
    emailLabel.place(x=90,y=220)

    emailEntry = Entry(reg_frame,textvar=customer_emailVar)
    emailEntry.place(x=260,y=220)

    passLabel = Label(reg_frame, text="Password",width=20,font=("bold", 10))
    passLabel.place(x=90,y=250)

    passEntry = Entry(reg_frame,textvar=customer_passVar,show='*')
    passEntry.place(x=260,y=250)

    Button(reg_frame, text='Submit',width=20,bg='blue',fg='white',pady=5,command=addNewCustomer).place(x=180,y=380)

# ========================================================================
# ============ Login Window by default (for now) ========================================
# ========================================================================

 

def LoginActivity():
    # ========================================================================
    # ============================background image============================
    # ========================================================================

    bg_frame = Image.open('images/background1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(win, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')

    # ====== Login Frame =========================

    lgn_frame = Frame(win, bg='#d4d4ff', width=950, height=600)
    lgn_frame.place(x=470, y=200)

    # ========================================================================
    # ========================================================
    # ========================================================================

    txt = "WELCOME"
    heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="#d4d4ff",
                            fg='black',
                            bd=10,
                            relief=FLAT)
    heading.place(x=300, y=30, width=300, height=30)

    # ========================================================================
    # ============ Left Side Image ================================================
    # ========================================================================

    side_image = Image.open('images/vector.png')
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(lgn_frame, image=photo, bg='#d4d4ff')
    side_image_label.image = photo
    side_image_label.place(x=5, y=100)

    # ========================================================================
    # ============ Sign In Image =============================================
    # ========================================================================

    sign_in_image = Image.open('images/hyy.png')
    photo = ImageTk.PhotoImage(sign_in_image)
    sign_in_image_label = Label(lgn_frame, image=photo, bg='#d4d4ff')
    sign_in_image_label.image = photo
    sign_in_image_label.place(x=620, y=130)

    # ========================================================================
    # ============ Sign In label =============================================
    # ========================================================================

    form_frame = Frame(lgn_frame, bg='#964b85', width=315, height=250)
    form_frame.place(x=550, y=300)

    sign_in_label = Label(lgn_frame, text="Sign In", bg="#d4d4ff", fg="black",
                                font=("yu gothic ui", 17, "bold"))
    sign_in_label.place(x=650, y=240)
    emailLabel = Label(form_frame, text="Email",width=10,font=("bold", 10))
    emailLabel.place(x=20,y=20)
    emailEntry = Entry(form_frame,width = 25,textvar=customer_emailVar)
    emailEntry.place(x=120,y=20)
    passwordLabel = Label(form_frame, text="Password",width=10,font=("bold", 10))
    passwordLabel.place(x=20,y=65)

    passwordEntry = Entry(form_frame,width = 25, textvar=customer_passVar)
    passwordEntry.place(x=120,y=65) 

    # //////////////// Password icon ////////////////////////////////////

    def show():
        hide_button = Button(form_frame, image=hide_image, command=hide, relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        hide_button.place(x=280, y=65)
        password_entry.config(show='')

    def hide():
        show_button = Button(form_frame, image=show_image, command=show, relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        show_button.place(x=280, y=65)
        password_entry.config(show='*')

    show_image = ImageTk.PhotoImage \
        (file='images/show.png')

    hide_image = ImageTk.PhotoImage \
        (file='images/hide.png')

    show_button = Button(form_frame, image=show_image, command=show, relief=FLAT,
                                activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2")
    show_button.place(x=280, y=65)

    # ///////////////////// Password icon eye ///////////////////////////////

    Button(form_frame, text='Login Now',width=23,bg='blue',fg='white',pady=5,command=operator_landing).place(x=60,y=120)

    Button(form_frame,text="Have no Accout! Create one",bg="red",fg="white",font=("bold",10), command=registerWindow).place(x=60,y=170)

    win.mainloop()

 

LoginActivity()