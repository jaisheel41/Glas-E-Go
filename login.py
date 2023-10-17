import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
from operator_landing_page import *
import os

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


# ////////////////////////// operator variables ////////////////////////////
operator_nameVar=StringVar()
operator_surnameVar=StringVar()
operator_gendervar=StringVar()
operator_addressVar=StringVar()
operator_emailVar=StringVar()
operator_passportnoVar=StringVar()
operator_contactVar=StringVar()
operator_bankaccountVar=StringVar()
operator_workinghoursVar=StringVar()
operator_shiftVar=StringVar()
operator_allowancesVar=StringVar()
operator_managerVar=StringVar()
operator_passwordVar=StringVar()

# //////////////////////////// bike details variables /////////////////////////////////



# ///////////////////////////////// Database creation /////////////////////////////////////

conn = sqlite3.connect('Database.db')
with conn:
    cursor=conn.cursor()


# ////////////////////// to destroy a window ///////////////////////////////

def destroywindow(fr):
    fr.destroy()

# ========================================================================
# ============ method to add user register data in database ========================================
# ========================================================================


# ///////////////////////// generate customer ids ///////////////////////////////////////

def generate_customer_id():
    cursor.execute("SELECT MAX(id) FROM CUSTOMER_TABLE")
    max_id = cursor.fetchone()[0]
    return max_id + 1 if max_id else 1

def generate_operator_id():
    cursor.execute("SELECT MAX(id) FROM OPERATOR_TABLE")
    max_id = cursor.fetchone()[0]
    return max_id + 1 if max_id else 1

def generate_manager_id():
    cursor.execute("SELECT MAX(id) FROM MANAGER_TABLE")
    max_id = cursor.fetchone()[0]
    return max_id + 1 if max_id else 1
