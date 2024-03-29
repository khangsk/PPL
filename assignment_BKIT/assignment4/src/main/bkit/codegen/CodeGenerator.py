'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

from AST import *

def printlist(lst,f=str,start="[",sepa=",",ending="]"):
	return start + sepa.join(f(i) for i in lst) + ending

class SubBody():
    def __init__(self, frame, sym, isGlobal=False):
        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal
class Symbol:
    def __init__(self,name,mtype,value = None, val=None, isGlobal=False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.val = val
        self.isGlobal = isGlobal
    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ')'
class CName:
    def __init__(self,n):
        self.value = n
class Index:
    def __init__(self,n):
        self.value = n
class Type(ABC): pass
class IntType(Type):
    def __str__(self):
        return "IntType"
class FloatType(Type):
    def __str__(self):
        return "FloatType"
class VoidType(Type):
    def __str__(self):
        return "VoidType()"
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
class StringType(Type):
    def __str__(self):
        return "StringType"
class BoolType(Type):
    def __str__(self):
        return "BoolType"
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type	
    def __str__(self):
        return 'MType(' + printlist(self.partype) + ',' + str(self.rettype) + ')'
class ArrayType(Type):
    def __init__(self,et,s):
        self.eleType = et #Type
        self.dimen = s   #List[int] 
    def __str__(self):
        return "ArrayType(" + printlist(self.dimen) + ',' + str(self.eleType) + ")"
class ArrayPointerType(Type):
    def __init__(self, ctype):
        # cname: String
        self.eleType = ctype

class Access():
    def __init__(self, frame, sym, isLeft, isFirst, checkArrayType=False, typ=None):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.checkArrayType = checkArrayType
        self.typ = typ

class Utils:
    @staticmethod
    def getSymbol(scope, x):
        s = ''
        if type(x) is Id:
            s = x.name
        elif type(x) is ArrayCell:
            if type(x.arr) is Id:
                s = x.arr.name
            elif type(x.arr) is CallExpr:
                s = x.arr.method.name
        elif type(x) is CallExpr:
            s = x.method.name
        else:
            s = x
        for i in scope:
            if i.name == s:
                return i

    @staticmethod
    def retrieveType(originType):
        if type(originType) is ArrayType: return ArrayPointerType(originType.eleType)
        return originType

    @staticmethod
    def lookup(name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None
    
    @staticmethod
    def getArrayType(ast):
        arr = []
        stack = [ast]
        temp = []
        check = 0
        while stack:
            check += 1
            if type(stack[0]) is not ArrayLiteral:
                if type(stack[0]) is IntLiteral:
                    return ArrayType(IntType(), arr)
                elif type(stack[0]) is FloatLiteral:
                    return ArrayType(FloatType(), arr)
                elif type(stack[0]) is BooleanLiteral:
                    return ArrayType(BoolType(), arr)
                elif type(stack[0]) is StringLiteral:
                    return ArrayType(StringType(), arr)
            x = stack.pop(0)
            if check == 1:
                arr.append(len(x.value))
            temp += x.value
            if not stack:
                stack = temp.copy()
                temp = []
                check = 0
    
    @staticmethod
    def listElements(ast):
        arr = []
        stack = [ast]
        temp = []
        check = 0
        while stack:
            check += 1
            if type(stack[0]) is not ArrayLiteral:
                return stack
            x = stack.pop(0)
            if check == 1:
                arr.append(len(x.value))
            temp += x.value
            if not stack:
                stack = temp.copy()
                temp = []
                check = 0


class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("read", MType([], StringType()), CName(self.libName)),
            Symbol("printLn", MType([], VoidType()), CName(self.libName)),
            Symbol("printStrLn", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("print", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("string_of_int", MType([IntType()], StringType()), CName(self.libName)),
            Symbol("int_of_float", MType([FloatType()], IntType()), CName(self.libName)),
            Symbol("float_to_int", MType([IntType()], FloatType()), CName(self.libName)),
            Symbol("int_of_string", MType([StringType()], IntType()), CName(self.libName)),
            Symbol("float_of_string", MType([StringType()], FloatType()), CName(self.libName)),
            Symbol("string_of_float", MType([FloatType()], StringType()), CName(self.libName)),
            Symbol("bool_of_string", MType([StringType()], BoolType()), CName(self.libName)),
            Symbol("string_of_bool", MType([BoolType()], StringType()), CName(self.libName))
        ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)



class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.listGlobalArray = [] 
        self.function = []
        self.visitFunc = []
        self.paramMain = []
        self.visitedPara = []
        self.inferType = []

    def visitProgram(self, ast, c):
        # #ast: Program
        # #c: Any
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        staticDecl = self.env
        for x in ast.decl:
            if type(x) is FuncDecl and x.name.name == 'main':
                self.paramMain = x.param
                staticDecl = [Symbol(x.name.name, MType([], VoidType()), CName(self.className))] + staticDecl
            elif type(x) is VarDecl:
                newSym = self.visit(x, SubBody(None, None, isGlobal=True))
                staticDecl = [newSym] + staticDecl
            else:
                self.function.append(x)
        self.inferType = staticDecl.copy()
        e = SubBody(None, staticDecl)
        [self.visit(x, e) for x in ast.decl if type(x) is FuncDecl and x.name.name == 'main']
        for x in self.visitFunc:
            staticDecl = [Symbol(x.name.name, x.param[1], CName(self.className))] + staticDecl
            self.visit(x, SubBody(None, staticDecl))
        self.emit.emitEPILOG()
        return c
    
    def inferReturn(self, func, scope): 
        param = [Symbol(func.param[0][i], func.param[1].partype[i]) for i in range(len(func.param[0]))]
        scope += param
        for x in func.body[0]:
            scope.append(Symbol(x.variable.name, self.getTypeVar(x.varInit)))
        for x in func.body[1]:
            if type(x) is Return:
                typ = Utils.getSymbol(scope[::-1], x.expr)
                if typ is not None:
                    return typ.mtype
                else:
                    return Utils.getArrayType(x.expr)
            if type(x) is If:
                for i in x.ifthenStmt:
                    for j in i[1]:
                        scope.append(Symbol(j.variable.name, self.getTypeVar(j.varInit)))
                    if len(i[2])>0 and type(i[2][-1]) is Return:
                        typ = Utils.getSymbol(scope[::-1], i[2][-1].expr)
                        if typ is not None:
                            return typ.mtype
                        else:
                            return Utils.getArrayType(i[2][-1].expr)
    
    def visitVarDecl(self, ast, o):
        frame = o.frame
        isGlobal = o.isGlobal
        varName = ast.variable.name
        varType = self.getTypeVar(ast.varInit)
        if isGlobal:
            self.emit.printout(self.emit.emitATTRIBUTE(varName, Utils.retrieveType(varType), False, ""))
            if type(varType) is ArrayType: 
                self.listGlobalArray.append(ast)
            return Symbol(varName, varType, val=ast.varInit, isGlobal=True)
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, varName, Utils.retrieveType(varType), frame.getStartLabel(), frame.getEndLabel(), frame))
        return SubBody(frame, [Symbol(varName, varType, Index(idx), val=ast.varInit)] + o.sym)
    
    def getTypeVar(self, x):
        if type(x) is IntLiteral: return IntType() 
        elif type(x) is FloatLiteral: return FloatType() 
        elif type(x) is BooleanLiteral: return BoolType() 
        elif type(x) is StringLiteral: return StringType() 
        elif type(x) is ArrayLiteral: return Utils.getArrayType(x)

    def visitFuncDecl(self, ast, o):
        ret = Utils.getSymbol(o.sym, ast.name.name)
        frame = Frame(ast.name.name, ret)
        self.genMETHOD(ast, o.sym, frame)

    def genMETHOD(self, decl, o, frame):
        glenv = o
        methodName = decl.name.name
        returnType = Utils.getSymbol(o, decl.name.name).mtype.rettype
        if methodName == "main": returnType = VoidType()
        isMain = methodName == "main"
        isProc = type(returnType) is VoidType
        intype = [ArrayType(StringType(),[])] if isMain else decl.param[1].partype
        mtype = MType(intype, returnType)
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, True, frame))
        frame.enterScope(isProc)
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args",
                StringType(), frame.getStartLabel(), frame.getEndLabel(), frame))
        listLocalArray = [] 
        varList = SubBody(frame, glenv)
        if not isMain:
            for i in range(len(decl.param[0])):
                idx = varList.frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(idx, decl.param[0][i], Utils.retrieveType(decl.param[1].partype[i]), varList.frame.getStartLabel(), varList.frame.getEndLabel(), varList.frame))
                varList = SubBody(varList.frame, [Symbol(decl.param[0][i], decl.param[1].partype[i], Index(idx))] + varList.sym)
        for x in decl.body[0]:
            varList = self.visit(x, varList)
            if type(self.getTypeVar(x.varInit)) is ArrayType:
                listLocalArray.append(varList.sym[0])
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if isMain:
            for x in self.listGlobalArray:
                arr = Utils.getArrayType(x.varInit)
                size = 1
                for i in arr.dimen: size *= i
                self.emit.printout(self.emit.emitInitNewStaticArray(self.className + "/" + x.variable.name, size, arr.eleType, frame))
        for sym in listLocalArray:
            arr = sym.mtype
            size = 1
            for i in arr.dimen: size *= i
            self.emit.printout(self.emit.emitInitNewLocalArray(sym.value.value, size, arr.eleType, frame))
        visitSym = []
        for x in varList.sym:
            if x.val and x.name not in visitSym:
                if not isMain and x.isGlobal: continue
                visitSym.append(x.name)
                self.visit(Assign(Id(x.name), x.val), varList)
        list(map(lambda x: self.visit(x, varList), decl.body[1]))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if isProc:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitCallStmt(self, ast, o):
        self.handleCall(ast, o.frame, o.sym, isStmt=True)

    def handleCall(self, ast, frame, symbols, isStmt=False, typ=VoidType()):
        sym = Utils.lookup(ast.method.name, symbols, lambda x: x.name)
        paramsCode = ""
        idx = 0
        parType = []
        for i in range(len(ast.param)):
            if sym:
                pCode, pType = self.visit(ast.param[i], Access(frame, symbols, False, True, typ=sym.mtype.partype[i]))
            else:
                pCode, pType = self.visit(ast.param[i], Access(frame, symbols, False, True, typ=typ))
            paramsCode = paramsCode + pCode
            parType.append(pType)
            idx = idx + 1
        ctype = MType(parType, IntType()) if type(typ) is BoolType else MType(parType, typ)
        code = ""
        if sym is None:
            for i in self.function:
                if i.name.name == ast.method.name and not Utils.lookup(i.name.name, self.visitFunc, lambda x: x.name.name):
                    varD = [j.variable.name for j in i.param]
                    if type(ctype.rettype) is ArrayType:
                        typFunc = self.inferReturn(FuncDecl(i.name, (varD, ctype), i.body), symbols)
                        ctype = MType(parType, typFunc)
                    self.visitFunc.append(FuncDecl(i.name, (varD, ctype), i.body))         
            code = paramsCode + self.emit.emitINVOKESTATIC(self.className + "/" + ast.method.name, ctype, frame)
        else:
            ctype = sym.mtype
            code = paramsCode + self.emit.emitINVOKESTATIC(sym.value.value + "/" + sym.name, ctype, frame)
        if isStmt: self.emit.printout(code)
        else: return code, ctype.rettype

    def visitReturn(self, ast, o):
        frame = o.frame
        nenv = o.sym
        retType = frame.returnType.mtype.rettype
        if not type(retType) is VoidType:
            expCode, expType = self.visit(ast.expr, Access(frame, nenv, False, True, typ=retType))
            self.emit.printout(expCode)     
        self.emit.printout(self.emit.emitRETURN(retType, frame))
        return True

    def visitIf(self, ast, o):
        frame = o.frame
        nenv = o.sym 
        labelE = frame.getNewLabel() 
        hasReturnStmt = False
        for ele in ast.ifthenStmt:
            expCode, expType = self.visit(ele[0], Access(frame, nenv, False, True, typ=BoolType()))
            labelF = frame.getNewLabel()
            self.emit.printout(expCode)
            self.emit.printout(self.emit.emitIFFALSE(labelF, frame))
            newScope = o
            for x in ele[1]:
                newScope = self.visit(x, newScope)
            for x in ele[1]:
                self.visit(Assign(Id(x.variable.name), x.varInit), newScope)
            hasReturnStmt = True in [self.visit(x, newScope) for x in ele[2]]
            if len(ele[2]) == 0 or type(ele[2][-1]) is not Return: 
                self.emit.printout(self.emit.emitGOTO(labelE, frame))
            self.emit.printout(self.emit.emitLABEL(labelF, frame))
        newScope = o
        for x in ast.elseStmt[0]:
            newScope = self.visit(x, newScope)
        for x in ast.elseStmt[0]:
            self.visit(Assign(Id(x.variable.name), x.varInit), newScope)
        hasReturnStmt = True in [self.visit(x, newScope) for x in ast.elseStmt[1]]
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        return hasReturnStmt

    def visitWhile(self, ast, o):
        frame = o.frame
        nenv = o.sym
        expCode, expType = self.visit(ast.exp, Access(frame, nenv, False, True, typ=BoolType()))
        labelS = frame.getNewLabel() 
        labelE = frame.getNewLabel() 
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFFALSE(labelE, frame))
        newScope = o
        for x in ast.sl[0]:
            newScope = self.visit(x, newScope)
        for x in ast.sl[0]:
            self.visit(Assign(Id(x.variable.name), x.varInit), newScope)
        hasReturnStmt = True in [self.visit(x, newScope) for x in ast.sl[1]]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelS, frame))
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitDowhile(self, ast, o):
        frame = o.frame
        nenv = o.sym
        expCode, _ = self.visit(ast.exp, Access(frame, nenv, False, True, typ=BoolType()))
        labelS = frame.getNewLabel() 
        labelE = frame.getNewLabel()
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        newScope = o
        for x in ast.sl[0]:
            newScope = self.visit(x, newScope)
        for x in ast.sl[0]:
            self.visit(Assign(Id(x.variable.name), x.varInit), newScope)
        hasReturnStmt = True in [self.visit(x, newScope) for x in ast.sl[1]]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        if hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelE, frame)) 
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFTRUE(labelS, frame))
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitFor(self, ast, o):
        frame = o.frame
        nenv = o.sym
        exp1Code, _ = self.visit(ast.expr1, Access(frame, nenv, False, True, typ=IntType()))
        exp2Code, _ = self.visit(ast.expr2, Access(frame, nenv, False, True, typ=BoolType()))
        exp3Code, _ = self.visit(ast.expr3, Access(frame, nenv, False, True, typ=IntType()))
        lhsWCode, _ = self.visit(ast.idx1, Access(frame, nenv, True, True, typ=IntType())) 
        lhsRCode, _ = self.visit(ast.idx1, Access(frame, nenv, False, False, typ=IntType())) 
        labelS = frame.getNewLabel() 
        labelE = frame.getNewLabel() 
        self.emit.printout(exp1Code)
        self.emit.printout(lhsWCode)
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        self.emit.printout(exp2Code)
        self.emit.printout(self.emit.emitIFFALSE(labelE, frame))
        newScope = o
        for x in ast.loop[0]:
            newScope = self.visit(x, newScope)
        for x in ast.loop[0]:
            self.visit(Assign(Id(x.variable.name), x.varInit), newScope)
        hasReturnStmt = True in [self.visit(x, newScope) for x in ast.loop[1]]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        self.emit.printout(lhsRCode)
        self.emit.printout(exp3Code)
        self.emit.printout(self.emit.emitADDOP('+', IntType(), frame))
        self.emit.printout(lhsWCode)
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelS, frame)) 
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitBreak(self, ast, o):    
        frame = o.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast, o):    
        frame = o.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitAssign(self, ast, o):
        frame = o.frame
        nenv = o.sym
        if type(ast.rhs) is ArrayLiteral:
            listEle = Utils.listElements(ast.rhs)
            for i in range(len(listEle)):
                temp = ArrayCell(ast.lhs, [IntLiteral(i)])
                isArray, _ = self.visit(temp, Access(frame, nenv, True, True, checkArrayType=True))
                if isArray: [frame.push() for i in range(0,2)]
                rhsCode, rhsType = self.visit(listEle[i], Access(frame, nenv, False, True, typ=self.getTypeVar(listEle[i])))
                lhsCode, lhsType = self.visit(temp, Access(frame, nenv, True, True, typ=self.getTypeVar(listEle[i])))
                self.emit.printout(lhsCode[0] + rhsCode + lhsCode[1])
                [frame.pop() for i in range(0,2)]
        else:
            isArray, _ = self.visit(ast.lhs, Access(frame, nenv, True, True, checkArrayType=True))
            if isArray: [frame.push() for i in range(0,2)]
            left = Utils.getSymbol(nenv, ast.lhs)
            leftType = left.mtype if left else IntType()
            rhsCode, rhsType = self.visit(ast.rhs, Access(frame, nenv, False, True, typ=leftType))
            lhsCode, lhsType = self.visit(ast.lhs, Access(frame, nenv, True, True, typ=rhsType))
            if not isArray:
                self.emit.printout(rhsCode + lhsCode)
            else:
                self.emit.printout(lhsCode[0] + rhsCode + lhsCode[1])
                [frame.pop() for i in range(0,2)]

    def visitId(self, ast, o):
        frame = o.frame
        symbols = o.sym
        isLeft = o.isLeft
        isFirst = o.isFirst
        if isLeft and o.checkArrayType: return False, None
        sym = Utils.lookup(ast.name, symbols, lambda x: x.name)
        if sym is None:
            sym = Utils.lookup(ast.name, self.visitedPara, lambda x: x.name)
            if sym is None:
                for x in self.paramMain:
                    if x.variable.name == ast.name:
                        idx = frame.getNewIndex()
                        if len(x.varDimen) > 0:
                            self.emit.printout(self.emit.emitVAR(idx, ast.name, Utils.retrieveType(ArrayType(o.typ, x.varDimen)), frame.getStartLabel(), frame.getEndLabel(), frame))
                            size = 1
                            for i in x.varDimen: size *= i
                            self.emit.printout(self.emit.emitInitNewLocalArray(idx, size, o.typ, frame))
                            self.visitedPara.append(Symbol(ast.name, ArrayType(o.typ, x.varDimen), Index(idx)))
                        else:
                            self.emit.printout(self.emit.emitVAR(idx, ast.name, Utils.retrieveType(o.typ), frame.getStartLabel(), frame.getEndLabel(), frame))
                            self.visitedPara.append(Symbol(ast.name, o.typ, Index(idx)))
                        symbols = [Symbol(ast.name, Utils.retrieveType(o.typ), Index(idx))] + o.sym
                        sym = Utils.lookup(ast.name, self.visitedPara, lambda x: x.name)
                        self.paramMain.remove(x)
        if not isFirst and isLeft: frame.push()
        elif not isFirst and not isLeft: frame.pop()
        isArrayType = type(sym.mtype) is ArrayType
        emitType = Utils.retrieveType(sym.mtype)
        if sym.value is None: 
            if isLeft and not isArrayType: retCode = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, emitType, frame)
            else:
                if isLeft and type(o.typ) is ArrayType: retCode = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, emitType, frame)
                else: retCode = self.emit.emitGETSTATIC(self.className + "/" + sym.name, emitType, frame)
        else:
            if isLeft and not isArrayType: retCode = self.emit.emitWRITEVAR(sym.name, emitType, sym.value.value, frame)
            else:
                if isLeft and type(o.typ) is ArrayType: retCode = self.emit.emitWRITEVAR(sym.name, emitType, sym.value.value, frame)
                else: retCode = self.emit.emitREADVAR(sym.name, emitType, sym.value.value, frame)
        return retCode, sym.mtype

    def visitArrayCell(self, ast, o):
        frame = o.frame
        symbols = o.sym
        isLeft = o.isLeft
        isFirst = o.isFirst
        if isLeft and o.checkArrayType: return True, None
        idxCode = ""
        if type(ast.arr) is CallExpr:
            arrCode, arrType = self.visit(ast.arr, Access(frame, symbols, isLeft, True, typ=ArrayType(o.typ, [])))
            asym = arrType.dimen
            if len(ast.idx) > 1:
                for i in range(len(ast.idx)):
                    temp, _ = self.visit(ast.idx[i], Access(frame, symbols, False, True, typ=IntType()))
                    for j in range(i + 1, len(asym)):
                        temp = temp + self.emit.emitPUSHICONST(asym[j], frame) + self.emit.emitMULOP('*', IntType(), frame)
                    if i == 0: idxCode = temp
                    else: idxCode = idxCode + temp + self.emit.emitADDOP('+', IntType(), frame)
            else:
                idxCode, idxType = self.visit(ast.idx[0], Access(frame, symbols, False, True, typ=IntType()))
            if isLeft:
                return [arrCode + idxCode, self.emit.emitASTORE(o.typ, frame)], o.typ
            return arrCode + idxCode + self.emit.emitALOAD(o.typ, frame), o.typ
        else:
            arrCode, arrType = self.visit(ast.arr, Access(frame, symbols, isLeft, True, typ=o.typ))
            asym = Utils.getSymbol(symbols, ast.arr)
            if asym: asym = asym.mtype.dimen
            else: asym = Utils.lookup(ast.arr.name, self.visitedPara, lambda x: x.name).mtype.dimen
            if len(ast.idx) > 1:
                for i in range(len(ast.idx)):
                    temp, _ = self.visit(ast.idx[i], Access(frame, symbols, False, True, typ=IntType()))
                    for j in range(i + 1, len(asym)):
                        temp = temp + self.emit.emitPUSHICONST(asym[j], frame) + self.emit.emitMULOP('*', IntType(), frame)
                    if i == 0: idxCode = temp
                    else: idxCode = idxCode + temp + self.emit.emitADDOP('+', IntType(), frame)
            else:
                idxCode, idxType = self.visit(ast.idx[0], Access(frame, symbols, False, True, typ=IntType()))
            if isLeft:
                return [arrCode + idxCode, self.emit.emitASTORE(arrType.eleType, frame)], arrType.eleType
            return arrCode + idxCode + self.emit.emitALOAD(arrType.eleType, frame), arrType.eleType

    def visitCallExpr(self, ast, o):
        return self.handleCall(ast, o.frame, o.sym, isStmt=False, typ=o.typ)

    def visitBinaryOp(self, ast, o):  
        frame = o.frame
        op = ast.op
        if op in ['&&', '||']:
            o.typ = BoolType()
            frame = o.frame
            buffer = []
            labelT = frame.getNewLabel()
            labelF = frame.getNewLabel()
            lCode = self.visit(ast.left, o)[0]
            buffer.append(lCode)
            if ast.op == '||':
                buffer.append(self.emit.emitIFTRUE(labelT,frame))
            else:
                buffer.append(self.emit.emitIFFALSE(labelF,frame))
            rCode = self.visit(ast.right, o)[0]
            buffer.append(rCode)
            if ast.op == '||':
                buffer.append(self.emit.emitIFTRUE(labelT,frame))
                buffer.append(self.emit.emitPUSHICONST("False",frame))
                buffer.append(self.emit.emitGOTO(labelF,frame))
                buffer.append(self.emit.emitLABEL(labelT,frame))
                buffer.append(self.emit.emitPUSHICONST("True",frame))
                buffer.append(self.emit.emitLABEL(labelF,frame))
            else:
                buffer.append(self.emit.emitIFFALSE(labelF,frame))
                buffer.append(self.emit.emitPUSHICONST("True",frame))
                buffer.append(self.emit.emitGOTO(labelT,frame))
                buffer.append(self.emit.emitLABEL(labelF,frame))
                buffer.append(self.emit.emitPUSHICONST("False",frame))
                buffer.append(self.emit.emitLABEL(labelT,frame))
            return "".join(buffer),BoolType()
        if op in ['+', '-', '*', '\\', '%', '==', '!=', '>', '<', '>=', '<=']:
            o.typ = IntType()
        else: o.typ = FloatType()
        lCode, lType = self.visit(ast.left, o)
        rCode, rType = self.visit(ast.right, o)
        if op in ['+', '-', '+.', '-.']:
            return lCode + rCode + self.emit.emitADDOP(op, lType, frame), lType
        if op in ['*', '\\', '%', '*.', '\\.']:
            return lCode + rCode + self.emit.emitMULOP(op, lType, frame), lType
        if op in ['==', '!=', '>', '<', '>=', '<=', '=/=', '>.', '<.', '>=.', '<=.']:
            return lCode + rCode + self.emit.emitREOP(op, lType, frame), BoolType()

    def visitUnaryOp(self, ast, o):
        frame = o.frame
        op = ast.op
        bCode, bType = self.visit(ast.body, o)
        if op == '-': o.typ = IntType()
        if op == '-.': o.typ = FloatType()
        if op == '!': o.typ = BoolType()
        if op in ['-', '-.']: return bCode + self.emit.emitNEGOP(bType, frame), bType
        if op == '!': return bCode + self.emit.emitNOT(bType, frame), bType

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value), o.frame), BoolType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value.replace("'\"", '\\"'), StringType(), o.frame), StringType()

    def visitArrayLiteral(self, ast, o):
        listEle = Utils.listElements(ast)
        frame = o.frame
        idx = frame.getNewIndex()
        eletype = self.getTypeVar(listEle[0])
        code = self.emit.emitInitNewLocalArray(idx, len(listEle), eletype, frame)
        astr = ""
        if type(eletype) is FloatType: astr = "fastore"  
        elif type(eletype) is IntType: astr = "iastore" 
        elif type(eletype) is BoolType: astr = "bastore" 
        else: astr = "aastore"
        astore = "\t" + astr + "\n"
        aload = ""
        if idx >= 0 and idx <= 3: 
            aload = "\t" + "aload_" + str(idx) + "\n"
        else: 
            aload = "\t" + "aload" + str(idx) + "\n"
        for i in range(len(listEle)):
            code += aload
            code += self.emit.emitPUSHICONST(i, frame)
            rhsCode, rhsType = self.visit(listEle[i], Access(o.frame, o.sym, False, True, typ=eletype))
            code += rhsCode + astore
        code += aload
        return code, Utils.getArrayType(ast)
