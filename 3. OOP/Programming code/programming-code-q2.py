from abc import ABC


class Exp(ABC):
    def eval(self):
        pass

    def printPrefix(self):
        pass


class IntLit(Exp):
    def __init__(self, number):
        self.number = number

    def eval(self):
        return self.number
    def printPrefix(self):
        return str(self.number)


class FloatLit(Exp):
    def __init__(self, number):
        self.number = number

    def eval(self):
        return self.number
    def printPrefix(self):
        return str(self.number)


class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def eval(self):
        if self.operator == "-":
            return -self.operand.eval()
        return self.operand.eval()

    def printPrefix(self):
        return self.operator + ". " + self.operand.printPrefix()


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

    def printPrefix(self):
        return "{0} {1} {2}".format(
            self.operator, self.left.printPrefix(), self.right.printPrefix()
        )


x = BinExp(UnExp("-", IntLit(4)), "+", BinExp(IntLit(3), "*", IntLit(2)))
print(x.printPrefix())