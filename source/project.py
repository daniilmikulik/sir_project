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
root.geometry('250x200')
root.resizable(0, 0)

root.title("Pandemic statistics")
img = Image("photo", file="graphic.png")
root.tk.call('wm','iconphoto',root._w, img)

main_window = MainWindow(root)
main_window.determine()

root.mainloop()