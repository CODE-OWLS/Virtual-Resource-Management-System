from tkinter import *
from PIL import ImageTk,Image
import webbrowser

def books(root) :  
    def ecepush():
       #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       def openwebbook2():
         webbrowser.open(urlbook2,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=122,pady=105,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=3,column=2,padx=5,pady=5,rowspan=10,columnspan=10)  
       #list ece books and setup their info here itself
       urlbook1 = "https://drive.google.com/file/d/1BfJUZc6QZmCjBllSsvdWYu3kMHJLJuFj/view?usp=sharing"
       
       urlbook2 = "https://drive.google.com/file/d/1-ozF-lwUS24ZTM3on2FfrJh6uYtiw6ml/view?usp=sharing"
       urlbook3 = "https://drive.google.com/file/d/1-ozF-lwUS24ZTM3on2FfrJh6uYtiw6ml/view?usp=sharing"
       book1= Button(BFrame_Right,text="Introductory Circuit Analysis",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       book2= Button(BFrame_Right,text="Electronic Devices And Circuits",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook2)
       book2.grid(row=4,column=3)
       BFrame_Right.lift()


    def phypush():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       def openwebbook2():
         webbrowser.open(urlbook2,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=126,pady=105,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=3,column=2,padx=5,pady=5,rowspan=10,columnspan=10)
       #list ece books and setup their info here itself
       urlbook1 = "https://drive.google.com/file/d/1aMedhLqIBva1qXTFq4K26mvkZw6ZB3Z-/view?usp=sharing"
       
       urlbook2 = "https://drive.google.com/file/d/19AyL4xv-tcStsmWU0HBeANqT2IWdaU9D/view?usp=sharing"
       urlbook3 = "https://drive.google.com/file/d/1-ozF-lwUS24ZTM3on2FfrJh6uYtiw6ml/view?usp=sharing"
       book1= Button(BFrame_Right,text="Griffith's Into Electrodynamics",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=0,column=0)
       book2= Button(BFrame_Right,text="Instructors Solution Manual",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook2)
       book2.grid(row=0,column=1)
       BFrame_Right.lift()

    def mathpush():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       def openwebbook2():
         webbrowser.open(urlbook2,new)
       def openwebbook3():
         webbrowser.open(urlbook3,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=58,pady=105,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=3,column=2,rowspan=10,columnspan=10,pady=5,padx=5)
       
       #list ece books and setup their info here itself
       urlbook1 = "https://drive.google.com/file/d/1lQOd54h6lS-1uRBSLFh_f3wIrpjDetu2/view?usp=sharing"
       
       urlbook2 = "https://drive.google.com/file/d/1F_8YCTVB3f-7I3GwcXE4QasZ5VgX8Xc8/view?usp=sharing"
       urlbook3 = "https://drive.google.com/file/d/1LtY4BpQq5aBU5q_WjTZoNYEItrzeJdKu/view?usp=sharing"
       book1= Button(BFrame_Right,text="Introduction To Real Analysis",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2,padx=10)
       book2= Button(BFrame_Right,text="Ross Elementary Analysis",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook2)
       book2.grid(row=4,column=3,padx=10)
       book3= Button(BFrame_Right,text="Thomas Calculus",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook3)
       book3.grid(row=4,column=4,padx=10)
       BFrame_Right.lift()

    def csepush():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       def openwebbook2():
         webbrowser.open(urlbook2,new)
       def openwebbook3():
         webbrowser.open(urlbook3,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=98,pady=98,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=3,column=2,rowspan=10,columnspan=10,pady=5,padx=5)
       
       #list ece books and setup their info here itself
       urlbook1 = "https://drive.google.com/file/d/16WnwpmYBC5ULP5JvprACY6l7u09O9PxX/view?usp=sharing"
       
       urlbook2 = "https://drive.google.com/file/d/1ERSe-zEJxj1kut8xN-YgoKC4ZJmGanxs/view?usp=sharing"
       urlbook3 = "https://drive.google.com/file/d/1haFTD3ptgYbH25ZkgNH9A_BIUFkoi-V6/view?usp=sharing"
       book1= Button(BFrame_Right,text="Introduction To Computer \nScience Using Python",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2,padx=10)
       book2= Button(BFrame_Right,text="Think CS Python",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook2)
       book2.grid(row=4,column=3,padx=10)
       book3= Button(BFrame_Right,text="Think Python",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook3)
       book3.grid(row=4,column=4,padx=10)
       BFrame_Right.lift()

    img = ImageTk.PhotoImage(Image.open(r"images\pdf.png"),height=50,width=50)    
    BFrame_left = LabelFrame(root,bg="#24292e",pady=28,borderwidth=0)
    BFrame_left.grid(row = 3, column = 0,rowspan=10,padx=10)

    #my button definitions
    phybutton=Button(BFrame_left,text="EPHY ",command=phypush,padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0)
    csebutton=Button(BFrame_left,text="ECSE ",command=csepush,padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0)
    ecebutton=Button(BFrame_left,text="EECE ",command=ecepush,padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0)
    mathbutton=Button(BFrame_left,text="EMAT ",command=mathpush,padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0)

    #my button grids
    phybutton.grid(row=0,column=1)
    csebutton.grid(row=2,column=1)
    ecebutton.grid(row=4,column=1)
    mathbutton.grid(row=6,column=1)
   
    blank = []
    j = 1
    for i in range(4):
        blank.append(Label(BFrame_left, text=" Trying to make it long ",fg="#24292e",bg="#24292e"))
        blank[i].grid(row = j, column=1)
        j += 2
    BFrame_left.lift()