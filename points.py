from util import * 

class Points:
    INFINITY = 'infinity'
    
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.c = c
        
        if (((self.x**3 + c.a*self.x + c.b - self.y**2 + c.p)%c.p) != 0):
            raise Exception('point not in the curve')
        
    def __add__(self, other):
        if (other == Points.INFINITY):
            return self
        if (self == Points.INFINITY):
            return other
        assert (type(other).__name__ == type(self).__name__)
        assert (self.c == other.c)
        
        try:
            lamda = 0
            if (self == other):
                lamda = (3 * self.x**2 + self.c.a)* modInverse(2 * self.y, self.c.p)
            else:
                lamda = (other.y - self.y)*modInverse(other.x - self.x, self.c.p)
            
            lamda %= self.c.p
        except Exception:
            return Points.INFINITY
        
            
        x3 = (lamda**2 - self.x - other.x + self.c.p) % self.c.p
        y3 = (lamda * (self.x - x3) - self.y + self.c.p) % self.c.p
        return Points(
            x3, y3, self.c
        )
        
    def __mul__(self, k):
        return Points.mul(self, k)
        
    def __sub__(self, other):
        print(str(other))
        
        other.y = other.c.p  - other.y
        print(str(other))
        return self + other
        
        
    def mul(a, b):
        if (b < 0):
            raise Exception('multiply with negative number')
        if (b == 1):
            return a
        res = Points.mul(a, b//2)
        res = res.__add__(res)
        if (b % 2 == 1):
            res = res.__add__(a)
        return res
      
    def __rmul__(self, k):
        return Points.mul(self, k)
        
      
    def __str__(self):
        if (self == Points.INFINITY):
            return Points.INFINITY
        return '(' + str(self.x) + ', ' + str(self.y) + ')'