import tkinter
import random

X_MAX,Y_MAX=800,600

canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX, bg="white")
canvas.pack()

def pohyb(event):
    x,y= event.x,event.y
    r=10
    canvas.create_oval(x,y,x+r,y+r, fill="hot pink")
    a=X_MAX-x
    canvas.create_oval(a,y,a+r,y+r,fill="forest green")
    b=Y_MAX-y
    canvas.create_oval(x,b,x+r,b+r,fill="gold")
    canvas.create_oval(a,b,a+r,b+r,fill="dodgerblue3")
canvas.bind('<Motion>', pohyb)
    
