import sys, os
sys.path.append(os.pardir)

from ch01.FieldElement import FieldElement
from ch02.Point import Point
import matplotlib.pyplot as plt

# Set finite field
prime = 2389

# Define an elliptic curve
a = 0
b = 7

a_f = FieldElement(a, prime)
b_f = FieldElement(b, prime)

# Checks if a point is on the elliptic curve
def check(x, y):
    return y * y == x ** 3 + a_f * x + b_f

x_coord = []
y_coord = []

for i in range(0, prime):
    x = FieldElement(i, prime)
    for j in range(0, prime):
        y = FieldElement(j, prime)
        if check(x, y):
            x_coord.append(x.num)
            y_coord.append(y.num)

plt.title('y^2 = x^3 + {}x + {} on F_{}'.format(a, b, prime))
plt.axis('equal')
plt.scatter(x_coord, y_coord, marker='.')

plt.show()