from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        reduce(lambda x,y: [x[0] + [y.accept(self, x)],x[1] + [y.accept(self, x)]], ctx.decl,[[],[]])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if len(list(filter(lambda x: x.name == ctx.name, o[0]))) != 0:
            raise RedeclaredVariable(ctx.name)
        return ctx

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if len(list(filter(lambda x: x.name == ctx.name, o[0]))) != 0:
            raise RedeclaredConstant(ctx.name)
        return ctx

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if len(list(filter(lambda x: x.name == ctx.name, o[0]))) != 0:
            raise RedeclaredFunction(ctx.name)
        temp = reduce(lambda x,y: [x[0] + [y.accept(self, x)],x[1] + [y.accept(self, x)]], ctx.param + ctx.body[0],[[],o[1] + [ctx]])
        arr = [x.name for x in temp[1]]
        exp = list(filter(lambda x: type(x) is Id, ctx.body[1]))
        result = list(filter(lambda x: x.name not in arr, exp))
        if len(result) > 0:
            raise UndeclaredIdentifier(result[0].name)
        return ctx

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        return ctx
