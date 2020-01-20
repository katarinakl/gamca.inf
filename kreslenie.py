import tkinter
from random import randrange, randint

X_MAX,Y_MAX= 800,600
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX,background="white")
canvas.pack()

x1,y1=0,0

def klik(event):
    global x1,y1
    canvas.bind("<B1-Motion>",ciara)
    x1,y1=event.x,event.y

def ciara(event):
    x,y=event.x,event.y
    global x1,y1
    canvas.create_line(x1,y1,x,y,width=4)
    x1,y1=x,y

canvas.bind("<Button-1>", klik)
