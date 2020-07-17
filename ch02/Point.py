class Point:
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

        # handling identity point 0
        if self.x is None and self.y is None:
            return
        if self.y ** 2 != self.x ** 3 + a * x + b:
            raise ValueError('({}, {}) is not on the curve'.format(x, y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.a != other.a or self.b != other.b

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format(self, other))
        
        # Identity and inverse
        if self.x is None: # 0 + A = A
            return other
        if other.x is None: # A + 0 = A
            return self
        if self.x == other.x and self.y != other.y: # A + (-A) = 0
            return self.__class__(None, None, self.a, self.b)
        
        # Normal addition
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x3 = s * s - self.x - other.x
            y3 = s * (self.x - x3) - self.y
            return self.__class__(x3, y3, self.a, self.b)
        
        # Special case - same point
        if self == other:
            # y == 0
            if self.y == 0 * self.x:
                return self.__class__(None, None, self.a, self.b)
            
            # y != 0
            s = (3 * self.x * self.x + self.a) / (2 * self.y)
            x3 = s * s - 2 * self.x
            y3 = s * (self.x - x3) - self.y
            return self.__class__(x3, y3, self.a, self.b)
        

    def __str__(self):
        return 'Point({}, {})_{}_{}'.format(self.x, self.y, self.a, self.b)