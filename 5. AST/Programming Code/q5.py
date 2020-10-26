class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return [x for i in ctx.vardecl() for x in i.accept(self)]

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return [VarDecl(x, str(ctx.mptype().accept(self))) for x in ctx.ids().accept(self)]

    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE(): return IntType()
        return FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 1: return [Id(ctx.ID(0).getText())]
        return [Id(x.getText()) for x in ctx.ID()]