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
        if len(list(filter(lambda x: x.name == ctx.name, o[0]))) > 0:
            raise Redeclared(ctx)
        a = []
        para = []
        for x in ctx.param:
            if self.check(para, x):
                para.append([x, None])
            else:
                raise Redeclared(x)
        a = para.copy()
        self.func.append([ctx.name, [x[1] for x in para]])
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
                    self.func[i] = [ctx.name, [x[1] for x in para]]
        return ctx

    def visitCallStmt(self,ctx:CallStmt,o):
        if len(list(filter(lambda x: ctx.name == x[0], self.func))) == 0:
            raise UndeclaredIdentifier(ctx.name)
        k = []
        for i in self.func:
            if ctx.name == i[0]:
                k = i[1]
                break
        if len(k) != len(ctx.args):
            raise TypeMismatchInStatement(ctx)
        for i in range(len(k)):
            y = self.visit(ctx.args[i], o)
            x = y
            if type(y) is list:
                x = y[1]
            if type(x) is type(None) and type(k[i]) is type(None):
                raise TypeCannotBeInferred(ctx)
            elif type(x) is not type(None) and type(k[i]) is type(None):
                k[i] = x
            elif type(x) is type(None) and type(k[i]) is not type(None):
                y[1] = k[i]
            elif type(k[i]) is not type(x):
                raise TypeMismatchInStatement(ctx)
            

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