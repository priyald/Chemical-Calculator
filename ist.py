#ionic strength

#modules
from tkinter import *
from math import *

#enter variables
a=1
suu=0
g=0
ll=0
s=0
shu=0

#sum notation
def rest():
    global a
    global suu
    global s
    a=1
    suu=0
    s=0
    main(g,ll,shu)
    
def calc():
    global suu
    global s
    cause()
    if s!=-1:
        ll.config(text=suu)
        but2.config(text="Restart",command=rest)

def cause():
    global suu
    global Ee
    global Be
    global Esn
    global w
    global a
    global s
    
    try:
        #variable entries
        x=float(Ee.get())
        b=float(Be.get())
        
        es=Esn.get()

        #default values
        if len(es)==0:
            es=0
        else:
            es=int(es)

        #notation
        e=x*(10**es)
        suu+=e*b**2
        s=0
    except:
        s=-1
        ll.config(text="Invalid Values")
        a-=1
        go()
        
def su():
    global but2
    global s

    but2.config(text="Calculate",command=calc)

    if s==-1:
        ll.config(text="")
    else:
        cause()

    go()

def go():
    global a

    global Ee
    global Esn
    global Be
    global suu
    global s
    
    E=Label(g,text="Concentration of ion "+str(a)+" (mol/L): ")
    E.grid(column=0, row=1, pady=5)
    Ee=Entry(g,width=20)
    Ee.grid(column=1, row=1, pady=5)
    Es=Label(g,text=" ✕ 10^ ")
    Es.grid(column=2,row=1, pady=5)
    Esn=Entry(g,width=10)
    Esn.grid(column=3,row=1, padx=0, pady=5)

    B=Label(g,text="Charge of ion "+str(a)+": ")
    B.grid(column=0, row=2, pady=2)
    Be=Entry(g,width=20)
    Be.grid(column=1, row=2, pady=2)

    a+=1

    but=Button(g,text="Add another component/ion", command=su)
    but.grid(column=1,row=3)

#first components
def main(gui,la,shucks):
    global g
    global ll
    global w
    global but2
    global a
    
    g=gui
    ll=la
    
    global shu

    a=1
    shu=shucks

    cross=Button(gui,text="❌",width=2,height=1,command=lambda:shu(5))
    cross.grid(row=0,column=1000,sticky="ne")
    go()

    try:
        but2.config(text="Calculate",command=calc)
    except:
        but2=Button(g,text="Calculate", command=calc)
        but2.grid(column=1,row=4)

    Grid.columnconfigure(g,0,weight=10,minsize=20)
    Grid.columnconfigure(g,1,weight=10,minsize=20)
    Grid.columnconfigure(g,2,weight=10,minsize=20)
    Grid.columnconfigure(g,3,weight=10,minsize=20)
    Grid.rowconfigure(g,0,weight=10)
    Grid.rowconfigure(g,1,weight=10)
    Grid.rowconfigure(g,2,weight=10)
    Grid.rowconfigure(g,3,weight=10)
    Grid.rowconfigure(g,4,weight=10)
