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
    def __init__(self,name,mtype,value = None, val=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.val = val
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
class BoolType(Type): pass
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type	
    def __str__(self):
        return 'MType(' + printlist(self.partype) + ',' + str(self.rettype) + ')'
class ArrayType(Type):
    def __init__(self,et,*s):
        self.eleType = et #Type
        self.dimen = s   #List[int] 
    def __str__(self):
        return "ArrayType(" + printlist(self.dimen) + ',' + str(self.eletype) + ")"

class Unknown(Type):
    def __str__(self):
        return "Unknown()"

class ArrayPointerType(Type):
    def __init__(self, ctype):
        # cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

class Access():
    def __init__(self, frame, sym, isLeft, isFirst, checkArrayType=False):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.checkArrayType = checkArrayType

class Utils:
    @staticmethod
    def getSymbol(scope, name):
        for x in scope:
            if x.name == name:
                return x
    
    @staticmethod
    def isOpForNumberToNumber(operator):
        return str(operator) in ['+', '-', '*', '/', 'div', 'mod']

    @staticmethod
    def isOpForNumberToBoolean(operator):
        return str(operator) in ['<>', '=', '>', '<', '>=', '<=']

    @staticmethod
    def isOpForNumber(operator):
        return Utils.isOpForNumberToNumber(operator) or Utils.isOpForNumberToBoolean(operator)

    @staticmethod
    def mergeNumberType(lType, rType):
        return FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntType()

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


class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("read", MType([], StringType()), CName(self.libName)),
            Symbol("printLn", MType([], VoidType()), CName(self.libName)),
            Symbol("printStrLn", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("print", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("string_of_int", MType([IntType()], StringType()), CName(self.libName))
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

        self.listGlobalArray = [] # list(VarDecl: array declare global)


    def visitProgram(self, ast, c):
        # #ast: Program
        # #c: Any

        # self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # e = SubBody(None, self.env)
        # self.genMain(e)
        # # generate default constructor
        # self.genInit()
        # # generate class init if necessary
        # self.emit.emitEPILOG()
        # return c
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        staticDecl = self.env
        for x in ast.decl:
            if type(x) is FuncDecl:
                partype = [i.varType for i in x.param]
                staticDecl = [Symbol(x.name.name, MType(partype, Unknown()), CName(self.className))] + staticDecl
            else:
                newSym = self.visit(x, SubBody(None, None, isGlobal=True))
                staticDecl = [newSym] + staticDecl
        
        e = SubBody(None, staticDecl)
        [self.visit(x, e) for x in ast.decl if type(x) is FuncDecl]

        self.emit.emitEPILOG()
        return c
    
    def visitVarDecl(self, ast, o):
        frame = o.frame
        isGlobal = o.isGlobal
        varName = ast.variable.name
        varType = self.getTypeVar(ast.varInit)
        if isGlobal:
            self.emit.printout(self.emit.emitATTRIBUTE(varName, Utils.retrieveType(varType), False, ""))
            if type(varType) is ArrayType: 
                self.listGlobalArray.append(ast)
            return Symbol(varName, varType, val=ast.varInit)
        # params
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, varName, Utils.retrieveType(varType), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        return SubBody(frame, [Symbol(varName, varType, Index(idx), val=ast.varInit)] + o.sym)
    
    def getTypeVar(self, x):
        if type(x) is IntLiteral: return IntType() 
        elif type(x) is FloatLiteral: return FloatType() 
        elif type(x) is BooleanLiteral: return BoolType() 
        elif type(x) is StringLiteral: return StringType() 
        elif type(x) is ArrayLiteral: return ArrayType() 

    def visitFuncDecl(self, ast, o):
        ret = Utils.getSymbol(o.sym, ast.name.name)
        frame = Frame(ast.name.name, ret)
        self.genMETHOD(ast, o.sym, frame)

    def genMETHOD(self, decl, o, frame):
        # o: Any
        glenv = o
        methodName = decl.name.name
        returnType = Utils.getSymbol(o, decl.name.name).mtype.rettype
        if methodName == "main": returnType = VoidType()
        isMain = methodName == "main" and len(decl.param) == 0 and type(returnType) is VoidType
        isProc = type(returnType) is VoidType
        intype = [ArrayPointerType(StringType())] if isMain else [Utils.retrieveType(x.varType) for x in decl.param]
        returnType = VoidType()
        mtype = MType(intype, returnType)
        self.emit.printout(self.emit.emitMETHOD(methodName, MType([ArrayType(StringType())],VoidType()), True, frame))
        frame.enterScope(isProc)

        # Generate code for parameter declarations
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args",
                StringType(), frame.getStartLabel(), frame.getEndLabel(), frame))

        listParamArray = [] # list(Symbol(name, mtype, value: Index(idx)))
        listLocalArray = [] # list(Symbol(name, mtype, value: Index(idx)))
        varList = SubBody(frame, glenv)
        for x in decl.param:
            varList = self.visit(x, varList)
            if type(x.mtype) is ArrayType:
                listParamArray.append(varList.sym[0])
        for x in decl.body[0]:
            varList = self.visit(x, varList)
            if self.getTypeVar(x.varInit) is ArrayType:
                listLocalArray.append(varList.sym[0])

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Init local array declare
        for sym in listLocalArray:
            index = sym.value.value
            varType = sym.mtype
            size = varType.upper - varType.lower + 1
            self.emit.printout(self.emit.emitInitNewLocalArray(index, size, varType.eleType, frame))

        # Clone params array
        for sym in listParamArray:
            index = sym.value.value
            eleType = sym.mtype.eleType
            self.emit.printout(self.emit.emitCloneArray(index, eleType, frame))

        for x in varList.sym:
            if x.val:
                self.visit(Assign(Id(x.name), x.val), varList)

        list(map(lambda x: self.visit(x, varList), decl.body[1]))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if isProc:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()




# ================   Visit Statements   =================
# Param:    o: SubBody(frame, sym)


    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym
        self.handleCall(ast, frame, symbols, isStmt=True)



    def handleCall(self, ast, frame, symbols, isStmt=False):
        # ast: CallStmt | CallExpr

        sym = Utils.lookup(ast.method.name, symbols, lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype
        paramTypes = ctype.partype
        paramsCode = ""
        idx = 0
        for x in ast.param:
            pCode, pType = self.visit(x, Access(frame, symbols, False, True))
            if type(paramTypes[idx]) is FloatType and type(pType) is IntType:
                pCode = pCode + self.emit.emitI2F(frame)
            if type(paramTypes[idx]) is ArrayType:
                pass
            paramsCode = paramsCode + pCode
            idx = idx + 1
        # if sym.name == "main": ctype = MType([ArrayPointerType(StringType())], VoidType())
        code = paramsCode + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame) 
        if isStmt: self.emit.printout(code)
        else: return code, ctype.rettype



    def visitReturn(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        retType = frame.returnType
        if not type(retType) is VoidType:
            expCode, expType = self.visit(ast.expr, Access(frame, nenv, False, True))
            if type(retType) is FloatType and type(expType) is IntType:
                expCode = expCode + self.emit.emitI2F(frame)
            self.emit.printout(expCode)
        # self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(retType, frame))
        return True




    def visitIf(self, ast, o):
        frame = o.frame
        nenv = o.sym
        expCode, expType = self.visit(ast.expr, Access(frame, nenv, False, True))
        self.emit.printout(expCode)

        labelT = frame.getNewLabel() 
        labelE = frame.getNewLabel() 

        self.emit.printout(self.emit.emitIFTRUE(labelT, frame)) 
        hasReturnStmt = True in [self.visit(x, o) for x in ast.elseStmt]
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelE, frame)) # go to end
        # True
        self.emit.printout(self.emit.emitLABEL(labelT, frame))
        hasReturnStmt = True in [self.visit(x, o) for x in ast.thenStmt] and hasReturnStmt
        # End
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        return hasReturnStmt



    def visitWhile(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        expCode, expType = self.visit(ast.exp, Access(frame, nenv, False, True))
        
        labelS = frame.getNewLabel() # label start
        labelE = frame.getNewLabel() # label end
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFFALSE(labelE, frame))
        hasReturnStmt = True in [self.visit(x, o) for x in ast.sl]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelS, frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitDowhile(self, ast, o):
        pass

    def visitFor(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        exp1Code, _ = self.visit(ast.expr1, Access(frame, nenv, False, True))
        exp2Code, _ = self.visit(ast.expr2, Access(frame, nenv, False, True))
        lhsWCode, _ = self.visit(ast.id, Access(frame, nenv, True, True)) # Write code
        lhsRCode, _ = self.visit(ast.id, Access(frame, nenv, False, False)) # Read code
        
        labelS = frame.getNewLabel() # label start
        labelE = frame.getNewLabel() # label end

        # Init value
        self.emit.printout(exp1Code)
        self.emit.printout(lhsWCode)
        frame.enterLoop()
        # Loop
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        # 1. Condition
        self.emit.printout(lhsRCode)
        self.emit.printout(exp2Code)
        if ast.up:
            self.emit.printout(self.emit.emitIFICMPGT(labelE, frame))
        else:
            self.emit.printout(self.emit.emitIFICMPLT(labelE, frame))
        # 2. Statements
        hasReturnStmt = True in [self.visit(x, o) for x in ast.loop]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        # 3. Update index
        self.emit.printout(lhsRCode)
        self.emit.printout(self.emit.emitPUSHICONST(1, frame))
        self.emit.printout(self.emit.emitADDOP('+' if ast.up else '-', IntType(), frame))
        self.emit.printout(lhsWCode)

        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelS, frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitBreak(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))




    def visitAssign(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        # Pre-prepare for assign to array cell
        # stack: ..., arrayref, index, value -> ...
        # push 2 slot for arrayref and index, visit exp first
        isArray, _ = self.visit(ast.lhs, Access(frame, nenv, True, True, checkArrayType=True))
        if isArray: [frame.push() for i in range(0,2)]

        # Visit LHS: Id || ArrayCell
        rhsCode, rhsType = self.visit(ast.rhs, Access(frame, nenv, False, True))
        lhsCode, lhsType = self.visit(ast.lhs, Access(frame, nenv, True, True))
        if not isArray:
            self.emit.printout(rhsCode + lhsCode)
        else:
            self.emit.printout(lhsCode[0] + rhsCode + lhsCode[1])
            # recover stack status
            [frame.pop() for i in range(0,2)]



# ================   Visit Expression   =================
# Param:    o: Access(frame, sym, isLeft, isFirst)
# Return:   (code, type)

    def visitId(self, ast, o):
        # Return (name, type, index)
        frame = o.frame
        symbols = o.sym
        isLeft = o.isLeft
        isFirst = o.isFirst

        if isLeft and o.checkArrayType: return False, None

        sym = Utils.lookup(ast.name, symbols, lambda x: x.name)

        # recover status of stack in frame
        if not isFirst and isLeft: frame.push()
        elif not isFirst and not isLeft: frame.pop()

        isArrayType = type(sym.mtype) is ArrayType
        emitType = Utils.retrieveType(sym.mtype)
        if sym.value is None: # not index -> global var - static field
            if isLeft and not isArrayType: retCode = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, emitType, frame)
            else: retCode = self.emit.emitGETSTATIC(self.className + "/" + sym.name, emitType, frame)
        else:
            if isLeft and not isArrayType: retCode = self.emit.emitWRITEVAR(sym.name, emitType, sym.value.value, frame)
            else: retCode = self.emit.emitREADVAR(sym.name, emitType, sym.value.value, frame)

        return retCode, sym.mtype


    def visitArrayCell(self, ast, o):
        frame = o.frame
        symbols = o.sym
        isLeft = o.isLeft
        isFirst = o.isFirst

        if isLeft and o.checkArrayType: return True, None

        arrCode, arrType = self.visit(ast.arr, Access(frame, symbols, True, True))
        idxCode, idxType = self.visit(ast.idx, Access(frame, symbols, False, True))
        # update index jvm, i.e [3..5] -> [0..2], access [4] -> [1]
        idxCode = idxCode + self.emit.emitPUSHICONST(arrType.lower, frame) + self.emit.emitADDOP('-', IntType(), frame)
        # Steps: aload(address index) -> iconst(access index) -> iaload
        if isLeft:
            return [arrCode + idxCode, self.emit.emitASTORE(arrType.eleType, frame)], arrType.eleType
        return arrCode + idxCode + self.emit.emitALOAD(arrType.eleType, frame), arrType.eleType


    def visitCallExpr(self, ast, o):
        return self.handleCall(ast, o.frame, o.sym, isStmt=False)



    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        op = str(ast.op)
        
        if op in ['orelse', 'andthen']:
            result = []
            lCode, lType = self.visit(ast.left, ctxt)
            result.append(lCode)

            labelF = frame.getNewLabel() # eval is false
            labelT = frame.getNewLabel() # eval is true

            if op == 'andthen': result.append(self.emit.emitIFFALSE(labelF, frame)) # false
            else: result.append(self.emit.emitIFTRUE(labelT, frame)) # true

            rCode, rType = self.visit(ast.right, ctxt)
            result.append(rCode)

            if op == 'andthen':
                result.append(self.emit.emitIFFALSE(labelF, frame)) # false
                result.append(self.emit.emitPUSHICONST("true", frame)) # push true
                result.append(self.emit.emitGOTO(labelT, frame)) # go to true
                result.append(self.emit.emitLABEL(labelF, frame)) # push false
                result.append(self.emit.emitPUSHICONST("false", frame))
                result.append(self.emit.emitLABEL(labelT, frame))
            else:
                result.append(self.emit.emitIFTRUE(labelT, frame)) # true
                result.append(self.emit.emitPUSHICONST("false", frame)) # push false
                result.append(self.emit.emitGOTO(labelF, frame)) # go to false
                result.append(self.emit.emitLABEL(labelT, frame)) # push true
                result.append(self.emit.emitPUSHICONST("true", frame))
                result.append(self.emit.emitLABEL(labelF, frame))

            return ''.join(result), BoolType()
        
        lCode, lType = self.visit(ast.left, ctxt)
        rCode, rType = self.visit(ast.right, ctxt)
        if Utils.isOpForNumber(op): # for number type
            mType = Utils.mergeNumberType(lType, rType)
            if op == '/': mType = FloatType() # mergeType >= lType, rType
            if type(lType) is IntType and type(mType) != type(lType): lCode = lCode + self.emit.emitI2F(frame)
            if type(rType) is IntType and type(mType) != type(rType): rCode = rCode + self.emit.emitI2F(frame)
            if Utils.isOpForNumberToNumber(op):
                if op in ['+', '-']:
                    return lCode + rCode + self.emit.emitADDOP(op, mType, frame), mType
                if op in ['*', '/']:
                    return lCode + rCode + self.emit.emitMULOP(op, mType, frame), mType
                if op == 'div':
                    return lCode + rCode + self.emit.emitDIV(frame), mType
                if op == 'mod':
                    return lCode + rCode + self.emit.emitMOD(frame), mType
            else: # op to boolean: > <= = <>, ...
                return lCode + rCode + self.emit.emitREOP(op, mType, frame), BoolType()
        else: # for boolean type
            mType = BoolType()
            if op == 'or': return lCode + rCode + self.emit.emitOROP(frame), mType
            if op == 'and': return lCode + rCode + self.emit.emitANDOP(frame), mType



    def visitUnaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        op = str(ast.op)
        bCode, bType = self.visit(ast.body, ctxt)
        if op == '-': return bCode + self.emit.emitNEGOP(bType, frame), bType
        if op == 'not': return bCode + self.emit.emitNOT(bType, frame), bType



    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value), o.frame), BoolType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    # def visitArrayLiteral(self, ast, param):
    #     return Utils.getArrayType(ast)
    # def genInit(self):
    #     methodname,methodtype = "<init>",MType([],VoidType())
    #     frame = Frame(methodname, methodtype.rettype)
    #     self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
    #     frame.enterScope(True)
    #     varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
    #     startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
    #     self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
    #     self.emit.printout(self.emit.emitLABEL(startLabel,frame))
    #     self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
    #     self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
    #     self.emit.printout(self.emit.emitLABEL(endLabel, frame))
    #     self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
    #     self.emit.printout(self.emit.emitENDMETHOD(frame))

    # # The following code is just for initial, students should remove it and write your visitor from here
    def genMain(self,o):
        methodname,methodtype = "main",MType([ArrayType(StringType())],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "args",methodtype.partype[0],frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitPUSHICONST(120, frame))
        sym = next(filter(lambda x: x.name == "string_of_int",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/string_of_int",sym.mtype,frame))
        sym = next(filter(lambda x: x.name == "print",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/print",sym.mtype,frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))



    
