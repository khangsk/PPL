    def visitIf(self,ctx,o):
        exp, typeExp = self.visit(ctx.expr, Access(o.frame, o.sym, True))
        self.emit.printout(exp)
        labelT = o.frame.getNewLabel()
        labelE = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFTRUE(labelT, o.frame))
        if ctx.estmt is not None:
            self.visit(ctx.estmt, o)
        self.emit.printout(self.emit.emitGOTO(labelE, o.frame))
        self.emit.printout(self.emit.emitLABEL(labelT, o.frame))
        self.visit(ctx.tstmt, o)
        self.emit.printout(self.emit.emitLABEL(labelE, o.frame))
        