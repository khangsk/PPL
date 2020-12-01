    def visitBinExpr(self,ctx,o):
        e1, type1 = self.visit(ctx.e1, o)
        e2, type2 = self.visit(ctx.e2, o)
        op = ctx.op
        x = IntType() if type(type1) is IntType and type(type2) is IntType else FloatType()
        if op == '/': x = FloatType()
        if type(type1) is IntType and type(x) is not type(type1): 
            e1 = e1 + self.emit.emitI2F(o.frame)
        if type(type2) is IntType and type(x) is not type(type2): 
            e2 = e2 + self.emit.emitI2F(o.frame)
        if op in ['+','-']:
            return e1 + e2 + self.emit.emitADDOP(op, x, o.frame), x
        elif op in ['*','/']:
            return e1 + e2 + self.emit.emitMULOP(op, x, o.frame), x
        else:
            return e1 + e2 + self.emit.emitREOP(op, x, o.frame), x
        
        