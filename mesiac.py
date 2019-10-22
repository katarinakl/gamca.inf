import tkinter
import random
canvas=tkinter.Canvas(width=800, height=500)
canvas.pack()


def mesiac(x,y,r,pozadie):
    canvas.create_rectangle(0,0,800,250,fill='white')
    canvas.create_oval(0,210,200,410,fill='brown',outline='black')
    canvas.create_oval(560,210,760,410,fill='brown',outline='black')
    canvas.create_line(100,210,100,50)
    canvas.create_rectangle(100,50,210,130,fill='dark green')
    canvas.create_rectangle(0,250,800,500,fill='dark blue')
    canvas.create_oval(x,250+y,x+r,320+y,fill='yellow',outline='dark blue')
    canvas.create_oval(x,250-y,x+r,180-y,fill='yellow',outline='white')
    canvas.create_oval(x+20,250+y,x+20+r,320+y,fill='dark blue',outline='dark blue')
    canvas.create_oval(x+20,250-y,x+20+r,180-y,fill='white',outline='white')
mesiac(520,random.randint(10,150),70,'white')

def vlajka():
    canvas.create_line(100,50,100,210)
    canvas.create_rectangle(100,50,210,130,fill='dark green')
    canvas.create_line(660,50,660,210)
    canvas.create_rectangle(660,50,770,130,fill='red3')
vlajka()

def mesiac2 (x,y,r):
    canvas.create_oval(x,y,x+r,y+r,fill='red',outline='red')
    canvas.create_oval(x+10,y,x+r+10,y+r,fill='dark green',outline='dark green')
mesiac2 (125,65,50)

def mesiac_obrateny(x,y,r=35):
    canvas.create_oval(x-2-r,y,x-2,y+r,fill='light blue',outline='light blue')
    canvas.create_oval(x-2-r-0.5*r,y,x-2-0.5*r,y+r,fill='red3',outline='red3')
    canvas.create_oval(x+2,y,x+r+2,y+r,fill='light blue',outline='light blue')
    canvas.create_oval(x+2+0.5*r,y,x+r+2+0.5*r,y+r,fill='red3',outline='red3')
mesiac_obrateny(715,70)

def lodka(x,y,a,b,m,c,n,p):
    canvas.create_line(x,y,x+a,y)
    canvas.create_line(x+a,y,x+a+b,y-m)
    canvas.create_line(x,y,x-b,y-m)
    canvas.create_line(x-b,y-m,x+a+b,y-m)
    canvas.create_polygon(x,y,x+a,y,x+a+b,y-m,x-b,y-m,fill='brown')
    canvas.create_rectangle(x+0.5*a-c,y-m,x+0.5*a+c,y-m-n,fill='brown2', outline='brown2')
    canvas.create_polygon(x+0.5*a,y-p,x+0.5*a,y-3.25*p,x+0.95*a,y-1.5*p,fill='white',outline='black')
lodka(80,470,120,60,60,10,210,85)
        

