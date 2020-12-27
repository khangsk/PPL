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

        self.listGlobalArray = [] # list(VarDecl: array declare global)

        self.function = []

        self.visitFunc = []

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
            if type(x) is FuncDecl and x.name.name == 'main':
                # partype = [i.varType for i in x.param]
                partype = []
                staticDecl = [Symbol(x.name.name, MType(partype, VoidType()), CName(self.className))] + staticDecl
            elif type(x) is VarDecl:
                newSym = self.visit(x, SubBody(None, None, isGlobal=True))
                staticDecl = [newSym] + staticDecl
            else:
                self.function.append(x)
        
        e = SubBody(None, staticDecl)
        [self.visit(x, e) for x in ast.decl if type(x) is FuncDecl and x.name.name == 'main']
        for x in self.visitFunc:
            staticDecl = [Symbol(x.name.name, x.param[1], CName(self.className))] + staticDecl
            self.visit(x, SubBody(None, staticDecl))
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
        elif type(x) is ArrayLiteral: return Utils.getArrayType(x)

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
        intype = [ArrayType(StringType(),[])] if isMain else decl.param[1].partype
        mtype = MType(intype, returnType)
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, True, frame))
        frame.enterScope(isProc)

        # Generate code for parameter declarations
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args",
                StringType(), frame.getStartLabel(), frame.getEndLabel(), frame))

        listParamArray = [] # list(Symbol(name, mtype, value: Index(idx)))
        listLocalArray = [] # list(Symbol(name, mtype, value: Index(idx)))
        varList = SubBody(frame, glenv)
        if not isMain:
            for i in range(len(decl.param[0])):
                idx = varList.frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(idx, decl.param[0][i], Utils.retrieveType(decl.param[1].partype[i]), varList.frame.getStartLabel(), varList.frame.getEndLabel(), varList.frame))
                varList = SubBody(varList.frame, [Symbol(decl.param[0][i], decl.param[1].partype[i], Index(idx))] + varList.sym)
                # varList = self.visit(x, varList)
                # if type(x.mtype) is ArrayType:
                #     listParamArray.append(varList.sym[0])
        for x in decl.body[0]:
            varList = self.visit(x, varList)
            if type(self.getTypeVar(x.varInit)) is ArrayType:
                listLocalArray.append(varList.sym[0])

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Init global array declare
        for x in self.listGlobalArray:
            arr = Utils.getArrayType(x.varInit)
            size = 1
            for i in arr.dimen: size *= i
            self.emit.printout(self.emit.emitInitNewStaticArray(self.className + "/" + x.variable.name, size, arr.eleType, frame))
        

        # # Init local array declare
        for sym in listLocalArray:
            arr = sym.mtype
            size = 1
            for i in arr.dimen: size *= i
            self.emit.printout(self.emit.emitInitNewLocalArray(sym.value.value, size, arr.eleType, frame))

        # # Clone params array
        # for sym in listParamArray:
        #     index = sym.value.value
        #     eleType = sym.mtype.eleType
        #     self.emit.printout(self.emit.emitCloneArray(index, eleType, frame))

        for x in varList.sym:
            if x.val:
                self.visit(Assign(Id(x.name), x.val), varList)

        list(map(lambda x: self.visit(x, varList), decl.body[1]))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if isProc:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        # else:
        #     self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()




