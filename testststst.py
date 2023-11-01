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
operator_gendervar=IntVar()
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
 
# ////////////////////////////////////////// Databases created ////////////////////////////////
 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS payment (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        payment_status BOOLEAN
    )''')
 
cursor.execute('''CREATE TABLE IF NOT EXISTS customers
             (customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              surname TEXT,
              email TEXT,
              password TEXT,
              gender INTEGER,
              address TEXT,
              contact_number TEXT)''')
 
cursor.execute('''CREATE TABLE IF NOT EXISTS operators
             (operator_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              surname TEXT,
              gender TEXT,
              address TEXT,
              email TEXT,
              passport_no TEXT,
              contact TEXT,
              bank_account TEXT,
              working_hours TEXT,
              shift TEXT,
              allowances TEXT,
              manager TEXT,
              password TEXT)''')
 
cursor.execute('''CREATE TABLE IF NOT EXISTS managers
             (manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              surname TEXT,
              gender TEXT,
              address TEXT,
              email TEXT,
              passport_no TEXT,
              contact TEXT,
              bank_account TEXT,
              working_hours TEXT,
              shift TEXT,
              allowances TEXT,
              password TEXT)''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS BIKES (
        BIKE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        BIKE_TYPE TEXT,
        BIKE_NAME TEXT,
        BIKE_MODEL TEXT,
        BIKE_LOCATION TEXT,
        is_available BOOLEAN,
        is_servicing BOOLEAN,
        is_charged BOOLEAN
    )
''')
 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_util (
        id INTEGER,
        bike_id INTEGER,
        alloted_time DATETIME,
        return_time DATETIME,
        payment_id INTEGER,
        is_offer BOOLEAN,
        payment_status BOOLEAN,
        FOREIGN KEY (id) REFERENCES customers(id),
        FOREIGN KEY (bike_id) REFERENCES bikes(bike_id),
        FOREIGN KEY (payment_id) REFERENCES payment(payment_id)
    )''')
 
'''
# Insert data for managers
managers_data = [
    ("John Doe", "manager1@example.com", "male", "123 Manager St.", "manager1@example.com", "MGR123", "1234567890", "123-456-789", "9-5", "Day", "$1000", "manager1password"),
    ("Jane Smith", "manager2@example.com", "female", "456 Manager Ave.", "manager2@example.com", "MGR456", "9876543210", "987-654-321", "8-4", "Day", "$1200", "manager2password"),
    ("Bob Johnson", "manager3@example.com", "male", "789 Manager Rd.", "manager3@example.com", "MGR789", "5555555555", "555-555-555", "10-6", "Night", "$800", "manager3password")
]
 
cursor.executemany("INSERT INTO managers (name, surname, gender, address, email, passport_no, contact, bank_account, working_hours, shift, allowances, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", managers_data)
 
# Insert data for operators
operators_data = [
    ("Operator 1", "operator1@example.com", "male", "123 Operator St.", "operator1@example.com", "OPR123", "1234567890", "123-456-789", "9-5", "Day", "$100", "Manager 1", "operator1password"),
    ("Operator 2", "operator2@example.com", "female", "456 Operator Ave.", "operator2@example.com", "OPR456", "9876543210", "987-654-321", "8-4", "Day", "$120", "Manager 2", "operator2password"),
    ("Operator 3", "operator3@example.com", "male", "789 Operator Rd.", "operator3@example.com", "OPR789", "5555555555", "555-555-555", "10-6", "Night", "$80", "Manager 3", "operator3password")
]
 
cursor.executemany("INSERT INTO operators (name, surname, gender, address, email, passport_no, contact, bank_account, working_hours, shift, allowances, manager, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", operators_data)
 
# Insert data for customers
customers_data = [
    ("Alice", "customer1@example.com", "female", "123 Customer St.", "customer1@example.com", 1234567890, "customer1password"),
    ("Bob", "customer2@example.com", "male", "456 Customer Ave.", "customer2@example.com", 9876543210, "customer2password"),
    ("Carol", "customer3@example.com", "female", "789 Customer Rd.", "customer3@example.com", 5555555555, "customer3password"),
    ("David", "customer4@example.com", "male", "101 Customer Ln.", "customer4@example.com", 1111111111, "customer4password"),
    ("Eve", "customer5@example.com", "female", "202 Customer Blvd.", "customer5@example.com", 2222222222, "customer5password")
]
 
cursor.executemany("INSERT INTO customers (name, email, gender, address, email, contact_number, password) VALUES (?, ?, ?, ?, ?, ?, ?)", customers_data)
 
'''
 
 
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
 
