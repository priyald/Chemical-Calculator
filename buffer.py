#buffer of ph

#modules
from tkinter import *
from math import *
from tkinter import ttk
from tkinter.font import Font

g=0
ll=0
shu=0
def calc():
    try:

        #variable entries
        t1=float(Ka.get())
        t2=float(HA.get())
        t3=float(CAB.get())
        
        t4=A1.get()
        t5=A2.get()
        t6=A3.get()

        #default values
        if len(t4)==0:
            t4=0
        else:
            t4=int(t4)
            
        if len(t5)==0:
            t5=0
        else:
            t5=int(t5)
            
        if len(t6)==0:
            t6=0
        else:
            t6=int(t6)

        #notation
        a=t1*(10**t4)
        b=t2*(10**t5)
        c=t3*(10**t6)
        
        #formula
        su=-(log10(a))+(log10(c/b))

    #error
    except:
        su="Invalid Values"

    ll.config(text=su)
    main(g,ll,shu)

def main(gui,lf,shucks):
    global g
    global ll
    global Ka
    global A1
    global HA
    global A2
    global CAB
    global A3
    ll=lf
    g=gui
    
    global shu
    
    shu=shucks

    cross=Button(g,text="❌",width=2,height=1,command=lambda:shu(1))
    cross.grid(row=0,column=1000,sticky="ne")

    K=Label(g,text="Enter acid /base dissociation constant: ",font=Font(size=10))
    K.grid(column=0, row=1)
    Ka=Entry(g,width=20,)
    Ka.grid(column=1, row=1)
    Mul=Label(g,text=" ✕ 10^ ",font=Font(size=10))
    Mul.grid(column=2,row=1)
    A1=Entry(g,width=10,)
    A1.grid(column=3,row=1, pady=5)

    C=Label(g,text="Enter concentration of acid/base (in mol/L): ",font=Font(size=10))
    C.grid(column=0, row=2)
    HA=Entry(g,width=20)
    HA.grid(column=1, row=2)
    Mul=Label(g,text=" ✕ 10^ ",font=Font(size=10))
    Mul.grid(column=2,row=2)
    A2=Entry(g,width=10,)
    A2.grid(column=3,row=2, pady=5)

    Co=Label(g,text="Enter concentration of salt (in mol/L): ",font=Font(size=10))
    Co.grid(column=0, row=3)
    CAB=Entry(g,width=20,)
    CAB.grid(column=1, row=3)
    Mul=Label(g,text=" ✕ 10^ ",font=Font(size=10))
    Mul.grid(column=2,row=3)
    A3=Entry(g,width=10,)
    A3.grid(column=3,row=3, pady=5)

    #call calc() function
    button=Button(g,text="Enter", command=calc, font=Font(size=10))
    button.grid(column=1,row=4)


    Grid.columnconfigure(g,0,weight=10,minsize=20)
    Grid.columnconfigure(g,1,weight=10,minsize=20)
    Grid.columnconfigure(g,2,weight=10,minsize=20)
    Grid.columnconfigure(g,3,weight=10,minsize=20)
    Grid.rowconfigure(g,0,weight=10)
    Grid.rowconfigure(g,1,weight=10)
    Grid.rowconfigure(g,2,weight=10)
    Grid.rowconfigure(g,3,weight=10)
    Grid.rowconfigure(g,4,weight=10)
