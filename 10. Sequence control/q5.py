    def visitWhile(self,ctx,o): 
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        expCode, expType = self.visit(ctx.expr, Access(frame, nenv, False, True))
        labelS = frame.getNewLabel() 
        labelE = frame.getNewLabel() 
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFFALSE(labelE, frame))
        self.visit(ctx.stmt, o)
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        self.emit.printout(self.emit.emitGOTO(labelS, frame))
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()