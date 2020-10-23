from abc import ABC


class Exp(ABC):
    def eval(self):
        pass


class IntLit(Exp):
    def __init__(self, number):
        self.number = number

    def eval(self):
        return self.number


class FloatLit(Exp):
    def __init__(self, number):
        self.number = number

    def eval(self):
        return self.number


class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def eval(self):
        if self.operator == "-":
            return -self.operand.eval()
        return self.operand.eval()


class BinExp(Exp):
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self):
        l = self.left.eval()
        r = self.right.eval()
        if self.operator == "+":
            return l + r
        elif self.operator == "-":
            return l - r
        elif self.operator == "*":
            return l * r
        elif self.operator == "/":
            return l / r


x = BinExp( IntLit(3), "+", BinExp(IntLit(4), "*", FloatLit(2.0)))
print(x.eval())
