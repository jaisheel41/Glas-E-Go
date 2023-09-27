import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk


win = tk.Tk()
win.geometry('1166x718')
win.resizable(1, 1)
win.state('zoomed')
win.title('Login Page')

customer_id=IntVar()
operator_id=IntVar()
manager_id=IntVar()
customer_nameVar=StringVar()
customer_surnameVar=StringVar()
customer_emailVar=StringVar()
customer_passVar=StringVar()
customer_genderVar = IntVar()
#javaVar= IntVar()
#pythonVar= IntVar()
customer_contact_number=StringVar()

# ========================================================================
# ============ method to add user register data in database ========================================
# ========================================================================
   
def addNewCustomer():
    name=customer_nameVar.get()
    surname=customer_surnameVar.get()
    email=customer_emailVar.get()
    password=customer_passVar.get()
    gender=customer_genderVar.get()

    #prog=javaVar.get()
    conn = sqlite3.connect('StudentDatabase.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER_TABLE 
                   (CUSTOMER_NAME TEXT, CUSTOMER_SURNAME TEXT,CUSTOMER_GENDER TEXT, CUSTOMER_EMAIL TEXT,CUSTOMER_PASSWORD TEXT)''')
    count=cursor.execute('''INSERT INTO CUSTOMER_TABLE 
                         (CUSTOMER_NAME , CUSTOMER_SURNAME ,CUSTOMER_GENDER , CUSTOMER_EMAIL ,CUSTOMER_PASSWORD ) 
                         VALUES(?,?,?,?,?)''',
                         (name, surname, gender,email,password))
    
    if(cursor.rowcount>0):
        print ("Signup Done")
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
    cursor.execute('CREATE TABLE IF NOT EXISTS CUSTOMER_TABLE (Name TEXT,Email TEXT,Password Text,Gender TEXT,Programming TEXT)')
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
    
    

    reg_frame = Frame(registerScreen, bg='#040405', width=950, height=600)
    reg_frame.place(x=200, y=70)
    
    label = Label(reg_frame, text="Registration Here",width=20,fg="blue",font=("bold", 20))
    label.place(x=90,y=53)


    nameLabel = Label(reg_frame, text="Name",width=20,font=("bold", 10))
    nameLabel.place(x=80,y=130)

    nameEntery = Entry(reg_frame,textvar=customer_nameVar)
    nameEntery.place(x=240,y=130)

    surnameLabel = Label(reg_frame, text="Name",width=20,font=("bold", 10))
    surnameLabel.place(x=80,y=130)

    surnameEntery = Entry(reg_frame,textvar=customer_nameVar)
    surnameEntery.place(x=240,y=130)

    genderLabel = Label(reg_frame, text="Gender",width=20,font=("bold", 10))
    genderLabel.place(x=70,y=280)

    Radiobutton(reg_frame, text="Male",padx = 5, variable=customer_genderVar, value=1).place(x=235,y=280)
    Radiobutton(reg_frame, text="Female",padx = 20, variable=customer_genderVar, value=2).place(x=290,y=280)

    emailLabel = Label(reg_frame, text="Email",width=20,font=("bold", 10))
    emailLabel.place(x=68,y=180)

    emailEntry = Entry(reg_frame,textvar=customer_emailVar)
    emailEntry.place(x=240,y=180)

    passLabel = Label(reg_frame, text="Password",width=20,font=("bold", 10))
    passLabel.place(x=78,y=230)

    passEntry = Entry(reg_frame,textvar=customer_passVar,show='*')
    passEntry.place(x=240,y=230)

    
    """labelLanguage = Label(reg_frame, text="Programming",width=20,font=("bold", 10))
    labelLanguage.place(x=88,y=325)"""

    #Checkbutton(reg_frame, text="java", variable=javaVar).place(x=238,y=325)

    #Checkbutton(reg_frame, text="python", variable=pythonVar).place(x=310,y=325)

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
    lgn_frame = Frame(win, bg='#040405', width=950, height=600)
    lgn_frame.place(x=200, y=70)

    # ========================================================================
    # ========================================================
    # ========================================================================
    txt = "WELCOME"
    heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                            fg='white',
                            bd=5,
                            relief=FLAT)
    heading.place(x=80, y=30, width=300, height=30)

    # ========================================================================
    # ============ Left Side Image ================================================
    # ========================================================================
    side_image = Image.open('images/vector.png')
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(lgn_frame, image=photo, bg='#040405')
    side_image_label.image = photo
    side_image_label.place(x=5, y=100)

    # ========================================================================
    # ============ Sign In Image =============================================
    # ========================================================================
    sign_in_image = Image.open('images/hyy.png')
    photo = ImageTk.PhotoImage(sign_in_image)
    sign_in_image_label = Label(lgn_frame, image=photo, bg='#040405')
    sign_in_image_label.image = photo
    sign_in_image_label.place(x=620, y=130)

    # ========================================================================
    # ============ Sign In label =============================================
    # ========================================================================
    sign_in_label = Label(lgn_frame, text="Sign In", bg="#040405", fg="white",
                                font=("yu gothic ui", 17, "bold"))
    sign_in_label.place(x=650, y=240)

    emailLabel = Label(win, text="Email",width=20,font=("bold", 10))
    emailLabel.place(x=68,y=130)

    emailEntry = Entry(win,textvar=customer_emailVar)
    emailEntry.place(x=240,y=130)

    passwordLabel = Label(win, text="Password",width=20,font=("bold", 10))
    passwordLabel.place(x=68,y=180)

    passwordEntry = Entry(win,textvar=customer_passVar,show='*')
    passwordEntry.place(x=240,y=180)

    Button(win, text='Login Now',width=20,bg='blue',fg='white',pady=5,command=loginNow).place(x=180,y=230)

    Button(win,text="Have no Accout! Create one",bg="red",fg="white",font=("bold",10),command=registerWindow).place(x=170,y=280)

    win.mainloop()

LoginActivity()