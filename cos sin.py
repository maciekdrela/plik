from tkinter import *
import math
szer=800
wys=600
ile_p=58
x=0

okres=2*math.pi
dx=szer/ile_p
ile_okr=1
alfa=0
zmienna=0
przedzial=ile_okr*okres

dalfa=przedzial/ile_p
prog=Tk()
tlo=Canvas(prog,width=szer,height=wys)
tlo.pack()

linia=tlo.create_line(0,300,800,300,width=2)

while x<=szer:
    y1=wys-(math.sin(alfa)*wys//4+wys//2)
    alfa+=dalfa
    y2=wys-(math.sin(alfa)*wys//4+wys//2)
    tlo.create_line(x,y1,x+dx,y2,width=2)
    zmienna+=1
    r=5
    if zmienna==3:
        tlo.create_oval(x-r,y1-r,x+r,y2+r,width=2)
        zmienna=1
    x+=dx
prog.mainloop()




# while x<=szer:
#     y1=wys-(math.sin(alfa)*wys//4+wys//2)
#     alfa+=dalfa
#     y2=wys-(math.sin(alfa)*wys//4+wys//2)
#     tlo.create_line(x,y1,x+dx,y2,width=2)
#     tlo.create_oval(x-dx,y1-dx,x+dx,y2+dx)
#     x+=dx
# prog.mainloop()