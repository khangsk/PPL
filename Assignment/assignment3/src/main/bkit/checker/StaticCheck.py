
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from main.bkit.checker.StaticError import Function, Variable
from main.bkit.utils.AST import ArrayCell, CallExpr, printlist
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
        mtype = None
        value = decl.varInit
        if value:
            if type(value.value) == int: mtype = IntType()
            elif type(value.value) == float: mtype = FloatType()
            elif type(value.value) == str: mtype = StringType()
            elif type(value.value) == bool: mtype = BoolType()
            else:
                t = value
                eleType = ''
                while type(t.value) == list:
                    t = t.value[0]
                    if type(t.value) == int:
                        eleType = IntType()
                        break
                    if type(t.value) == float:
                        eleType = FloatType()
                        break
                    if type(t.value) == str:
                        eleType = StringType()
                        break
                    if type(t.value) == bool:
                        eleType = BoolType()
                        break
                mtype = ArrayType(dimen, eleType)
        else:
            if len(dimen) > 0:
                mtype = ArrayType(dimen, None)
        return Symbol(name, mtype=mtype, kind=Variable())

    @staticmethod
    def fromFuncDecl(decl):
        if len(decl.param) > 0:
            listParam = [Symbol.fromVarDecl(x) for x in decl.param]
            return Symbol(decl.name.name, param=listParam, kind=Function(), isGlobal=True)
        return Symbol(decl.name.name, kind=Function(), isGlobal=True)

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
            if x.name == name.name:
                if (type(name) is Id and x.mtype != ArrayCell) or (type(name) is ArrayCell and x.mtype == ArrayType):
                    res = x
                    print(type(name), res, " ne` ")
        if res is None or str(res.kind) != str(kind):
            raise Undeclared(kind, name)
        return res
    

    @staticmethod
    def isStopTypeStatment(retType):
        return Checker.isReturnType(retType) or type(retType) in [Break, Continue]

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
        u = str(u)
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
            Symbol("int_of_float", MType([FloatType()], IntType())),
            Symbol("float_of_int", MType([IntType()], FloatType())),
            Symbol("int_of_string", MType([StringType()], IntType())),
            Symbol("string_of_int", MType([IntType()], StringType())),
            Symbol("float_of_string", MType([StringType()], FloatType())),
            Symbol("string_of_float", MType([FloatType()], StringType())),
            Symbol("bool_of_string", MType([StringType()], BoolType())),
            Symbol("string_of_bool", MType([BoolType()], StringType())),
            Symbol("read", MType([], StringType())),
            Symbol("printLn", MType([], VoidType())),
            Symbol("printStr", MType([StringType()], VoidType())),
            Symbol("printStrLn", MType([StringType()], VoidType()))]


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
        [self.visit(x, scope) for x in ast.decl]
        
    def visitVarDecl(self, ast, param):
        return Symbol.fromVarDecl(ast)
    
    def visitFuncDecl(self, ast, scope):
        listParam = [self.visit(x, scope) for x in ast.param]
        listLocalVar = [self.visit(x, scope) for x in ast.body[0]]
        listNewSymbols = listParam + listLocalVar
        localScope = Checker.checkRedeclared([], listNewSymbols)
        newScope = Utils.merge(scope, localScope)
        # Visit statments with params: (scope, loop, funcName)
        stmts = []
        for x in ast.body[1]:
            temp = self.visit(x, (newScope, False, ast.name.name))
            newScope = temp[1]
            stmts.append(temp[0])
        # retType =     
    
    def visitBinaryOp(self, ast, param):
        return None
    
    def visitUnaryOp(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, param):
        return None
    
    def visitId(self, ast, param):
        scope, funcName = param
        symbol = Checker.checkUndeclared(scope, ast, Variable())
        return symbol.mtype

    
    def visitArrayCell(self, ast, param):
        scope, funcName = param
        arr = self.visit(ast.arr, (scope, funcName))
        for x in ast.idx:
            idx = self.visit(x, (scope, funcName))
            if type(idx) is not IntType:
                raise TypeMismatchInExpression(ArrayCell(ast.arr, ast.idx))
    
    def visitAssign(self, ast, param):
        scope, loop, funcName = param
        lhsType = self.visit(ast.lhs, (scope, funcName))
        rhsType = self.visit(ast.rhs, (scope, funcName))
        if lhsType == None:
            if rhsType == None:
                raise TypeCannotBeInferred(Assign(ast.lhs, ast.rhs))
            else:
                lhsType = rhsType
                for i in range(len(scope)):
                    if type(ast.lhs) is Id:
                        if scope[i].name == ast.lhs.name:
                            scope[i] = Symbol(scope[i].name, mtype=rhsType, kind=scope[i].kind)
                    elif type(ast.lhs) is ArrayCell:
                        if type(ast.lhs.arr) is Id:
                            if scope[i].name == ast.lhs.arr.name:
                                scope[i] = Symbol(scope[i].name, mtype=rhsType, kind=scope[i].kind)
                        elif type(ast.lhs.arr) is CallExpr:
                            if scope[i].name == ast.lhs.arr.method.name:
                                scope[i] = Symbol(scope[i].name, mtype=rhsType, kind=scope[i].kind)
        # else:
        #     if rhsType == None:
        for i in scope:
            print(i)
        return (ast, scope, None)
        if type(lhsType) == ArrayType:
            print(123)
    
    def visitIf(self, ast, param):
        return None
    
    def visitFor(self, ast, param):
        return None
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast, param):
        return None
    
    def visitDowhile(self, ast, param):
        return None

    def visitWhile(self, ast, param):
        return None

    def visitCallStmt(self, ast, param):
        scope, loop, funcName = param
        self.handleCall(ast, scope, funcName, Function())
    
    def handleCall(self, ast, scope, funcName, kind):
        symbol = Checker.checkUndeclared(scope, ast.method, kind)
    
    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        return ArrayType()
