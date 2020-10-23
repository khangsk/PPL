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
        compound = self.visitCompound_stmt(ctx.compound_stmt())
        paraList = []
        if ctx.getChildCount() == 5:
            paraList = self.visitParams_list(ctx.params_list())
        return [FuncDecl(Id(ctx.ID().getText()), paraList, compound)]

    # list_variable: variable (COMMA variable)* ;
    def visitList_variable(self, ctx: BKITParser.List_variableContext):
        arr = []
        for i in ctx.variable():
            temp = self.visitVariable(i)
            if len(temp) == 1:
                arr.append(VarDecl(temp[0],[], None))
            else:
                arr.append(VarDecl(temp[0],temp[1],None))
        return arr

    # variable: ID (LSB INT RSB)* ;
    def visitVariable(self, ctx: BKITParser.VariableContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        arr = [IntLiteral(i.getText()) for i in ctx.INT()]
        return [Id(ctx.ID().getText()), arr]
        

    # params_list: PARAMETER COLON list_variable ;
    def visitParams_list(self, ctx: BKITParser.Params_listContext):
        return self.visitList_variable(ctx.list_variable())

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

    # compound_stmt: BODY COLON var_declare* stmt* ENDBODY DOT ;
    def visitCompound_stmt(self, ctx: BKITParser.Compound_stmtContext):
        arr_var = []
        for i in ctx.var_declare():
            arr_var += self.visitVar_declare(i)
        arr_stmt = []
        for i in ctx.stmt():
            arr_stmt.append(self.visitStmt(i))
        return (arr_var, arr_stmt)

    # stmt: assign_stmt|if_stmt|for_stmt|while_stmt|do_while_stmt|break_stmt|continue_stmt|call_stmt|return_stmt;
    def visitStmt(self, ctx: BKITParser.StmtContext):
        return self.visitChildren(ctx)

    # assign_stmt: (ID | index_exp ) EQUAL exp SEMI ;
    def visitAssign_stmt(self, ctx: BKITParser.Assign_stmtContext):
        if ctx.ID():
            return Assign(Id(ctx.ID().getText()), self.visitExp(ctx.exp()))
        return Assign(self.visitIndex_exp(ctx.index_exp()), self.visitExp(ctx.exp()))

    # if_stmt: IF exp THEN var_declare* stmt* (ELSEIF exp THEN var_declare* stmt*)* (ELSE var_declare* stmt*)? ENDIF DOT ;
    def visitIf_stmt(self, ctx: BKITParser.If_stmtContext):
        cexp = 0
        cvar = 0
        cstmt = 0
        arrExp = [] 
        arrVar = []
        arrStmt = []
        ifstmt = []
        elsestmt = []
        elseif = 0
        for i in range(ctx.getChildCount()):
            if ctx.getChild(i) == ctx.exp(cexp):
                arrExp.append(str(self.visitExp(ctx.exp(cexp))))
                cexp += 1
            elif ctx.getChild(i) == ctx.var_declare(cvar):
                arrVar += self.visitVar_declare(ctx.var_declare(cvar))
                cvar += 1
            elif ctx.getChild(i) == ctx.stmt(cstmt):
                arrStmt.append(str(self.visitStmt(ctx.stmt(cstmt))))
                cstmt += 1
            elif ctx.getChild(i) == ctx.ELSEIF(elseif) or ctx.getChild(i) == ctx.ELSE():
                ifstmt.append((arrExp[0], arrVar, arrStmt))
                arrExp = []
                arrVar = []
                arrStmt = []
                elseif += 1
        if ctx.ELSE():
            elsestmt = [arrVar, arrStmt]
            return If(ifstmt, elsestmt)
        ifstmt.append((arrExp[0], arrVar, arrStmt))
        return If(ifstmt, elsestmt)
        

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

    # call_stmt: call_exp SEMI ;
    def visitCall_stmt(self, ctx: BKITParser.Call_stmtContext):
        return self.visitCall_exp(ctx.call_exp())

    def visitReturn_stmt(self, ctx: BKITParser.Return_stmtContext):
        return None

    # call_exp: ID LP exps_list? RP ;
    def visitCall_exp(self, ctx: BKITParser.Call_expContext):
        if ctx.getChildCount() == 3:
            return CallExpr(Id(ctx.ID().getText()), [])
        return CallExpr(Id(ctx.ID().getText()), self.visitExps_list(ctx.exps_list()))

    # exps_list: exp (COMMA exp)* ;
    def visitExps_list(self, ctx: BKITParser.Exps_listContext):
        arr = []
        for i in ctx.exp():
            arr.append(self.visitExp(i))
        return arr

    # exp: exp1 (EQU | NQU | LT | GT | LTE | GTE | NOT_EQUAL | LT_DOT | GT_DOT | LTE_DOT | GTE_DOT) exp1 | exp1 ;
    def visitExp(self, ctx: BKITParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visitExp1(ctx.exp1(0))
        op = ctx.getChild(1).getText()
        left = self.visitExp1(ctx.exp1(0))
        right = self.visitExp1(ctx.exp1(1))
        return BinaryOp(op, left, right)

    # exp1: exp1 (AND | OR) exp2 | exp2;
    def visitExp1(self, ctx: BKITParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visitExp2(ctx.exp2())
        op = ctx.getChild(1).getText()
        left = self.visitExp1(ctx.exp1())
        right = self.visitExp2(ctx.exp2())
        return BinaryOp(op, left, right)

    # exp2: exp2 (ADD | ADD_DOT | SUB | SUB_DOT) exp3 | exp3;
    def visitExp2(self, ctx: BKITParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visitExp3(ctx.exp3())
        op = ctx.getChild(1).getText()
        left = self.visitExp2(ctx.exp2())
        right = self.visitExp3(ctx.exp3())
        return BinaryOp(op, left, right)

    # exp3: exp3 (MUL | MUL_DOT | DIV | DIV_DOT | MOD) exp4 | exp4 ;
    def visitExp3(self, ctx: BKITParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visitExp4(ctx.exp4())
        op = ctx.getChild(1).getText()
        left = self.visitExp3(ctx.exp3())
        right = self.visitExp4(ctx.exp4())
        return BinaryOp(op, left, right)

    # exp4: FACT exp4 | exp5 ;
    def visitExp4(self, ctx: BKITParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visitExp5(ctx.exp5())
        op = '!'
        right = self.visitExp4(ctx.exp4())
        return UnaryOp(op, right)

    # exp5: (SUB | SUB_DOT) exp5 | exp6 ;
    def visitExp5(self, ctx: BKITParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visitExp6(ctx.exp6())
        op = ctx.getChild(0).getText()
        right = self.visitExp5(ctx.exp5())
        return UnaryOp(op, right)

########### Khong chac
    # exp6: exp6 LSB exp RSB | exp7 ;
    def visitExp6(self, ctx: BKITParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visitExp7(ctx.exp7())
        return ArrayCell(self.visitExp6(ctx.exp6()), self.visitExp(ctx.exp()))

    # exp7: call_exp | operands ;
    def visitExp7(self, ctx: BKITParser.Exp7Context):
        return self.visitChildren(ctx)

    # operands:literal | ID | call_exp | LP exp RP | operands LSB exp RSB
    def visitOperands(self, ctx: BKITParser.OperandsContext):
        if ctx.getChildCount() == 1:
            if ctx.ID(): return Id(ctx.ID().getText())
            if ctx.literal(): return self.visitLiteral(ctx.literal())
            return self.visitCall_exp(ctx.call_exp())
        if ctx.LP():
            return self.visitExp(ctx.exp())
        return ArrayCell(self.visitOperands(ctx.operands()), [self.visitExp(ctx.exp())])

    # index_exp: operands LSB exp RSB ;
    def visitIndex_exp(self, ctx: BKITParser.Index_expContext):
        return ArrayCell(self.visitOperands(ctx.operands()), [self.visitExp(ctx.exp())])