# //////////////////////////////////////////////////////////////////////////////////////
conn = sqlite3.connect('Database.db')
with conn:
    cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS CUSTOMER_TABLE
                (CUSTOMER_ID INTEGER PRIMARY KEY AUTOINCREMENT,CUSTOMER_NAME TEXT, CUSTOMER_SURNAME TEXT,CUSTOMER_GENDER TEXT, CUSTOMER_EMAIL TEXT,CUSTOMER_PASSWORD TEXT);""")
print("Table created")



def addNewCustomer():
    name=customer_nameVar.get()
    surname=customer_surnameVar.get()
    email=customer_emailVar.get()
    password=customer_passVar.get()
    gender=customer_genderVar.get()

    print("Called add customer method")
    
    count=cursor.execute("""INSERT INTO CUSTOMER_TABLE
                         (CUSTOMER_NAME , CUSTOMER_SURNAME ,CUSTOMER_GENDER , CUSTOMER_EMAIL ,CUSTOMER_PASSWORD )
                         VALUES(?,?,?,?,?)""",
                         (name, surname, gender,email,password))
    print("Data inserted")
    if(cursor.rowcount>0):
        print ("Signup Done")
        #LoginActivity()
        messagebox.showinfo("Success!!!","You have registered successfully. Now Login")
        #registerScreen.destroy()
    else:
        print ("Signup Error")
    
    conn.commit()
    

# ========================================================================
# ============ method to perform login ========================================
# ========================================================================

def loginNow():
    email=customer_emailVar.get()
    password=customer_passVar.get()
    conn = sqlite3.connect('Database.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute("Select CUSTOMER_PASSWORD from CUSTOMER_TABLE Where CUSTOMER_EMAIL=?",[email])
    check_password = cursor.fetchone()
    if check_password[0] == password:
        operator_landing(win)
        
    else:
        messagebox.showerror("Login Failed!", "Invalid username or password.")
        
    '''
        if cursor.fetchone() is not None:
            print ("Welcome")
            operator_landing()
        else:
            print ("Login failed")
    '''
    

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
   
    label = Label(reg_frame, text="Registration Here",width=22,fg="blue",font=("bold", 20))
    label.place(x=520,y=250)

    # /////////////////////////////// form for registration ///////////////////////////////////

    reg_form_frame = Frame(reg_frame, bg='#964b85', width=360, height=250)
    reg_form_frame.place(x=520, y=300)

    nameLabel = Label(reg_form_frame, text="Name",width=20,font=("bold", 10))
    nameLabel.place(x=20,y=30)

    nameEntery = Entry(reg_form_frame,textvar=customer_nameVar)
    nameEntery.place(x=190,y=30)

    surnameLabel = Label(reg_form_frame, text="Surname",width=20,font=("bold", 10))
    surnameLabel.place(x=20,y=60)

    surnameEntery = Entry(reg_form_frame,textvar=customer_surnameVar)
    surnameEntery.place(x=190,y=60)

    genderLabel = Label(reg_form_frame, text="Gender",width=20,font=("bold", 10))
    genderLabel.place(x=20,y=90)

    Radiobutton(reg_form_frame, text="Male",padx = 5, variable=customer_genderVar, value=1).place(x=190,y=90)
    Radiobutton(reg_form_frame, text="Female",padx = 20, variable=customer_genderVar, value=2).place(x=245,y=90)

    emailLabel = Label(reg_form_frame, text="Email",width=20,font=("bold", 10))
    emailLabel.place(x=20,y=120)

    emailEntry = Entry(reg_form_frame,textvar=customer_emailVar)
    emailEntry.place(x=190,y=120)

    passLabel = Label(reg_form_frame, text="Password",width=20,font=("bold", 10))
    passLabel.place(x=20,y=150)

    passEntry = Entry(reg_form_frame,textvar=customer_passVar,show='*')
    passEntry.place(x=190,y=150)

    Button(reg_form_frame, text='Submit',width=20,bg='blue',fg='white',pady=5,command=addNewCustomer).place(x=100,y=180)

    #destroywindow(registerScreen)

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
        passwordEntry.config(show='')

    def hide():
        show_button = Button(form_frame, image=show_image, command=show, relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        show_button.place(x=280, y=65)
        passwordEntry.config(show='*')

    show_image = ImageTk.PhotoImage \
        (file='images/show.png')

    hide_image = ImageTk.PhotoImage \
        (file='images/hide.png')

    show_button = Button(form_frame, image=show_image, command=hide, relief=FLAT,
                                activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2")
    show_button.place(x=280, y=65)

    # //////////////////// Clear email and password entry ////////////////

    emailEntry.delete(0,END)
    passwordEntry.delete(0,END)


    # ///////////////////// Password icon eye ///////////////////////////////

    Button(form_frame, text='Login Now',width=23,bg='blue',fg='white',pady=5, command=loginNow).place(x=60,y=120)

    Button(form_frame,text="Have no Accout! Create one",bg="red",fg="white",font=("bold",10), command=registerWindow).place(x=60,y=170)

    win.mainloop()



# =====================================================================================
# ================================== Operator add =============================
# =====================================================================================

def addOperator():
    name=operator_nameVar.get()
    surname=operator_surnameVar.get()
    gender=operator_gendervar.get()
    address=operator_addressVar.get()
    email=operator_emailVar.get()
    passportno=operator_passportnoVar.get()
    contactno=operator_contactVar.get()
    bankaccount=operator_bankaccountVar.get()
    workinghrs=operator_workinghoursVar.get()
    shifthrs=operator_shiftVar.get()
    allowances=operator_allowancesVar.get()
    manager=operator_managerVar.get()
    password=operator_passwordVar.get()

    
    cursor.execute("""CREATE TABLE IF NOT EXISTS OPERATOR_TABLE
                    (OPERATOR_ID INTEGER PRIMARY KEY AUTOINCREMENT, OPERATOR_NAME TEXT, OPERATOR_SURNAME TEXT,OPERATOR_GENDER TEXT, OPERATOR_ADDRESS TEXT,
                    OPERATOR_EMAIL TEXT,OPERATOR_PASSPORTNO TEXT, OPERATOR_CONTACTNO TEXT, OPERATOR_BANKACCOUNT TEXT, OPERATOR_WORKINGHOURS TEXT,
                OPERATOR_SHIFTHRS INTEGER,OPERATOR_ALLOWANCES INTEGER, OPERATOR_MANAGER TEXT,OPERATOR_PASSWORD TEXT);""")
    print("Table created")
    count=cursor.execute("""INSERT INTO CUSTOMER_TABLE
                            (OPERATOR_NAME, OPERATOR_SURNAME, OPERATOR_GENDER, OPERATOR_ADDRESS, OPERATOR_EMAIL, OPERATOR_PASSPORTNO, OPERATOR_CONTACTNO,
                        OPERATOR_BANKACCOUNT, OPERATOR_WORKINGHOURS, OPERATOR_SHIFTHRS, OPERATOR_ALLOWANCES, OPERATOR_MANAGER, OPERATOR_PASSWORD)
                            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                            (name,surname,gender,address,email,passportno,contactno,bankaccount,workinghrs,shifthrs,allowances,manager,password))
    print("Data inserted")
    if(cursor.rowcount>0):
        print ("Signup Done")
        #LoginActivity()
        messagebox.showinfo("Success!!!","You have registered successfully. Now Login")
        #registerScreen.destroy()
    else:
        print ("Signup Error")
    
    conn.commit()


