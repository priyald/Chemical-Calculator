#freezing point depression

#modules
from tkinter import *
from math import *

g=0
ll=0
shu=0
def calc():
    try:

        #variable entries
        a=float(Ee.get())
        b=float(Le.get())
        c=Ae.get()
        
        es=Esn.get()
        ls=Lsn.get()

        #default values
        if len(es)==0:
            es=0
        else:
            es=int(es)
            
        if len(ls)==0:
            ls=0
        else:
            ls=int(ls)
            
        if len(c)==0:
            c=1
        else:
            c=float(c)

        #notation
        e=a*(10**es)
        l=b*(10**ls)
        
        #formula
        su=c*e*l

    #error
    except:
        su="Invalid Values"

    ll.config(text=su)
    main(g,ll,shu)

def main(gui,lf, shucks):
    global g
    global ll
    global Ee
    global Esn
    global Le
    global Lsn
    global Ae
    g=gui
    ll=lf
    
    global shu
    
    shu=shucks

    cross=Button(gui,text="❌",width=2,height=1,command=lambda:shu(3))
    cross.grid(row=0,column=1000,sticky="ne")
    
    #enter variables
    E=Label(g,text="Molality (mol/kg): ")
    E.grid(column=0, row=1)
    Ee=Entry(g,width=20)
    Ee.grid(column=1, row=1)
    Es=Label(g,text=" ✕ 10^ ")
    Es.grid(column=2,row=1)
    Esn=Entry(g,width=10)
    Esn.grid(column=3,row=1, padx=0)

    L=Label(g,text="Cryoscopic constant (K*kg/mol): ")
    L.grid(column=0, row=2)
    Le=Entry(g,width=20)
    Le.grid(column=1, row=2)
    Ls=Label(g,text=" ✕ 10^ ")
    Ls.grid(column=2,row=2)
    Lsn=Entry(g,width=10)
    Lsn.grid(column=3,row=2, padx=5)

    A=Label(g,text="Van't Hoff factor: ")
    A.grid(column=0, row=3)
    Ae=Entry(g,width=20)
    Ae.grid(column=1, row=3)


    #calling dem() function
    button=Button(g,text="Enter", command=calc)
    button.grid(column=1,row=4, pady=10)


    Grid.columnconfigure(g,0,weight=10,minsize=20)
    Grid.columnconfigure(g,1,weight=10,minsize=20)
    Grid.columnconfigure(g,2,weight=10,minsize=20)
    Grid.columnconfigure(g,3,weight=10,minsize=20)
    Grid.rowconfigure(g,0,weight=10)
    Grid.rowconfigure(g,1,weight=10)
    Grid.rowconfigure(g,2,weight=10)
    Grid.rowconfigure(g,3,weight=10)
    Grid.rowconfigure(g,4,weight=10)
