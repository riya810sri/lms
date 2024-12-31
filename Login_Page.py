                                          #importing libraries here
from tkinter import *
from tkinter import messagebox
                                            #Creation of frame
frame = Tk()
frame.config(bg='#fff')
frame.title('login_page')
frame.geometry('925x500+300+200')

#--------------------------------------------------------Sign_in proccess----------------------------
def signin():
    username=t1.get()
    password=t2.get()
    if username=='shikhar' or 'saloni' or 'vishwa' and password=='12345':
        screen=Toplevel(frame)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='sky blue')

        Label(screen,text='Welcome to Library!',bg='sky blue',font=('Calibri(Body)',50,'bold')).pack(expand=True)
        screen.mainloop()
    elif username!='shikhar' or 'saloni' or 'vishwa' and password!='12345':
        messagebox.showinfo('Invalid', 'invalid username and password')
    elif username!='shikhar' or 'saloni' or 'vishwa':
        messagebox.showinfo('Invalid','invalid username')
    elif password!='12345':
        messagebox.showinfo('Invalid','invalid password')
                                      #Starting of intrinsic work
img=PhotoImage(file='logo.png')
l1=Label(frame, image=img, bg='#fff')
#----------------------------------------------------------------------------------------
#for username entry
def on_enter(e):
    t1.delete(0,'end')

def on_leave(e):
    name=t1.get()
    if name=='':
        t1.insert(0,'Username')

t1=Entry(frame, width=40, bg='sky blue',border=0, font=("Times New Roman", 18))
t1.insert(0,'Username')
t1.bind('<FocusIn>',on_enter)
t1.bind('<FocusOut>',on_leave)
#----------------------------------------------------------------------------------------
#for password entry
def on_enter(e):
    t2.delete(0,'end')

def on_leave(e):
    name=t2.get()
    if name=='':
        t2.insert(0,'Password')

t2=Entry(frame, width=40, bg='sky blue',border=0, font=("Times New Roman", 18))
t2.insert(0,'Password')
t2.bind('<FocusIn>',on_enter)
t2.bind(',FocusOut>',on_leave)
#-----------------------------------------------------------------------------------------
b1=Button(frame,width=25,pady=7,text='Sign in', bg='#57a1f8',fg='white',border=0,command=signin,font=("Times New Roman",10))
l2=Label(frame,width=27,text="Don't have account?",fg='black',bg='white',font=('Microsoft YaHai UI Light',10))
b2=Button(frame,width=6,text='Sign Up',border=0,bg='white',cursor='hand2',fg='#57a1f8')

                                          #Alignment Process
l1.place(x=250, y=40)
t1.place(x=120, y=150)
t2.place(x=120, y=200)
b1.place(x=400,y=300)
l2.place(x=120, y=310)
b2.place(x=290,y=310)

frame.mainloop()
