from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce


class ASTGeneration(BKITVisitor):
    # program  : var_declare* func_declare* EOF ;
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        arrVar = reduce(lambda x, y: x + self.visitVar_declare(y), ctx.var_declare(), [])
        arrFunc = reduce(lambda x, y: x + self.visitFunc_declare(y), ctx.func_declare(), [])
        return Program(arrVar + arrFunc)

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
        paraList = self.visitParams_list(ctx.params_list()) if ctx.params_list() else []
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
        arr = [self.convertInt(i.getText()) for i in ctx.INT()]
        return [Id(ctx.ID().getText()), arr]
        

    # params_list: PARAMETER COLON list_variable ;
    def visitParams_list(self, ctx: BKITParser.Params_listContext):
        return self.visitList_variable(ctx.list_variable())

    # array: LCB (literal (COMMA literal)*)? RCB ;
    def visitArray(self, ctx: BKITParser.ArrayContext):
        if ctx.getChildCount() == 2: return ArrayLiteral([])
        return ArrayLiteral([self.visitLiteral(x) for x in ctx.literal()])

    # literal:  INT | FLOAT | BOOLEAN | STRING | array;
    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if ctx.INT(): return IntLiteral(self.convertInt(ctx.INT().getText()))
        elif ctx.FLOAT(): return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.BOOLEAN(): return BooleanLiteral(True) if ctx.BOOLEAN().getText() == "True" else BooleanLiteral(False)
        elif ctx.STRING(): return StringLiteral(ctx.STRING().getText())
        else: return self.visitArray(ctx.array())
    
    def convertInt(self, s):
        return int(s, 8) if 'o' in s or 'O' in s else int(s,16) if 'x' in s or 'X' in s else int(s)
    # compound_stmt: BODY COLON var_declare* stmt* ENDBODY DOT ;
    def visitCompound_stmt(self, ctx: BKITParser.Compound_stmtContext):
        arrVar = reduce(lambda x, y: x + self.visitVar_declare(y), ctx.var_declare(), [])
        arrStmt = [self.visitStmt(i) for i in ctx.stmt()]
        return (arrVar, arrStmt)

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
        expr = ""
        arrVar = []
        arrStmt = []
        ifstmt = []
        for i in range(ctx.getChildCount()):
            if ctx.getChild(i) in ctx.exp():
                expr = self.visitExp(ctx.getChild(i))
            elif ctx.getChild(i) in ctx.var_declare():
                arrVar += self.visitVar_declare(ctx.getChild(i))
            elif ctx.getChild(i) in ctx.stmt():
                arrStmt.append(self.visitStmt(ctx.getChild(i)))
            elif ctx.getChild(i) in ctx.ELSEIF() or ctx.getChild(i) == ctx.ELSE():
                ifstmt.append((expr, arrVar, arrStmt))
                expr = ""
                arrVar = []
                arrStmt = []
        if ctx.ELSE():
            return If(ifstmt, (arrVar, arrStmt))
        ifstmt.append((expr, arrVar, arrStmt))
        return If(ifstmt, [])
        
    # for_stmt: FOR LP ID EQUAL exp COMMA exp COMMA exp RP DO var_declare* stmt* ENDFOR DOT ;
    def visitFor_stmt(self, ctx: BKITParser.For_stmtContext):
        idx1 = Id(ctx.ID().getText())
        expr1 = self.visitExp(ctx.exp(0))
        expr2 = self.visitExp(ctx.exp(1))
        expr3 = self.visitExp(ctx.exp(2))
        arrVar = reduce(lambda x, y: x + self.visitVar_declare(y), ctx.var_declare(), [])
        arrStmt = [self.visitStmt(i) for i in ctx.stmt()]
        return For(idx1, expr1, expr2, expr3, (arrVar, arrStmt))

    # while_stmt: WHILE exp DO var_declare* stmt* ENDWHILE DOT ;
    def visitWhile_stmt(self, ctx: BKITParser.While_stmtContext):
        arrVar = reduce(lambda x, y: x + self.visitVar_declare(y), ctx.var_declare(), [])
        arrStmt = [self.visitStmt(i) for i in ctx.stmt()]
        expr = self.visitExp(ctx.exp())
        return While(expr, (arrVar, arrStmt))

    # do_while_stmt: DO var_declare* stmt* WHILE exp ENDDO DOT ;
    def visitDo_while_stmt(self, ctx: BKITParser.Do_while_stmtContext):
        arrVar = reduce(lambda x, y: x + self.visitVar_declare(y), ctx.var_declare(), [])
        arrStmt = [self.visitStmt(i) for i in ctx.stmt()]
        expr = self.visitExp(ctx.exp())
        return Dowhile((arrVar, arrStmt), expr)

    # break_stmt: BREAK SEMI ;
    def visitBreak_stmt(self, ctx: BKITParser.Break_stmtContext):
        return Break()

    # continue_stmt: CONTINUE SEMI ;
    def visitContinue_stmt(self, ctx: BKITParser.Continue_stmtContext):
        return Continue()

    # call_stmt: call_exp SEMI ;
    def visitCall_stmt(self, ctx: BKITParser.Call_stmtContext):
        callexp = self.visitCall_exp(ctx.call_exp())
        method = callexp.method
        param = callexp.param
        return CallStmt(method, param)

    # return_stmt: RETURN exp? SEMI ;
    def visitReturn_stmt(self, ctx: BKITParser.Return_stmtContext):
        return Return(self.visitExp(ctx.exp())) if ctx.exp() else Return(None)

    # call_exp: ID LP exps_list? RP ;
    def visitCall_exp(self, ctx: BKITParser.Call_expContext):
        method = Id(ctx.ID().getText())
        param = []
        if ctx.exps_list():
            param = self.visitExps_list(ctx.exps_list())
        return CallExpr(method, param)

    # exps_list: exp (COMMA exp)* ;
    def visitExps_list(self, ctx: BKITParser.Exps_listContext):
        return [self.visitExp(i) for i in ctx.exp()]

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
    # exp6: exp7 (LSB exp RSB)* ;
    def visitExp6(self, ctx: BKITParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visitExp7(ctx.exp7())
        return ArrayCell(self.visitExp7(ctx.exp7()), [self.visitExp(x) for x in ctx.exp()])

    # exp7: call_exp | operands ;
    def visitExp7(self, ctx: BKITParser.Exp7Context):
        return self.visitChildren(ctx)

    # operands:literal | ID | call_exp | LP exp RP
    def visitOperands(self, ctx: BKITParser.OperandsContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        if ctx.literal(): return self.visitLiteral(ctx.literal())
        if ctx.call_exp(): return self.visitCall_exp(ctx.call_exp())
        return self.visitExp(ctx.exp())

    # index_exp: operands (LSB exp RSB)+ ;
    def visitIndex_exp(self, ctx: BKITParser.Index_expContext):
        return ArrayCell(self.visitOperands(ctx.operands()), [self.visitExp(x) for x in ctx.exp()])
