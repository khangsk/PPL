    def visitAssign(self,ctx,o):
        right, typeRight = self.visit(ctx.rhs, Access(o.frame, o.sym, False))
        left, typeLeft = self.visit(ctx.lhs, Access(o.frame, o.sym, True))
        self.emit.printout(right + left)
        