import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

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
        plt.title('SIR model according to the input data')
        plt.plot(t, z[:,0], 'b-', label = r'Susceptible')
        plt.plot(t, z[:,1], 'r-', label = r'Infected')
        plt.plot(t, z[:,2], 'g-', label = r'Recovered')
        plt.ylabel('Population')
        plt.xlabel('time')
        plt.legend(loc = 'best')
        plt.grid(True)
        plt.show()

#A = SIR(0.128, 0.0963, 5742000, 638000, 0)
#A.build()