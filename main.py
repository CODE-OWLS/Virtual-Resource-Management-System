from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import Modules.driver as ma
import Modules.register as regi
import Modules.forget as fg

root = Tk()
root.title("VRMS")
root.iconbitmap("images\mainlogo.ico")
root.configure(bg="#24292e")
root.geometry("600x400")
ProfileMain=Label(root)

def registerfn():
    username = regi_user.get()
    password = regi_pass.get()
    pass2 = regi_passcheck.get()
    mail = regi_email.get()

    if len(username) < 4 or len(username)>12:
        messagebox.showerror("Input Error","Username should be of length 4 - 12")
        return
    
    if len(password) < 4 or len(password)>12:
        messagebox.showerror("Input Error","Password should be of length 4 - 12")
        return

    if password != pass2:
        messagebox.showerror("Input Error","Passwords don't match !")
        return
    
    i = regi.call(username,password,mail)
    if i == -1:
        messagebox.showinfo("Registration Error","Username already exsists")
        return

    if i == 0:
        messagebox.showinfo("Registration","Registration Complete")


def check() :
    us = loginuser.get()
    pas = loginpass.get()

    I = regi.check(us,pas)
    if I == 0:
        root.destroy()
        ma.call()
    else:
        msg = Label(root,text="Invalid Credentials",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0)
        msg.grid(row=6,column=0)

def rn():
    regi.call()
def fp ():
    fg.call()

#Logo
logo=ImageTk.PhotoImage(Image.open ("images\codeowls.png"),width=10, height =50)
main = Label(root,image=logo,borderwidth="0")

#Login labels, Buttons and griding
LoginFrame = LabelFrame(root,bg="#24292e",borderwidth=0)
LoginFrame.grid(row = 0, column = 0,padx=20,pady=10)

looogin= Label(LoginFrame,text="LOGIN",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1)
loginuser=Entry(LoginFrame)
loginuser.insert(0,"Enter Username") 
loginpass=Entry(LoginFrame,text="Enter Password",show="*")
loginpass.insert(0,"Enter Password")
login=Button(LoginFrame,text="Login",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=check)
fp= Button(LoginFrame,text="Forgot Password ?", padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=fp)

looogin.grid(row=0,column=0,pady=5)
loginuser.grid(row=3,column=0,pady=5)
loginpass.grid(row=5,column=0,pady=5)
login.grid(row=7,column=0,pady=5)
fp.grid(row=10,column=0,pady=5)


#Registration Labels, Buttons and  grid
RegiFrame = LabelFrame(root,bg="#24292e",borderwidth=0)
RegiFrame.grid(row = 0, column = 5)

registration= Label(RegiFrame,text="SIGN UP",fg="white",bg="#1d2125",borderwidth=1)
regi_user = Entry(RegiFrame)
regi_user.insert(0,"Enter Username") 
regi_pass = Entry(RegiFrame,show="*")
regi_pass.insert(0,"Enter Password")
regi_passcheck = Entry(RegiFrame,show="*")
regi_passcheck.insert(0,"Re-Enter Password")
regi_email = Entry(RegiFrame)
regi_email.insert(0,"Enter Mail")
register = Button(RegiFrame,text="Register Now",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=registerfn)

registration.grid(row=0,column=5)
regi_user.grid(row=2,column=5)
regi_pass.grid(row=4,column=5)
regi_passcheck.grid(row=6,column=5)
regi_email.grid(row=8,column=5)
register.grid(row=10,column=5)

blank = []
for i in range(6):
    blank.append(Label(LoginFrame,fg="#24292e",bg="#24292e"))
    blank[i].grid(row = 1, column=i)

blank = []
for i in range(6):
    blank.append(Label(RegiFrame,fg="#24292e",bg="#24292e"))
    blank[i].grid(row = 1, column=i)


root.mainloop()