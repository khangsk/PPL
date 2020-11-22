
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from main.bkit.checker.StaticError import Function, Parameter, Variable
from main.bkit.utils.AST import ArrayCell, ArrayLiteral, CallExpr, FuncDecl, printlist
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class IntType(Prim):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)


class FloatType(Prim):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)


class StringType(Prim):
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return v.visitStringType(self, param)


class BoolType(Prim):
    def __str__(self):
        return "BoolType"

    def accept(self, v, param):
        return v.visitBoolType(self, param)


class VoidType(Type):
    def __str__(self):
        return "VoidType()"

    def accept(self, v, param):
        return v.visitVoidType(self, param)


class Unknown(Type):
    def __str__(self):
        return "Unknown()"

    def accept(self, v, param):
        return v.visitUnknown(self, param)


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type

    def __str__(self):
        return "ArrayType(" + printlist(self.dimen) + ',' + str(self.eletype) + ")"
    
    def accept(self, v, param):
        return v.visitArrayType(self, param)


@dataclass
class MType:
    intype: List[Type]
    restype: Type
    def __str__(self):
        return 'MType(' + printList(self.intype) + ',' + str(self.restype) + ')'

class ExpUtils:
    @staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntType, FloatType]

    @staticmethod
    def isOpForInt(operator):
        return str(operator) in ['+', '-', '*', '\\', '%', '==', '!=', '>', '<', '>=', '<=']
    
    @staticmethod
    def isOpForFloat(operator):
        return str(operator) in ['+.', '-.', '*.', '\\.', '=/=', '>.', '<.', '>=.', '<=.']

    @staticmethod
    def mergeNumberType(lType, rType):
        return FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntType()

