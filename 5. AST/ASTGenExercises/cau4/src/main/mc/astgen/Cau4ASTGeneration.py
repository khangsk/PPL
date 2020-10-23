from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
import functools

class ASTGeneration(MCVisitor):
	# exp: term COMPARE term | term ;
    def visitExp(self,ctx:MCParser.ExpContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visitTerm(ctx.term(0))
            right = self.visitTerm(ctx.term(1))
            return Binary(op, left, right) # return a Binary object for the first right hand side
        else:
            return self.visitTerm(ctx.term(0)) # generate code for the second right hand side

    # term: factor EXPONENT term | factor ;
    def visitTerm(self,ctx:MCParser.TermContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visitFactor(ctx.factor())
            right = self.visitTerm(ctx.term())
            return Binary(op, left, right) # return a Binary object for the first right hand side
        else:
            return self.visitFactor(ctx.factor()) # generate code for the second right hand side

    # factor: operand (ANDOR operand)* ; 
    def visitFactor(self,ctx:MCParser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visitOperand(ctx.operand(0))
        temp = self.visitOperand(ctx.operand(0))
        countOperand, countANDOR = 0, 0
        op = ''
        for _ in ctx.operand():
            if countOperand == 0: 
                countANDOR = 1
                countOperand = 1
                continue
            op = ctx.getChild(countANDOR).getText()
            right = self.visitOperand(ctx.operand(countOperand))
            Binary(op, temp, right)
            temp = Binary(op, temp, right)
            countANDOR += 2
            countOperand += 1
        return temp # return a Binary object 
  
  	# operand: INTLIT | BOOLIT | LB exp RB ;
    def visitOperand(self,ctx:MCParser.OperandContext):
        if ctx.getChildCount() == 3:
            return self.visitExp(ctx.exp()) # generate code for the third right hand side
        elif ctx.INTLIT():
            return IntLit(ctx.INTLIT().getText()) # return a IntLit object
        if ctx.BOOLIT().getText() == 'true': return True
        else: return False # return a BoolLit object

