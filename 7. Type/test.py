from functools import reduce

class Type(ABC): pass

class IntType(Type): pass

class FloatType(Type): pass

class BoolType(Type): pass

class StaticCheck(Visitor):

    func = []

    def visitProgram(self, ctx: Program, o):
        self.func = []
        a = reduce(lambda x,y: [x[0] + [(y.accept(self, x))[0]], x[1] + [(y.accept(self, x))[0]], x[2] + [y.accept(self, x)]] if type(y) is VarDecl else [x[0] + [y.accept(self, x)], x[1] + [y.accept(self, x)], x[2]], ctx.decl, [[],[],[]])
        for x in ctx.stmts:
            x.accept(self, a)

    def visitVarDecl(self, ctx: VarDecl, o):
        if len(list(filter(lambda x: x.name == ctx.name, o[0]))) > 0:
            raise Redeclared(ctx)
        return [ctx, None]
    
    def visitFuncDecl(self,ctx:FuncDecl,o):
        a = []
        para = []
        for x in ctx.param:
            if self.check(para, x):
                para.append([x, None])
            else:
                raise Redeclared(x)
        a = para.copy()
        self.func.append([ctx.name, para.copy()])
        for x in ctx.local:
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
            for i in range(len(para)):
                for j in b[2]:
                    if para[i][0].name == j[0].name:
                        para[i] = [para[i][0], j[1]]
                        break
            for i in range(len(self.func)):
                if self.func[i][0] == ctx.name:
                    self.func[i] = [ctx.name, para.copy()]
        return ctx
            


    def visitCallStmt(self,ctx:CallStmt,o):
        if len(list(filter(lambda x: ctx.name == x.name, o[1]))) == 0:
            raise UndeclaredIdentifier(ctx.name)
        k = []
        for i in self.func:
            if ctx.name == i[0]:
                k = i[1]
                break
        if len(k) != len(ctx.args):
            raise TypeMismatchInStatement(ctx)
        for i in range(len(k)):
            if type(k[i]) is type(None) and type(ctx.args[i]) is type(None):
                raise TypeCannotBeInferred(ctx)
            if type(k[i]) is type(None) and type(ctx.args[i]) is not type(None):
                k[i] = ctx.args[i]
            if type(k[i]) is not type(None) and type(ctx.args[i]) is type(None):
                for i in o[2]:
                    if i[0].name == ctx.args[i].name:
                        i = [i[0], ctx.args[i]]
            if type(k[i]) is not type(ctx.args[i]):
                raise TypeMismatchInStatement(ctx)
        for i in range(len(self.func)):
            if ctx.name == self.func[i][0]:
                self.func[i] = [ctx.name, ctx.args]
            

    def check(self, a, b):
        if len(a) == 0:
            return True
        else:
            for x in a:
                if b.name == x[0].name:
                    return False
        return True

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