from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        # return Program([VarDecl(Id(ctx.ID().getText()),[],None)])
        return None

    def visitVar_declare(self, ctx: BKITParser.Var_declareContext):
        return None

    def visitList_var(self, ctx: BKITParser.List_varContext):
        return None

    def visitFunc_declare(self, ctx: BKITParser.Func_declareContext):
        return None

    def visitList_variable(self, ctx: BKITParser.List_variableContext):
        return None

    def visitVariable(self, ctx: BKITParser.VariableContext):
        return None

    def visitParams_list(self, ctx: BKITParser.Params_listContext):
        return None

    def visitArray(self, ctx: BKITParser.ArrayContext):
        return None

    def visitLit_array(self, ctx: BKITParser.Lit_arrayContext):
        return None

    def visitArr_array(self, ctx: BKITParser.Arr_arrayContext):
        return None

    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        return None

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
