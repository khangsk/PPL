class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o):
        op = ctx.op
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        if op in ['+', '-', '*']:
            if e1 not in ['int', 'float'] or e2 not in ['int', 'float']:
                raise TypeMismatchInExpression(BinOp(op, ctx.e1, ctx.e2))
            if e1 == 'float' or e2 == 'float':
                return 'float'
            else:
                return 'int'
        elif op == '/':
            if e1 not in ['int', 'float'] or e2 not in ['int', 'float']:
                raise TypeMismatchInExpression(BinOp(op, ctx.e1, ctx.e2))
            return 'float'
        elif op in ['!', '&&', '||']:
            if e1 is not 'bool' or e2 is not 'bool':
                raise TypeMismatchInExpression(BinOp(op, ctx.e1, ctx.e2))
            return 'bool'
        else:
            if e1 != e2:
                raise TypeMismatchInExpression(BinOp(op, ctx.e1, ctx.e2))
            return 'bool'
            

    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        e = self.visit(ctx.e, o)
        if op == '-':
            if e not in ['int', 'float']:
                raise TypeMismatchInExpression(UnOp(op, ctx.e))
            return 'int' if e == 'int' else 'float'
        elif op == '!':
            if e is not 'bool':
                raise TypeMismatchInExpression(UnOp(op, ctx.e))
            return 'bool'

    def visitIntLit(self,ctx:IntLit,o):
        return 'int'

    def visitFloatLit(self,ctx,o):
        return 'float'

    def visitBoolLit(self,ctx,o):
        return 'bool'