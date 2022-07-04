#standard free energy

#modules
from tkinter import *
from math import *
from Extra import *

g=0
ll=0
shu=0
lol=-1
def calc():
    global lmao
    try:

        #variable entries
        a=float(Ee.get())
        d=Le1.get()
        c=Le2.get()
        
        es=str(cl.get())

        #default values
        if es=="Kelvin":
            ee=float(a)
        elif es=="Celsius":
            ee=C2K(a)
        elif es=="Fahrenheit":
            ee=F2K(a)
        else:
            raise

        a=0
        if len(d)==0:
                go.config(text="Equilibrium Constant was calculated!")
                ls=Lsn2.get()
                b=float(c)
                a=1
                lmao=1
        elif len(c)==0:
                b=float(d)
                go.config(text="Standard Free Energy was calculated!")
                ls=Lsn1.get()
                a=2
                lmao=1
            
        if len(ls)==0:
            ls=0
        else:
            ls=int(ls)

        #notation
        l=b*(10**ls)
        
        #formula
        if a==2:
            su= -(R*ee*(log(l)))
        elif a==1:
            su= exp(-(l/(R*ee)))

    #error
    except:
        su="Invalid Values"

    ll.config(text=su)
    main(g,ll,shu, 0)

def main(gui,la,shucks, lmao):
        global g
        global ll
        global lol
        g=gui
        ll=la
        lol=lmao
        global Ee
        global cl
        global Esn
        global Le1
        global Lsn1
        global Le2
        global Lsn2
    
        global shu
        
        shu=shucks

        cross=Button(gui,text="❌",width=2,height=1,command=lambda:shu(9))
        cross.grid(row=0,column=1000,sticky="ne")

        ###enter variables
        E=Label(g,text="Temperature: ")
        E.grid(column=0, row=1)
        Ee=Entry(g,width=20)
        Ee.grid(column=1, row=1)
        Es=Label(g,text="  Unit: ")
        Es.grid(column=2,row=1)
        k=["Kelvin","Fahrenheit","Celsius"]
        cl = StringVar(g)
        cl.set("Kelvin")
        Esn = OptionMenu(g, cl, *k)
        Esn.grid(column=3,row=1, padx=0)

        L1=Label(g,text="Equilibrium constant: ")
        L1.grid(column=0, row=2)
        Le1=Entry(g,width=20)
        Le1.grid(column=1, row=2)
        Ls1=Label(g,text=" ✕ 10^ ")
        Ls1.grid(column=2,row=2)
        Lsn1=Entry(g,width=10)
        Lsn1.grid(column=3,row=2, padx=5)

        O=Label(g,text="OR")
        O.grid(column=1,columnspan=2,row=3)

        L2=Label(g,text="Standard Free Energy (J/mol): ")
        L2.grid(column=0, row=4)
        Le2=Entry(g,width=20)
        Le2.grid(column=1, row=4)
        Ls2=Label(g,text=" ✕ 10^ ")
        Ls2.grid(column=2,row=4)
        Lsn2=Entry(g,width=10)
        Lsn2.grid(column=3,row=4, padx=5)


        #calling dem() function
        button=Button(g,text="Enter", command=calc)
        button.grid(column=1,row=5, pady=10)

        global go
        if lol!=0:
            try:
                go.config(text="")
            except:
                go=Label(g,text="")
                go.grid(row=6,column=1,columnspan=2)

        Grid.columnconfigure(g,0,weight=10,minsize=150)
        Grid.columnconfigure(g,1,weight=10,minsize=150)
        Grid.columnconfigure(g,2,weight=10,minsize=150)
        Grid.columnconfigure(g,3,weight=10,minsize=150)
        Grid.rowconfigure(g,0,weight=10,minsize=20)
        Grid.rowconfigure(g,1,weight=10,minsize=20)
        Grid.rowconfigure(g,2,weight=10,minsize=20)
        Grid.rowconfigure(g,3,weight=10,minsize=20)
        Grid.rowconfigure(g,4,weight=10,minsize=20)
        Grid.rowconfigure(g,5,weight=10,minsize=20)
        Grid.rowconfigure(g,6,weight=10,minsize=20)
