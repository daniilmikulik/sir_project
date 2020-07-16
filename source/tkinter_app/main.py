'''
from tkinter import *

def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

root = Tk()

e = Entry(root, width = 20) #creates a simple emtry space
b = Button(root, text = 'Change') #adds a button
l = Label(root, bg = 'black', fg = 'white', width = 20) #adds a label

b.bind('<Button-1>', strToSortlist) #Button-1 event means a LMB click

e.pack()
b.pack()
l.pack()
root.mainloop()

class Block:
    def __init__(self, master):
        self.e = Entry(master, width = 20)
        self.b = Button(master, text = "Change")
        self.l = Label(master, bg = 'green', fg = 'white', width = 20)
        self.b['command'] = self.strToSortlist
        self.e.pack()
        self.b.pack()
        self.l.pack()

    def setFunc(self, func):
        self.b['command'] = eval('self.' + func)

    def strToSortlist(self):
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l['text'] = ' '.join(s)

    def strReverse(self):
        s = self.e.get()
        s = s.split()
        s.reverse()
        self.l['text'] = ' '.join(s)

root = Tk()

first_block = Block(root)
first_block.setFunc('strToSortlist')

second_block = Block(root)
second_block.setFunc('strReverse')
root.mainloop()



from tkinter import *

class Calc:
    def __init__(self, master):
        self.a = Entry(master, width = 20)
        self.b = Entry(master, width = 20)
        self.sum = Button(master, text = '+', fg = 'red', width = 5, height = 5)
        self.dis = Button(master, text = '-', width = 5, height = 5)
        self.mul = Button(master, text = '*', width = 5, height = 5)
        self.div = Button(master, text = '/', width = 5, height = 5)
        self.res = Label(master, bg = 'white', fg = 'black', width = 30)
        self.a.pack()
        self.b.pack()
        self.sum.pack()
        self.dis.pack()
        self.mul.pack()
        self.div.pack()
        self.res.pack()

    def compute(self):
        self.sum['command'] = self.add
        self.dis['command'] = self.distract
        self.mul['command'] = self.multiply
        self.div['command'] = self.divide

    def add(self):
        try:
            self.res['text'] = str(int(self.a.get())+int(self.b.get()))
        except ValueError:
            self.res['text'] = 'Inappropriate format of input data!'
        
    def distract(self):
        try:
            self.res['text'] = str(int(self.a.get()) - int(self.b.get()))
        except ValueError:
            self.res['text'] = 'Inappropriate format of input data!'

    def multiply(self):
        try:
            self.res['text'] = str(int(self.a.get()) * int(self.b.get()))
        except ValueError:
            self.res['text'] = 'Inappropriate format of input data!'

    def divide(self):
        try:
            self.res['text'] = str(int(self.a.get()) // int(self.b.get()))
        except ZeroDivisionError:
            self.res['text'] = 'Division by zero! Check your input data.'
        except ValueError:
            self.res['text'] = 'Inappropriate format of input data!'

root = Tk()
root.title("Calculator")
img = Image("photo", file="calculator.png")
root.tk.call('wm','iconphoto',root._w, img)
calc = Calc(root)
calc.compute()

root.mainloop()

from tkinter import *
root = Tk()
b1 = Button(text = 'Change', width = 15, height = 3)

def change():
    b1['text'] = 'Changed'
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'

b1.config(command = change)
b1.pack()

l1 = Label(text = 'Machine learning', font = 'Arial 32')
l2 = Label(text = 'Lorem ipsum', font = ('Comic Sans MS', 24, 'bold'))
l1.config(bd=20, bg='#ffaaaa')
l2.config(bd=20, bg='#aaffff')
l1.pack()
l2.pack()
root.mainloop()
'''
from tkinter import *

