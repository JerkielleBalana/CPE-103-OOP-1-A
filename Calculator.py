from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number')
        self.lbl2=Label(win, text='Second number')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Add', fg= 'Blue')
        self.btn2=Button(win, text='Subtract', fg= 'Pink')
        self.btn3=Button(win,text='Multiply', fg='Red')
        self.btn4= Button(win, text = 'Divide', fg='Brown')
        self.btn5=Button(win, text = 'Clear')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1 = Button(win, text='Add', command=self.add)
        self.b2 = Button(win, text='Subtract', command=self.sub)
        self.b2.bind('<Button-1>', self.sub)
        self.b3 = Button(win, text='Multiply', command=self.multiply)
        self.b3.bind('<Button-2>', self.multiply)
        self.b4 = Button(win, text = 'Divide', command = self.divide)
        self.b4.bind('<Button-3>', self.divide)
        self.b5 = Button(win, text = 'Clear', command = self.clear)
        self.b5.bind('<Button-4>', self.clear)
        self.b1.place(x=100, y=150)
        self.b2.place(x=140, y=150)
        self.b3.place(x=200,y=150)
        self.b4.place(x = 260, y=150)
        self.b5.place( x = 330, y= 150)

        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)


    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def multiply(self):
        self.t3.delete(0,'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def divide(self):
        self.t3.delete( 0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1/num2
        self.t3.insert(END, str(result))
    def clear(self):
        self.t1.delete( 0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete( 0, 'end')
window=Tk()
mywin=MyWindow(window)
window.title('asd')
window.geometry("400x300+10+10")
window.mainloop()
