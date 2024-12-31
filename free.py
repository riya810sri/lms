from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as c

# Create the main application window
root = Tk()
root.config(bg='#fff')
root.title('Login and SignUp')
root.geometry('2000x650')

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
student_frame = Frame(container, bg='#fff')
book_issue_frame = Frame(container, bg='lightpink')
search_book_frame = Frame(container, bg='#fff')
return_book_frame = Frame(container, bg='lightpink')

for frame in (login_frame, signup_frame, welcome_frame, student_frame, book_issue_frame, search_book_frame, return_book_frame):
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
# Function to show a message box
def show_message(message):
    messagebox.showinfo("Information", message)

# Load the background image
background_image = Image.open("LIB1.jpg")  # Replace with your image path
background_image = background_image.resize((2000, 1000), Image.LANCZOS)  # Resize if necessary
bg_image = ImageTk.PhotoImage(background_image)


# Create a canvas to hold the background image
canvas = Canvas(welcome_frame, width=700, height=400)
canvas.pack(fill="both", expand=True)


# Set the background image on the canvas
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Add a welcome label
welcome_label = Label(welcome_frame, text="Welcome to the Library", font=("Helvetica", 30), bg='YELLOW')
welcome_label.place(relx=0.5, rely=0.1, anchor='center')

# Add a frame for buttons
button_frame = Frame(welcome_frame, bg='lightblue')
button_frame.place(relx=0.5, rely=0.4, anchor='center')

# Example buttons with pop-up messages
button1 = Button(button_frame,height=2, text="Student Card", command=lambda: show_frame(student_frame), bg='#90EE90', width=50)
button1.pack(pady=5)


button2 = Button(button_frame,height=2, text="Book Issue Card", command=lambda: show_frame(book_issue_frame), bg='#FFD700', width=50)
button2.pack(pady=6)

button3 = Button(button_frame,height=2, text="Return Book", command=lambda: show_frame(return_book_frame), bg='#FFB6C1', width=50)
button3.pack(pady=5)

button4 = Button(button_frame,height=2, text="Search Books", command=lambda: show_frame(search_book_frame), bg='lightyellow', width=50)
button4.pack(pady=5)

button5 = Button(button_frame,height=2, text="Exit", command=welcome_frame.destroy, bg='#FF6347', width=30)
button5.pack(pady=5)

#--------------------------------------------------Student Frame-----------------------------------------------------------

def save():
    student_id = student_id_Entry.get()
    student_name = student_name_Entry.get()
    student_email = student_email_Entry.get()
    student_phone = student_phone_Entry.get()
    student_add = student_add_Entry.get()
    student_mem_date = student_mem_date_Entry.get()
    
    # Check if any field is empty
    if not student_id or not student_name or not student_email or not student_phone or not student_add or not student_mem_date:
        messagebox.showerror("Error", "Please fill all the details")
        return
    
    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        query = "INSERT INTO members (member_id, name, email, phone, address, membership_date) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (student_id, student_name, student_email, student_phone, student_add, student_mem_date))
        con.commit()
        messagebox.showinfo("Success", "Data inserted successfully")
        con.close()
        
        # Clear the entry fields
        student_id_Entry.delete(0, END)
        student_name_Entry.delete(0, END)
        student_email_Entry.delete(0, END)
        student_phone_Entry.delete(0, END)
        student_add_Entry.delete(0, END)
        student_mem_date_Entry.delete(0, END)
        
    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")


def search():
    student_id = student_id_Entry.get()
    student_name = student_name_Entry.get()
    
    # Check if both fields are empty
    if not student_id and not student_name:
        messagebox.showerror("Error", "Please enter either Student ID or Student Name to search")
        return
    
    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        if student_id:
            query = "SELECT * FROM members WHERE member_id = %s"
            cursor.execute(query, (student_id,))
        else:
            query = "SELECT * FROM members WHERE name = %s"
            cursor.execute(query, (student_name,))
        
        record = cursor.fetchone()
        con.close()
        
        if record:
            student_id_Entry.delete(0, END)
            student_name_Entry.delete(0, END)
            student_email_Entry.delete(0, END)
            student_phone_Entry.delete(0, END)
            student_add_Entry.delete(0, END)
            student_mem_date_Entry.delete(0, END)
            
            student_id_Entry.insert(0, record[0])
            student_name_Entry.insert(0, record[1])
            student_email_Entry.insert(0, record[2])
            student_phone_Entry.insert(0, record[3])
            student_add_Entry.insert(0, record[4])
            student_mem_date_Entry.insert(0, record[5])
            
            messagebox.showinfo("Found", f"Student found: {record}")
        else:
            messagebox.showinfo("Not Found", "Student not found in the database")
        
    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")


