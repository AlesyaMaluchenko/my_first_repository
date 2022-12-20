import math
import numbers

class Complex_numbers:

    def __init__(self, re, im):
        self._re = re
        self._im = im

    def get_re(self):
        return self._re

    def set_re(self, re):
        self._re = re
        if not isinstance(re, numbers.Number):
            raise ValueError

    def get_im(self):
        return self._im

    def set_im(self, im):
        self._im = im
        if not isinstance(im, numbers.Number):
            raise ValueError

    def modul(self):
        return (self._re**2 + self._im**2)**0.5

    def angle(self):
        try:
            return math.acos(self._re/(self._re**2 + self._im**2)**0.5)
        except ZeroDivisionError:
            raise Exception("choose another operation")

    def in_exp(self):
        return Complex_numbers(self.modul(), self.angle())



    def __str__(self):
        return str(self._re) + " + i * " + str(self._im)

    def out_exp(self):
        return Complex_numbers(float(self._re)*math.cos(float(self._im)), float(self._re)*math.sin(float(self._im)))

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return Complex_numbers(self._re + other, self._im)
        elif isinstance(other, Complex_numbers):
            return Complex_numbers(self._re + other.get_re(),
                                   self._im + other.get_im())
        else:
            print("enter a number!")



    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            return Complex_numbers(self._re - other, self._im)
        if isinstance(other, Complex_numbers):
            return Complex_numbers(self._re - other.get_re(),
                                   self._im - other.get_im())
        return False


    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Complex_numbers(self._re * other, self._im * other)
        if isinstance(other, Complex_numbers):
            return Complex_numbers(self._re*other.get_re - self._im*other.get_im,
                                   self._re*other.get_im + self._im*other.get_re)
        return False

    def __truediv__(self, other):
        try:
            if isinstance(other, numbers.Number):
                return Complex_numbers(self._re / other, self._im / other)
            if isinstance(other, Complex_numbers):
                return Complex_numbers((self._re*other._re + self._im*other._im)/other._re**2 + other._im**2,
                               (other._re*self._im - self._re*other._im)/other._re**2 + other._im**2)
        except ZeroDivisionError:
            print("choose another operation")

    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            if self._im == 0 and self._re == other:
                return True
            return False
        if isinstance(other, Complex_numbers):
            if self._re == other._re and self._im == other._im:
                return True
            return False
    def __abs__(self):
        return float((self._re**2 + self._im**2)**0.5)

    def __getitem__(self, item):
        if item == 0:
            return self._re
        elif item == 1:
            return self._im
        else:
            raise Exception("out of range index")

    def __setitem__(self, item, value):
        if item == 0:
            self._re = value
        elif item == 1:
            self._im = value
        else:
            raise Exception("incorrect index")



c = Complex_numbers(0, 0)
#print(c[3])
print(c.in_exp())
