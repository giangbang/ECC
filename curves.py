from points import Points
import util

class Curves:
    secp256k1 = (
    0,
    7,
    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,
    (
        0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
    )
    )

    def __init__(self, params = Curves.secp256k1):
        self.a = params[0]
        self.b = params[1]
        self.p = params[2]
        if (len(params) == 4):
            self.g = Points(params[3][0], params[3][1], self)
      
    def setG(self, g):
        self.g = g
        
    def getG(self):
        return self.g
    
    
if __name__ == '__main__':
    c = Curves()
    p1 = c.getG()
    print(type(p1))
    for i in range(2, 15):
        print(p1*i)