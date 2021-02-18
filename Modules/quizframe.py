from tkinter import *
import Modules.quiz as qui

def phys():
    qui.phy()
def ecse():
    qui.cse()
def eece():
    qui.ece()
def emat():
    qui.mat()

def notesmain(root):
    LeftFrame = LabelFrame(root,bg="#24292e",pady=28,borderwidth=0)
    LeftFrame.grid(row = 3, column = 0,rowspan=10,padx=10)

    Phynotes = Button(LeftFrame,text="EPHY",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=phys)
    CSEnotes = Button(LeftFrame,text="ECSE",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=ecse)
    EECEnotes = Button(LeftFrame,text="EECE",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command =eece)
    EMATnotes = Button(LeftFrame,text="EMAT",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command =emat)

    Phynotes.grid(row = 0, column = 1)
    CSEnotes.grid(row = 2, column = 1)
    EECEnotes.grid(row = 4, column = 1)
    EMATnotes.grid(row = 6, column = 1)
 
    #blank
    blank = []
    j = 1
    for i in range(4):
        blank.append(Label(LeftFrame, text=" Trying to make it long ",fg="#24292e",bg="#24292e"))
        blank[i].grid(row = j, column=1)
        j += 2

    LeftFrame.lift()