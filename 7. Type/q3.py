from functools import reduce

class Type(ABC): pass

class IntType(Type): pass

class FloatType(Type): pass

class BoolType(Type): pass

class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        a = reduce(lambda x,y: x + [y.accept(self, x)], ctx.decl, [])
        for x in ctx.stmts:
            x.accept(self, a[1])

    def visitVarDecl(self, ctx: VarDecl, o):
        if len(list(filter(lambda x: x.name == ctx.name, o[0]))) > 0:
            raise RedeclaredVariable(ctx.name)
        return [ctx, None]

    def visitAssign(self, ctx: Assign, o):
        lhs = ctx.lhs.accept(self,o)
        rhs = ctx.rhs.accept(self,o)
        if (lhs is None) and (rhs is None):
            raise TypeCannotBeInferred(ctx)
        elif (lhs is None) and (rhs is not None):
            lhs = rhs
        elif (lhs is not None) and (rhs is None):
            rhs = lhs
        elif (lhs is not None) and (rhs is not None):
            if type(lhs) is not type(rhs):
                raise TypeMismatchInStatement(ctx)


    def visitBinOp(self, ctx: BinOp, o):
        l_exp, r_exp = ctx.e1.accept(self, o), ctx.e2.accept(self, o)
        type_lexp = type(l_exp)
        type_rexp = type(r_exp)
        if type_lexp is list:
                type_lexp = type(l_exp[1])
        if type_rexp is list:
                type_rexp = type(r_exp[1])
        if ctx.op in ['+', '-', '*', '/']:
            if type_lexp is type(None):
                l_exp[1] = IntType()
            if type_rexp is type(None):
                r_exp[1] = IntType()
            if BoolType in [type_lexp, type_rexp] or FloatType in [type_lexp, type_rexp]:
                raise TypeMismatchInExpression(ctx)
            return IntType()
        if ctx.op in ['+.', '-.', '*.', '/.']:
            if type_lexp is type(None):
                l_exp[1] = FloatType()
            if type_rexp is type(None):
                r_exp[1] = FloatType()
            if BoolType in [type_lexp, type_rexp] or IntType in [type_lexp, type_rexp]:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if ctx.op in ['>', '=']:
            if type_lexp is type(None):
                l_exp[1] = IntType()
            if type_rexp is type(None):
                r_exp[1] = IntType()
            if BoolType in [type_lexp, type_rexp] or FloatType in [type_lexp, type_rexp]:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if ctx.op in ['>.', '=.']:
            if type_lexp is type(None):
                l_exp[1] = FloatType()
            if type_rexp is type(None):
                r_exp[1] = FloatType()
            if BoolType in [type_lexp, type_rexp] or IntType in [type_lexp, type_rexp]:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if ctx.op in ['!', '&&', '||', '>b', '=b']:
            if type_lexp is type(None):
                l_exp[1] = BoolType()
            if type_rexp is type(None):
                r_exp[1] = BoolType()
            if IntType in [type_lexp, type_rexp] or FloatType in [type_lexp, type_rexp]:
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnOp(self, ctx: UnOp, o):
        exp = ctx.e.accept(self, o)
        type_exp = type(exp)
        if type_exp is list:
                type_exp = type(exp[1])
        if ctx.op == '-':
            if type_exp is type(None):
                exp[1] = IntType()
            elif type_exp is not IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()
        if ctx.op == '-.':
            if type_exp is type(None):
                exp[1] = FloatType()
            elif type_exp is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if ctx.op == '!':
            if type_exp is type(None):
                exp[1] = BoolType()
            elif type_exp is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if ctx.op == 'i2f':
            if type_exp is type(None):
                exp[1] = IntType()
            elif type_exp is not IntType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if ctx.op == 'floor':
            if type_exp is type(None):
                exp[1] = FloatType()
            elif type_exp is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return IntType()

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx, o):
        return BoolType()

    def visitId(self, ctx, o):
        arr = list(filter(lambda x: x.name == ctx.name, o))
        if len(arr) == 0:
            raise UndeclaredIdentifier(ctx.name)
        return arr[-1][1]