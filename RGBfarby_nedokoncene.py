import tkinter
from random import randrange
X_MAX,Y_MAX= 800,600
c=tkinter.Canvas(width=X_MAX,height=Y_MAX,bg="white")
c.pack()

r,g,b,=randrange(256), randrange(256), randrange(256)
ar,ag,ab= 1,1,1

while True:
    c.delete('all')
    farba= f"#{r:02x}{g:02x}{b:02x}"
    r+=ar
    g+=ag
    b+=ab    
    c.create_rectangle(X_MAX/2-200,Y_MAX/2-200,X_MAX/2+200,Y_MAX/2+200,fill=farba)
    if r==255 or r==0:
        ar*=-1
    if g==255 or g==0:
        ag*=-1
    if b==255 or b==0:
        ab*=-1
    c.update()
    c.after(1)
