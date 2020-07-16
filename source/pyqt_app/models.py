import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from tkinter import PhotoImage



class SEIRD:
    def __init__(self, b, g, d, m,  S0, E0, I0, R0, D0):
        self.beta = b
        self.gamma = g
        self.delta = d
        self.mu = m
        self.S0 = S0
        self.E0 = E0
        self.I0 = I0
        self.R0 = R0
        self.D0 = D0
        self.N = S0 + E0 + I0 + R0 + D0

    def model(self, z, t):
    
        dSdt = -self.beta * z[0] * z[2] / self.N
        dEdt =  (self.beta * z[0] *z[2] / self.N) - (self.delta * z[1])
        dIdt = (self.delta * z[1]) - (self.gamma * z[2]) - (self.mu * z[2])
        dRdt = self.gamma * z[2]
        dDdt = self.mu * z[2]
        dzdt = [dSdt, dEdt, dIdt, dRdt, dDdt]
        return dzdt

    def s_build(self):
        z0 = [self.S0, self.E0, self.I0, self.R0, self.D0]

        t = np.linspace(0, 365)

        z = odeint(self.model, z0, t)

        fig = plt.figure()
        thismanager = plt.get_current_fig_manager()
        img = PhotoImage(file='graphic.png')
        thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
        plt.title('SEIRD model according to the input data')
        plt.plot(t, z[:,0], color = 'blue', label = r'Susceptible')
        plt.plot(t, z[:,1], color = 'yellow', label = r'Exposed')
        plt.plot(t, z[:,2], color = 'red', label = r'Infected')
        plt.plot(t, z[:,3], color = 'green', label = r'Recovered')
        plt.plot(t, z[:,4], color = 'black', label = r'Dead')
        plt.ylabel('Population')
        plt.xlabel('Time')
        plt.legend(loc = 'best')
        plt.grid(True)
        plt.gcf().canvas.set_window_title('SEIRD model')
        plt.show()

class SIR:
    def __init__(self, b, g, S0, I0, R0):
        self.beta = b
        self.gamma = g
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.N = S0 + I0 + R0

    def model(self, z, t):
    
        dSdt = -self.beta * z[0] * z[1] / self.N
        dIdt =  (self.beta * z[0] *z[1] / self.N) - (self.gamma * z[1])
        dRdt = self.gamma * z[1]
        dzdt = [dSdt, dIdt, dRdt]
        return dzdt

    def build(self):
        z0 = [self.S0, self.I0, self.R0]

        t = np.linspace(0, 365)

        z = odeint(self.model, z0, t)

        fig = plt.figure()
        thismanager = plt.get_current_fig_manager()
        img = PhotoImage(file='graphic.png')
        thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
        #thismanager.title('SIR model')
        plt.title('SIR model according to the input data')
        plt.plot(t, z[:,0], 'b-', label = r'Susceptible')
        plt.plot(t, z[:,1], 'r-', label = r'Infected')
        plt.plot(t, z[:,2], 'g-', label = r'Recovered')
        plt.ylabel('Population')
        plt.xlabel('Time')
        plt.legend(loc = 'best')
        plt.grid(True)
        plt.gcf().canvas.set_window_title('SIR model')
        plt.show()
