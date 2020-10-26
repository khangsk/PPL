class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visitVardecls(ctx.vardecls())
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail()) 

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.getChildCount() == 0: return []
        return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        lst = self.visitIds(ctx.ids())
        typ = self.visitMptype(ctx.mptype())
        return [VarDecl(i, typ) for i in lst]

    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE(): return IntType()
        if ctx.FLOATTYPE(): return FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 1: return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visitIds(ctx.ids())