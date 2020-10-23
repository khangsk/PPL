import math

class Rational:
    def __init__(self, n = 0, d = 1):
        assert(d != 0)
        g = math.gcd(abs(n), abs(d))
        self.numer = int(n / g)
        self.denom = int(d / g)

    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)

    def __add__(self, another):
        targetType = type(another).__name__
        if targetType == 'int':
            return self.addRational(Rational(another))
        elif targetType == 'Rational':
            return self.addRational(another)

        raise Exception('Rational not support operator + with type ' + targetType)

    def addRational(self, r):
        assert(type(r).__name__ == 'Rational')
        return Rational(
            self.numer * r.denom + self.denom * r.numer,
            self.denom * r.denom
        )

a = Rational(-12, 5)
b = Rational(56, 64)

print('a = ' + str(a))
print('b = ' + str(b))

print(str(a) + '+' + str(b) + ' = ' + str(a+b))
print(str(a) + '+ 8' + ' = ' + str(a+8))
print(str(a) + '+ -8' + ' = ' + str(a+-8))

