from abc import ABC, abstractmethod

class expr(ABC):
    pass

class Var(expr):
    def __init__(self, name):
        self.name = name

class Number(expr):
    def __init__(self, num):
        self.num = num
    def print(self):
        print("%.2f" % self.num)

class UnOp(expr):
    def __init__(self, operator, arg):
        self.operator = operator
        self.arg = arg

class BinExp(expr):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right
    def eval(self):
        if self.operator == '+':
            return self.left + self.right
        if self.operator == '-':
            return self.left - self.right
        if self.operator == '*':
            return self.left * self.right
        if self.operator == '/':
            return self.left / self.right

class UnExp(expr):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
    def eval():
        if self.   

if __name__ == "__main__":
    x = 1
    temp = BinOp("+", x, 0.2).eval()
    t = BinOp("*", temp, 3).eval()
    Number(t).print()

