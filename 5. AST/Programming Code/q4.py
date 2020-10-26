class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visitExp(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.getChildCount() == 1: return self.visitTerm(ctx.term())
        return Binary(ctx.getChild(1).getText(), self.visitTerm(ctx.getChild(0)), self.visitExp(ctx.getChild(2)))
    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.getChildCount() == 1: return self.visitFactor(ctx.factor(0))
        return Binary(ctx.getChild(1).getText(), self.visitFactor(ctx.getChild(0)), self.visitFactor(ctx.getChild(2)))

    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.getChildCount() == 1: return self.visitOperand(ctx.operand())
        return Binary(ctx.getChild(1).getText(), self.visitFactor(ctx.getChild(0)), self.visitOperand(ctx.getChild(2)))

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        if ctx.INTLIT(): return IntLiteral(ctx.INTLIT().getText())
        if ctx.BOOLIT(): return BooleanLiteral(True) if ctx.BOOLIT().getText() == 'True' else BooleanLiteral(False)
        return self.visitExp(ctx.exp())
        