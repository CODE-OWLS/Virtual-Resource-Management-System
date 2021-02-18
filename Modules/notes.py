from tkinter import *
from PIL import ImageTk,Image
import webbrowser

#Functions for all the drive links.
def csenote():
    webbrowser.open("https://drive.google.com/drive/folders/1WjknjKJ81ajNQZpb7tKUy5ohMxGJWz30")
    return 0

def csetut():
    webbrowser.open("https://drive.google.com/drive/folders/1uNngYCa-L4JyXOwR14lT7Yi0BCMDXiNt")
    return 0

def eecenote():
    webbrowser.open("https://drive.google.com/drive/folders/1YSPKLGk-Q2Ml1Lr3rZIVedcgj65IKp5z")
    return 0

def eecetut():
    webbrowser.open("https://drive.google.com/drive/folders/1O2riFGPlZuxZ8di4nCl5QG2jM46Rwd-D")
    return 0

def mathnote():
    webbrowser.open("https://drive.google.com/drive/folders/1PVM_4r4bBMDs1nzJsQEBVuL--hxHOtvw")
    return 0

def mathtut():
    webbrowser.open("https://drive.google.com/drive/folders/1cwessWTlenOgAD3lClxvP2Bov61FULAO")
    return 0

def phynote():
    webbrowser.open("https://drive.google.com/drive/folders/1Bch6DpcM1T_YesopG06C_RL9Yd-cN_UH")
    return 0

def phytut():
    webbrowser.open("https://drive.google.com/drive/folders/1YO43v74zG0hD2FFtEjusOGOl3thlkOwV")
    return 0

def phys(root):
    pdf_logo=ImageTk.PhotoImage(Image.open (r"images\pdf.png"),width=10, height =50)
    phy_img=ImageTk.PhotoImage(Image.open (r"images\notebook.png"),width=10, height =50)

    phy_frame = LabelFrame(root, padx=82,pady=76,bg="#455954",width=200,height=200)
    phy_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)

    phy_notes=Button(phy_frame,text="Physics Notes", image = phy_img, compound="top",padx=50,bg="#455954",borderwidth=0,fg="#dfdbd8",command=phynote)
    phy_notes.grid(row=0,column=5,padx=10,columnspan=5,pady=30)
    phy_notes.image=phy_img

    phy_tut=Button(phy_frame,text="Physics Tutorials", image = pdf_logo, compound="top",padx=50,bg="#455954",fg="#dfdbd8",borderwidth=0,command=phytut)
    phy_tut.grid(row=0,column=10,padx=10,columnspan=5,pady=30)
    phy_tut.image=pdf_logo

    phy_frame.lift()
    return 0

def eece(root):
    pdf_logo=ImageTk.PhotoImage(Image.open (r"images\pdf.png"),width=10, height =50)
    eece_img=ImageTk.PhotoImage(Image.open (r"images\notebook.png"),width=10, height =50)

    eece_frame = LabelFrame(root, padx=80,pady=75,bg="#455954",width=200,height=200)
    eece_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)
    
    eece_notes=Button(eece_frame,text="EECE Notes", image = eece_img, compound="top",padx=50,bg="#455954",fg="#dfdbd8",borderwidth=0,command=eecenote)
    eece_notes.grid(row=0,column=5,padx=17,columnspan=5,pady=31)
    eece_notes.image=eece_img

    eece_tut=Button(eece_frame,text="EECE Tutorials", image = pdf_logo, compound="top",padx=50,bg="#455954",fg="#dfdbd8",borderwidth=0,command=eecetut)
    eece_tut.grid(row=0,column=10,padx=17,columnspan=5,pady=31)
    eece_tut.image=pdf_logo

    eece_frame.lift()
    return 0

def cse(root):
    pdf_logo=ImageTk.PhotoImage(Image.open (r"images\pdf.png"),width=10, height =50)
    cse_img=ImageTk.PhotoImage(Image.open (r"images\notebook.png"),width=10, height =50)

    cse_frame = LabelFrame(root, padx=80,pady=75,bg="#455954",width=200,height=200)
    cse_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)
    

    cse_notes=Button(cse_frame, text="Computer Notes", image = cse_img, compound="top",padx=50, bg="#455954",fg="#dfdbd8",borderwidth=0,command=csenote)
    cse_notes.grid(row=0,column=5,columnspan=5,pady=31,padx=3)
    cse_notes.image=cse_img

    cse_tut=Button(cse_frame,text="Computer Tutorials", image = pdf_logo, compound="top",padx=50,bg="#455954",fg="#dfdbd8",borderwidth=0,command=csetut)
    cse_tut.grid(row=0,column=10,pady=31,columnspan=5,padx=3)
    cse_tut.image=pdf_logo
    return 0

def math(root):
    pdf_logo=ImageTk.PhotoImage(Image.open (r"images\pdf.png"),width=10, height =50)
    nb=ImageTk.PhotoImage(Image.open (r"images\notebook.png"),width=10, height =50)
    
    mat_frame = LabelFrame(root, padx=80,pady=75,bg="#455954",width=200,height=200)
    mat_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)

    mat_notes=Button(mat_frame,text="Math Notes", image = nb, compound="top",padx=50,bg="#455954",fg="#dfdbd8",borderwidth=0,command=mathnote)
    mat_notes.grid(row=0,column=5,padx=16,pady=31,columnspan=5)
    mat_notes.image=nb

    mat_tut=Button(mat_frame,text="Math Tutorials", image = pdf_logo, compound="top",padx=50,bg="#455954",fg="#dfdbd8",borderwidth=0,command=mathtut)
    mat_tut.grid(row=0,column=10,padx=16,columnspan=5,pady=31)
    mat_tut.image=pdf_logo

    return 0

def notesmain(root):
    left_frame = LabelFrame(root,bg="#24292e",pady=28,borderwidth=0)
    left_frame.grid(row = 3, column = 0,rowspan=10,padx=10)

    PhyNotes = Button(left_frame,text="EPHY",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=lambda:phys(root))
    CseNotes = Button(left_frame,text="ECSE",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=lambda:cse(root))
    EeceNotes = Button(left_frame,text="EECE",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command =lambda:eece(root))
    MathNotes = Button(left_frame,text="EMAT",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command = lambda:math(root))

    PhyNotes.grid(row = 0, column = 1)
    CseNotes.grid(row = 2, column = 1)
    EeceNotes.grid(row = 4, column = 1)
    MathNotes.grid(row = 6, column = 1)
 
    #Adding blank spaces.
    blank = []
    j = 1
    for i in range(4):
        blank.append(Label(left_frame, text=" Trying to make it long ",fg="#24292e",bg="#24292e"))
        blank[i].grid(row = j, column=1)
        j += 2

    left_frame.lift()