# =====================================================================================
# ================================== Operator Login =============================
# =====================================================================================


def loginNowOp():
    email=operator_emailVar.get()
    password=operator_passwordVar.get()
    conn = sqlite3.connect('Database.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute("Select OPERATOR_PASSWORD from OPERATOR_TABLE Where OPERATOR_EMAIL=?",[email])
    check_password = cursor.fetchone()
    if check_password[0] == password:
        operator_landing(win)
        
    else:
        messagebox.showerror("Login Failed!", "Invalid username or password.")
        
    '''
        if cursor.fetchone() is not None:
            print ("Welcome")
            operator_landing()
        else:
            print ("Login failed")
    '''
    conn.commit()


# =====================================================================================
# ================================== Operator register =============================
# =====================================================================================



def OperatorRegisterActivity():
    OpregisterScreen=Toplevel(win)
    OpregisterScreen.title("Registration Operator Here")

    
    bg_frame = Image.open('images/background1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(OpregisterScreen, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')
    
    #OperatorLoginActivity.lgn_frame_op.destroy()
    
    label = Label(OpregisterScreen, text="Registration Here",width=20,fg="blue",font=("bold", 20))
    label.place(x=90,y=53)

    reg_frame = Frame(OpregisterScreen, bg='#d4d4ff', width=950, height=600)
    reg_frame.place(x=200, y=90)

    '''reg_frame = tk.Frame(window)
    reg_frame.pack(padx=20, pady=20)'''

    # Labels and Entry widgets using grid
    
    tk.Label(reg_frame, text="Id", width=20, font=("bold", 10)).grid(row=0, column=0)
    nameEntery = tk.Entry(reg_frame, textvariable=operator_nameVar)
    nameEntery.grid(row=0, column=1)

    tk.Label(reg_frame, text="Name", width=20, font=("bold", 10)).grid(row=1, column=0)
    nameEntery = tk.Entry(reg_frame, textvariable=operator_nameVar)
    nameEntery.grid(row=1, column=1)

    tk.Label(reg_frame, text="Surname", width=20, font=("bold", 10)).grid(row=2, column=0)
    surnameEntery = tk.Entry(reg_frame, textvariable=operator_surnameVar)
    surnameEntery.grid(row=2, column=1)

    tk.Label(reg_frame, text="Gender", width=20, font=("bold", 10)).grid(row=3, column=0)
    tk.Radiobutton(reg_frame, text="Male", padx=5, variable=operator_gendervar, value=1).grid(row=3, column=1)
    tk.Radiobutton(reg_frame, text="Female", padx=20, variable=operator_gendervar, value=2).grid(row=3, column=2)

    tk.Label(reg_frame, text="Email", width=20, font=("bold", 10)).grid(row=4, column=0)
    emailEntry = tk.Entry(reg_frame, textvariable=operator_emailVar)
    emailEntry.grid(row=4, column=1)

    tk.Label(reg_frame, text="Passport No", width=20, font=("bold", 10)).grid(row=5, column=0)
    passportEntry = tk.Entry(reg_frame, textvariable=operator_passportnoVar)
    passportEntry.grid(row=5, column=1)

    tk.Label(reg_frame, text="Contact No", width=20, font=("bold", 10)).grid(row=6, column=0)
    contactEntry = tk.Entry(reg_frame, textvariable=operator_contactVar)
    contactEntry.grid(row=6, column=1)

    tk.Label(reg_frame, text="Bank Account", width=20, font=("bold", 10)).grid(row=7, column=0)
    bankEntry = tk.Entry(reg_frame, textvariable=operator_bankaccountVar)
    bankEntry.grid(row=7, column=1)

    tk.Label(reg_frame, text="Working Hours", width=20, font=("bold", 10)).grid(row=8, column=0)
    workingHrsEntry = tk.Entry(reg_frame, textvariable=operator_workinghoursVar)
    workingHrsEntry.grid(row=8, column=1)

    tk.Label(reg_frame, text="Shift Hours", width=20, font=("bold", 10)).grid(row=9, column=0)
    shiftEntry = tk.Entry(reg_frame, textvariable=operator_shiftVar)
    shiftEntry.grid(row=9, column=1)

    tk.Label(reg_frame, text="Allowances", width=20, font=("bold", 10)).grid(row=10, column=0)
    allowanceEntry = tk.Entry(reg_frame, textvariable=operator_allowancesVar)
    allowanceEntry.grid(row=10, column=1)

    tk.Label(reg_frame, text="Manager", width=20, font=("bold", 10)).grid(row=11, column=0)
    managerEntry = tk.Entry(reg_frame, textvariable=operator_managerVar)
    managerEntry.grid(row=11, column=1)

    tk.Label(reg_frame, text="Password", width=20, font=("bold", 10)).grid(row=12, column=0)
    passEntry = tk.Entry(reg_frame, textvariable=operator_passwordVar, show='*')
    passEntry.grid(row=12, column=1)

    tk.Button(reg_frame, text='Submit', width=20, bg='blue', fg='white', pady=5, command=addOperator).grid(row=13, column=1)


    #destroywindow(registerScreen)


def OperatorLoginActivity():
    # ============================background image============================
    '''
    bg_frame = Image.open('images/background1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(win, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')
    '''
    # ====== Login Frame =========================

    #LoginActivity.lgn_frame.destroy()
    lgn_frame_op = Frame(win, bg='#d4d4ff', width=950, height=600)
    lgn_frame_op.place(x=470, y=200)

    # ========================================================

    txt = "WELCOME OPERATOR"
    heading = Label(lgn_frame_op, text=txt, font=('yu gothic ui', 25, "bold"), bg="#d4d4ff",
                            fg='black',
                            bd=10,
                            relief=FLAT)
    heading.place(x=300, y=30, width=350, height=30)

    # ============ Left Side Image ================================================

    side_image = Image.open('images/vector.png')
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(lgn_frame_op, image=photo, bg='#d4d4ff')
    side_image_label.image = photo
    side_image_label.place(x=5, y=100)

    # ============ Sign In Image =============================================

    sign_in_image = Image.open('images/hyy.png')
    photo = ImageTk.PhotoImage(sign_in_image)
    sign_in_image_label = Label(lgn_frame_op, image=photo, bg='#d4d4ff')
    sign_in_image_label.image = photo
    sign_in_image_label.place(x=620, y=130)

    # ============ Sign In label =============================================

    form_frame = Frame(lgn_frame_op, bg='#964b85', width=315, height=250)
    form_frame.place(x=550, y=300)

    sign_in_label = Label(lgn_frame_op, text="Sign In", bg="#d4d4ff", fg="black",
                                font=("yu gothic ui", 17, "bold"))
    sign_in_label.place(x=650, y=240)
    emailLabel = Label(form_frame, text="Email",width=10,font=("bold", 10))
    emailLabel.place(x=20,y=20)
    emailEntry = Entry(form_frame,width = 25,textvar=operator_emailVar)
    emailEntry.place(x=120,y=20)
    passwordLabel = Label(form_frame, text="Password",width=10,font=("bold", 10))
    passwordLabel.place(x=20,y=65)

    passwordEntry = Entry(form_frame,width = 25, textvar=operator_passportnoVar)
    passwordEntry.place(x=120,y=65) 

    # //////////////// Password icon ////////////////////////////////////

    def show():
        hide_button = Button(form_frame, image=hide_image, command=hide, relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        hide_button.place(x=280, y=65)
        passwordEntry.config(show='')

    def hide():
        show_button = Button(form_frame, image=show_image, command=show, relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        show_button.place(x=280, y=65)
        passwordEntry.config(show='*')

    show_image = ImageTk.PhotoImage \
        (file='images/show.png')

    hide_image = ImageTk.PhotoImage \
        (file='images/hide.png')

    show_button = Button(form_frame, image=show_image, command=hide, relief=FLAT,
                                activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2")
    show_button.place(x=280, y=65)

    # //////////////////// Clear email and password entry ////////////////

    emailEntry.delete(0,END)
    passwordEntry.delete(0,END)


    # ///////////////////// Password icon eye ///////////////////////////////

    Button(form_frame, text='Login Now',width=23,bg='blue',fg='white',pady=5, command=loginNowOp).place(x=60,y=120)

    Button(form_frame,text="Have no Accout! Create one",bg="red",fg="white",font=("bold",10), command=OperatorRegisterActivity).place(x=60,y=170)


def ManagerLoginActivity():
    # ============================background image============================
    '''
    bg_frame = Image.open('images/background1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(win, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')
    '''
    # ====== Login Frame =========================

    #LoginActivity.lgn_frame.destroy()
    lgn_frame_op = Frame(win, bg='#d4d4ff', width=950, height=600)
    lgn_frame_op.place(x=470, y=200)

    # ========================================================

    txt = "WELCOME MANAGER"
    heading = Label(lgn_frame_op, text=txt, font=('yu gothic ui', 25, "bold"), bg="#d4d4ff",
                            fg='black',
                            bd=10,
                            relief=FLAT)
    heading.place(x=300, y=30, width=350, height=30)

    # ============ Left Side Image ================================================

    side_image = Image.open('images/vector.png')
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(lgn_frame_op, image=photo, bg='#d4d4ff')
    side_image_label.image = photo
    side_image_label.place(x=5, y=100)

    # ============ Sign In Image =============================================

    sign_in_image = Image.open('images/hyy.png')
    photo = ImageTk.PhotoImage(sign_in_image)
    sign_in_image_label = Label(lgn_frame_op, image=photo, bg='#d4d4ff')
    sign_in_image_label.image = photo
    sign_in_image_label.place(x=620, y=130)

    # ============ Sign In label =============================================

    form_frame = Frame(lgn_frame_op, bg='#964b85', width=315, height=250)
    form_frame.place(x=550, y=300)

    sign_in_label = Label(lgn_frame_op, text="Sign In", bg="#d4d4ff", fg="black",
                                font=("yu gothic ui", 17, "bold"))
    sign_in_label.place(x=650, y=240)
    emailLabel = Label(form_frame, text="Email",width=10,font=("bold", 10))
    emailLabel.place(x=20,y=20)
    emailEntry = Entry(form_frame,width = 25,textvar=operator_emailVar)
    emailEntry.place(x=120,y=20)
    passwordLabel = Label(form_frame, text="Password",width=10,font=("bold", 10))
    passwordLabel.place(x=20,y=65)

    passwordEntry = Entry(form_frame,width = 25, textvar=operator_passportnoVar)
    passwordEntry.place(x=120,y=65) 

    # //////////////// Password icon ////////////////////////////////////

    def show():
        hide_button = Button(form_frame, image=hide_image, command=hide, relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        hide_button.place(x=280, y=65)
        passwordEntry.config(show='')

    def hide():
        show_button = Button(form_frame, image=show_image, command=show, relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        show_button.place(x=280, y=65)
        passwordEntry.config(show='*')

    show_image = ImageTk.PhotoImage \
        (file='images/show.png')

    hide_image = ImageTk.PhotoImage \
        (file='images/hide.png')

    show_button = Button(form_frame, image=show_image, command=hide, relief=FLAT,
                                activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2")
    show_button.place(x=280, y=65)

    # //////////////////// Clear email and password entry ////////////////

    emailEntry.delete(0,END)
    passwordEntry.delete(0,END)


    # ///////////////////// Password icon eye ///////////////////////////////

    Button(form_frame, text='Login Now',width=23,bg='blue',fg='white',pady=5, command=loginNowOp).place(x=60,y=120)

    Button(form_frame,text="Have no Accout! Create one",bg="red",fg="white",font=("bold",10), command=OperatorRegisterActivity).place(x=60,y=170)




# ========================================================================
# ============ Login Window by default (for now) ========================================
# ========================================================================

menu_bar = tk.Menu(win)
# Create a top-level menu
menu = tk.Menu(menu_bar, tearoff=0)
# Add menu items and associate them with functions
menu.add_command(label="Operator", command = OperatorLoginActivity)
menu.add_command(label="Manager", command = ManagerLoginActivity)
menu.add_command(label="Customer", command=LoginActivity)
# Add the menu to the menu bar
menu_bar.add_cascade(label="Admin Portal", menu=menu)
# Configure the root window to use the menu bar
win.config(menu=menu_bar)




LoginActivity()