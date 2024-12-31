from tkinter import *
from tkinter import messagebox

import mysql.connector as c

# Create the main application window
root = Tk()
root.config(bg='#fff')
root.title('Login and SignUp')
root.geometry('925x500+300+200')

def show_frame(frame):
    frame.tkraise()

# Create container frame to hold all frames
container = Frame(root)
container.pack(fill=BOTH, expand=True)

# Configure the grid layout
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Create the frames
login_frame = Frame(container, bg='#fff')
signup_frame = Frame(container, bg='#fff')
welcome_frame = Frame(container, bg='sky blue')

for frame in (login_frame, signup_frame, welcome_frame):
    frame.grid(row=0, column=0, sticky='nsew')

#--------------------------------------------------------Login Frame----------------------------
def signin():
    con = c.connect(host='localhost', user='root', password='root', database='lms')
    cursor = con.cursor()
    query = "select * from signup where username='{}' and password='{}'".format(t1.get(), t2.get())
    cursor.execute(query)
    record = cursor.fetchone()
    if record is None:
        messagebox.showinfo("Sorry", message="Invalid ID or Password")
    else:
        show_frame(welcome_frame)

# Login frame widgets
img1 = PhotoImage(file='logo.png')
l1 = Label(login_frame, image=img1, bg='#fff')
l1.image = img1 

# Username entry
def on_enter1(e):
    t1.delete(0, 'end')

def on_leave1(e):
    name = t1.get()
    if name == '':
        t1.insert(0, 'Username')

t1 = Entry(login_frame, width=40, bg='sky blue', border=0, font=("Times New Roman", 18))
t1.insert(0, 'Username')
t1.bind('<FocusIn>', on_enter1)
t1.bind('<FocusOut>', on_leave1)

# Password entry
def on_enter2(e):
    t2.delete(0, 'end')

def on_leave2(e):
    name = t2.get()
    if name == '':
        t2.insert(0, 'Password')

t2 = Entry(login_frame, width=40, bg='sky blue', border=0, font=("Times New Roman", 18), show='*')
t2.insert(0, 'Password')
t2.bind('<FocusIn>', on_enter2)
t2.bind('<FocusOut>', on_leave2)

# Login button
b1 = Button(login_frame, width=25, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin, font=("Times New Roman", 10))
l2 = Label(login_frame, width=27, text="Don't have account?", fg='black', bg='white', font=('Microsoft YaHai UI Light', 10))
b2 = Button(login_frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda: show_frame(signup_frame))

# Place widgets in login frame
l1.place(x=250, y=40)
t1.place(x=120, y=150)
t2.place(x=120, y=200)
b1.place(x=400, y=300)
l2.place(x=120, y=310)
b2.place(x=290, y=310)

#--------------------------------------------------------SignUp Frame----------------------------
def signup():
    username = t3.get()
    email = t4.get()
    password = t5.get()
    confirm_pass = t6.get()

    if password != confirm_pass:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        query = "Insert into signup (username, email, password) values (%s, %s, %s)"
        cursor.execute(query, (username, email, password))
        con.commit()
        messagebox.showinfo("Success", "Data inserted successfully")
        messagebox.showinfo("Login", "Now click on Login button")
        con.close()
    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")

# SignUp frame widgets
img2 = PhotoImage(file='sign.png')
l3 = Label(signup_frame, image=img2, bg='#fff')
l3.image = img2
l3.place(x=50, y=40)

# Username entry
def on_enter3(e):
    t3.delete(0, 'end')

def on_leave3(e):
    name = t3.get()
    if name == '':
        t3.insert(0, 'Username')

t3 = Entry(signup_frame, width=40, bg='sky blue', border=0, font=("Times New Roman", 18))
t3.insert(0, 'Username')
t3.bind('<FocusIn>', on_enter3)
t3.bind('<FocusOut>', on_leave3)
t3.place(x=420, y=80)

# Email entry
def on_enter4(e):
    t4.delete(0, 'end')

def on_leave4(e):
    name = t4.get()
    if name == '':
        t4.insert(0, 'Email')

t4 = Entry(signup_frame, width=40, bg='sky blue', border=0, font=("Times New Roman", 18))
t4.insert(0, 'Email')
t4.bind('<FocusIn>', on_enter4)
t4.bind('<FocusOut>', on_leave4)
t4.place(x=420, y=120)

# Password entry
def on_enter5(e):
    t5.delete(0, 'end')

def on_leave5(e):
    name = t5.get()
    if name == '':
        t5.insert(0, 'Password')

t5 = Entry(signup_frame, width=40, bg='sky blue', border=0, font=("Times New Roman", 18), show='*')
t5.insert(0, 'Password')
t5.bind('<FocusIn>', on_enter5)
t5.bind('<FocusOut>', on_leave5)
t5.place(x=420, y=160)

# Confirm Password entry
def on_enter6(e):
    t6.delete(0, 'end')

def on_leave6(e):
    name = t6.get()
    if name == '':
        t6.insert(0, 'Confirm Password')

t6 = Entry(signup_frame, width=40, bg='sky blue', border=0, font=("Times New Roman", 18), show='*')
t6.insert(0, 'Confirm Password')
t6.bind('<FocusIn>', on_enter6)
t6.bind('<FocusOut>', on_leave6)
t6.place(x=420, y=200)

# SignUp button
b3 = Button(signup_frame, width=25, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup, font=("Times New Roman", 10))
b3.place(x=700, y=280)

# Login label and button
l4 = Label(signup_frame, width=27, text="Already have an account?", fg='black', bg='white', font=('Microsoft YaHai UI Light', 10))
l4.place(x=420, y=290)
b4 = Button(signup_frame, width=6, text='Login', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda: show_frame(login_frame))
b4.place(x=610, y=290)

#--------------------------------------------------------Welcome Frame----------------------------
Label(welcome_frame, text='Welcome to Instagram!', bg='sky blue', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

# Start by showing the login frame
show_frame(login_frame)

root.mainloop()
