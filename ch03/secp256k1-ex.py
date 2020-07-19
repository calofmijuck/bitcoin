# secp256k1-example

import os, sys
sys.path.append(os.pardir)

from ch01.FieldElement import FieldElement
from ch02.Point import Point

gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8

prime = 2 ** 256 - 2 ** 32 - 977

# order
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

print(gy ** 2 % prime == (gx ** 3 + 7) % prime)

x = FieldElement(gx, prime)
y = FieldElement(gy, prime)

# Define curve
a = 0
b = 7

a_f = FieldElement(a, prime)
b_f = FieldElement(b, prime)

G = Point(x, y, a_f, b_f)
print(n * G) # should be 0