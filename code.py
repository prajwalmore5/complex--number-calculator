# --------------
import pandas as pd
import numpy as np
import math
import cmath
#Code starts here
class complex_numbers(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

    def __add__(self, other):
        a = self.real + other.real
        b = self.imag + other.imag
        return complex_numbers(a,b)

    def __sub__(self, other):
        a = self.real - other.real
        b = self.imag - other.imag
        return complex_numbers(a,b)

    def __mul__(self, other):
        a = (self.real*other.real) - (self.imag*other.imag)
        b = (self.imag*other.real) + (self.real*other.imag)
        return complex_numbers(a,b)
        
    def __truediv__(self, other):
        a = ((self.real*other.real) + (self.imag*other.imag))/((other.real*other.real)+(other.imag*other.imag))
        b = ((self.imag*other.real) - (self.real*other.imag))/((other.real*other.real)+(other.imag*other.imag))
        return complex_numbers(a,b)

    def absolute(self):
        a = math.sqrt((self.real*self.real)+(self.imag*self.imag))
        return a
    def argument(self):
        a = np.angle(complex(self.real,self.imag), deg=True)
        return a
    def conjugate(self):
        a = self.real
        b = -(self.imag)
        return complex_numbers(a,b)
    
comp_1 = complex_numbers(3,5)
comp_2 = complex_numbers(4,4)
print(comp_1.__repr__())
comp_sum = comp_1.__add__(comp_2)
comp_diff = comp_1.__sub__(comp_2)
comp_prod = comp_1.__mul__(comp_2)
comp_quot = comp_1.__truediv__(comp_2)
comp_abs = comp_1.absolute()
comp_conj = comp_1.conjugate()
comp_arg = comp_1.argument()
print(comp_abs)
print(comp_arg)



