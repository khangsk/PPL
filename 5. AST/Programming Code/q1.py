class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return 1 + self.visitVardecls(ctx.vardecls())

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.getChildCount() == 0: return 0
        return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 2 + self.visitIds(ctx.ids())

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 1

    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 1: return 1
        return 2 + self.visitIds(ctx.ids())