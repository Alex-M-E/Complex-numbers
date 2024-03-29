import math

class complex_numbers():
    def __init__(self, a=0, b=0):
        if type(a) == float or type(a) == int:
            self.a = a
            self.b = b
        else:
            self.a = a
            self.b = b
    def __add__(self, self1):
        return complex_numbers(self.a + self1.a, self.b + self1.b)
    def __sub__(self, self1):
        return complex_numbers(self.a - self1.a, self.b - self1.b)
    def __mul__(self, self1):
        return complex_numbers(self.a * self1.a - (self.b * self1.b), self.a * self1.b + (self.b * self1.a))
    def __truediv__(self, self1):
        s1 = (self.a * self1.a + self.b * self1.b) / (self1.a ** 2 + self1.b ** 2)
        s2 = (self1.a * self.b - self1.b * self.a) / (self1.a ** 2 + self1.b ** 2)
        return complex_numbers(s1, s2)
    def __str__(self):
        if type(self.a) == int or type(self.a) == float:
            if self.b < 0:
                return str(self.a) + '' + str(self.b) + 'i'
            return str(self.a) + '+' + str(self.b) + 'i'
        else:
            k = ''
            for i in self.a:
                k = k + complex_numbers.neznaykaknazvat(i)
                k = k + '\n'
            return k[:len(k) - 1]
    @staticmethod
    def neznaykaknazvat(self):
        a = self[0]
        b = self[1]
        if b < 0:
            return str(a) + '' + str(b) + 'i'
        return str(a) + '+' + str(b) + 'i'
    @staticmethod
    def mod(self):
        return ((self.a ** 2) + (self.b ** 2)) ** 0.5
    def __pow__(self, n):
        b = self.b
        a = self.a
        fi = math.atan(b / a)
        r = (a ** 2 + b ** 2) ** 0.5
        return complex_numbers((r ** n) * math.cos(n * fi), (r ** n) * math.sin(n * fi))
        
    @staticmethod
    def arg(self):
        r = (self.a ** 2 + self.b ** 2) ** 0.5
        return math.asin(self.b / r)
    @staticmethod
    def coren(self, n):
        d = complex_numbers.trigform(self)
        w = d[0]
        cos = d[1]
        sin = d[2]
        fi = d[3]
        r = d[0] ** (1 / n)
        d = []
        for k in range(n):
            s1 = r * math.cos((fi) + math.pi * 2 * k / n)
            s2 = r * math.sin((fi) + math.pi * 2 * k / n)
            d.append([s1, s2])
        return complex_numbers(d)
            
    @staticmethod
    def trigform(self):
        r = (self.a ** 2 + self.b ** 2) ** 0.5
        a = self.a
        b = self.b
        if (a > 0 and b > 0) or (a > 0 and b < 0):
            fi = math.atan(b / a)
        if (a < 0 and b > 0):
            fi = math.pi + math.atan(b / a)
        if (a < 0 and b < 0):
            fi = -1 * math.pi + math.atan(b / a)
        if a == 0 and b < 0:
            fi = -1 * math.pi / 2
        if a == 0 and b > 0:
            fi = math.pi / 2
        if b == 0:
            fi = math.atanh(0)
        cos = math.cos(fi)
        sin = math.sin(fi)
        return [r, cos, sin, fi]
        