def update():
    student_id = student_id_Entry.get()
    student_name = student_name_Entry.get()
    student_email = student_email_Entry.get()
    student_phone = student_phone_Entry.get()
    student_add = student_add_Entry.get()
    student_mem_date = student_mem_date_Entry.get()
    
    # Check if any field is empty
    if not student_id or not student_name or not student_email or not student_phone or not student_add or not student_mem_date:
        messagebox.showerror("Error", "Please fill all the details to update")
        return

    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        query = """
            UPDATE members 
            SET name = %s, email = %s, phone = %s, address = %s, membership_date = %s 
            WHERE member_id = %s
        """
        cursor.execute(query, (student_name, student_email, student_phone, student_add, student_mem_date, student_id))
        con.commit()
        messagebox.showinfo("Success", "Data updated successfully")
        con.close()

    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")


def delete():
    student_id = student_id_Entry.get()
    
    # Check if student_id field is empty
    if not student_id:
        messagebox.showerror("Error", "Please enter Student ID to delete")
        return

    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        query = "DELETE FROM members WHERE member_id = %s"
        cursor.execute(query, (student_id,))
        con.commit()
        con.close()
        
        # Clear the entry fields
        student_id_Entry.delete(0, END)
        student_name_Entry.delete(0, END)
        student_email_Entry.delete(0, END)
        student_phone_Entry.delete(0, END)
        student_add_Entry.delete(0, END)
        student_mem_date_Entry.delete(0, END)
        
        messagebox.showinfo("Success", "Record deleted successfully")
        
    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")


img3 = PhotoImage(file='student.png')
l4 = Label(student_frame, image=img3, bg="#FFF")
l4.image = img3
l4.place(x=180, y=30)

def on_enter7(e):
    student_mem_date_Entry.delete(0, 'end')

def on_leave7(e):
    name = student_mem_date_Entry.get()
    if name == '':
        student_mem_date_Entry.insert(0, 'YY-MM-DD')


student_label = Label(student_frame, text = "Student Entry!", fg="#FF8C00", bg="#fff", font=('Times New Roman', 40, 'bold'))
student_label.place(x=330, y=50)

student_id = Label(student_frame, text="STUDENT ID:", bg="#fff", font=("Georgia", 15))
student_id.place(x=100, y=205)

