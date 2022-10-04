import math
class Complex_numbers:

    def __init__(self, re, im):
        self._re = re
        self._im = im

    def get_re(self):
        return self._re

    def set_re(self, re):
        self._re = re

    def get_im(self):
        return self._im

    def set_im(self, im):
        self._im = im

    def modul(self):
        return (self._re**2 + self._im**2)**0.5

    def angle(self):
        return math.acos(self._re/(self._re**2 + self._im**2)**0.5)

    def in_exp(self):
        return Complex_numbers(self.modul(), self.angle())

    def __str__(self):
        return str(self._re) + " " + str(self._im)

    def out_exp(self):
        return Complex_numbers(float(self._re)*math.cos(float(self._im)), float(self._re)*math.sin(float(self._im)))


