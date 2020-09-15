from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self)) # 0 retorna falso el resto retorna true

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__=='__main__':
    v = Vector(3,4)
    print(abs(v))
    print(v * 3)
    v2 = Vector(3,9)
    print(v+v2)
    v3 = Vector()
    if bool(v3):
        print ('Vacio')
    else:
        print('No vacio')