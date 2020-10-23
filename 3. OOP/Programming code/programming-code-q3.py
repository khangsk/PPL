from abc import ABC, abstractmethod

class Exp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class IntLit(Exp):
    def __init__(self, number):
        self.number = number

    def accept(self, visitor):
        return visitor.visitIntLit(self)

class FloatLit(Exp):
    def __init__(self, number):
        self.number = number

    def accept(self, visitor):
        return visitor.visitFloatLit(self)

class UnExp(Exp):
    def __init__(self, operation, operand):
        self.operation = operation
        self.operand = operand

    def accept(self, visitor):
        return visitor.visitUnExp(self)

class BinExp(Exp):
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right

    def accept (self,visitor):
        return visitor.visitBinExp(self)
    
class Visitor(ABC):
    @abstractmethod
    def visitIntLit(self, intLit): pass
    
    @abstractmethod
    def visitFloatLit(self, floatLit): pass

    @abstractmethod
    def visitUnExp(self, unExp): pass

    @abstractmethod
    def visitBinExp(self, binExp): pass

class Eval(Visitor):
    def visitIntLit(self, intLit):
        return intLit.number

    def visitFloatLit(self, floatLit):
        return floatLit.number

    def visitUnExp(self, unExp):
        expression = unExp.operand.accept(Eval())
        if unExp.operation == '+':
            return expression
        if unExp.operation == '-':
            return -expression 

    def visitBinExp(self, binExp):
        left = binExp.left.accept(Eval())
        right = binExp.right.accept(Eval())
        if binExp.operation == '+':
            return left + right
        if binExp.operation == '-':
            return left - right
        if binExp.operation == '*':
            return left * right
        if binExp.operation == '/':
            return left / right

class PrintPrefix(ABC):
    def visitIntLit(self, intLit):
        return str(intLit.number)

    def visitFloatLit(self, floatLit):
        return str(floatLit.number)

    def visitUnExp(self, unExp):
        return str(unExp.operation) + '. ' + unExp.operand.accept(PrintPrefix())

    def visitBinExp(self, binExp):
        return str(binExp.operation) + " " + binExp.left.accept(PrintPrefix()) + " " + binExp.right.accept(PrintPrefix())

class PrintPostfix(ABC):
    def visitIntLit(self, intLit):
        return str(intLit.number) + " "

    def visitFloatLit(self, floatLit):
        return str(floatLit.number) + " "

    def visitUnExp(self, unExp):
        return  unExp.operand.accept(PrintPostfix()) + str(unExp.operation) + '. '
        
    def visitBinExp(self, binExp):
        return  binExp.left.accept(PrintPostfix()) + binExp.right.accept(PrintPostfix()) + str(binExp.operation) + " "

x = BinExp(UnExp("-", IntLit(4)), "+", BinExp(IntLit(3), "*", IntLit(2)))
print(x.accept(Eval()))
