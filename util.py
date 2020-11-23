def modInverse(a, p):
    x, y, d = extGCD(a, p)
    if (d != 1):
        raise Exception('not coprime')
    
    x = (x % p + p) % p
    return x
    
    
def extGCD(a, b):
    if (b == 0):
        return 1, 0, a
        
    x1, y1, d = extGCD(b, a%b)
    x = y1
    y = x1 - y1 * (a//b)
    return x, y, d
    
def power(a, b, m):
    half = power(a, b//2, m)
    res = (half * half) % m
    if (b % 2 == 1):
        res = (res * a) % m
    return res
    
