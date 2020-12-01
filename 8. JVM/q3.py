from functools import reduce

class Type(ABC): pass

class IntType(Type): pass

class FloatType(Type): pass

class BoolType(Type): pass

class Unknow(Type):
    def __str__(self):
        return "Unknow()"

    def accept(self, v, param):
        return v.visitUnknow(self, param)


class Symbol:
    def __init__(self, name, mtype, param = None, kind='func', isGlobal=False):
        self.name = name
        self.mtype = mtype
        self.param = param
        self.kind = kind
        self.isGlobal = isGlobal
    def __str__(self):
        return 'Symbol(' + str(self.name) + ',' + str(self.mtype) + ')'
    @staticmethod
    def fromVarDecl(decl):
        return Symbol(decl.name, Unknow(), kind='var')
    
    @staticmethod
    def fromFuncDecl(decl):
        param = [Symbol.fromVarDecl(x).mtype for x in decl.param]
        return Symbol(decl.name, Unknow(), param=param, kind='func', isGlobal=True)
    def toGlobal(self):
        self.isGlobal = True
        return self 

class Checker:
    @staticmethod
    def reDecl(scope):
        for i in range(len(scope) - 1):
            for j in range(i + 1, len(scope)):
                if scope[i].name == scope[j].name:
                    raise Redeclared(scope[j].name)
        return scope
    @staticmethod
    def unDecl(scope, name):
        for i in scope:
            if name == i.name:
                return i
        raise UndeclaredIdentifier(name)

class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        sym = [Symbol.fromVarDecl(x).toGlobal() if type(x) is VarDecl else Symbol.fromFuncDecl(x) for x in ctx.decl]
        scope = Checker.reDecl(sym)
        for x in ctx.decl:
            if type(x) is FuncDecl:
                self.visit(x, scope)
        for x in ctx.stmts:
            self.visit(x, scope)

    def visitVarDecl(self, ctx: VarDecl, o):
        return Symbol.fromVarDecl(ctx)
    
    def visitFuncDecl(self,ctx:FuncDecl,o):
        sym = None
        for i in o:
            if ctx.name == i.name:
                sym = i
                break
        param = [self.visit(x, o) for x in ctx.param]
        for i in range(len(ctx.param)):
            param[i].mtype = sym.param[i]
        localVar = [self.visit(x, o) for x in ctx.local]
        ar = param + localVar
        newScope = Checker.reDecl(ar)
        temp = [x.name for x in newScope]
        for i in o:
            if i.kind == 'var' and i.name not in temp:
                newScope.append(i)
        for x in ctx.stmts:
            self.visit(x, newScope)
            
    def visitCallStmt(self,ctx:CallStmt,scope):
        sym = Checker.unDecl(scope, ctx.name)
        typArgs = [self.visit(x, scope) for x in ctx.args]
        if len(sym.param) != len(typArgs):
            raise TypeMismatchInStatement(ctx)
        if len(sym.param) > 0:
            if type(sym.param[0]) is Unknow:
                for i in range(len(sym.param)):
                    if type(typArgs[i]) is Unknow:
                        raise TypeCannotBeInferred(ctx)
                sym.param = typArgs.copy()
            else:
                for i in range(len(sym.param)):
                    if type(typArgs[i]) is Unknow:
                        for j in scope:
                            if j.name == ctx.args.name:
                                j = Symbol(j.name, sym.param[i], param=j.param, kind=j.kind,isGlobal=j.isGlobal)
                                break
                    else:
                        if type(typArgs[i]) is not type(sym.param[0]):
                            raise TypeMismatchInStatement(ctx)

    def visitAssign(self, ctx: Assign, scope):
        left = self.visit(ctx.lhs, scope)
        right = self.visit(ctx.rhs, scope)
        if type(left) is Unknow and type(right) is Unknow:
            raise TypeCannotBeInferred(ctx)
        elif type(left) is Unknow and type(right) is not Unknow:
            for j in scope:
                if j.name == ctx.lhs.name:
                    j = Symbol(j.name, right, param=j.param, isGlobal=j.isGlobal)
                    break
        elif type(left) is not Unknow and type(right) is Unknow:
            for j in scope:
                if j.name == ctx.rhs.name:
                    j = Symbol(j.name, left, param=j.param, kind=j.kind,isGlobal=j.isGlobal)
                    break
        elif type(left) is not type(right):
            raise TypeMismatchInStatement(ctx)

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx, o):
        return BoolType()

    def visitId(self, ctx, scope):
        sym = Checker.unDecl(scope, ctx.name)
        for i in scope:
            if sym.name == i.name:
                return sym.mtype