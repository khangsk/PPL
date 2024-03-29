from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class Count(MCVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        # return ctx.vardecls().accept(self) + 1
        return self.visitVardecls(ctx.vardecls()) + 1

    # mctype: INTTYPE | FLOATTYPE | ARRAY LB INTLIT RB OF mctype ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.getChildCount() == 6:
            return 5 + ctx.mctype().accept(self) # return number of leaf nodes from the third right hand side
        else:
            return ctx.getChildCount() # return number of leaf nodes from the first or second right hand side

    # vardecls: vardecl vardecls | vardecl ;
    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        if ctx.getChildCount() == 2:
            return ctx.vardecls().accept(self) + ctx.vardecl().accept(self)# return number of leaf nodes from the first right hand side
        else:
            return ctx.vardecl().accept(self) # return number of leaf nodes from the first right hand side
  	
    # vardecl: mctype ids SEMI ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        return ctx.mctype().accept(self) + ctx.ids().accept(self) + 1

    # ids: ID (COMMA ID)* ;
    def visitIds(self,ctx:MCParser.IdsContext):
        return ctx.getChildCount()

