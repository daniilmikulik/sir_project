from tkinter import *
from models import *

class MainWindow(Frame):
    def __init__(self, master):
        super().__init__()
        self.sir = Button(master, text = 'Open SIR window:', width = 15, height = 3)
        self.seird = Button(master, text = 'Open SEIRD window:', width = 15, height = 3)
        self.sir.pack(side = LEFT)
        self.seird.pack(side = RIGHT)
        self.isSirOpened = 0
        self.isSeirdOpened = 0

    def determine(self):
        self.sir['command'] = self.callSir
        self.seird['command'] = self.callSeird

    def callSir(self):
        if (self.isSirOpened == 0):
            self.isSirOpened = 1
            sir_path = Toplevel()
            sir_path.geometry('350x220')
            sir_path.resizable(False, False)
            sir_window = SirWindow(sir_path)
            sir_window.call()
            sir_path.mainloop()
            
        else:
            pass


    def callSeird(self):
        if (self.isSeirdOpened == 0):
            self.isSeirdOpened = 1
            seird_path = Toplevel()
            seird_path.geometry('350x300')
            seird_path.resizable(False, False)
            seird_window = SeirdWindow(seird_path)
            seird_window.call()
            seird_path.mainloop()
            
        else:
            pass


class SeirdWindow(Frame):
    def __init__(self, master):
        super().__init__()
        self.fleft = Frame(master)
        self.fright = Frame(master)

        self.S = Entry(self.fleft, width = 20)
        self.E = Entry(self.fleft, width = 20)
        self.I = Entry(self.fleft, width = 20)
        self.R = Entry(self.fleft, width = 20)
        self.D = Entry(self.fleft, width = 20)

        self.Slabel = Label(self.fleft, text = 'Susceptible', font = ('Comic Sans MS', 12, 'bold'))
        self.Elabel = Label(self.fleft, text = 'Exposed', font = ('Comic Sans MS', 12, 'bold'))
        self.Ilabel = Label(self.fleft, text = 'Infected', font = ('Comic Sans MS', 12, 'bold'))
        self.Rlabel = Label(self.fleft, text = 'Recovered', font = ('Comic Sans MS', 12, 'bold'))
        self.Dlabel = Label(self.fleft, text = 'Dead', font = ('Comic Sans MS', 12, 'bold'))
        
        self.beta = Entry(self.fright, width = 20)
        self.delta = Entry(self.fright, width = 20)
        self.gamma = Entry(self.fright, width = 20)
        self.mu = Entry(self.fright, width = 20)
        
        self.Blabel = Label(self.fright, text = 'Your beta:', font = ('Comic Sans MS', 12, 'bold'))
        self.Glabel = Label(self.fright, text = 'Your gamma:', font = ('Comic Sans MS', 12, 'bold'))
        self.DElabel = Label(self.fright, text = 'Your delta:', font = ('Comic Sans MS', 12, 'bold'))
        self.MUlabel = Label(self.fright, text = 'Your mu:', font = ('Comic Sans MS', 12, 'bold'))
        self.Bbutton = Button(self.fright, text = 'Build a SEIRD model:', width = 15, height = 2)

        self.fleft.pack(side = LEFT)
        self.fright.pack(side = RIGHT)
        
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
        self.Bbutton.pack()

    def call(self):
        self.Bbutton['command'] = self.createModel

    def callError(self):
        err_path = Toplevel()
        err_path.geometry('250x150')
        err_path.resizable(False, False)
        err_window = ErrorWindow(err_path)
        err_path.mainloop()

    def createModel(self):
        #try:
            S0 = int(self.S.get())
            E0 = int(self.E.get())
            I0 = int(self.I.get())
            R0 = int(self.R.get())
            D0 = int(self.D.get())
            b = float(self.beta.get())
            d= float(self.delta.get())
            g = float(self.gamma.get())
            m = float(self.mu.get())
            SEIRD_instance = SEIRD(b, g, d, m,  S0, E0, I0, R0, D0)
            SEIRD_instance.build()
        #except ValueError:
        #    self.callError


class SirWindow(Frame):
    def __init__(self, master):
        super().__init__()
        self.fleft = Frame(master)
        self.fright = Frame(master)

        self.S = Entry(self.fleft, width = 20)
        self.I = Entry(self.fleft, width = 20)
        self.R = Entry(self.fleft, width = 20)
        self.Slabel = Label(self.fleft, text = 'Susceptible', font = ('Comic Sans MS', 12, 'bold'))
        self.Ilabel = Label(self.fleft, text = 'Infected', font = ('Comic Sans MS', 12, 'bold'))
        self.Rlabel = Label(self.fleft, text = 'Recovered', font = ('Comic Sans MS', 12, 'bold'))
        
        self.beta = Entry(self.fright, width = 20)
        self.gamma = Entry(self.fright, width = 20)
        self.Blabel = Label(self.fright, text = 'Your beta:', font = ('Comic Sans MS', 12, 'bold'))
        self.Glabel = Label(self.fright, text = 'Your gamma:', font = ('Comic Sans MS', 12, 'bold'))
        self.Bbutton = Button(self.fright, text = 'Build a SIR model:', width = 15, height = 2)

        self.fleft.pack(side = LEFT)
        self.fright.pack(side = RIGHT)

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
        self.Bbutton.pack()
    
    def call(self):
        self.Bbutton['command'] = self.createModel

    def callError(self):
        err_path = Toplevel()
        err_path.geometry('250x150')
        err_path.resizable(False, False)
        err_window = ErrorWindow(err_path)
        err_path.mainloop()

    def createModel(self):
        try:
            S0 = int(self.S.get())
            I0 = int(self.I.get())
            R0 = int(self.R.get())
            b = float(self.beta.get())
            g = float(self.gamma.get())
            SIR_instance = SIR(b, g, S0, I0, R0)
            SIR_instance.build()
        except ValueError:
            self.callError
            

class ErrorWindow(Frame):
    def __init__(self, master):
        super().__init__()
        self.l = Label(master, text = 'Incorrect input data!', font = ('Comic Sans MS', 24, 'bold'))
        self.l.pack()

    

        

root = Tk()
root.geometry('300x150')
root.resizable(0, 0)

root.title("Pandemic statistics")
img = Image("photo", file="graphic.png")
root.tk.call('wm','iconphoto',root._w, img)

main_window = MainWindow(root)
main_window.determine()

root.mainloop()