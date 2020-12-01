    def visitBinExpr(self,ctx,o):
        e1, type1 = self.visit(ctx.e1, o)
        e2, type2 = self.visit(ctx.e2, o)
        op = ctx.op
        if op in ['+', '-']: return e1 + e2 + self.emit.emitADDOP(op, IntType(), o.frame), IntType()
        elif op in ['*', '/']: return e1 + e2 + self.emit.emitMULOP(op, IntType(), o.frame), IntType()
        elif op == '+.': return e1 + e2 + self.emit.emitADDOP('+', FloatType(), o.frame), FloatType()
        elif op == '-.': return e1 + e2 + self.emit.emitADDOP('-', FloatType(), o.frame), FloatType()
        elif op == '*.': return e1 + e2 + self.emit.emitMULOP('*', FloatType(), o.frame), FloatType()
        elif op == '/.': return e1 + e2 + self.emit.emitMULOP('/', FloatType(), o.frame), FloatType()