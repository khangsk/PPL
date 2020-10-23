from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):

    # program: vardecls EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(self.visitVardecls(ctx.vardecls())) # return a Program object
    
    # vardecls: vardecl vardecls | vardecl ;
    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        if ctx.getChildCount() == 2:
            return [self.visitVardecl(ctx.vardecl())] + self.visitVardecls(ctx.vardecls()) # return the list of VarDecl for the first right hand side
        else:
            return [self.visitVardecl(ctx.vardecl())] # return the list of VarDecl for the second right hand side  

    # vardecl: mctype ids ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        return VarDecl(self.visitMctype(ctx.mctype()), self.visitIds(ctx.ids()))
  
  	# mctype: INTTYPE | FLOATTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.INTTYPE(): return IntType()
        if ctx.FLOATTYPE(): return FloatType()

    # ids: ID (COMMA ID)* ;
    def visitIds(self,ctx:MCParser.IdsContext):
        return [str(id) for id in ctx.ID()]