from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        reduce(lambda x,y: x + [y.accept(self, x)], ctx.decl,[])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if len(list(filter(lambda x: x.name == ctx.name, o))) != 0:
            raise RedeclaredVariable(ctx.name)
        return ctx

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if len(list(filter(lambda x: x.name == ctx.name, o))) != 0:
            raise RedeclaredConstant(ctx.name)
        return ctx

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if len(list(filter(lambda x: x.name == ctx.name, o))) != 0:
            raise RedeclaredFunction(ctx.name)
        reduce(lambda x,y: x + [y.accept(self, x)], ctx.param + ctx.body,[])
        
        return ctx

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass
