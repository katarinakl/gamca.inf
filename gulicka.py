import tkinter
from random import randrange,randint

X_MAX,Y_MAX = 800,600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

r=10
a=2
b=2
x,y= randint(0,800),randint(0,600)
canvas.create_oval(x,y,x+r,y+r,fill="dodgerblue3")

while True:
    canvas.delete("all")
    canvas.create_oval(x,y,x+r,y+r,fill="dodgerblue3")
    x=x+a
    y=y+b

    
    canvas.update()
    canvas.after(1)
    if x>=X_MAX-r or x<=r:
        a*=-1
    if y>=Y_MAX-r or y<=r:
        b*=-1
