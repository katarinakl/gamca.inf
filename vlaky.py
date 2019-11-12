import tkinter
import random
canvas= tkinter.Canvas(width=800, height=600)
canvas.pack()

x=0
def vlacik(x,y,farba):
    canvas.create_rectangle(x-10,y-10,x+130,y-14,width=4)
    canvas.create_rectangle(x,y-75,x+120,y,fill=farba)
    canvas.create_oval(x+15,y-17.5,x+50,y+17.5,fill="black")
    canvas.create_oval(x+70,y-17.5,x+105,y+17.5,fill="black")
for i in range(1,5):
    vlacik(100+x,150,"red")
    x=x+140

x=0
for i in range(1,3):
    vlacik(100+x,350,"green")
    x=x+140

x=0
for i in range(1,4):
    vlacik(100+x,525,"blue")
    x=x+140