class Symbol:
    def __init__(self, name, dimen=None, mtype=None, param=None,value=None, kind=Function(), isGlobal=False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.isGlobal = isGlobal
        self.dimen = dimen

    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ',' + str(self.kind) + ')'
    
    def getKind(self):
        return self.kind if type(self.mtype) is MType else Identifier()

    def toTuple(self):
        return (str(self.name), type(self.getKind()))

    def toTupleString(self):
        return (str(self.name), str(self.mtype))

    def toParam(self):
        self.kind = Parameter()
        return self

    def toVar(self):
        self.kind = Variable()
        return self

    def toGlobal(self):
        self.isGlobal = True
        return self

    # compare function between 2 instances
    @staticmethod
    def cmp(symbol):
        return str(symbol.name)

    @staticmethod
    def fromVarDecl(decl):
        name = decl.variable.name
        dimen = decl.varDimen
        mtype = Unknown()
        value = decl.varInit
        if value:
            if type(value) is IntLiteral: mtype = IntType()
            elif type(value) is FloatLiteral: mtype = FloatType()
            elif type(value) is StringLiteral: mtype = StringType()
            elif type(value) is BooleanLiteral: mtype = BoolType()
            else: 
                mtype = Utils.getArrayType(value)
                if not Checker.sameDimen(dimen, mtype.dimen):
                    raise 
        else:
            if len(dimen) > 0:
                mtype = ArrayType(dimen, Unknown())
        return Symbol(name, mtype=mtype, kind=Variable())

    @staticmethod
    def fromFuncDecl(decl):
        if len(decl.param) > 0:
            listParam = [Symbol.fromVarDecl(x) for x in decl.param]
            return Symbol(decl.name.name, mtype=Unknown(), param=listParam, kind=Function(), isGlobal=True)
        return Symbol(decl.name.name, mtype=Unknown(), kind=Function(), isGlobal=True)

    @staticmethod
    def fromDecl(decl):
        return Symbol.fromVarDecl(decl) if type(decl) is VarDecl else Symbol.fromFuncDecl(decl)

class Utils:
    @staticmethod
    def findName(name, lst):
        for x in lst:
            if name == x.name:
                return x
        return None

    @staticmethod
    def isExisten(listSymbols, symbol):
        return len([x for x in listSymbols if str(x.name) == str(symbol.name)]) > 0
    
    @staticmethod
    def merge(curScope, newScope):
        return reduce(lambda lst, sym: lst if Utils.isExisten(lst, sym) else lst+ [sym], curScope, newScope)
    
    @staticmethod
    def typeElementArray(arr):
        if not arr:
            return True
        typ = type(arr[0])
        for i in range(1, len(arr)):
            if typ is not type(arr[i]):
                return False
        return True

    @staticmethod
    def getArrayType(ast):
        arr = []
        stack = [ast]
        temp = []
        check = 0
        while stack:
            check += 1
            if type(stack[0]) is not ArrayLiteral:
                if not Utils.typeElementArray(stack):
                    raise InvalidArrayLiteral(ast)
                return ArrayType(arr, type(stack[0]))
            x = stack.pop(0)
            if check == 1:
                arr.append(len(x.value))
            else:
                if arr[-1] != len(x.value):
                    raise InvalidArrayLiteral(ast)
            if not Utils.typeElementArray(x.value):
                raise InvalidArrayLiteral(ast)
            if type(x) is ArrayLiteral:
                # if len(x) != arr[-1]
                temp += x.value
                if not stack:
                    stack = temp.copy()
                    temp = []
                    check = 0

class Checker:
    @staticmethod
    def checkRedeclared(currentScope, newSymbols):
        newScope = currentScope.copy()
        for x in newSymbols:
            f = Utils.findName(x.name, newScope)
            if f is not None:
                raise Redeclared(x.kind, x.name)
            newScope.append(x)
        return newScope
    
    @staticmethod
    def checkUndeclared(visibleScope, name, kind, notGlobal=False):
        # Return Symbol declared in scope
        scope = visibleScope if not notGlobal else [x for x in visibleScope if not x.isGlobal]
        res = None
        for x in scope:
            if x.name == name and str(x.kind) == str(kind):
                res = x
        if res is None or str(res.kind) != str(kind):
            raise Undeclared(kind, name)
        return res
    
    @staticmethod
    def handleReturnStmts(listStmt):
        for i in range(0, len(stmts)-1):
            if Checker.isStopTypeStatment(stmts[i][1]):
                raise UnreachableStatement(stmts[i+1][0])
        return None if stmts == [] else stmts[-1][1]

    @staticmethod
    def isStopTypeStatment(retType):
        return Checker.isReturnType(retType) or type(retType) in [Break, Continue]
    
    @staticmethod
    def matchType(a, b):
        if type(a) is ArrayType and type(b) is ArrayType:
            return Checker.matchArray(a, b)
        if type(a) is ArrayType or type(b) is ArrayType:
            return False
        if type(a) is type(b):
            return True
        return False

    @staticmethod
    def matchArray(a, b):
        return type(a.eletype) == type(b.eletype) and Checker.sameDimen(a.dimen, b.dimen)

    @staticmethod
    def sameDimen(a, b):
        if len(a) != len(b): return False
        for i in range(len(a)):
            if a[i] != b[i]: return False
        return True

class Graph:
    link = {}
    visited = {}
    invoked = {}

    @staticmethod
    def initialize():
        Graph.link.clear()
        Graph.visited.clear()
        Graph.invoked.clear()

    @staticmethod
    def add(u, v=None): # v is None when add new node, else u call v
        u = str(u)
        if type(Graph.link.get(u)) != list:
            Graph.link[u] = []
            Graph.visited[u] = False
            Graph.invoked[u] = False
        if v is None: return
        v = str(v)
        if v != u and v not in Graph.link[u]: 
            Graph.link[u].append(v)
            Graph.invoked[v] = True # v is invoked by u

    @staticmethod
    def dfs(u):
        Graph.visited[u] = True
        [Graph.dfs(v) for v in Graph.link[u] if not Graph.visited[v]]

    @staticmethod
    def getUnreachableNode():
        for u in Graph.link:
            if not Graph.visited[u] and not Graph.invoked[u]: return u
        for u in Graph.link:
            if not Graph.visited[u]: return u
        return None

    @staticmethod
    def setDefaultVisitedNodes(listNodes):
        for u in listNodes: Graph.visited[str(u)] = True
    


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float", MType([FloatType()], IntType()), isGlobal=True),
            Symbol("float_of_int", MType([IntType()], FloatType()), isGlobal=True),
            Symbol("int_of_string", MType([StringType()], IntType()), isGlobal=True),
            Symbol("string_of_int", MType([IntType()], StringType()), isGlobal=True),
            Symbol("float_of_string", MType([StringType()], FloatType()), isGlobal=True),
            Symbol("string_of_float", MType([FloatType()], StringType()), isGlobal=True),
            Symbol("bool_of_string", MType([StringType()], BoolType()), isGlobal=True),
            Symbol("string_of_bool", MType([BoolType()], StringType()), isGlobal=True),
            Symbol("read", MType([], StringType()), isGlobal=True),
            Symbol("printLn", MType([], VoidType()), isGlobal=True),
            Symbol("printStr", MType([StringType()], VoidType()), isGlobal=True),
            Symbol("printStrLn", MType([StringType()], VoidType()), isGlobal=True)]


    def check(self):
        Graph.initialize()
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, c):
        symbols = [Symbol.fromDecl(x).toGlobal() for x in ast.decl]
        scope = Checker.checkRedeclared(c, symbols)
        symbolMain = Utils.findName("main", symbols)
        if not symbolMain or str(symbolMain.kind) != str(Function()):
            raise NoEntryPoint()
        listFuncDecl = c + [Symbol.fromDecl(x) for x in ast.decl if type(x) is FuncDecl]
        for x in listFuncDecl:
            Graph.add(x.name)
        Graph.setDefaultVisitedNodes([x.name for x in c])
        for x in ast.decl:
            if type(x) is FuncDecl:
                scope = (self.visit(x, scope)).copy()

        
    def visitVarDecl(self, ast, param):
        return Symbol.fromVarDecl(ast)
    
    def visitFuncDecl(self, ast, scope):
        listParam = []
        for x in ast.param:
            sym = self.visit(x, scope)
            listParam.append(Symbol(sym.name, mtype=sym.mtype, kind=Parameter()))
        listLocalVar = [self.visit(x, scope) for x in ast.body[0]]
        listNewSymbols = listParam + listLocalVar
        localScope = Checker.checkRedeclared([], listNewSymbols)
        newScope = Utils.merge(scope, localScope)
        stmts = [self.visit(x, (newScope, False, ast.name.name)) for x in ast.body[1]]
        return list(filter(lambda x: x.isGlobal, newScope))
        # retType =     
    
    def visitBinaryOp(self, ast, param):
        return None
    
    def visitUnaryOp(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, param):
        scope, funcName = param
        symbol = self.handleCall(ast, scope, funcName, Function())
        return symbol.mtype
    
    def visitId(self, ast, param):
        scope, funcName = param
        symbol = Checker.checkUndeclared(scope, ast.name, Variable())
        # print(symbol)
        return symbol.mtype

    
    def visitArrayCell(self, ast, param):
        scope, funcName = param
        arr = self.visit(ast.arr, (scope, funcName))
        if type(arr) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        
        for x in ast.idx:
            idx = self.visit(x, (scope, funcName))
            if type(idx) is not IntType:
                raise TypeMismatchInExpression(ast)
        return arr
    
    def visitAssign(self, ast, param):
        scope, loop, funcName = param
        # for x in scope:
        #     print(x)
        lhsType = self.visit(ast.lhs, (scope, funcName))
        rhsType = self.visit(ast.rhs, (scope, funcName))
        print(ast.rhs)
        print(rhsType)
        # if type(ast.lhs) is Id:
        # print(lhsType is Unknown, rhsType is IntType)
        if type(lhsType) is Unknown:
            if type(rhsType) is Unknown:
                raise TypeCannotBeInferred(ast)
            else:
                lhsType = rhsType
                if type(lhsType) is VoidType:
                    raise TypeMismatchInStatement(ast)
                for i in range(len(scope)):
                    if type(ast.lhs) is Id:
                        if scope[i].name == ast.lhs.name:
                            scope[i] = Symbol(scope[i].name, mtype=rhsType, kind=scope[i].kind, isGlobal=scope[i].isGlobal)
                    elif type(ast.lhs) is ArrayCell:
                        print("yes")
                        if type(ast.lhs.arr) is Id:
                            if scope[i].name == ast.lhs.arr.name:
                                scope[i] = Symbol(scope[i].name, mtype=rhsType, kind=scope[i].kind, isGlobal=scope[i].isGlobal)
                                print(scope[i])
                        elif type(ast.lhs.arr) is CallExpr:
                            if scope[i].name == ast.lhs.arr.method.name:
                                scope[i] = Symbol(scope[i].name, mtype=rhsType, kind=scope[i].kind, isGlobal=scope[i].isGlobal)
        else:
            if type(lhsType) is VoidType:
                raise TypeMismatchInStatement(ast)
            if type(rhsType) is not Unknown:
                if type(lhsType) is not type(rhsType):
                    raise TypeMismatchInStatement(ast)
            else:
                rhsType = lhsType
                for i in range(len(scope)):
                    if type(ast.rhs) is Id:
                        if scope[i].name == ast.rhs.name:
                            scope[i] = Symbol(scope[i].name, mtype=rhsType, kind=scope[i].kind, isGlobal=scope[i].isGlobal)
                    elif type(ast.rhs) is ArrayCell:
                        if type(ast.rhs.arr) is Id:
                            if scope[i].name == ast.rhs.arr.name:
                                scope[i] = Symbol(scope[i].name, mtype=rhsType, kind=scope[i].kind, isGlobal=scope[i].isGlobal)
                        elif type(ast.rhs.arr) is CallExpr:
                            if scope[i].name == ast.rhs.arr.method.name:
                                scope[i] = Symbol(scope[i].name, mtype=rhsType, kind=scope[i].kind, isGlobal=scope[i].isGlobal)
                    elif type(ast.rhs) is CallExpr:
                        if scope[i].name == ast.rhs.method.name:
                            scope[i] = Symbol(scope[i].name, mtype=rhsType, kind=scope[i].kind, isGlobal=scope[i].isGlobal)
        #     if rhsType == None:
        # for i in scope:
        #     print(i)
        return (ast, None)
    
    def visitIf(self, ast, param):
        scope, loop, funcName = param
        for x in ast.ifthenStmt:
            condType = self.visit(x[0], param)
            if type(condType) is not BoolType:
                raise TypeMismatchInStatement(ast)
            listLocalVar = [self.visit(i, scope) for i in x[1]]
            localScope = Checker.checkRedeclared([], listLocalVar)
            newScope = Utils.merge(scope, localScope)
            listStmt = []
            for i in x[2]:
                listStmt.append(self.visit(i, (newScope, False, funcName)))
                for j in newScope:
                    if j.isGlobal:
                        for k in range(len(scope)):
                            if scope[k].name == j.name:
                                scope[k] = Symbol(scope[k].name, mtype=j.mtype, kind=scope[k].kind, isGlobal=scope[k].isGlobal)
                                break
            ret = Checker.handleReturnStmts(listStmt)
    
    def visitFor(self, ast, param):
        return None
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast, param):
        scope, loop, funcName = param
        ret = self.visit(ast.expr, (scope, funcName)) if ast.expr else VoidType()
        for i in range(len(scope)):
            if scope[i].name == funcName:
                if type(scope[i].mtype) is Unknown:
                    scope[i] = Symbol(scope[i].name, mtype=ret, kind=scope[i].kind, isGlobal=scope[i].isGlobal)
                elif not Checker.matchType(scope[i].mtype, ret):
                        raise TypeMismatchInStatement(ast)
        return (ast, ret)
    
    def visitDowhile(self, ast, param):
        return None

    def visitWhile(self, ast, param):
        return None

    def visitCallStmt(self, ast, param):
        scope, loop, funcName = param
        symbol = self.handleCall(ast, scope, funcName, Function())
        for i in range(len(scope)):
            if scope[i].name == ast.method.name:
                if type(scope[i].mtype) is Unknown:
                    scope[i] = Symbol(scope[i].name, mtype=VoidType(), kind=scope[i].kind, isGlobal=scope[i].isGlobal)
                elif type(scope[i].mtype) is not VoidType:
                    raise TypeMismatchInStatement(ast)
        return (ast, None)
    
    def handleCall(self, ast, scope, funcName, kind):
        symbol = Checker.checkUndeclared(scope, ast.method.name, kind)
        Graph.add(funcName, ast.method.name)
        paramType = [self.visit(x, (scope, funcName)) for x in ast.param]

        return symbol
    
    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        return Utils.getArrayType(ast)
