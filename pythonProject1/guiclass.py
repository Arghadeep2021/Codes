from tkinter import *
calc=Tk()
calc.geometry('300x300+200+200')
calc.title("GUI CALCULATOR")
equation = ""
def press(num):
    global equation
    equation= equation + str(num)
    expression.set(equation)

def equals():
    try:
        global equation
        result = str(eval(equation))
        expression.set(result)
        equation = " "
    except:
        expression.set("error")
        equation = " "

def clear():
    global equation
    equation=""
    expression.set(" ")


expression=StringVar()

equation_field = Entry(calc, textvariable=expression,bg='orange')
equation_field.grid(row=0,columnspan=6)


plus=Button(calc,text="+", font=10,bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press("+"),fg='Blue')
plus.grid(row=1,column=0)

substract=Button(calc,text="-", font=10,bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press("-"), fg='Blue')
substract.grid(row=2,column=0)

multiply=Button(calc,text="*", font=10,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press("*"))
multiply.grid(row=3,column=0)\

divide=Button(calc,text="/", font=10, fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press("/"))
divide.grid(row=1,column=1)

b1=Button(calc,text="1", font=10,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press(1))
b1.grid(row=2,column=1)

b2=Button(calc,text="2", font=10,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press(2))
b2.grid(row=3,column=1)

b3=Button(calc,text='3', font=10,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press(3))
b3.grid(row=1,column=2)

b4=Button(calc,text='4', font=10,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press(4))
b4.grid(row=2,column=2)

b5=Button(calc,text='5', font=10,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press(5))
b5.grid(row=3,column=2)

b6=Button(calc,text='6',font=10,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press(6))
b6.grid(row=1,column=3)

b7=Button(calc,text='7',font=10,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press(7))
b7.grid(row=2,column=3)

b8=Button(calc,text='8',font=10,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press(8))
b8.grid(row=3,column=3)

b9=Button(calc,text='9',font=10,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press(9))
b9.grid(row=1,column=4)

b10=Button(calc,text='0',font=12,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=lambda: press(0))
b10.grid(row=2,column=4)

b11=Button(calc,text='=',font=10,fg='Blue',bg='yellow',activebackground='gray',cursor='hand2',command=equals)
b11.grid(row=3,column=4)

clr=Button(calc,text='CLEAR',font=15,fg='Blue',bg='yellow',activebackground='gray',command=clear)
clr.grid(row=12,columnspan=6)

calc.mainloop()