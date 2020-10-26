from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import reduce

class ASTGeneration(MCVisitor):
	# exp: term COMPARE term | term ;
    def visitExp(self,ctx:MCParser.ExpContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = ctx.term(0).accept(self)
            right = ctx.term(1).accept(self)
            return Binary(op, left, right) # return a Binary object for the first right hand side
        else:
            return ctx.term(0).accept(self) # generate code for the second right hand side

    # term: (factor EXPONENT)* factor ; 
    def visitTerm(self,ctx:MCParser.TermContext):
        rl = ctx.factor()[::-1]
        cl = zip(ctx.EXPONENT()[::-1],rl[1:])
        dl = zip(ctx.EXPONENT(),ctx.factor()[1:])
        return reduce(lambda x, y: Binary(y[0].getText(),self.visit(y[1]),x),cl,self.visit(rl[0]))

        # if ctx.getChildCount() == 3:
        #     op = ctx.getChild(1).getText()
        #     left = ctx.factor().accept(self)
        #     right = ctx.term().accept(self)
        #     return Binary(op, left, right) # return a Binary object for the first right hand side
        # else:
        #     return ctx.factor().accept(self) # generate code for the second right hand side
    # factor: operand (ANDOR operand)* ; 
    def visitFactor(self,ctx:MCParser.FactorContext):
        rl = ctx.operand()[::-1]
        cl = zip(ctx.ANDOR()[::-1], rl[1:])
        dl = zip(ctx.ANDOR(), ctx.operand()[1:])
        return reduce(lambda x, y: Binary(y[0].getText(),x,self.visit(y[1])),dl,self.visit(ctx.operand(0)))

        # if ctx.getChildCount() == 1:
        #     return ctx.operand(0).accept(self)
        # temp = ctx.operand(0).accept(self)
        # countANDOR = 0
        # op = ''
        # for x in ctx.operand():
        #     if x == ctx.operand(0): continue
        #     op = ctx.ANDOR(countANDOR).getText()
        #     right = x.accept(self)
        #     temp = Binary(op, temp, right)
        #     countANDOR += 1
        # return temp # return a Binary object 
  
  	# operand: INTLIT | BOOLIT | LB exp RB ;
    def visitOperand(self,ctx:MCParser.OperandContext):
        # if ctx.getChildCount() == 3:
        #     return ctx.exp().accept(self) # generate code for the third right hand side
        # elif ctx.INTLIT():
        #     return IntLit(int(ctx.INTLIT().getText())) # return a IntLit object
        # print(ctx.BOOLIT().getText(), type(ctx.BOOLIT().getText()))    
        # if ctx.BOOLIT().getText() == 'true': return True
        # else: return False # return a BoolLit object
        # return BoolLit(ctx.BOOLIT().getText())
        return self.visit(ctx.exp()) if ctx.getChildCount() == 3 else IntLit(int(ctx.INTLIT().getText())) if ctx.INTLIT() else True if ctx.BOOLIT().getText() == 'true' else False