from points import Points
import util
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

secp256k1 = (
    0, #a
    7, #b
    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F, #p
    ( # g
        0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
    ), 
    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 # n
)

class Curves(object):

    def __init__(self, params = secp256k1):
        self.a = params[0]
        self.b = params[1]
        self.p = params[2]
        if (len(params) >= 5):
            self.g = Points(params[3][0], params[3][1], self)
            
        if (len(params) >= 5):
            self.n = params[4]
      
      
    def setG(self, g):
        self.g = g
        
    def getG(self):
        return self.g
        
    def getN(self):
        return self.n;
        
    def setN(self, n):
        self.n = n
        
    def __str__(self):
        return ('a: ' + str(self.a) + '\nb: ' + str(self.b) + '\np: ' + str(self.p) +
            '\ng: ' + str(self.g) + '\nn: ' + str(self.n))
    
    
def encrypt(message):
    res = 0
    for c in message.lower():
        res = res * 26 + ord(c) - ord('a')
    return res


if __name__ == '__main__':
    c = Curves()
    g = c.getG()
    message = "hello"
    print("parameters of the elliptic curve are\n" + str(c))
    na = random.randint(0, c.getN())
    print('-'*10)
    print("private key for a is na = " + str(na))
    pa = na * g
    print('then, Pa is ' + str(pa))
    print("the message is " + message)
    encryptMessage = encrypt(message) % c.getN()
    print("message is encrypted to " + str(encryptMessage))
    p = encryptMessage * g
    print('and is mapped to point: ')
    print('---\n' +   str(p) + '\n---\n' )
    k = random.randint(0, c.getN())
    print('let k be ' + str(k))
    pc = (k * g, p + k * pa)
    print('the cipher text pair of points of the message is ' + (str(pc[0])) + ', ' + str(pc[1]))
    decrypt = pc[1] - (na * pc[0])
    print('finally, the plainttext point is decrypted as ' )
    print('---\n' +  str(decrypt)+ '\n---\n' )