    def visitVarDecl(self,ctx,o):
        frame = o.frame
        if frame:
            idx = frame.getNewIndex() 
            start = frame.getStartLabel()
            end = frame.getEndLabel()
            self.emit.printout(self.emit.emitVAR(idx, ctx.name, ctx.typ, start, end))
            return Symbol(ctx.name, ctx.typ, Index(idx))
        else:
            self.emit.printout(self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False, ""))
            return Symbol(ctx.name, ctx.typ, CName('MCClass'))
        