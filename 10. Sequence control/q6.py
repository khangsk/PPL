    def visitFuncDecl(self,ctx,o):
        frame = Frame(ctx.name, ctx.returnType)
        methodName = ctx.name
        returnType = ctx.returnType
        intype = [x.typ for x in ctx.param]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, True))

        frame.enterScope(True)

        varList = SubBody(frame, o.sym)
        for x in ctx.param:
            self.visit(x, varList)
        for x in ctx.body[0]:
            self.visit(x, varList)

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        list(map(lambda x: self.visit(x, varList), ctx.body[1]))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        self.emit.printout(self.emit.emitENDMETHOD(frame))

        frame.exitScope()
        return Symbol(methodName, MType([],returnType), CName(self.className))