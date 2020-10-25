from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    # program: vardecl+ EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        arr = []
        for i in ctx.vardecl():
            arr += i.accept(self)
        return Program(arr) # return a Program object

    # vardecl: mctype manyvar ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        arr = []
        typ = ctx.mctype().accept(self)
        for x in ctx.manyvar().accept(self):
            if len(x) == 1:
                arr.append(str(VarDecl(typ, x)))
            else:
                arr.append(str(VarDecl(ArrayType(typ, x[1]), x[0])))
        return arr # return the list of VarDecl
  	
    # mctype: INTTYPE | FLOATTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.INTTYPE():
            return IntType()
        else:
            return FloatType()

    # manyvar: var (COMMA var)* ;
    def visitManyvar(self,ctx:MCParser.ManyvarContext):
        return [i.accept(self) for i in ctx.var()]

    # var: ID (LSB INTLIT RSB)? ;
    def visitVar(self,ctx:MCParser.VarContext):
        if ctx.getChildCount() == 1:
            return ctx.ID().getText()
        return [ctx.ID().getText(), ctx.INTLIT().getText()]