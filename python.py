
from tkinter import *
oldgui=Tk()
newgui=Tk()
def inbutton():
    m=a.get()
    X=Label(text=m,fg='Blue',bg='Green',font='25').pack()
def outbutton():
    Y = Label(newgui,text='GET OUT', fg='Blue', bg='Green', font='25').pack()


oldgui.geometry('500x500+200+300')
newgui.geometry('500x500+700+250')
oldgui.title("NEW WINDOW")
newgui.title("TKinter")

a=StringVar()

l=Label(text='HI',fg='black',bg='Yellow',font='15').pack()
b1=Button(text='Click Here',fg='black',bg='pink',command=inbutton,font='30').pack()
L=Button(newgui,text='Stay Away',fg='black',bg='pink',command=lambda :L.destroy(),font='30')
L.pack()


text= Entry(textvariable=a).pack()

oldgui.mainloop()