student_id_Entry = Entry(student_frame, width=30, fg="#FF8C00", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_id_Entry.place(x=400, y=200)

student_name = Label(student_frame, text="NAME:", bg="#fff", font=("Georgia", 15))
student_name.place(x=100, y=245)

student_name_Entry = Entry(student_frame, width=30, fg="#FF8C00", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_name_Entry.place(x=400, y=240)

student_email = Label(student_frame, text="EMAIL:", bg="#fff", font=("Georgia", 15))
student_email.place(x=100, y=285)

student_email_Entry = Entry(student_frame, width=30, fg="#FF8C00", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_email_Entry.place(x=400, y=280)

student_phone = Label(student_frame, text="PHONE:", bg="#fff", font=("Georgia", 15))
student_phone.place(x=100, y=325)

student_phone_Entry = Entry(student_frame, width=30, fg="#FF8C00", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_phone_Entry.place(x=400, y=320)

student_add = Label(student_frame, text="ADDRESS:", bg="#fff", font=("Georgia", 15))
student_add.place(x=100, y=365)

student_add_Entry = Entry(student_frame, width=30, fg="#FF8C00", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_add_Entry.place(x=400, y=360)

student_mem_date = Label(student_frame, text="MEMBERSHIP DATE:", bg="#fff", font=("Georgia", 15))
student_mem_date.place(x=100, y=405)

student_mem_date_Entry = Entry(student_frame, width=30, fg="#FF8C00", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_mem_date_Entry.insert(0, 'YY-MM-DD')
student_mem_date_Entry.bind('<FocusIn>', on_enter7)
student_mem_date_Entry.bind('<FocusOut>', on_leave7)
student_mem_date_Entry.place(x=400, y=400)

b5 = Button(student_frame, width=8, text="SAVE", border=0, padx='4', pady='4', bg='#FF8C00', cursor='hand2', command=save, fg='#fff', font=('Times New Roman', 10, 'bold'))
b5.place(x=800, y=220)

b6 = Button(student_frame, width=8, text="SEARCH", border=0, padx='4', pady='4', bg='#FF8C00', cursor='hand2', command=search, fg='#fff', font=('Times New Roman', 10, 'bold'))
b6.place(x=800, y=270)

b7 = Button(student_frame, width=8, text="UPDATE", border=0, padx='4', pady='4', bg='#FF8C00', cursor='hand2', command=update, fg='#fff', font=('Times New Roman', 10, 'bold'))
b7.place(x=800, y=320)

b8 = Button(student_frame, width=8, text="DELETE", border=0, padx='4', pady='4', bg='#FF8C00', cursor='hand2', fg='#fff',command=delete, font=('Times New Roman', 10, 'bold'))                             
b8.place(x=800, y=370)

b9 = Button(student_frame, width=8, text="BACK", border=0, padx='4', pady='4', bg='#FF0000', cursor='hand2', fg='#fff',command=lambda: show_frame(welcome_frame), font=('Times New Roman', 10, 'bold'))                             
b9.place(x=800, y=450)
#-----------------------------------------Book Issue Card--------------------------------------------------------------------

def save():
    book_id = book_id_Entry.get()
    book_title = book_title_Entry.get()
    author_name = author_name_Entry.get()
    student_id = student_id_Entry.get()
    student_name = student_name_Entry.get()
    issue_date = issue_date_Entry.get()
    return_date = return_date_Entry.get()

    # Check if any field is empty
    if not book_id or not book_title or not author_name or not student_id or not student_name or not issue_date or not return_date:
        messagebox.showerror("Error", "Please fill all the details")
        return

    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        query = "INSERT INTO book_issue_card (book_id, book_title, author_name, student_id, student_name, issue_date, return_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (book_id, book_title, author_name, student_id, student_name, issue_date, return_date))
        con.commit()
        messagebox.showinfo("Success", "Data inserted successfully")
        con.close()

        # Clear the entry fields
        book_id_Entry.delete(0, END)
        book_title_Entry.delete(0, END)
        author_name_Entry.delete(0, END)
        student_id_Entry.delete(0, END)
        student_name_Entry.delete(0, END)
        issue_date_Entry.delete(0, END)
        return_date_Entry.delete(0, END)

    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")

def search():
    book_id = book_id_Entry.get()
    student_id = student_id_Entry.get()

    # Check if both fields are empty
    if not book_id and not student_id:
        messagebox.showerror("Error", "Please enter either Book ID or Student ID to search")
        return

    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        if book_id:
            query = "SELECT * FROM book_issue_card WHERE book_id = %s"
            cursor.execute(query, (book_id,))
        else:
            query = "SELECT * FROM book_issue_card WHERE student_id = %s"
            cursor.execute(query, (student_id,))
        record = cursor.fetchone()
        con.close()

        if record:
            book_id_Entry.delete(0, END)
            book_title_Entry.delete(0, END)
            author_name_Entry.delete(0, END)
            student_id_Entry.delete(0, END)
            student_name_Entry.delete(0, END)
            issue_date_Entry.delete(0, END)
            return_date_Entry.delete(0, END)

            book_id_Entry.insert(0, record[0])
            book_title_Entry.insert(0, record[1])
            author_name_Entry.insert(0, record[2])
            student_id_Entry.insert(0, record[3])
            student_name_Entry.insert(0, record[4])
            issue_date_Entry.insert(0, record[5])
            return_date_Entry.insert(0, record[6])

            messagebox.showinfo("Found", f"Record found: {record}")
        else:
            messagebox.showinfo("Not Found", "Record not found in the database")

    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")

def update():
    book_id = book_id_Entry.get()
    book_title = book_title_Entry.get()
    author_name = author_name_Entry.get()
    student_id = student_id_Entry.get()
    student_name = student_name_Entry.get()
    issue_date = issue_date_Entry.get()
    return_date = return_date_Entry.get()

    # Check if any field is empty
    if not book_id or not book_title or not author_name or not student_id or not student_name or not issue_date or not return_date:
        messagebox.showerror("Error", "Please fill all the details to update")
        return

    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        query = """UPDATE book_issue_card SET book_title = %s, author_name = %s, student_id = %s, student_name = %s, issue_date = %s, return_date = %s WHERE book_id = %s"""
        cursor.execute(query, (book_title, author_name, student_id, student_name,issue_date, return_date, book_id))
        con.commit()
        messagebox.showinfo("Success", "Data updated successfully")
        con.close()

    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")

def delete():
    book_id = book_id_Entry.get()
    
    # Check if book_id field is empty
    if not book_id:
        messagebox.showerror("Error", "Please enter Student ID to delete")
        return

    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        query = "DELETE FROM book_issue_card WHERE book_id = %s"
        cursor.execute(query, (book_id,))
        con.commit()
        con.close()
        
        # Clear the entry fields
        book_id_Entry.delete(0, END)
        book_title_Entry.delete(0, END)
        author_name_Entry.delete(0, END)
        student_id_Entry.delete(0, END)
        student_name_Entry.delete(0, END)
        issue_date_Entry.delete(0, END)
        return_date_Entry.delete(0, END)
        
        messagebox.showinfo("Success", "Record deleted successfully")
        
    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")

img = Image.open('image-23.png')
img.thumbnail((100, 100))  # width, height
img4 = ImageTk.PhotoImage(img)
l5 = Label(book_issue_frame, image=img4, bg="lightpink")
l5.image = img4
l5.place(x=150,y=30)


def on_enter8(e):
    issue_date_Entry.delete(0, 'end')

def on_leave8(e):
    name = issue_date_Entry.get()
    if name == '':
        issue_date_Entry.insert(0, 'YY-MM-DD')

def on_enter9(e):
    return_date_Entry.delete(0, 'end')

def on_leave9(e):
    name = return_date_Entry.get()
    if name == '':
        return_date_Entry.insert(0, 'YY-MM-DD')

ISSUE_label = Label(book_issue_frame, text = "ISSUE CARD DETAILS!",fg="red", bg="lightpink",font=('Times New Roman', 40, 'bold'))
ISSUE_label.place(x=330, y=50)

book_id = Label(book_issue_frame, text="BOOK ID:", bg="lightpink", font=("Georgia", 15))
book_id.place(x=100, y=205)

book_id_Entry = Entry(book_issue_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
book_id_Entry.place(x=400, y=200)

book_title = Label(book_issue_frame, text="BOOK NAME:", bg="lightpink", font=("Georgia", 15))
book_title.place(x=100, y=245)

book_title_Entry = Entry(book_issue_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
book_title_Entry.place(x=400, y=240)

author_name = Label(book_issue_frame, text="AUTHOR NAME:", bg="lightpink", font=("Georgia", 15))
author_name.place(x=100, y=285)

author_name_Entry = Entry(book_issue_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
author_name_Entry.place(x=400, y=280)

student_id = Label(book_issue_frame, text="STUDENT ID:", bg="lightpink", font=("Georgia", 15))
student_id.place(x=100, y=325)

student_id_Entry = Entry(book_issue_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_id_Entry.place(x=400, y=320)

student_name = Label(book_issue_frame, text="STUDENT NAME:", bg="lightpink", font=("Georgia", 15))
student_name.place(x=100, y=365)

student_name_Entry = Entry(book_issue_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_name_Entry.place(x=400, y=360)

issue_date = Label(book_issue_frame, text="ISSUE DATE:", bg="lightpink", font=("Georgia", 15))
issue_date.place(x=100, y=405)

issue_date_Entry = Entry(book_issue_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
issue_date_Entry.insert(0, 'YY-MM-DD')
issue_date_Entry.bind('<FocusIn>', on_enter8)
issue_date_Entry.bind('<FocusOut>', on_leave8)
issue_date_Entry.place(x=400, y=400)

return_date = Label(book_issue_frame, text="RETURN DATE:", bg="lightpink", font=("Georgia", 15))
return_date.place(x=100, y=445)

return_date_Entry = Entry(book_issue_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
return_date_Entry.insert(0, 'YY-MM-DD')
return_date_Entry.bind('<FocusIn>', on_enter9)
return_date_Entry.bind('<FocusOut>', on_leave9)
return_date_Entry.place(x=400, y=440)

b10 = Button(book_issue_frame, width=8, text="SAVE", border=0, padx='4', pady='4', bg='RED', cursor='hand2', command=save, fg='#fff', font=('Times New Roman', 10, 'bold'))
b10.place(x=800, y=220)

b11 = Button(book_issue_frame, width=8, text="SEARCH", border=0, padx='4', pady='4', bg='RED', cursor='hand2', command=search, fg='#fff', font=('Times New Roman', 10, 'bold'))
b11.place(x=800, y=270)

b12 = Button(book_issue_frame, width=8, text="UPDATE", border=0, padx='4', pady='4', bg='RED', cursor='hand2', command=update, fg='#fff', font=('Times New Roman', 10, 'bold'))
b12.place(x=800, y=320)

b13 = Button(book_issue_frame, width=8, text="DELETE", border=0, padx='4', pady='4', bg='RED', cursor='hand2', fg='#fff',command=delete, font=('Times New Roman', 10, 'bold'))                               
b13.place(x=800, y=370)

b14 = Button(book_issue_frame, width=8, text="BACK", border=0, padx='4', pady='4', bg='#FF0000', cursor='hand2', fg='#fff',command=lambda: show_frame(welcome_frame), font=('Times New Roman', 10, 'bold'))                             
b14.place(x=800, y=450)

#--------------------------------------------------------Search Book Frame--------------------------------------------------------

img5 = PhotoImage(file='book.png')
l6 = Label(search_book_frame, image=img5, bg="#FFF")
l6.image = img5
l6.place(x=10, y=10)

# Add Book Category Label and Dropdown
book_category_label = Label(search_book_frame, text="CATEGORY:", bg="#fff", font=("Georgia", 15))
book_category_label.place(x=400, y=40)

book_category_options = ["CS/IT", "Electronics", "Mechanical", "BCA", "BSc", "Pharmacy"]
book_category_var = StringVar(search_book_frame)
book_category_var.set(book_category_options[0])  # Set default value

book_category_menu = OptionMenu(search_book_frame, book_category_var, *book_category_options)
book_category_menu.config(width=28, fg="#000080", bg="#D3D3D3", font=("Times New Roman", 13, "bold"))
book_category_menu.place(x=570, y=40)

book_name = Label(search_book_frame, text="BOOK NAME:", bg="#fff", font=("Georgia", 15))
book_name.place(x=400, y=80)

book_name_Entry = Entry(search_book_frame, width=30, fg="#000080", bg="#D3D3D3", font=("Times New Roman", 15, "bold"))
book_name_Entry.place(x=570, y=80)

author = Label(search_book_frame, text="AUTHOR:", bg="#fff", font=("Georgia", 15))
author.place(x=400, y=120)

author_Entry = Entry(search_book_frame, width=30, fg="#000080", bg="#D3D3D3", font=("Times New Roman", 15, "bold"))
author_Entry.place(x=570, y=120)

quantity = Label(search_book_frame, text="QUANTITY:", bg="#fff", font=("Georgia", 15))
quantity.place(x=400, y=160)

quantity_Entry = Entry(search_book_frame, width=30, fg="#000080", bg="#D3D3D3", font=("Times New Roman", 15, "bold"))
quantity_Entry.place(x=570, y=160)

def search_books():
    category = book_category_var.get()
    book_name = book_name_Entry.get()
    author_name = author_Entry.get()
    
    if not book_name and not author_name:
        messagebox.showerror("Error", "Please enter Book Name or Author Name to search")
        return
    
    try:
        con = c.connect(host='localhost', user='root', password='root', database='lms')
        cursor = con.cursor()
        
        if book_name:
            query = f"SELECT * FROM {category.replace('/', '_')} WHERE book_name = %s"
            cursor.execute(query, (book_name,))
        else:
            query = f"SELECT * FROM {category.replace('/', '_')} WHERE author_name = %s"
            cursor.execute(query, (author_name,))

            
        record = cursor.fetchone()
        
        if record:
            messagebox.showinfo("Found", f"Book found: {record}")
            book_name_Entry.delete(0, END)
            book_name_Entry.insert(0, record[1])
            author_Entry.delete(0, END)
            author_Entry.insert(0, record[2])
            quantity_Entry.delete(0, END)
            quantity_Entry.insert(0, record[3])
        else:
            messagebox.showinfo("Not Found", "Book not found in the selected category.")
        
        con.close()
        
    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")

def save_book():
    category = book_category_var.get()
    book_name = book_name_Entry.get()
    author_name = author_Entry.get()
    quantity = quantity_Entry.get()
    
    if not book_name or not author_name or not quantity:
        messagebox.showerror("Error", "Please fill all the details")
        return
    
    try:
        con = c.connect(host='localhost', user='root', password='root', database='lms')
        cursor = con.cursor()
        
        query = f"INSERT INTO {category.replace('/', '_')} (book_name, author_name, quantity) VALUES (%s, %s, %s)"
        cursor.execute(query, (book_name, author_name, quantity))
        con.commit()
        
        messagebox.showinfo("Success", "Book has been saved in the database successfully")
        
        con.close()
        
        # Clear the entry fields
        book_name_Entry.delete(0, END)
        author_Entry.delete(0, END)
        quantity_Entry.delete(0, END)
        
    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")

def delete_book():
    category = book_category_var.get()
    book_name = book_name_Entry.get()
    author_name = author_Entry.get()
    
    if not book_name and not author_name:
        messagebox.showerror("Error", "Please enter Book Name or Author Name to delete")
        return
    
    try:
        con = c.connect(host='localhost', user='root', password='root', database='lms')
        cursor = con.cursor()
        
        if book_name:
            query = f"DELETE FROM {category.replace('/', '_')} WHERE book_name = %s"
            cursor.execute(query, (book_name,))
        else:
            query = f"DELETE FROM {category.replace('/', '_')} WHERE author_name = %s"
            cursor.execute(query, (author_name,))
        
        con.commit()
        
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Book has been deleted from the database successfully")
        else:
            messagebox.showinfo("Not Found", "Book not found in the selected category.")
        
        con.close()
        
        # Clear the entry fields
        book_name_Entry.delete(0, END)
        author_Entry.delete(0, END)
        quantity_Entry.delete(0, END)
        
    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")

# Buttons
b15 = Button(search_book_frame, width=8, text="SEARCH", border=0, padx='4', pady='4', bg='#D3D3D3', cursor='hand2', fg='#000080', font=('Times New Roman', 10, 'bold'), command=search_books)
b15.place(x=450, y=300)

b16 = Button(search_book_frame, width=8, text="SAVE", border=0, padx='4', pady='4', bg='#D3D3D3', cursor='hand2', fg='#000080', font=('Times New Roman', 10, 'bold'), command=save_book)
b16.place(x=550, y=300)

b17 = Button(search_book_frame, width=8, text="DELETE", border=0, padx='4', pady='4', bg='#D3D3D3', cursor='hand2', fg='#000080', font=('Times New Roman', 10, 'bold'), command=delete_book)
b17.place(x=650, y=300)

b18 = Button(search_book_frame, width=8, text="BACK", border=0, padx='4', pady='4', bg='#D3D3D3', cursor='hand2', fg='#000080', font=('Times New Roman', 10, 'bold'), command= lambda: show_frame(welcome_frame))
b18.place(x=750, y=300)

#------------------------------------------------------Return Book Frame-------------------------------------------------------

def save():
    book_id = book_id_Entry.get()
    book_title = book_title_Entry.get()
    author_name = author_name_Entry.get()
    student_id = student_id_Entry.get()
    student_name = student_name_Entry.get()
    issue_date = issue_date_Entry.get()
    return_date = return_date_Entry.get()

    # Check if any field is empty
    if not book_id or not book_title or not author_name or not student_id or not student_name or not issue_date or not return_date:
        messagebox.showerror("Error", "Please fill all the details")
        return

    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        query = "INSERT INTO book_issue_card (book_id, book_title, author_name, student_id, student_name, issue_date, return_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (book_id, book_title, author_name, student_id, student_name, issue_date, return_date))
        con.commit()
        messagebox.showinfo("Success", "Data inserted successfully")
        con.close()

        # Clear the entry fields
        book_id_Entry.delete(0, END)
        book_title_Entry.delete(0, END)
        author_name_Entry.delete(0, END)
        student_id_Entry.delete(0, END)
        student_name_Entry.delete(0, END)
        issue_date_Entry.delete(0, END)
        return_date_Entry.delete(0, END)

    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")

def search():
    book_id = book_id_Entry.get()
    student_id = student_id_Entry.get()

    # Check if both fields are empty
    if not book_id and not student_id:
        messagebox.showerror("Error", "Please enter either Book ID or Student ID to search")
        return

    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        if book_id:
            query = "SELECT * FROM book_issue_card WHERE book_id = %s"
            cursor.execute(query, (book_id,))
        else:
            query = "SELECT * FROM book_issue_card WHERE student_id = %s"
            cursor.execute(query, (student_id,))
        record = cursor.fetchone()
        con.close()

        if record:
            book_id_Entry.delete(0, END)
            book_title_Entry.delete(0, END)
            author_name_Entry.delete(0, END)
            student_id_Entry.delete(0, END)
            student_name_Entry.delete(0, END)
            issue_date_Entry.delete(0, END)
            return_date_Entry.delete(0, END)

            book_id_Entry.insert(0, record[0])
            book_title_Entry.insert(0, record[1])
            author_name_Entry.insert(0, record[2])
            student_id_Entry.insert(0, record[3])
            student_name_Entry.insert(0, record[4])
            issue_date_Entry.insert(0, record[5])
            return_date_Entry.insert(0, record[6])

            messagebox.showinfo("Found", f"Record found: {record}")
        else:
            messagebox.showinfo("Not Found", "Record not found in the database")

    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")

def update():
    book_id = book_id_Entry.get()
    book_title = book_title_Entry.get()
    author_name = author_name_Entry.get()
    student_id = student_id_Entry.get()
    student_name = student_name_Entry.get()
    issue_date = issue_date_Entry.get()
    return_date = return_date_Entry.get()

    # Check if any field is empty
    if not book_id or not book_title or not author_name or not student_id or not student_name or not issue_date or not return_date:
        messagebox.showerror("Error", "Please fill all the details to update")
        return

    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        query = """UPDATE book_issue_card SET book_title = %s, author_name = %s, student_id = %s, student_name = %s, issue_date = %s, return_date = %s WHERE book_id = %s"""
        cursor.execute(query, (book_title, author_name, student_id, student_name,issue_date, return_date, book_id))
        con.commit()
        messagebox.showinfo("Success", "Data updated successfully")
        con.close()

    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")

def delete():
    book_id = book_id_Entry.get()
    
    # Check if book_id field is empty
    if not book_id:
        messagebox.showerror("Error", "Please enter Student ID to delete")
        return

    try:
        con = c.connect(host="localhost", user="root", password='root', database="lms")
        cursor = con.cursor()
        query = "DELETE FROM book_issue_card WHERE book_id = %s"
        cursor.execute(query, (book_id,))
        con.commit()
        con.close()
        
        # Clear the entry fields
        book_id_Entry.delete(0, END)
        book_title_Entry.delete(0, END)
        author_name_Entry.delete(0, END)
        student_id_Entry.delete(0, END)
        student_name_Entry.delete(0, END)
        issue_date_Entry.delete(0, END)
        return_date_Entry.delete(0, END)
        
        messagebox.showinfo("Success", "Record deleted successfully")
        
    except c.Error as err:
        messagebox.showerror("Database Error", f"Error occurred: {err}")


def calculate_fine():
    return_date = return_date_Entry.get()
    submit_date = submit_date_Entry.get()
    
    if not return_date or not submit_date:
        messagebox.showerror("Error", "Please enter both return date and submit date")
        return
    
    try:
        return_date_obj = datetime.strptime(return_date, '%Y-%m-%d')
        submit_date_obj = datetime.strptime(submit_date, '%Y-%m-%d')
        
        if submit_date_obj > return_date_obj:
            days_late = (submit_date_obj - return_date_obj).days
            fine_amount = days_late * 5
            messagebox.showinfo("Fine", f"You have to pay a fine of {fine_amount} rupees")
        else:
            messagebox.showinfo("No Fine", "No need to pay any fine")
    
    except ValueError:
        messagebox.showerror("Error", "Incorrect date format. Please use YYYY-MM-DD")

img = Image.open('return.png')
img.thumbnail((130, 130))  # width, height
img6 = ImageTk.PhotoImage(img)
l7 = Label(return_book_frame, image=img6, bg="lightpink")
l7.image = img6
l7.place(x=150, y=25)

def on_enter10(e):
    issue_date_Entry.delete(0, 'end')

def on_leave10(e):
    name = issue_date_Entry.get()
    if name == '':
        issue_date_Entry.insert(0, 'YY-MM-DD')

def on_enter11(e):
    return_date_Entry.delete(0, 'end')

def on_leave11(e):
    name = return_date_Entry.get()
    if name == '':
        return_date_Entry.insert(0, 'YY-MM-DD')

def on_enter12(e):
    submit_date_Entry.delete(0, 'end')

def on_leave12(e):
    name = submit_date_Entry.get()
    if name == '':
        submit_date_Entry.insert(0, 'YY-MM-DD')

ISSUE_label = Label(return_book_frame, text="RETURN CARD DETAILS!", fg="red", bg="lightpink", font=('Times New Roman', 40, 'bold'))
ISSUE_label.place(x=330, y=50)

book_id = Label(return_book_frame, text="BOOK ID:", bg="lightpink", font=("Georgia", 15))
book_id.place(x=100, y=205)

book_id_Entry = Entry(return_book_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
book_id_Entry.place(x=400, y=200)

book_title = Label(return_book_frame, text="BOOK NAME:", bg="lightpink", font=("Georgia", 15))
book_title.place(x=100, y=245)

book_title_Entry = Entry(return_book_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
book_title_Entry.place(x=400, y=240)

author_name = Label(return_book_frame, text="AUTHOR NAME:", bg="lightpink", font=("Georgia", 15))
author_name.place(x=100, y=285)

author_name_Entry = Entry(return_book_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
author_name_Entry.place(x=400, y=280)

student_id = Label(return_book_frame, text="STUDENT ID:", bg="lightpink", font=("Georgia", 15))
student_id.place(x=100, y=325)

student_id_Entry = Entry(return_book_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_id_Entry.place(x=400, y=320)

student_name = Label(return_book_frame, text="STUDENT NAME:", bg="lightpink", font=("Georgia", 15))
student_name.place(x=100, y=365)

student_name_Entry = Entry(return_book_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_name_Entry.place(x=400, y=360)

issue_date = Label(return_book_frame, text="ISSUE DATE:", bg="lightpink", font=("Georgia", 15))
issue_date.place(x=100, y=405)

issue_date_Entry = Entry(return_book_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
issue_date_Entry.insert(0, 'YY-MM-DD')
issue_date_Entry.bind('<FocusIn>', on_enter10)
issue_date_Entry.bind('<FocusOut>', on_leave10)
issue_date_Entry.place(x=400, y=400)

return_date = Label(return_book_frame, text="RETURN DATE:", bg="lightpink", font=("Georgia", 15))
return_date.place(x=100, y=445)

return_date_Entry = Entry(return_book_frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
return_date_Entry.insert(0, 'YY-MM-DD')
return_date_Entry.bind('<FocusIn>', on_enter11)
return_date_Entry.bind('<FocusOut>', on_leave11)
return_date_Entry.place(x=400, y=440)

submit_date = Label(return_book_frame, text="SUBMIT DATE:", bg="lightpink", font=("Georgia", 15))
submit_date.place(x=100, y=485)

submit_date_Entry = Entry(return_book_frame, width=30, fg="red", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
submit_date_Entry.insert(0, 'YY-MM-DD')
submit_date_Entry.bind('<FocusIn>', on_enter12)
submit_date_Entry.bind('<FocusOut>', on_leave12)
submit_date_Entry.place(x=400, y=480)

b19 = Button(return_book_frame, width=8, text="SAVE", border=0, padx='4', pady='4', bg='RED', cursor='hand2', command=save, fg='#fff', font=('Times New Roman', 10, 'bold'))
b19.place(x=800, y=220)

b20 = Button(return_book_frame, width=8, text="SEARCH", border=0, padx='4', pady='4', bg='RED', cursor='hand2', command=search, fg='#fff', font=('Times New Roman', 10, 'bold'))
b20.place(x=800, y=270)

b21 = Button(return_book_frame, width=8, text="UPDATE", border=0, padx='4', pady='4', bg='RED', cursor='hand2', command=update, fg='#fff', font=('Times New Roman', 10, 'bold'))
b21.place(x=800, y=320)

b22 = Button(return_book_frame, width=8, text="DELETE", border=0, padx='4', pady='4', bg='RED', cursor='hand2', fg='#fff', command=delete, font=('Times New Roman', 10, 'bold'))                               
b22.place(x=800, y=370)

b23 = Button(return_book_frame, width=8, text="FINE", border=0, padx='4', pady='4', bg='RED', cursor='hand2', fg='#fff', command=calculate_fine, font=('Times New Roman', 10, 'bold'))                               
b23.place(x=800, y=420)

b24 = Button(return_book_frame, width=8, text="BACK", border=0, padx='4', pady='4', bg='#FF0000', cursor='hand2', fg='#fff',command=lambda: show_frame(welcome_frame), font=('Times New Roman', 10, 'bold'))                             
b24.place(x=800, y=470)

# Start by showing the login frame
show_frame(login_frame)

root.mainloop()
