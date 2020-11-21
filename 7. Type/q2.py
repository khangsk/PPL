from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        self.visit(ctx.exp, ctx.decl)

    def visitVarDecl(self,ctx:VarDecl,o): pass

    def visitBinOp(self,ctx:BinOp,o):
        op = ctx.op
        e1 = type(self.visit(ctx.e1, o))
        e2 = type(self.visit(ctx.e2, o))
        if op in ['+', '-', '*']:
            if e1 not in [IntType, FloatType] or e2 not in [IntType, FloatType]:
                raise TypeMismatchInExpression(BinOp(op, ctx.e1, ctx.e2))
            if e1 == FloatType or e2 == FloatType:
                return FloatType()
            else:
                return IntType()
        elif op == '/':
            if e1 not in [IntType, FloatType] or e2 not in [IntType, FloatType]:
                raise TypeMismatchInExpression(BinOp(op, ctx.e1, ctx.e2))
            return FloatType()
        elif op in ['!', '&&', '||']:
            if e1 is not BoolType or e2 is not BoolType:
                raise TypeMismatchInExpression(BinOp(op, ctx.e1, ctx.e2))
            return BoolType()
        else:
            if e1 != e2:
                raise TypeMismatchInExpression(BinOp(op, ctx.e1, ctx.e2))
            return BoolType()

    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        e = type(self.visit(ctx.e, o))
        if op == '-':
            if e not in [IntType, FloatType]:
                raise TypeMismatchInExpression(UnOp(op, ctx.e))
            return IntType() if e == IntType else FloatType()
        elif op == '!':
            if e is not BoolType:
                raise TypeMismatchInExpression(UnOp(op, ctx.e))
            return BoolType()

    def visitIntLit(self,ctx:IntLit,o):
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        return BoolType()

    def visitId(self,ctx,o):
        arr = list(filter(lambda x: ctx.name == x.name, o))
        if len(arr) == 0:
            raise UndeclaredIdentifier(ctx.name)
        return arr[0].typ