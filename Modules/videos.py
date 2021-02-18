from tkinter import *
from PIL import ImageTk,Image
import webbrowser

def phy_playlist():
    webbrowser.open("https://www.youtube.com/playlist?list=PLygAjP_YxBHt_UujAIJW1KxW4qWDpWS5U")
def ece_playlist():
    webbrowser.open("https://www.youtube.com/playlist?list=PLygAjP_YxBHuwloF5QEiJqnq_o5zQMPZo")
def cse_playlist():
    webbrowser.open("https://www.youtube.com/playlist?list=PLygAjP_YxBHu79djZc_rtMDA1YiAPeBSQ")
def math_playlist():
    webbrowser.open("https://www.youtube.com/playlist?list=PLygAjP_YxBHv7BhIK0hj2mA7v-zdnlp3d")

def videos(root) :
    VideoFrame = LabelFrame(root,pady=59,bg="#455954",width=200,height=200,padx=110)
    VideoFrame.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)

    yt_logo=ImageTk.PhotoImage(Image.open (r"images\video.png"))

    blank = []
    for l in range(2):
        j = 1
        for i in range(2):
         blank.append(Label(VideoFrame, text="         ",fg="#455954",bg="#455954"))
         blank[i].grid(row = l, column=j)
         j += 2

    phy_button=Button(VideoFrame,text="Physics Lectures", image=yt_logo, compound="top",padx=10,command=phy_playlist,bg="#455954",borderwidth=0)
    phy_button.grid(row=0,column=0,pady=10)
    phy_button.image=yt_logo

    ece_button=Button(VideoFrame,text="Electrical Lectures", image=yt_logo, compound="top",padx=10,command=ece_playlist,bg="#455954",borderwidth=0)
    ece_button.grid(row=0,column=2,pady=10)
    ece_button.image=yt_logo

    cse_button=Button(VideoFrame,text="Computer Science Lectures", image=yt_logo, compound="top",padx=10,command=cse_playlist,bg="#455954",borderwidth=0)
    cse_button.grid(row=1,column=0,pady=10)
    cse_button.image=yt_logo

    math_button=Button(VideoFrame,text="Maths Lectures", image=yt_logo, compound="top",padx=10,command=math_playlist,bg="#455954",borderwidth=0)
    math_button.grid(row=1,column=2,pady=10)
    math_button.image=yt_logo