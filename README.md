# Elliptic-curve cryptography 

A simple implementation of elliptic-curve cryptosystem, using secp256k1 standard by default. However, it is possible to use other curves by passing parameters of the curve to the constructor as follow
```
Curves([a, b, p])
```
and set the base point by 
```
curve.setG(Points)
```