cursor.execute("""CREATE TABLE IF NOT EXISTS CUSTOMER_TABLE
                (CUSTOMER_ID INTEGER PRIMARY KEY AUTOINCREMENT,CUSTOMER_NAME TEXT, CUSTOMER_SURNAME TEXT,CUSTOMER_GENDER TEXT, CUSTOMER_EMAIL TEXT,CUSTOMER_PASSWORD TEXT);""")
print("Table created")
 
 
 
def addNewCustomer():
    # customer_id
    name=customer_nameVar.get()
    surname=customer_surnameVar.get()
    email=customer_emailVar.get()
    password=customer_passVar.get()
    gender=customer_genderVar.get()
    contact_number=customer_contact_number.get()
 
    #customer_id += 1
 
    print("Called add customer method")
   
    count=cursor.execute("INSERT INTO customers (name, surname, email, password, gender, contact_number) VALUES (?, ?, ?, ?, ?, ?)",
              (name, surname, email, password, gender, contact_number))
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
    cursor.execute("SELECT * FROM customers WHERE email = ? AND password = ?", (email, password))
    check_password = cursor.fetchone()
    if check_password[0] == password:
        operator_landing(win)
    else:
        messagebox.showerror("Login Failed!", "Invalid username or password.")
 
    conn.commit()
 
 
 
 
def validate_text(text):
    # Check if the input text contains only alphabetic characters
    return text.isalpha()
 
def validate_numbers(P):
    # Check if the input contains only numeric characters
    return P.isdigit()
 
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
 
    side_image = Image.open('images/register_side_screen.png')
    #side_image = Image.open('images/vector.png')
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(reg_frame, image=photo, bg='#d4d4ff')
    side_image_label.image = photo
    side_image_label.place(x=5, y=60)
   
    label = Label(reg_frame, text="Create your account",width=20,fg="blue",font=("bold", 20))
    label.place(x=290,y=53)
 
    nameLabel = Label(reg_frame, text="First Name",width=20,font=("bold", 10))
    nameLabel.place(x=525,y=210)
   
    validate_text_func = win.register(validate_text)
 
    nameEntery = Entry(reg_frame,textvar=customer_nameVar, validate="key", validatecommand=(validate_text_func, "%P"))
    #nameEntery.pack()
    nameEntery.place(x=710,y=210,width=150)
 
    #nameEntery = Entry(reg_frame,textvar=customer_nameVar)
    #nameEntery.place(x=460,y=130)
 
    surnameLabel = Label(reg_frame, text="Last Name",width=20,font=("bold", 10))
    surnameLabel.place(x=525,y=240)
 
    surnameEntery = Entry(reg_frame,textvar=customer_surnameVar)
    surnameEntery.place(x=710,y=240,width=150)
 
    genderLabel = Label(reg_frame, text="Gender",width=20,font=("bold", 10))
    genderLabel.place(x=525,y=270)
 
    Radiobutton(reg_frame, text="Male",padx = 5, variable=customer_genderVar, value=1).place(x=710,y=270)
    Radiobutton(reg_frame, text="Female",padx = 5, variable=customer_genderVar, value=2).place(x=780,y=270)
    Radiobutton(reg_frame, text="Other",padx = 1, variable=customer_genderVar, value=3).place(x=860,y=270)
   
    emailLabel = Label(reg_frame, text="Email",width=20,font=("bold", 10))
    emailLabel.place(x=525,y=300)
 
    emailEntry = Entry(reg_frame,textvar=customer_emailVar)
    emailEntry.place(x=710,y=300,width=150)
 
    NumberLabel = Label(reg_frame, text="Mobile Number",width=20,font=("bold", 10))
    NumberLabel.place(x=525,y=330)
 
    validate_numbers_func = win.register(validate_numbers)
 
    NumberEntry = Entry(reg_frame,textvar=customer_contact_number,validate="key", validatecommand=(validate_numbers_func, "%P"))
    #NumberEntry.pack()
 
    #NumberEntry = Entry(reg_frame,textvar=customer_contact_number)
    NumberEntry.place(x=710,y=330,width=150)
 
    passLabel = Label(reg_frame, text="Password",width=20,font=("bold", 10))
    passLabel.place(x=525,y=360)
 
    passEntry = Entry(reg_frame,textvar=customer_passVar,show='*')
    passEntry.place(x=710,y=360,width=150)
 
    Button(reg_frame, text='Submit',width=20,bg='blue',fg='white',pady=5,command=addNewCustomer).place(x=620,y=420)
# ========================================================================
# ============ Login Window by default (for now) ========================================
# ========================================================================
 
 
 
def LoginActivity():
    # ========================================================================
    # ============================background image============================
    # ========================================================================
 
    bg_frame = Image.open('images/Bike.png')
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
 
    txt = "Welcome to GLAS'E-GO"
    heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 20, "bold"), bg="#d4d4ff",
                            fg='black',
                            bd=10,
                            relief=FLAT)
    heading.place(x=300, y=30, width=300, height=30)
 
    # ========================================================================
    # ============ Left Side Image ================================================
    # ========================================================================
 
    side_image = Image.open('images/bikesmain.png')
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
 
    Button(form_frame, text='Login Now',width=23,bg='blue',fg='white',pady=5, command=loginNow).place(x=70,y=120)
 
    Button(form_frame,text="Dont't have an account? Create new",bg="red",fg="white",font=("bold",10), command=registerWindow).place(x=45,y=170)
 
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
    passport_no=operator_passportnoVar.get()
    contact=operator_contactVar.get()
    bank_account=operator_bankaccountVar.get()
    working_hours=operator_workinghoursVar.get()
    shift=operator_shiftVar.get()
    allowances=operator_allowancesVar.get()
    manager=operator_managerVar.get()
    password=operator_passwordVar.get()
 
    count=cursor.execute("INSERT INTO operators (name, surname, gender, address, email, passport_no, contact, bank_account, working_hours, shift, allowances, manager, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (name, surname, gender, address, email, passport_no, contact, bank_account, working_hours, shift, allowances, manager, password))
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
    cursor.execute("SELECT * FROM operators WHERE email = ? AND password = ?", (email, password))
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
    OpregisterScreen.title("Operator Registration Here")
 
   
    bg_frame = Image.open('images/background1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(OpregisterScreen, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')
   
    #OperatorLoginActivity.lgn_frame_op.destroy()
   
    label = Label(OpregisterScreen, text="Registration Here",width=20,fg="blue",font=("bold", 20))
    label.place(x=490,y=53)
 
    operator_reg_frame = Frame(OpregisterScreen, bg='#d4d4ff', width=950, height=600)
    operator_reg_frame.place(x=200, y=90)
 
    side_image = Image.open('images/operator.png')
    #side_image = Image.open('images/vector.png')
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(OpregisterScreen, image=photo, bg='#d4d4ff')
    side_image_label.image = photo
    side_image_label.place(x=200, y=150)
 
    operator_reg_form_frame = Frame(operator_reg_frame, bg='#964b85', width=460, height=400)
    operator_reg_form_frame.place(x=480, y=110)
 
    '''reg_frame = tk.Frame(window)
    reg_frame.pack(padx=20, pady=20)'''
 
    # Labels and Entry widgets using grid
 
    nameLabel = Label(operator_reg_frame, text="First Name",width=20,font=("bold", 10))
    nameLabel.place(x=525,y=180)
   
    validate_text_func = win.register(validate_text)
 
    nameEntery = Entry(operator_reg_frame,textvar=operator_nameVar, validate="key", validatecommand=(validate_text_func, "%P"))
    #nameEntery.pack()
    nameEntery.place(x=710,y=180,width=150)
 
    #nameEntery = Entry(reg_frame,textvar=customer_nameVar)
    #nameEntery.place(x=460,y=130)
 
    surnameLabel = Label(operator_reg_frame, text="Last Name",width=20,font=("bold", 10))
    surnameLabel.place(x=525,y=210)
 
    surnameEntery = Entry(operator_reg_frame,textvar=operator_surnameVar)
    surnameEntery.place(x=710,y=210,width=150)
 
    genderLabel = Label(operator_reg_frame, text="Gender",width=20,font=("bold", 10))
    genderLabel.place(x=525,y=240)
 
    Radiobutton(operator_reg_frame, text="Male",padx = 5, variable=operator_gendervar, value=1).place(x=710,y=240)
    Radiobutton(operator_reg_frame, text="Female",padx = 5, variable=operator_gendervar, value=2).place(x=780,y=240)
    Radiobutton(operator_reg_frame, text="Other",padx = 1, variable=operator_gendervar, value=3).place(x=860,y=240)
   
    emailLabel = Label(operator_reg_frame, text="Email",width=20,font=("bold", 10))
    emailLabel.place(x=525,y=270)
 
    emailEntry = Entry(operator_reg_frame,textvar=operator_emailVar)
    emailEntry.place(x=710,y=270,width=150)
 
    passport_label = Label(operator_reg_frame, text="Passport No", width=20, font=("bold", 10))
    passport_label.place(x=525,y=300)
 
    passportEntry = tk.Entry(operator_reg_frame, textvariable=operator_passportnoVar)
    passportEntry.place(x=710,y=300,width=150)
 
    NumberLabel = Label(operator_reg_frame, text="Contact No",width=20,font=("bold", 10))
    NumberLabel.place(x=525,y=330)
 
    validate_numbers_func = win.register(validate_numbers)
 
    contactEntry = Entry(operator_reg_frame,textvar=operator_contactVar,validate="key", validatecommand=(validate_numbers_func, "%P"))
    #NumberEntry.pack()
 
    #NumberEntry = Entry(reg_frame,textvar=customer_contact_number)
    contactEntry.place(x=710,y=330,width=150)
 
    bank_label = Label(operator_reg_frame, text="Bank Account", width=20, font=("bold", 10))
    bank_label.place(x=525,y=360)
 
    bankEntry = tk.Entry(operator_reg_frame, textvariable=operator_bankaccountVar)
    bankEntry.place(x=710,y=360,width=150)
 
    workhours_label = Label(operator_reg_frame, text="Working Hours", width=20, font=("bold", 10))
    workhours_label.place(x=525,y=390)
 
    workingHrsEntry = tk.Entry(operator_reg_frame, textvariable=operator_workinghoursVar)
    workingHrsEntry.place(x=710,y=390,width=150)
 
    passLabel = Label(operator_reg_frame, text="Password",width=20,font=("bold", 10))
    passLabel.place(x=525,y=420)
 
    passEntry = Entry(operator_reg_frame,textvar=operator_passwordVar,show='*')
    passEntry.place(x=710,y=420,width=150)
 
 
   
    # tk.Label(operator_reg_form_frame, text="Id", width=20, font=("bold", 10)).grid(row=0, column=0)
    # idEntery = tk.Entry(operator_reg_form_frame, textvariable=operator_id, state='readonly')
    # idEntery.grid(row=0, column=1)
    # #idEntery.insert(0, generate_operator_id())
 
    # tk.Label(operator_reg_form_frame, text="First Name", width=20, font=("bold", 10)).grid(row=1, column=0)
    # nameEntery = tk.Entry(operator_reg_form_frame, textvariable=operator_nameVar)
    # nameEntery.grid(row=1, column=1)
 
    # tk.Label(operator_reg_form_frame, text="Last Name", width=20, font=("bold", 10)).grid(row=2, column=0)
    # surnameEntery = tk.Entry(operator_reg_form_frame, textvariable=operator_surnameVar)
    # surnameEntery.grid(row=2, column=1)
 
    # tk.Label(operator_reg_form_frame, text="Gender", width=20, font=("bold", 10)).grid(row=3, column=0)
    # tk.Radiobutton(operator_reg_form_frame, text="Male", padx=5, variable=operator_gendervar, value=1).grid(row=3, column=1)
    # tk.Radiobutton(operator_reg_form_frame, text="Female", padx=1, variable=operator_gendervar, value=2).grid(row=3, column=2)
    # tk.Radiobutton(operator_reg_form_frame, text="Other", padx=1, variable=operator_gendervar, value=3).grid(row=3, column=3)
 
    # tk.Label(operator_reg_form_frame, text="Email", width=20, font=("bold", 10)).grid(row=4, column=0)
    # emailEntry = tk.Entry(operator_reg_form_frame, textvariable=operator_emailVar)
    # emailEntry.grid(row=4, column=1)
 
    # tk.Label(operator_reg_form_frame, text="Passport No", width=20, font=("bold", 10)).grid(row=5, column=0)
    # passportEntry = tk.Entry(operator_reg_form_frame, textvariable=operator_passportnoVar)
    # passportEntry.grid(row=5, column=1)
 
    # tk.Label(operator_reg_form_frame, text="Contact No", width=20, font=("bold", 10)).grid(row=6, column=0)
    # contactEntry = tk.Entry(operator_reg_form_frame, textvariable=operator_contactVar)
    # contactEntry.grid(row=6, column=1)
 
    # tk.Label(operator_reg_form_frame, text="Bank Account", width=20, font=("bold", 10)).grid(row=7, column=0)
    # bankEntry = tk.Entry(operator_reg_form_frame, textvariable=operator_bankaccountVar)
    # bankEntry.grid(row=7, column=1)
 
    # tk.Label(operator_reg_form_frame, text="Working Hours", width=20, font=("bold", 10)).grid(row=8, column=0)
    # workingHrsEntry = tk.Entry(operator_reg_form_frame, textvariable=operator_workinghoursVar)
    # workingHrsEntry.grid(row=8, column=1)
 
    # tk.Label(operator_reg_form_frame, text="Shift Hours", width=20, font=("bold", 10)).grid(row=9, column=0)
    # shiftEntry = tk.Entry(operator_reg_form_frame, textvariable=operator_shiftVar)
    # shiftEntry.grid(row=9, column=1)
 
    # tk.Label(operator_reg_form_frame, text="Allowances", width=20, font=("bold", 10)).grid(row=10, column=0)
    # allowanceEntry = tk.Entry(operator_reg_form_frame, textvariable=operator_allowancesVar)
    # allowanceEntry.grid(row=10, column=1)
 
    # tk.Label(operator_reg_form_frame, text="Manager", width=20, font=("bold", 10)).grid(row=11, column=0)
    # managerEntry = tk.Entry(operator_reg_form_frame, textvariable=operator_managerVar)
    # managerEntry.grid(row=11, column=1)
 
    # tk.Label(operator_reg_form_frame, text="Password", width=20, font=("bold", 10)).grid(row=12, column=0)
    # passEntry = tk.Entry(operator_reg_form_frame, textvariable=operator_passwordVar, show='*')
    # passEntry.grid(row=12, column=1)
 
    Button(operator_reg_frame, text='Submit',width=20,bg='blue',fg='white',pady=5,command=addOperator).place(x=620,y=460)
 
    #destroywindow(registerScreen)
 
 
def addManager():
    name=operator_nameVar.get()
    surname=operator_surnameVar.get()
    gender=operator_gendervar.get()
    address=operator_addressVar.get()
    email=operator_emailVar.get()
    passport_no=operator_passportnoVar.get()
    contact=operator_contactVar.get()
    bank_account=operator_bankaccountVar.get()
    working_hours=operator_workinghoursVar.get()
    shift=operator_shiftVar.get()
    allowances=operator_allowancesVar.get()
    password=operator_passwordVar.get()
 
    count=cursor.execute("INSERT INTO managers (name, surname, gender, address, email, passport_no, contact, bank_account, working_hours, shift, allowances, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (name, surname, gender, address, email, passport_no, contact, bank_account, working_hours, shift, allowances, password))
    print("Data inserted")
    if(cursor.rowcount>0):
        print ("Signup Done")
        #LoginActivity()
        messagebox.showinfo("Success!!!","You have registered successfully. Now Login")
        #registerScreen.destroy()
    else:
        print ("Signup Error")
   
    conn.commit()
 
def ManagerRegisterActivity():
   
    mnregisterScreen=Toplevel(win)
    mnregisterScreen.title("Manager Registration Here")
 
    bg_frame = Image.open('images/background1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(mnregisterScreen, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')
   
    #OperatorLoginActivity.lgn_frame_op.destroy()
 
    label = Label(mnregisterScreen, text="Registration Here",width=20,fg="blue",font=("bold", 20))
    label.place(x=490,y=53)
 
    reg_frame_mn = Frame(mnregisterScreen, bg='#d4d4ff', width=1050, height=600)
    reg_frame_mn.place(x=100, y=90)
 
    side_image = Image.open('images/manager.png')
    #side_image = Image.open('images/vector.png')
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(mnregisterScreen, image=photo, bg='#d4d4ff')
    side_image_label.image = photo
    side_image_label.place(x=110, y=160)
 
    manager_reg_form_frame = Frame(reg_frame_mn, bg='#964b85', width=410, height=410)
    manager_reg_form_frame.place(x=560, y=90)
 
    # Labels and Entry widgets using grid
 
    nameLabel = Label(reg_frame_mn, text="First Name",width=20,font=("bold", 10))
    nameLabel.place(x=575,y=180)
   
    validate_text_func = win.register(validate_text)
 
    nameEntery = Entry(reg_frame_mn,textvar=operator_nameVar, validate="key", validatecommand=(validate_text_func, "%P"))
    #nameEntery.pack()
    nameEntery.place(x=750,y=180,width=150)
 
    #nameEntery = Entry(reg_frame,textvar=customer_nameVar)
    #nameEntery.place(x=460,y=130)
 
    surnameLabel = Label(reg_frame_mn, text="Last Name",width=20,font=("bold", 10))
    surnameLabel.place(x=575,y=210)
 
    surnameEntery = Entry(reg_frame_mn,textvar=operator_surnameVar)
    surnameEntery.place(x=750,y=210,width=150)
 
    genderLabel = Label(reg_frame_mn, text="Gender",width=20,font=("bold", 10))
    genderLabel.place(x=575,y=240)
 
    Radiobutton(reg_frame_mn, text="Male",padx = 5, variable=operator_gendervar, value=1).place(x=750,y=240)
    Radiobutton(reg_frame_mn, text="Female",padx = 1, variable=operator_gendervar, value=2).place(x=820,y=240)
    Radiobutton(reg_frame_mn, text="Other",padx = 1, variable=operator_gendervar, value=3).place(x=890,y=240)
   
    emailLabel = Label(reg_frame_mn, text="Email",width=20,font=("bold", 10))
    emailLabel.place(x=575,y=270)
 
    emailEntry = Entry(reg_frame_mn,textvar=operator_emailVar)
    emailEntry.place(x=750,y=270,width=150)
 
    passport_label = Label(reg_frame_mn, text="Passport No", width=20, font=("bold", 10))
    passport_label.place(x=575,y=300)
 
    passportEntry = tk.Entry(reg_frame_mn, textvariable=operator_passportnoVar)
    passportEntry.place(x=750,y=300,width=150)
 
    NumberLabel = Label(reg_frame_mn, text="Contact No",width=20,font=("bold", 10))
    NumberLabel.place(x=575,y=330)
 
    validate_numbers_func = win.register(validate_numbers)
 
    contactEntry = Entry(reg_frame_mn,textvar=operator_contactVar,validate="key", validatecommand=(validate_numbers_func, "%P"))
    #NumberEntry.pack()
 
    #NumberEntry = Entry(reg_frame,textvar=customer_contact_number)
    contactEntry.place(x=750,y=330,width=150)
 
    bank_label = Label(reg_frame_mn, text="Bank Account", width=20, font=("bold", 10))
    bank_label.place(x=575,y=360)
 
    bankEntry = tk.Entry(reg_frame_mn, textvariable=operator_bankaccountVar)
    bankEntry.place(x=750,y=360,width=150)
 
    workhours_label = Label(reg_frame_mn, text="Working Hours", width=20, font=("bold", 10))
    workhours_label.place(x=575,y=390)
 
    workingHrsEntry = tk.Entry(reg_frame_mn, textvariable=operator_workinghoursVar)
    workingHrsEntry.place(x=750,y=390,width=150)
 
    allowances_label = Label(reg_frame_mn, text="Allowances", width=20, font=("bold", 10))
    allowances_label.place(x=575,y=420)
 
    allowanceEntry = tk.Entry(reg_frame_mn, textvariable=operator_allowancesVar)
    allowanceEntry.place(x=750,y=390,width=150)
 
    passLabel = Label(reg_frame_mn, text="Password",width=20,font=("bold", 10))
    passLabel.place(x=575,y=420)
 
    passEntry = Entry(reg_frame_mn,textvar=operator_passwordVar,show='*')
    passEntry.place(x=750,y=420,width=150)
 
   
   
    # tk.Label(manager_reg_form_frame, text="Id", width=20, font=("bold", 10)).grid(row=0, column=0)
    # nameEntery = tk.Entry(manager_reg_form_frame, textvariable=operator_nameVar)
    # nameEntery.grid(row=0, column=1)
 
    # tk.Label(manager_reg_form_frame, text="Name", width=20, font=("bold", 10)).grid(row=1, column=0)
    # nameEntery = tk.Entry(manager_reg_form_frame, textvariable=operator_nameVar)
    # nameEntery.grid(row=1, column=1)
 
    # tk.Label(manager_reg_form_frame, text="Surname", width=20, font=("bold", 10)).grid(row=2, column=0)
    # surnameEntery = tk.Entry(manager_reg_form_frame, textvariable=operator_surnameVar)
    # surnameEntery.grid(row=2, column=1)
 
    # tk.Label(manager_reg_form_frame, text="Gender", width=20, font=("bold", 10)).grid(row=3, column=0)
    # tk.Radiobutton(manager_reg_form_frame, text="Male", padx=5, variable=operator_gendervar, value=1).grid(row=3, column=1)
    # tk.Radiobutton(manager_reg_form_frame, text="Female", padx=20, variable=operator_gendervar, value=2).grid(row=3, column=2)
 
    # tk.Label(manager_reg_form_frame, text="Email", width=20, font=("bold", 10)).grid(row=4, column=0)
    # emailEntry = tk.Entry(manager_reg_form_frame, textvariable=operator_emailVar)
    # emailEntry.grid(row=4, column=1)
 
    # tk.Label(manager_reg_form_frame, text="Passport No", width=20, font=("bold", 10)).grid(row=5, column=0)
    # passportEntry = tk.Entry(manager_reg_form_frame, textvariable=operator_passportnoVar)
    # passportEntry.grid(row=5, column=1)
 
    # tk.Label(manager_reg_form_frame, text="Contact No", width=20, font=("bold", 10)).grid(row=6, column=0)
    # contactEntry = tk.Entry(manager_reg_form_frame, textvariable=operator_contactVar)
    # contactEntry.grid(row=6, column=1)
 
    # tk.Label(manager_reg_form_frame, text="Bank Account", width=20, font=("bold", 10)).grid(row=7, column=0)
    # bankEntry = tk.Entry(manager_reg_form_frame, textvariable=operator_bankaccountVar)
    # bankEntry.grid(row=7, column=1)
 
    # tk.Label(manager_reg_form_frame, text="Working Hours", width=20, font=("bold", 10)).grid(row=8, column=0)
    # workingHrsEntry = tk.Entry(manager_reg_form_frame, textvariable=operator_workinghoursVar)
    # workingHrsEntry.grid(row=8, column=1)
 
    # tk.Label(manager_reg_form_frame, text="Shift Hours", width=20, font=("bold", 10)).grid(row=9, column=0)
    # shiftEntry = tk.Entry(manager_reg_form_frame, textvariable=operator_shiftVar)
    # shiftEntry.grid(row=9, column=1)
 
    # tk.Label(manager_reg_form_frame, text="Allowances", width=20, font=("bold", 10)).grid(row=10, column=0)
    # allowanceEntry = tk.Entry(manager_reg_form_frame, textvariable=operator_allowancesVar)
    # allowanceEntry.grid(row=10, column=1)
 
    # tk.Label(manager_reg_form_frame, text="Password", width=20, font=("bold", 10)).grid(row=12, column=0)
    # passEntry = tk.Entry(manager_reg_form_frame, textvariable=operator_passwordVar, show='*')
    # passEntry.grid(row=12, column=1)
    Button(reg_frame_mn, text='Submit',width=20,bg='blue',fg='white',pady=5,command=addOperator).place(x=680,y=460)
    #tk.Button(manager_reg_form_frame, text='Submit', width=20, bg='blue', fg='white', pady=5, command=addManager).grid(row=13, column=1)
 
 
 
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
 
    txt = "Welcome Operator"
    heading = Label(lgn_frame_op, text=txt, font=('yu gothic ui', 20, "bold"), bg="#d4d4ff",
                            fg='black',
                            bd=10,
                            relief=FLAT)
    heading.place(x=300, y=30, width=350, height=30)
 
    # ============ Left Side Image ================================================
 
    side_image = Image.open('images/electric.png')
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
 
    Button(form_frame, text='Login Now',width=23,bg='blue',fg='white',pady=5, command=loginNowOp).place(x=70,y=120)
 
    Button(form_frame,text="Dont't have an account? Create new",bg="red",fg="white",font=("bold",10), command=OperatorRegisterActivity).place(x=60,y=170)
 
 
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
 
    txt = "Welcome Manager"
    heading = Label(lgn_frame_op, text=txt, font=('yu gothic ui', 20, "bold"), bg="#d4d4ff",
                            fg='black',
                            bd=10,
                            relief=FLAT)
    heading.place(x=300, y=30, width=350, height=30)
 
    # ============ Left Side Image ================================================
 
    side_image = Image.open('images/man.png')
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
 
    Button(form_frame, text='Login Now',width=23,bg='blue',fg='white',pady=5, command=ManagerLoginActivity).place(x=70,y=120)
 
    Button(form_frame,text="Dont't have an account? Create new",bg="red",fg="white",font=("bold",10), command=ManagerRegisterActivity).place(x=60,y=170)
 
 
 
 
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