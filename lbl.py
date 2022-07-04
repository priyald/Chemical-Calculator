#beer lambert law

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
        c=float(Ae.get())
        
        es=Esn.get()
        ls=Lsn.get()
        asn=Asn.get()

        #default values
        if len(es)==0:
            es=0
        else:
            es=int(es)
            
        if len(ls)==0:
            ls=0
        else:
            ls=int(ls)
            
        if len(asn)==0:
            asn=0
        else:
            asn=int(asn)

        #notation
        e=a*(10**es)
        l=b*(10**ls)
        a=c*(10**asn)
        
        #formula
        su=a/(l*e)

    #error
    except:
        su="Invalid Values"

    ll.config(text=su)
    main(g,ll,shu)

def main(gui,la,shucks):
    global g
    global ll
    g=gui
    ll=la
    global Ee
    global Esn
    global Le
    global Lsn
    global Ae
    global Asn
    
    global shu
    
    shu=shucks

    cross=Button(gui,text="❌",width=2,height=1,command=lambda:shu(6))
    cross.grid(row=0,column=1000,sticky="ne")
    
    #enter variables
    E=Label(g,text="Enter molar absorption coefficient/molar absorptivity (1/M*cm): ")
    E.grid(column=0, row=1)
    Ee=Entry(g,width=20)
    Ee.grid(column=1, row=1)
    Es=Label(g,text=" ✕ 10^ ")
    Es.grid(column=2,row=1)
    Esn=Entry(g,width=10)
    Esn.grid(column=3,row=1, padx=0)

    L=Label(g,text="Enter path length (cm): ")
    L.grid(column=0, row=2)
    Le=Entry(g,width=20)
    Le.grid(column=1, row=2)
    Ls=Label(g,text=" ✕ 10^ ")
    Ls.grid(column=2,row=2)
    Lsn=Entry(g,width=10)
    Lsn.grid(column=3,row=2, padx=5)

    A=Label(g,text="Enter absorbance: ")
    A.grid(column=0, row=3)
    Ae=Entry(g,width=20)
    Ae.grid(column=1, row=3)
    As=Label(g,text=" ✕ 10^ ")
    As.grid(column=2,row=3)
    Asn=Entry(g,width=10)
    Asn.grid(column=3,row=3, padx=5)


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
