from functools import reduce

class Type(ABC): pass

class IntType(Type): pass

class FloatType(Type): pass

class BoolType(Type): pass

class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        a = reduce(lambda x,y: [x[0] + [(y.accept(self, x))[0]], x[1] + [(y.accept(self, x))[0]], x[2] + [y.accept(self, x)]], ctx.decl, [[],[],[]])
        for x in ctx.stmts:
            x.accept(self, a)

    def visitVarDecl(self, ctx: VarDecl, o):
        if len(list(filter(lambda x: x.name == ctx.name, o[0]))) > 0:
            raise Redeclared(ctx)
        return [ctx, None]
    
    def check(self, a, b):
        if len(a) == 0:
            return True
        else:
            for x in a:
                if b.name == x[0].name:
                    return False
        return True
    
    def visitBlock(self,ctx:Block,o):
        a = []
        for x in ctx.decl:
            if self.check(a, x):
                a.append([x, None])
            else:
                raise Redeclared(x)
        temp = [x[0].name for x in a]
        for i in o[2]:
            if i[0].name not in temp:
                a.append(i)
        c = [x[0] for x in a]
        b = [c, c, a]
        for x in ctx.stmts:
            x.accept(self, b)

    def visitAssign(self, ctx: Assign, o):
        lhs_id = ctx.lhs.accept(self,o)
        rhs_exp = ctx.rhs.accept(self,o)
        type_lhs = lhs_id[1]
        type_rhs = rhs_exp
        if type(type_rhs) is list:
            type_rhs = rhs_exp[1]
        if (type_lhs is None) and (type_rhs is None):
            raise TypeCannotBeInferred(ctx)
        elif (type_lhs is None) and (type_rhs is not None):
            lhs_id[1] = type_rhs
        elif (type_lhs is not None) and (type_rhs is None):
            rhs_exp[1] = type_lhs
        elif (type_lhs is not None) and (type_rhs is not None):
            if type(type_lhs) is not type(type_rhs):
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
        arr = list(filter(lambda x: x.name == ctx.name, o[1]))
        if len(arr) == 0:
            raise UndeclaredIdentifier(ctx.name)
        for i in o[2]:
            if arr[-1].name == i[0].name:
                return i