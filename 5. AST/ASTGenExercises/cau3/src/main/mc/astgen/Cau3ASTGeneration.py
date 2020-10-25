from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):

    # program: vardecls EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(ctx.vardecls().accept(self)) # return a Program object
    
    # vardecls: vardecl vardecls | vardecl ;
    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        if ctx.getChildCount() == 2:
            return ctx.vardecl().accept(self) + ctx.vardecls().accept(self) # return the list of VarDecl for the first right hand side
        else:
            return ctx.vardecl().accept(self) # return the list of VarDecl for the second right hand side  

    # vardecl: mctype ids ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        lst = ctx.ids().accept(self)
        typ = ctx.mctype().accept(self)
        return [VarDecl(typ, i) for i in lst] # return the list of VarDecl objects
  
  	# mctype: INTTYPE | FLOATTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        # return IntType() or FloatType()
        if ctx.INTTYPE(): return IntType()
        if ctx.FLOATTYPE(): return FloatType()
        
    # ids: ID (COMMA ID)* ;
    def visitIds(self,ctx:MCParser.IdsContext):
        # return the list of identifier's lexemes
        return [idx.getText() for idx in ctx.ID()]