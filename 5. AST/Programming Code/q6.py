from functools import reduce
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return ctx.exp().accept(self)

    def visitExp(self,ctx:MPParser.ExpContext):
        rl = ctx.term()[::-1]
        cl = zip(ctx.ASSIGN()[::-1],rl[1:])
        return reduce(lambda x, y: Binary(y[0].getText(),self.visit(y[1]),x),cl,self.visit(rl[0]))        
    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.getChildCount() == 1: return ctx.factor(0).accept(self)
        op = ctx.COMPARE().getText()
        left = ctx.factor(0).accept(self)
        right = ctx.factor(1).accept(self)
        return Binary(op, left, right)

    def visitFactor(self,ctx:MPParser.FactorContext):
        dl = zip(ctx.ANDOR(), ctx.operand()[1:])
        return reduce(lambda x, y: Binary(y[0].getText(),x,self.visit(y[1])),dl,self.visit(ctx.operand(0)))

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        if ctx.INTLIT(): return IntLiteral(ctx.INTLIT().getText())
        if ctx.BOOLIT(): return BooleanLiteral(True) if ctx.BOOLIT().getText() == 'True' else BooleanLiteral(False)
        return self.visitExp(ctx.exp())
    