# ================   Visit Statements   =================
# Param:    o: SubBody(frame, sym)


    def visitCallStmt(self, ast, o):
        
        frame = o.frame
        symbols = o.sym
        self.handleCall(ast, frame, symbols, isStmt=True)



    def handleCall(self, ast, frame, symbols, isStmt=False, typ=VoidType()):
        # ast: CallStmt | CallExpr
        sym = Utils.lookup(ast.method.name, symbols, lambda x: x.name)
        paramsCode = ""
        idx = 0
        parType = []
        for i in range(len(ast.param)):
            if sym:
                pCode, pType = self.visit(ast.param[i], Access(frame, symbols, False, True, typ=sym.mtype.partype[i]))
            else:
                pCode, pType = self.visit(ast.param[i], Access(frame, symbols, False, True))
            paramsCode = paramsCode + pCode
            parType.append(pType)
            idx = idx + 1
        ctype = MType(parType, IntType()) if type(typ) is BoolType else MType(parType, typ)
        code = ""
        if sym is None:
            for i in self.function:
                if i.name.name == ast.method.name and not Utils.lookup(i.name.name, self.visitFunc, lambda x: x.name.name):
                    varD = [j.variable.name for j in i.param]
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
            #  var 
            newScope = o
            for x in ele[1]:
                newScope = self.visit(x, newScope)
            for x in ele[1]:
                self.visit(Assign(Id(x.variable.name), x.varInit), newScope)
            hasReturnStmt = True in [self.visit(x, newScope) for x in ele[2]]
            self.emit.printout(self.emit.emitGOTO(labelE, frame)) # go to end
            self.emit.printout(self.emit.emitLABEL(labelF, frame))

        #  var 
        newScope = o
        for x in ast.elseStmt[0]:
            newScope = self.visit(x, newScope)
        for x in ast.elseStmt[0]:
            self.visit(Assign(Id(x.variable.name), x.varInit), newScope)
        hasReturnStmt = True in [self.visit(x, newScope) for x in ast.elseStmt[1]]
        # End
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        return hasReturnStmt



    def visitWhile(self, ast, o):
        
        frame = o.frame
        nenv = o.sym
        expCode, expType = self.visit(ast.exp, Access(frame, nenv, False, True, typ=BoolType()))
        
        labelS = frame.getNewLabel() # label start
        labelE = frame.getNewLabel() # label end
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
            self.emit.printout(self.emit.emitGOTO(labelS, frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitDowhile(self, ast, o):
        frame = o.frame
        nenv = o.sym
        expCode, expType = self.visit(ast.exp, Access(frame, nenv, False, True, typ=BoolType()))
        
        labelS = frame.getNewLabel() # label start
        labelE = frame.getNewLabel() # label end
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
            self.emit.printout(self.emit.emitGOTO(labelE, frame)) # loop
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

        lhsWCode, _ = self.visit(ast.idx1, Access(frame, nenv, True, True, typ=IntType())) # Write code
        lhsRCode, _ = self.visit(ast.idx1, Access(frame, nenv, False, False, typ=IntType())) # Read code
        
        labelS = frame.getNewLabel() # label start
        labelE = frame.getNewLabel() # label end

        # Init value
        self.emit.printout(exp1Code)
        self.emit.printout(lhsWCode)
        frame.enterLoop()
        # Loop
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        # 1. Condition
        self.emit.printout(exp2Code)
        self.emit.printout(self.emit.emitIFFALSE(labelE, frame))
        # 2. Statements
        newScope = o
        for x in ast.loop[0]:
            newScope = self.visit(x, newScope)
        for x in ast.loop[0]:
            self.visit(Assign(Id(x.variable.name), x.varInit), newScope)
        hasReturnStmt = True in [self.visit(x, newScope) for x in ast.loop[1]]

        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        # 3. Update index
        self.emit.printout(lhsRCode)
        self.emit.printout(exp3Code)
        self.emit.printout(self.emit.emitADDOP('+', IntType(), frame))
        self.emit.printout(lhsWCode)

        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelS, frame)) # loop
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
                # Visit LHS: Id || ArrayCell
                rhsCode, rhsType = self.visit(listEle[i], Access(frame, nenv, False, True, typ=self.getTypeVar(listEle[i])))
                lhsCode, lhsType = self.visit(temp, Access(frame, nenv, True, True))
                self.emit.printout(lhsCode[0] + rhsCode + lhsCode[1])
                    # recover stack status
                [frame.pop() for i in range(0,2)]
        else:
            isArray, _ = self.visit(ast.lhs, Access(frame, nenv, True, True, checkArrayType=True))
            if isArray: [frame.push() for i in range(0,2)]

            # Visit LHS: Id || ArrayCell
            leftType = Utils.getSymbol(nenv, ast.lhs).mtype
            rhsCode, rhsType = self.visit(ast.rhs, Access(frame, nenv, False, True, typ=leftType))
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
            else: 
                retCode = self.emit.emitREADVAR(sym.name, emitType, sym.value.value, frame)
        return retCode, sym.mtype


    def visitArrayCell(self, ast, o):
        frame = o.frame
        symbols = o.sym
        isLeft = o.isLeft
        isFirst = o.isFirst

        if isLeft and o.checkArrayType: return True, None
        arrCode, arrType = self.visit(ast.arr, Access(frame, symbols, True, True))
        asym = Utils.getSymbol(symbols, ast.arr).mtype.dimen
        idxCode = ""
        if len(ast.idx) > 1:
            index = 0
            for i in range(len(ast.idx)):
                temp = ast.idx[i].value
                for j in range(i + 1, len(asym)):
                    temp *= asym[j]
                index += temp
            idxCode, idxType = self.visit(IntLiteral(index), Access(frame, symbols, False, True))
        else:
            idxCode, idxType = self.visit(ast.idx[0], Access(frame, symbols, False, True))
        # Steps: aload(address index) -> iconst(access index) -> iaload
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
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    def visitArrayLiteral(self, ast, param):
        return Utils.getArrayType(ast)
    
