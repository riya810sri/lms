from tkinter import *
from tkinter import messagebox
import mysql.connector as c
from PIL import Image, ImageTk


frame = Tk()
frame.geometry("925x500+300+200")
frame.title("Book Issue Card")
frame.config(bg="LIGHTPINK")

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
        con = c.connect(host="localhost", user="root", password='#JAISHREERAM', database="lms")
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
        query = "DELETE FROM bookissue WHERE member_id = %s"
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
img5 = ImageTk.PhotoImage(img)

l10 = Label(frame, image=img5, )
l10.image = img5
l10.place(x=150,y=30)


def on_enter1(e):
    issue_date_Entry.delete(0, 'end')

def on_leave1(e):
    name = issue_date_Entry.get()
    if name == '':
        issue_date_Entry.insert(0, 'YY-MM-DD')


ISSUE_label = Label(frame, text = "ISSUE CARD DETAILS!",fg="red", bg="yellow",font=('Times New Roman', 40, 'bold'))
ISSUE_label.place(x=330, y=50)

book_id = Label(frame, text="BOOK ID:", bg="#fff", font=("Georgia", 15))
book_id.place(x=100, y=205)

book_id_Entry = Entry(frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
book_id_Entry.place(x=400, y=200)

book_title = Label(frame, text="Book name:", bg="#fff", font=("Georgia", 15))
book_title.place(x=100, y=245)

book_title_Entry = Entry(frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
book_title_Entry.place(x=400, y=240)

author_name = Label(frame, text="Author name:", bg="#fff", font=("Georgia", 15))
author_name.place(x=100, y=285)

author_name_Entry = Entry(frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
author_name_Entry.place(x=400, y=280)

student_id = Label(frame, text="Student id:", bg="#fff", font=("Georgia", 15))
student_id.place(x=100, y=325)

student_id_Entry = Entry(frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_id_Entry.place(x=400, y=320)

student_name = Label(frame, text="STUDENT NAME:", bg="#fff", font=("Georgia", 15))
student_name.place(x=100, y=365)

student_name_Entry = Entry(frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
student_name_Entry.place(x=400, y=360)

issue_date = Label(frame, text="ISSUE DATE:", bg="#fff", font=("Georgia", 15))
issue_date.place(x=100, y=405)

issue_date_Entry = Entry(frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
issue_date_Entry.insert(0, 'YY-MM-DD')
issue_date_Entry.bind('<FocusIn>', on_enter1)
issue_date_Entry.bind('<FocusOut>', on_leave1)
issue_date_Entry.place(x=400, y=400)

return_date = Label(frame, text="RETURN DATE:", bg="#fff", font=("Georgia", 15))
return_date.place(x=100, y=445)

return_date_Entry = Entry(frame, width=30, fg="#000080", bg="#FFFFE0", font=("Times New Roman", 15, "bold"))
return_date_Entry.insert(0, 'YY-MM-DD')
return_date_Entry.bind('<FocusIn>', on_enter1)
return_date_Entry.bind('<FocusOut>', on_leave1)
return_date_Entry.place(x=400, y=440)

b9 = Button(frame, width=8, text="SAVE", border=0, padx='4', pady='4', bg='RED', cursor='hand2', command=save, fg='#fff', font=('Times New Roman', 10, 'bold'))
b9.place(x=800, y=220)


b10 = Button(frame, width=8, text="SEARCH", border=0, padx='4', pady='4', bg='RED', cursor='hand2', command=search, fg='#fff', font=('Times New Roman', 10, 'bold'))
b10.place(x=800, y=270)

b11 = Button(frame, width=8, text="UPDATE", border=0, padx='4', pady='4', bg='RED', cursor='hand2', command=update, fg='#fff', font=('Times New Roman', 10, 'bold'))
b11.place(x=800, y=320)

b12 = Button(frame, width=8, text="DELETE", border=0, padx='4', pady='4', bg='RED', cursor='hand2', fg='#fff',command=delete, font=('Times New Roman', 10, 'bold'))
                               
b12.place(x=800, y=370)

frame.mainloop()
