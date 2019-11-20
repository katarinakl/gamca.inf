
import tkinter
import random
w=1000
h=500
canvas=tkinter.Canvas(width=w, height=h, background="white")
canvas.pack()

def ostrov(ostrov_x,ostrov_y):
    canvas.create_oval(ostrov_x,ostrov_y,ostrov_x+200/800*w,ostrov_y+200/500*h,fill="brown",outline="black")
def mesiac(x,y,d,farba_1,farba_2,pozadie):
    canvas.create_oval(x,y,x+d,y+d, fill=farba_1,outline=farba_1)
    canvas.create_oval(x+d/2,y,x+d*1.5,y+d, fill=farba_2,outline=farba_2)
y=random.randint(100/500*h,160/500*h)
def vlajka(x,y,farba):
    canvas.create_line(x,y,x,y+160/500*h)
    canvas.create_rectangle(x,y,x+110/800*w,y+80/500*h,fill=farba)
def mesiac_obrateny(x,y,d,farba_1,farba_2,pozadie):
    canvas.create_oval(x,y,x-d,y+d,fill=farba_1,outline=farba_1)
    canvas.create_oval(x-d/2,y,x-d*1.5,y+d,fill=farba_2,outline=farba_2)
def logo(x,y,d,farba_1,farba_2,pozadie):
    mesiac(x,y,d,farba_1,farba_2,pozadie)
    mesiac_obrateny(x,y,d,farba_1,farba_2,pozadie)
def lodka (n,y,velkost):
    canvas.create_polygon(n-2*velkost,y,n+2*velkost,y,n+velkost,y+velkost,n-velkost,y+velkost,fill="saddle brown",outline="black")
    canvas.create_rectangle(n-velkost/10,y-2.5*velkost,n+velkost/10,y,fill="brown",outline="black")
    canvas.create_polygon(n,y-velkost/5,n,y-2.5*velkost,n+velkost,y-velkost/2,fill="white",outline="black")
    logo(n,y+velkost/8,velkost*0.65,"light sky blue","saddle brown","saddle brown")
def cely():
    ostrov(0,210/500*h)
    ostrov(560/800*w,210/500*h)
    canvas.create_rectangle(0,h/2,w,h,fill='dark blue')
    mesiac(500/800*w,h/2-y,70/800*w,"yellow","white",'white')
    mesiac(500/800*w,h/2+y-70/800*w,70/800*w,"yellow","dark blue", "dark blue")
    vlajka(100/800*w,50/500*h,"dark green")
    vlajka(660/800*w,50/500*h,"red3")
    mesiac(125/800*w,65/500*h,50/800*w,"red","dark green","dark green")
    logo(715/800*w,75/500*h,30/800*w,"light sky blue","red3","red3")

a=330/800*w
b=290/800*w
c=210/800*w
for i in range(40):
    canvas.delete("all")
    cely()   
    lodka(a,160/500*h+75/500*h,25/800*w+20/800*w)
    a=a+20
    lodka(b,160/500*h+150/500*h,25/800*w+40/800*w)
    b=b+45
    lodka(c,160/500*h+225/500*h,25/800*w+60/800*w)
    c=c+65
    canvas.update()
    canvas.after(100)
