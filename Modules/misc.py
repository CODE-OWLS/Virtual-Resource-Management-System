from tkinter import *
import webbrowser
import requests 
import json
import random
import Modules.calculator as calc
import Modules.weather as wea
import Modules.ttt as tt
import Modules.colour as col
import Modules.snake as sna

def calcu(root):
    calc.call()

def we(root):
    wea.call()

def snake():
    sna.call()

def tak():
    tt.call()
def colours():
    col.call()



def notesmain(root):
    LeftFrame = LabelFrame(root,bg="#24292e",pady=28,borderwidth=0)
    LeftFrame.grid(row = 3, column = 0,rowspan=10,padx=10)

    Calcnotes = Button(LeftFrame,text="Calculator",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=lambda:calcu(root))
    Weathernotes = Button(LeftFrame,text="Weather",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=lambda:we(root))
    tic = Button(LeftFrame,text="Tic-Tac-Toe",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=tak)
    colour = Button(LeftFrame,text="Colour",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=colours)
    snakegame = Button(LeftFrame,text="Snake",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=snake)
    Calcnotes.grid(row = 0, column = 1)
    Weathernotes.grid(row = 2, column = 1)
    tic.grid(row = 4, column = 1)
    colour.grid(row = 6, column = 1)
    snakegame.grid(row = 6, column = 1)
 
    #blank
    blank = []
    j = 1
    for i in range(6):
        blank.append(Label(LeftFrame, text=" Trying to make it long ",fg="#24292e",bg="#24292e"))
        blank[i].grid(row = j, column=1)
        j += 2

    LeftFrame.lift()