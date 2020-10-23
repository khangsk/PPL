from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):
    # program  : var_declare* func_declare* EOF ;
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        arr = []
        for i in ctx.var_declare():
            arr += self.visitVar_declare(i)
        for i in ctx.func_declare():
            arr += self.visitFunc_declare(i)
        return Program(arr)

    # var_declare: VAR COLON list_var (COMMA list_var)* SEMI ;
    def visitVar_declare(self, ctx: BKITParser.Var_declareContext):
        arr = []
        for i in ctx.list_var():
            initVar = self.visitList_var(i)
            if len(initVar) == 1: 
                if len(initVar[0]) == 1: arr.append(VarDecl(initVar[0][0],[],None))
                else: 
                    arr.append(VarDecl(initVar[0][0],initVar[0][1],None))
            else:
                if len(initVar[0]) == 1: arr.append(VarDecl(initVar[0][0],[],initVar[1]))
                else: 
                    arr.append(VarDecl(initVar[0][0],initVar[0][1],initVar[1]))
        return arr

    # list_var: variable (EQUAL literal)? ;
    def visitList_var(self, ctx: BKITParser.List_varContext):
        if ctx.getChildCount() == 1: return [self.visitVariable(ctx.variable())]
        return [self.visitVariable(ctx.variable()), self.visitLiteral(ctx.literal())]

    # func_declare: FUNCTION COLON ID params_list? compound_stmt;
    def visitFunc_declare(self, ctx: BKITParser.Func_declareContext):
        return None

    # list_variable: variable (COMMA variable)* ;
    def visitList_variable(self, ctx: BKITParser.List_variableContext):
        return None

    # variable: ID (LSB INT RSB)* ;
    def visitVariable(self, ctx: BKITParser.VariableContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        arr = [IntLiteral(i.getText()) for i in ctx.INT()]
        return [Id(ctx.ID().getText()), arr]
        

    # params_list: PARAMETER COLON list_variable ;
    def visitParams_list(self, ctx: BKITParser.Params_listContext):
        return None

    # array: (lit_array | arr_array) ;
    def visitArray(self, ctx: BKITParser.ArrayContext):
        return self.visitChildren(ctx)

    # lit_array: LCB literal? (COMMA literal)* RCB ;
    def visitLit_array(self, ctx: BKITParser.Lit_arrayContext):
        return None

    # arr_array: LCB array? (COMMA array)* RCB ;
    def visitArr_array(self, ctx: BKITParser.Arr_arrayContext):
        return None

    # literal:  INT | FLOAT | BOOLEAN | STRING | array;
    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if ctx.INT(): return IntLiteral(ctx.INT().getText())
        elif ctx.FLOAT(): return FloatLiteral(ctx.FLOAT().getText())
        elif ctx.BOOLEAN(): return BooleanLiteral(ctx.BOOLEAN().getText())
        elif ctx.STRING(): return StringLiteral(ctx.STRING().getText())
        else: return self.visitArray(ctx.array())

    def visitCompound_stmt(self, ctx: BKITParser.Compound_stmtContext):
        return None

    def visitStmt(self, ctx: BKITParser.StmtContext):
        return None

    def visitAssign_stmt(self, ctx: BKITParser.Assign_stmtContext):
        return None

    def visitIf_stmt(self, ctx: BKITParser.If_stmtContext):
        return None

    def visitFor_stmt(self, ctx: BKITParser.For_stmtContext):
        return None

    def visitWhile_stmt(self, ctx: BKITParser.While_stmtContext):
        return None

    def visitDo_while_stmt(self, ctx: BKITParser.Do_while_stmtContext):
        return None

    def visitBreak_stmt(self, ctx: BKITParser.Break_stmtContext):
        return None

    def visitContinue_stmt(self, ctx: BKITParser.Continue_stmtContext):
        return None

    def visitCall_stmt(self, ctx: BKITParser.Call_stmtContext):
        return None

    def visitReturn_stmt(self, ctx: BKITParser.Return_stmtContext):
        return None

    def visitCall_exp(self, ctx: BKITParser.Call_expContext):
        return None

    def visitExps_list(self, ctx: BKITParser.Exps_listContext):
        return None

    def visitExp(self, ctx: BKITParser.ExpContext):
        return None

    def visitExp1(self, ctx: BKITParser.Exp1Context):
        return None

    def visitExp2(self, ctx: BKITParser.Exp2Context):
        return None

    def visitExp3(self, ctx: BKITParser.Exp3Context):
        return None

    def visitExp4(self, ctx: BKITParser.Exp4Context):
        return None

    def visitExp5(self, ctx: BKITParser.Exp5Context):
        return None

    def visitExp6(self, ctx: BKITParser.Exp6Context):
        return None

    def visitExp7(self, ctx: BKITParser.Exp7Context):
        return None

    def visitOperands(self, ctx: BKITParser.OperandsContext):
        return None

    def visitIndex_exp(self, ctx: BKITParser.Index_expContext):
        return None
