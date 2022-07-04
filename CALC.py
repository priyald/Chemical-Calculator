from tkinter import *
import tkinter.ttk as ttk
from tkinter.font import Font
import buffer as b
import activ as ac
import dep
import ele
import ist
import lbl
import mol
import rc
import sf

g=Tk()
g.geometry("700x450+50+180")
g.minsize(width=600,height=400)

g.title("Chemistry Calculator")

s=ttk.Style()

n=ttk.Notebook(g,height=140)
n.grid(row=0,column=0,sticky="news")

lf=LabelFrame(g, text="Answer",relief="sunken", bg="#ffffef")
lf.grid(row=1,column=0, pady=(5,10),sticky="news",padx=10)

L=Label(lf,text="", bg="#ffffef", font=('Helvatical',15))
L.grid(row=0,column=0,padx=20)

I=Frame(n,padx=5,pady=5)
II=Frame(n,padx=5,pady=5)
III=Frame(n,padx=5,pady=5)
IV=Frame(n,padx=5,pady=5)
V=Frame(n,padx=5,pady=5)
VI=Frame(n,padx=5,pady=5)
VII=Frame(n,padx=5,pady=5)
VIII=Frame(n,padx=5,pady=5)
IX=Frame(n,padx=5,pady=5)
i=ii=iii=iv=v=vi=vii=viii=ix=0

def hide(x):
    if x==1:
        n.hide(I)
        i=0
    elif x==2:
        n.hide(II)
        ii=0
    elif x==3:
        n.hide(III)
        iii=0
    elif x==4:
        n.hide(IV)
        iv=0
    elif x==5:
        n.hide(V)
        v=0
    elif x==6:
        n.hide(VI)
        vi=0
    elif x==7:
        n.hide(VII)
        vii=0
    elif x==8:
        n.hide(VIII)
        viii=0
    elif x==9:
        n.hide(IX)
        ix=0

def show(a):
    global i
    global ii
    global iii
    global iv
    global v
    global vi
    global vii
    global viii
    global ix
    global n
    L.config(text="")
    if a==1:
        b.main(I,L,hide)
        if i==0:
            n.add(I,text=" Buffer pH ")
        n.select(I)
        i=1
    elif a==2:
        ac.main(II,L,hide)
        if ii==0:
            n.add(II,text=" Activation Energy ")
        n.select(II)
        ii=1
    elif a==3:
        dep.main(III,L,hide)
        if iii==0:
            n.add(III,text=" Freeing Point Depression ")
        n.select(III)
        iii=1
    elif a==4:
        ele.main(IV,L,hide)
        if iv==0:
            n.add(IV,text=" Boiling Point Elevation ")
        n.select(IV)
        iv=1
    elif a==5:
        ist.main(V,L,hide)
        if v==0:
            n.add(V,text=" Ionic Strength ")
        n.select(V)
        v=1
    elif a==6:
        lbl.main(VI,L,hide)
        if vi==0:
            n.add(VI,text=" Beer Lambert Law ")
        n.select(VI)
        vi=1
    elif a==7:
        mol.main(VII,L,hide)
        if vii==0:
            n.add(VII,text=" Molarity ")
        n.select(VII)
        vii=1
    elif a==8:
        rc.main(VIII,L,hide)
        if viii==0:
            n.add(VIII,text=" Rate Constant ")
        n.select(VIII)
        viii=1
    elif a==9:
        sf.main(IX,L,hide,-1)
        if ix==0:
            n.add(IX,text=" Standard Free Energy ")
        n.select(IX)
        ix=1

z=Frame(n)
n.add(z,text="Home")

ti=Label(z, text="Calculator", font=('Helvatical bold',25), fg="#1212ff", justify="center", bg="#efefff")
ti.grid(row=0,column=0,columnspan=3, sticky="news")

b1=Button(z, text="Buffer pH",relief="raised",bg="#ffffff", font=Font(size=10),command=lambda: show(1))
b1.grid(row=1,column=0, sticky="news")
b2=Button(z, text="Activation Energy",relief="raised",bg="#ffffff", font=Font(size=10),command=lambda: show(2))
b2.grid(row=1,column=1, sticky="news")
b3=Button(z, text="Freezing Point Depression",relief="raised",bg="#ffffff", font=Font(size=10),command=lambda: show(3))
b3.grid(row=1,column=2, sticky="news")
b4=Button(z, text="Boiling Point Elevation",relief="raised",bg="#ffffff", font=Font(size=10),command=lambda: show(4))
b4.grid(row=2,column=0, sticky="news")
b5=Button(z, text="Ionic Strength",relief="raised",bg="#ffffff", font=Font(size=10),command=lambda: show(5))
b5.grid(row=2,column=1, sticky="news")
b6=Button(z, text="Beer Lambert Law",relief="raised",bg="#ffffff", font=Font(size=10),command=lambda: show(6))
b6.grid(row=2,column=2, sticky="news")
b7=Button(z, text="Molarity",relief="raised",bg="#ffffff", font=Font(size=10),command=lambda: show(7))
b7.grid(row=3,column=0, sticky="news")
b8=Button(z, text="Rate Constant",relief="raised",bg="#ffffff", font=Font(size=10),command=lambda: show(8))
b8.grid(row=3,column=1, sticky="news")
b9=Button(z, text="Standard Free Energy",relief="raised",bg="#ffffff", font=Font(size=10),command=lambda: show(9))
b9.grid(row=3,column=2, sticky="news")

go=Label(g,text="All answers in SI units",justify="right")
go.grid(row=2,column=0)

for a in range(4):
    Grid.rowconfigure(z,a,weight=100)
for a in range(3):
    Grid.columnconfigure(z,a,weight=100)

Grid.rowconfigure(g,0,weight=100)
Grid.rowconfigure(g,1,weight=45)
Grid.rowconfigure(g,2,weight=5)
Grid.columnconfigure(g,0,weight=100)

g.mainloop()
