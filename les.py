import tkinter
import random
canvas=tkinter.Canvas(width=1000, height=800, background="white")
canvas.pack()

def strom():
    x=random.randint(40,960)
    y=random.randint(50,750)
    r=random.randint(10,40)
    canvas.create_rectangle(x-5,y,x+5,y+50,fill="brown")
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="green")

for i in range(1,11):
    strom()

def trava ():
    x= random.randint(15,985)
    y= random.randint(20,800)
    for i in range (1,random.randint(3,10)):
        w= random.randint(1,3)
        m= random.randint(-15,15)
        n= random.randint(5,20)
        canvas.create_line(x,y,x+m,y-n,fill="dark green",width=w)
for i in range (1,21):
    trava()