class MainWindow(Frame):
    def __init__(self, master):
        super().__init__()
        self.sir = Button(master, text = 'Open SIR window:', width = 15, height = 3)
        self.seird = Button(master, text = 'Open SEIRD window:', width = 15, height = 3)
        self.sir.pack()
        self.seird.pack()

    def determine(self):
        self.sir['command'] = self.callSir
        self.seird['command'] = self.callSeird

    def callSir(self):
        sir_path = Toplevel()
        sir_path.geometry('200x270')
        sir_path.resizable(False, False)
        sir_window = SirWindow(sir_path)
        sir_path.mainloop()


    def callSeird(self):
        seird_path = Toplevel()
        seird_path.geometry('200x450')
        seird_path.resizable(False, False)
        seird_window = SeirdWindow(seird_path)
        seird_path.mainloop()



class SeirdWindow:
    def __init__(self, master):
        self.S = Entry(master, width = 20)
        self.E = Entry(master, width = 20)
        self.I = Entry(master, width = 20)
        self.R = Entry(master, width = 20)
        self.D = Entry(master, width = 20)
        self.Slabel = Label(master, text = 'Susceptible', font = ('Comic Sans MS', 12, 'bold'))
        self.Elabel = Label(master, text = 'Exposed', font = ('Comic Sans MS', 12, 'bold'))
        self.Ilabel = Label(master, text = 'Infected', font = ('Comic Sans MS', 12, 'bold'))
        self.Rlabel = Label(master, text = 'Recovered', font = ('Comic Sans MS', 12, 'bold'))
        self.Dlabel = Label(master, text = 'Dead', font = ('Comic Sans MS', 12, 'bold'))
        self.beta = Entry(master, width = 20)
        self.delta = Entry(master, width = 20)
        self.gamma = Entry(master, width = 20)
        self.mu = Entry(master, width = 20)
        self.Blabel = Label(master, text = 'Your beta:', font = ('Comic Sans MS', 12, 'bold'))
        self.Glabel = Label(master, text = 'Your gamma:', font = ('Comic Sans MS', 12, 'bold'))
        self.DElabel = Label(master, text = 'Your delta:', font = ('Comic Sans MS', 12, 'bold'))
        self.MUlabel = Label(master, text = 'Your mu:', font = ('Comic Sans MS', 12, 'bold'))
        self.Slabel.pack()
        self.S.pack()
        self.Elabel.pack()
        self.E.pack()
        self.Ilabel.pack()
        self.I.pack()
        self.Rlabel.pack()
        self.R.pack()
        self.Dlabel.pack()
        self.D.pack()
        self.Blabel.pack()
        self.beta.pack()
        self.DElabel.pack()
        self.delta.pack()
        self.Glabel.pack()
        self.gamma.pack()
        self.MUlabel.pack()
        self.mu.pack()

class SirWindow:
    def __init__(self, master):
        self.S = Entry(master, width = 20)
        self.I = Entry(master, width = 20)
        self.R = Entry(master, width = 20)
        self.Slabel = Label(master, text = 'Susceptible', font = ('Comic Sans MS', 12, 'bold'))
        self.Ilabel = Label(master, text = 'Infected', font = ('Comic Sans MS', 12, 'bold'))
        self.Rlabel = Label(master, text = 'Recovered', font = ('Comic Sans MS', 12, 'bold'))
        self.beta = Entry(master, width = 20)
        self.gamma = Entry(master, width = 20)
        self.Blabel = Label(master, text = 'Your beta:', font = ('Comic Sans MS', 12, 'bold'))
        self.Glabel = Label(master, text = 'Your gamma:', font = ('Comic Sans MS', 12, 'bold'))
        self.Slabel.pack()
        self.S.pack()
        self.Ilabel.pack()
        self.I.pack()
        self.Rlabel.pack()
        self.R.pack()
        self.Blabel.pack()
        self.beta.pack()
        self.Glabel.pack()
        self.gamma.pack()
        

root = Tk()
root.geometry('200x200')
root.resizable(0, 0)

root.title("Pandemic statistics")
img = Image("photo", file="graphic.png")
root.tk.call('wm','iconphoto',root._w, img)

main_window = MainWindow(root)
main_window.determine()

root.mainloop()










