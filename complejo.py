import numpy as np
import matplotlib.pyplot as plt
import math

class Complejo:
    def __init__(self, realpart, imagpart):
        self.real = realpart
        self.imaginario = imagpart
        self.norma = math.sqrt(realpart**2 + imagpart**2)

    def conjugado(self):
        self.imaginario = -self.imaginario
        self.real, self.imaginario
        
    def calcula_norma(self):
        self.norma
        
    def pow(self, n):
        x = self.norma**n
        t = math.atan(self.imaginario/self.real)**n
        
        self.real = x*np.cos(t)
        self.imaginario = x*np.sin(t)
        self.imaginario = -self.imaginario
        self.real, self.imaginario