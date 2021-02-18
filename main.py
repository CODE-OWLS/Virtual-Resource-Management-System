from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import driver as ma
import Modules.register as regi

root = Tk()
root.title("VRMS")
root.iconbitmap("images\inverted.ico")
root.configure(bg="#24292e")
root.geometry("550x200")
ProfileMain=Label(root)

def registerfn():
    username = regi_user.get()
    password = regi_pass.get()
    pass2 = regi_passcheck.get()

    if len(username) < 4 or len(username)>12:
        messagebox.showerror("Input Error","Username should be of length 4 - 12")
        return
    
    if len(password) < 4 or len(password)>12:
        messagebox.showerror("Input Error","Password should be of length 4 - 12")
        return

    if password != pass2:
        messagebox.showerror("Input Error","Passwords don't match !")
        return
    
    i = regi.call(username,password)
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
        msg = Label(LoginFrame,text="Invalid Credentials",padx=10,fg="red",bg="#24292e",borderwidth=0)
        msg.grid(row=6,column=0,columnspan=3)

def rn():
    regi.call()


#Logo
logo=ImageTk.PhotoImage(Image.open ("images\codeowls.png"),width=10, height =50)
main = Label(root,image=logo,borderwidth="0")

#Login labels, Buttons and griding
LoginFrame = LabelFrame(root,bg="#24292e",borderwidth=0)
LoginFrame.grid(row = 0, column = 0,padx=20)

looogin= Label(LoginFrame,text="Exsisting User",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=1)
loginusertxt = Label(LoginFrame, text="Username:", padx = 5, fg="white",bg="#24292e",borderwidth=0)
loginuser=Entry(LoginFrame)
loginpasstxt = Label(LoginFrame, text="Password:", padx = 5, fg="white",bg="#24292e",borderwidth=0)
loginpass=Entry(LoginFrame,text="Enter Password",show="*")
login=Button(LoginFrame,text="Login",padx=10,pady=5,fg="white",bg="#24292e",borderwidth=2,command=check)

looogin.grid(row=0,column=0,columnspan=3)
loginusertxt.grid(row=3,column=0)
loginuser.grid(row=3,column=2,pady=5)
loginpasstxt.grid(row=5,column=0)
loginpass.grid(row=5,column=2,pady=5)
login.grid(row=7,column=0,padx=25,columnspan=3)



#Registration Labels, Buttons and  grid
RegiFrame = LabelFrame(root,bg="#24292e",borderwidth=0)
RegiFrame.grid(row = 0, column = 1,padx=30)

registration= Label(RegiFrame,text="Register Now",fg="white",bg="#24292e",borderwidth=1,pady=20)
regi_user = Entry(RegiFrame)
regiusertxt = Label(RegiFrame,text="Username:",fg = "white", bg="#24292e",borderwidth=0)
regi_pass = Entry(RegiFrame,show="*")
regipasstxt = Label(RegiFrame,text="Password:",fg = "white", bg="#24292e",borderwidth=0)
regi_passcheck = Entry(RegiFrame,show="*")
regipass2txt = Label(RegiFrame,text="Re-Enter Password:",fg = "white", bg="#24292e",borderwidth=0)
register = Button(RegiFrame,text="Sign Up",padx=10,pady=5,fg="white",bg="#24292e",borderwidth=2,command=registerfn)

registration.grid(row=0,column=1,columnspan=3)
regiusertxt.grid(row=2,column=0)
regi_user.grid(row=2,column=2)
regipasstxt.grid(row=4,column=0)
regi_pass.grid(row=4,column=2,pady=10)
regipass2txt.grid(row=6,column=0,padx=5)
regi_passcheck.grid(row=6,column=2)
register.grid(row=10,column=1,columnspan=3,pady=10)

blank = Label(LoginFrame,fg="#24292e",bg="#24292e", text="l")
blank.grid(row = 6, column=0)



root.mainloop()