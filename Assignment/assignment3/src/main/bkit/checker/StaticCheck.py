
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
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
class Symbol:
    def __init__(self, name, dimen=None, mtype=Unknown(), param=None,value=None, kind=Function(), isGlobal=False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.isGlobal = isGlobal
        self.dimen = dimen
        self.param = param

    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ',' + str(self.kind) + ')'
    
    def getKind(self):
        return self.kind if type(self.kind) is Function else Identifier()

    def toTuple(self):
        return (str(self.name), type(self.getKind()))

    def toParam(self):
        self.kind = Parameter()
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
                if dimen != mtype.dimen:
                    print("LOI~~~~~~~~~~~~~~~~~", dimen, mtype.dimen)
                    raise InvalidArrayLiteral(decl)
        else:
            if len(dimen) > 0:
                mtype = ArrayType(dimen, Unknown())
        return Symbol(name, mtype=mtype, kind=Variable())

    @staticmethod
    def fromFuncDecl(decl):
        if len(decl.param) > 0:
            listTypeParam = [Symbol.fromVarDecl(x).mtype for x in decl.param]
            return Symbol(decl.name.name, param=listTypeParam, isGlobal=True)
        return Symbol(decl.name.name, param=[],isGlobal=True)

    @staticmethod
    def fromDecl(decl):
        return Symbol.fromVarDecl(decl) if type(decl) is VarDecl else Symbol.fromFuncDecl(decl)

class Utils:

    @staticmethod
    def lookup(name, lst, func):
        for x in lst:
            if name == func(x):
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
                if type(stack[0]) is IntLiteral:
                    return ArrayType(arr, IntType())
                elif type(stack[0]) is FloatLiteral:
                    return ArrayType(arr, FloatType())
                elif type(stack[0]) is BooleanLiteral:
                    return ArrayType(arr, BoolType())
                elif type(stack[0]) is StringLiteral:
                    return ArrayType(arr, StringType())
            x = stack.pop(0)
            if check == 1:
                arr.append(len(x.value))
            else:
                if arr[-1] != len(x.value):
                    raise InvalidArrayLiteral(ast)
            if not Utils.typeElementArray(x.value):
                raise InvalidArrayLiteral(ast)
            
            temp += x.value
            if not stack:
                stack = temp.copy()
                temp = []
                check = 0
    
    @staticmethod
    def updateScope(scope, typ, x):
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
        for i in range(len(scope)):
            if scope[i].name == s:
                if type(x) is ArrayCell:
                    scope[i] = Symbol(scope[i].name, mtype=ArrayType(scope[i].mtype.dimen, typ), param=scope[i].param, kind=scope[i].kind, isGlobal=scope[i].isGlobal)
                else:
                    scope[i] = Symbol(scope[i].name, mtype=typ, param=scope[i].param, kind=scope[i].kind, isGlobal=scope[i].isGlobal)
                break
    
    @staticmethod
    def updateTypeParam(scope, name, paramType, idx):
        for i in range(len(scope)):
            if scope[i].name == name:
                temp = [x for x in scope[i].param]
                temp[idx] = paramType
                scope[i] = Symbol(scope[i].name, mtype=scope[i].mtype, param=temp, kind=scope[i].kind, isGlobal=scope[i].isGlobal)
                break
    
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
        for i in scope:
            if i.name == s:
                return i
    
    @staticmethod
    def updateScopeToGlobal(scope, newScope):
        temp = [x.name for x in scope]
        for j in newScope:
            if j.name in temp:
                Utils.updateScope(scope, j.mtype, Id(j.name))
    
    @staticmethod
    def updateParam(scope, listNameParam, funcName):
        sym = Utils.getSymbol(scope, Id(funcName))
        if type(sym.kind) is not Function: return
        for i in scope:
            if type(i.kind) is Parameter:
                for j in range(len(listNameParam)):
                    if listNameParam[j] == i.name:
                        if type(sym.param[j]) is Unknown:
                            sym.param[j] = i.mtype
                        elif type(sym.param[j]) is ArrayType:
                            if type(sym.param[j].eletype) is Unknown:
                                sym.param[j].eletype = i.mtype.eletype
                            else:
                                Utils.updateScope(scope, sym.param[j], Id(i.name))
                        else:
                            Utils.updateScope(scope, sym.param[j], Id(i.name))

class Checker:
    @staticmethod
    def checkRedeclared(currentScope, newSymbols):
        newScope = currentScope.copy()
        for x in newSymbols:
            f = Utils.lookup(Symbol.cmp(x), newScope, Symbol.cmp)
            if f is not None:
                raise Redeclared(x.kind, x.name)
            newScope.append(x)
        return newScope
    
    @staticmethod
    def checkUndeclared(visibleScope, name, kind):
        # Return Symbol declared in scope
        res = Utils.lookup((name, type(kind)), visibleScope, lambda x: x.toTuple())
        if res is None:
            raise Undeclared(kind, name)
        return res
    
    @staticmethod
    def handleReturnStmts(stmts):
        # stmts: (stmt, type) with type: None, VoidType, (...)Type, Break
        for i in range(0, len(stmts)-1):
            if Checker.isStopTypeStatment(stmts[i][1]):
                raise UnreachableStatement((stmts[i+1][0]))
        return None if stmts == [] else stmts[-1][1]

    @staticmethod
    def isStopTypeStatment(retType):
        return Checker.isReturnType(retType) or type(retType) in [Break, Continue]

    @staticmethod
    def isReturnType(retType):
        return type(retType) in [IntType, FloatType, BoolType, StringType, ArrayType, VoidType]

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
        return type(a.eletype) == type(b.eletype) and a.dimen == b.dimen

    @staticmethod
    def constantIndexValue(x):
        if type(x) is BinaryOp:
            left = Checker.constantIndexValue(x.left)
            right = Checker.constantIndexValue(x.right)
            if x.op == '+': return left + right
            elif x.op == '-': return left - right
            elif x.op == '*': return left * right
            elif x.op == '\\': return left // right
            elif x.op == '%': return left % right     
        elif type(x) is UnaryOp:
            val = Checker.constantIndexValue(x.body)
            if x.op == '-': return -val
        elif type(x) is IntLiteral:
            return x.value

    @staticmethod
    def checkConstant(x):
        if type(x) is BinaryOp:
            if x.op not in ['+','-','*','\\','%']:
                return False
            left = Checker.checkConstant(x.left)
            right = Checker.checkConstant(x.right)
            return left and right
        elif type(x) is UnaryOp:
            if x.op != '-':
                return False
            val = Checker.checkConstant(x.body)
            return True
        elif type(x) is IntLiteral:
            return True
        else:
            return False
    
    @staticmethod
    def checkArrayFunc(scope, funcName, x, ast):
        if type(x) is ArrayCell:
            if type(x.arr) is CallExpr:
                sym = Checker.checkUndeclared(scope, x.arr.method.name, Function())
                if type(sym.mtype) is not ArrayType:
                    raise TypeCannotBeInferred(ast)

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
            Symbol("int_of_float", param=[FloatType()], mtype=IntType(), isGlobal=True),
            Symbol("float_of_int", param=[IntType()], mtype=FloatType(), isGlobal=True),
            Symbol("int_of_string", param=[StringType()], mtype=IntType(), isGlobal=True),
            Symbol("string_of_int", param=[IntType()], mtype=StringType(), isGlobal=True),
            Symbol("float_of_string", param=[StringType()], mtype=FloatType(), isGlobal=True),
            Symbol("string_of_float", param=[FloatType()], mtype=StringType(), isGlobal=True),
            Symbol("bool_of_string", param=[StringType()], mtype=BoolType(), isGlobal=True),
            Symbol("string_of_bool", param=[BoolType()], mtype=StringType(), isGlobal=True),
            Symbol("read", param=[], mtype=StringType(), isGlobal=True),
            Symbol("printLn", param=[], mtype=VoidType(), isGlobal=True),
            Symbol("printStr", param=[StringType()], mtype=VoidType(), isGlobal=True),
            Symbol("printStrLn", param=[StringType()], mtype=VoidType(), isGlobal=True)]


    def check(self):
        Graph.initialize()
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, c):
        symbols = [Symbol.fromDecl(x).toGlobal() for x in ast.decl]
        scope = Checker.checkRedeclared(c, symbols)
        entryPoint = Symbol("main")
        symbolMain = Utils.lookup(entryPoint.toTuple(), symbols, lambda x: x.toTuple())
        if not symbolMain or str(symbolMain.kind) != str(Function()):
            raise NoEntryPoint()
        listFuncDecl = c + [Symbol.fromDecl(x) for x in ast.decl if type(x) is FuncDecl]
        for x in listFuncDecl:
            Graph.add(x.name)
        Graph.setDefaultVisitedNodes([x.name for x in c])
        for x in ast.decl:
            if type(x) is FuncDecl:
                temp = (self.visit(x, scope)).copy()
                scope = Utils.merge(scope, temp)
        Graph.dfs("main")
        node = Graph.getUnreachableNode()
        if node is not None:
            sym = Utils.lookup(node, listFuncDecl, Symbol.cmp)
            raise UnreachableFunction(sym.name)
        
    def visitVarDecl(self, ast, param):
        return Symbol.fromVarDecl(ast)
    
    def visitFuncDecl(self, ast, scope):
        sym = Utils.getSymbol(scope, ast.name)
        listParam = [self.visit(x, scope).toParam() for x in ast.param]
        for i in range(len(listParam)):
            listParam[i].mtype = sym.param[i]
        listLocalVar = [self.visit(x, scope) for x in ast.body[0]]
        listNewSymbols = listParam + listLocalVar
        localScope = Checker.checkRedeclared([], listNewSymbols)
        newScope = Utils.merge(scope, localScope)
        listNameParam = [x.name for x in listParam]
        stmts = []
        for x in ast.body[1]:
            stmts.append(self.visit(x, (newScope, False, ast.name.name)))
            Utils.updateParam(newScope, listNameParam, ast.name.name)
        ret = Checker.handleReturnStmts(stmts)
        newFunc = Utils.getSymbol(newScope, ast.name)
        if type(newFunc.mtype) is Unknown: newFunc.mtype = VoidType()
        if type(newFunc.mtype) in [IntType, FloatType, BoolType, StringType, ArrayType] and type(ret) not in [IntType, FloatType, BoolType, StringType, ArrayType]:
            raise FunctionNotReturn(ast.name.name)
        return list(filter(lambda x: x.isGlobal, newScope))    
    
    def visitBinaryOp(self, ast, param):
        scope, funcName = param
        op = ast.op
        if op in ['+', '-', '*', '\\', '%', '==', '!=', '>', '<', '>=', '<=']:
            ltype = None
            if type(ast.left) is CallExpr:
                ltype = Utils.getSymbol(scope, ast.left).mtype
            else:
                ltype = self.visit(ast.left, (scope, funcName))
            if type(ltype) not in [IntType, Unknown]:
                raise TypeMismatchInExpression(ast)
            elif type(ltype) is Unknown:
                Utils.updateScope(scope, IntType(), ast.left)
            if type(ast.left) is CallExpr:
                self.visit(ast.left, (scope, funcName))
            rtype = None
            if type(ast.right) is CallExpr:
                rtype = Utils.getSymbol(scope, ast.right).mtype
            else:
                rtype = self.visit(ast.right, (scope, funcName))
            if type(rtype) not in [IntType, Unknown]:
                raise TypeMismatchInExpression(ast)
            elif type(rtype) is Unknown:
                Utils.updateScope(scope, IntType(), ast.right)
            if type(ast.right) is CallExpr:
                self.visit(ast.right, (scope, funcName))
            if op in ['==', '!=', '>', '<', '>=', '<=']:
                return BoolType()
            return IntType()
        elif op in ['+.', '-.', '*.', '\\.', '=/=', '>.', '<.', '>=.', '<=.']:
            ltype = None
            if type(ast.left) is CallExpr:
                ltype = Utils.getSymbol(scope, ast.left).mtype
            else:
                ltype = self.visit(ast.left, (scope, funcName))
            if type(ltype) not in [FloatType, Unknown]:
                raise TypeMismatchInExpression(ast)
            elif type(ltype) is Unknown:
                Utils.updateScope(scope, FloatType(), ast.left)
            if type(ast.left) is CallExpr:
                self.visit(ast.left, (scope, funcName))
            rtype = None
            if type(ast.right) is CallExpr:
                rtype = Utils.getSymbol(scope, ast.right).mtype
            else:
                rtype = self.visit(ast.right, (scope, funcName))
            if type(rtype) not in [FloatType, Unknown]:
                raise TypeMismatchInExpression(ast)
            elif type(rtype) is Unknown:
                Utils.updateScope(scope, FloatType(), ast.right)
            if type(ast.right) is CallExpr:
                self.visit(ast.right, (scope, funcName))
            if op in ['=/=', '>.', '<.', '>=.', '<=.']:
                return BoolType()
            return FloatType()
        elif op in ['&&', '||']:
            ltype = None
            if type(ast.left) is CallExpr:
                ltype = Utils.getSymbol(scope, ast.left).mtype
            else:
                ltype = self.visit(ast.left, (scope, funcName))
            if type(ltype) not in [BoolType, Unknown]:
                raise TypeMismatchInExpression(ast)
            elif type(ltype) is Unknown:
                Utils.updateScope(scope, BoolType(), ast.left)
            if type(ast.left) is CallExpr:
                self.visit(ast.left, (scope, funcName))
            rtype = None
            if type(ast.right) is CallExpr:
                rtype = Utils.getSymbol(scope, ast.right).mtype
            else:
                rtype = self.visit(ast.right, (scope, funcName))
            if type(rtype) not in [BoolType, Unknown]:
                raise TypeMismatchInExpression(ast)
            elif type(rtype) is Unknown:
                Utils.updateScope(scope, BoolType(), ast.right)
            if type(ast.right) is CallExpr:
                self.visit(ast.right, (scope, funcName))
            return BoolType()
    
    def visitUnaryOp(self, ast, param):
        scope, funcName = param
        op = ast.op
        if op == '!':
            eType = None
            if type(ast.body) is CallExpr:
                eType = Utils.getSymbol(scope, ast.body).mtype
            else:
                eType = self.visit(ast.body, (scope, funcName))
            if type(eType) not in [BoolType, Unknown]:
                raise TypeMismatchInExpression(ast)
            elif type(eType) is Unknown:
                Utils.updateScope(scope, BoolType(), ast.body)
            if type(ast.body) is CallExpr:
                self.visit(ast.body, (scope, funcName))
            return BoolType()
        elif op == '-':
            eType = None
            if type(ast.body) is CallExpr:
                eType = Utils.getSymbol(scope, ast.body).mtype
            else:
                eType = self.visit(ast.body, (scope, funcName))
            if type(eType) not in [IntType, Unknown]:
                raise TypeMismatchInExpression(ast)
            elif type(eType) is Unknown:
                Utils.updateScope(scope, IntType(), ast.body)
            if type(ast.body) is CallExpr:
                self.visit(ast.body, (scope, funcName))
            return IntType()
        elif op == '-.':
            eType = None
            if type(ast.body) is CallExpr:
                eType = Utils.getSymbol(scope, ast.body).mtype
            else:
                eType = self.visit(ast.body, (scope, funcName))
            if type(eType) not in [FloatType, Unknown]:
                raise TypeMismatchInExpression(ast)
            elif type(eType) is Unknown:
                Utils.updateScope(scope, FloatType(), ast.body)
            if type(ast.body) is CallExpr:
                self.visit(ast.body, (scope, funcName))
            return FloatType()
    
    def visitCallExpr(self, ast, param):
        scope, funcName = param
        symbol = self.handleCall(ast, scope, funcName, 'void')
        return symbol.mtype
    
    def visitId(self, ast, param):
        scope, funcName = param
        symbol = Checker.checkUndeclared(scope, ast.name, Identifier())
        # print(symbol)
        return symbol.mtype

    def visitArrayCell(self, ast, param):
        scope, funcName = param
        arr = self.visit(ast.arr, (scope, funcName))
        if type(arr) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        listDimen = arr.dimen
        if len(listDimen) != len(ast.idx):
            raise TypeMismatchInExpression(ast)
        for i in range(len(listDimen)):
            if Checker.checkConstant(ast.idx[i]):
                val = Checker.constantIndexValue(ast.idx[i])
                if val < 0 or val >= listDimen[i]:
                    raise IndexOutOfRange(ast)
        for x in ast.idx:
            idx = self.visit(x, (scope, funcName))
            if type(idx) is Unknown:
                Utils.updateScope(scope, IntType(), x)
            elif type(idx) is not IntType:
                raise TypeMismatchInExpression(ast)
        return arr.eletype
    
    def visitAssign(self, ast, param):
        scope, loop, funcName = param
        Checker.checkArrayFunc(scope, funcName, ast.lhs, ast)
        Checker.checkArrayFunc(scope, funcName, ast.rhs, ast)
        lhsType = self.visit(ast.lhs, (scope, funcName))
        rhsType = self.visit(ast.rhs, (scope, funcName))
        if type(lhsType) is Unknown:
            if type(rhsType) is Unknown:
                raise TypeCannotBeInferred(ast)
            elif type(rhsType) in [VoidType, ArrayType]:
                raise TypeMismatchInStatement(ast)
            else:
                Utils.updateScope(scope, rhsType, ast.lhs)
        elif type(lhsType) is ArrayType:
            if type(rhsType) is ArrayType and lhsType.dimen == rhsType.dimen:
                if type(lhsType.eletype) is Unknown and type(rhsType.eletype) is Unknown:
                    raise TypeCannotBeInferred(ast)
                elif type(lhsType.eletype) is Unknown and type(rhsType.eletype) is not Unknown:
                    Utils.updateScope(scope, rhsType, ast.lhs)
                elif type(lhsType.eletype) is not Unknown and type(rhsType.eletype) is Unknown:
                    Utils.updateScope(scope, lhsType, ast.rhs)
                elif type(lhsType.eletype) is not type(rhsType.eletype):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
        elif type(lhsType) is VoidType:
            raise TypeMismatchInStatement(ast)
        else:
            if type(rhsType) is ArrayType:
                raise TypeMismatchInStatement(ast)
            elif type(rhsType) is Unknown:
                Utils.updateScope(scope, lhsType, ast.rhs)
            elif type(lhsType) is not type(rhsType):
                raise TypeMismatchInStatement(ast) 
                
        return (ast, None)
    
    def visitIf(self, ast, param):
        scope, loop, funcName = param
        ret = []
        for x in ast.ifthenStmt:
            condType = self.visit(x[0], (scope, funcName))
            if type(condType) is Unknown:
                Utils.updateScope(scope, BoolType(), x[0])
            elif type(condType) is not BoolType:
                raise TypeMismatchInStatement(ast)
            listLocalVar = [self.visit(i, scope) for i in x[1]]
            localScope = Checker.checkRedeclared([], listLocalVar)
            newScope = Utils.merge(scope, localScope)
            listStmt = []
            for i in x[2]:
                listStmt.append(self.visit(i, (newScope, False, funcName)))
                for j in newScope:
                    if j.isGlobal:
                        Utils.updateScope(scope, j.mtype, Id(j.name))
            ret.append(Checker.handleReturnStmts(listStmt))
        listLocalVar = [self.visit(i, scope) for i in ast.elseStmt[0]]
        localScope = Checker.checkRedeclared([], listLocalVar)
        newScope = Utils.merge(scope, localScope)
        listStmt = []
        for i in ast.elseStmt[1]:
            listStmt.append(self.visit(i, (newScope, False, funcName)))
            Utils.updateScopeToGlobal(scope, newScope)
        ret.append(Checker.handleReturnStmts(listStmt))
        sym = Utils.getSymbol(scope, Id(funcName))
        if any(x is None for x in ret): return (ast, None)
        if all(type(x) not in [Break, Continue] for x in ret): return (ast, sym.mtype)
        return (ast, Break())
    
    def visitFor(self, ast, param):
        scope, loop, funcName = param
        idx1 = Checker.checkUndeclared(scope, ast.idx1.name, Identifier())
        if type(idx1.mtype) is Unknown:
            Utils.updateScope(scope, IntType(), ast.idx1)
        elif type(idx1.mtype) is not IntType:
            raise TypeMismatchInStatement(ast)
        
        e1Type = None
        if type(ast.expr1) is CallExpr:
            e1Type = Utils.getSymbol(scope, ast.expr1).mtype
        else:
            e1Type = self.visit(ast.expr1, (scope, funcName))
        if type(e1Type) is Unknown:
            Utils.updateScope(scope, IntType(), ast.expr1)
            self.visit(ast.expr1, (scope, funcName))
        elif type(e1Type) is not IntType:
            raise TypeMismatchInStatement(ast)

        e2Type = None
        if type(ast.expr2) is CallExpr:
            e2Type = Utils.getSymbol(scope, ast.expr2).mtype
        else:
            e2Type = self.visit(ast.expr2, (scope, funcName))
        if type(e2Type) is Unknown:
            Utils.updateScope(scope, BoolType(), ast.expr2)
            self.visit(ast.expr2, (scope, funcName))
        elif type(e2Type) is not BoolType:
            raise TypeMismatchInStatement(ast)

        e3Type = None
        if type(ast.expr3) is CallExpr:
            e3Type = Utils.getSymbol(scope, ast.expr3).mtype
        else:
            e3Type = self.visit(ast.expr3, (scope, funcName))
        if type(e3Type) is Unknown:
            Utils.updateScope(scope, IntType(), ast.expr3)
            self.visit(ast.expr3, (scope, funcName))
        elif type(e3Type) is not IntType:
            raise TypeMismatchInStatement(ast)
        listLocalVar = [self.visit(i, scope) for i in ast.loop[0]]
        localScope = Checker.checkRedeclared([], listLocalVar)
        newScope = Utils.merge(scope, localScope)
        listStmt = []
        for i in ast.loop[1]:
            listStmt.append(self.visit(i, (newScope, True, funcName)))
            Utils.updateScopeToGlobal(scope, newScope)
        Checker.handleReturnStmts(listStmt)
        return (ast, None)
        
    def visitContinue(self, ast, param):
        scope, loop, funcName = param
        if not loop: raise NotInLoop(ast)
        return (ast, Continue())
    
    def visitBreak(self, ast, param):
        scope, loop, funcName = param
        if not loop: raise NotInLoop(ast)
        return (ast, Break())

    def visitReturn(self, ast, param):
        scope, loop, funcName = param
        ret = VoidType()
        if ast.expr:
            if type(ast.expr) is CallExpr:
                ret = Utils.getSymbol(scope, ast.expr).mtype
            else:
                ret = self.visit(ast.expr, (scope, funcName))
        s = Utils.getSymbol(scope, Id(funcName))
        if type(s.mtype) is Unknown and type(ret) is Unknown:
            raise TypeCannotBeInferred(ast)
        elif type(s.mtype) is Unknown and type(ret) is not Unknown:
            Utils.updateScope(scope, ret, Id(funcName))
        elif type(s.mtype) is not Unknown and type(ret) is Unknown:
            if type(s.mtype) is VoidType:
                if type(ast.expr) is CallExpr:
                    Utils.updateScope(scope, s.mtype, ast.expr)
                else:
                    raise TypeMismatchInStatement(ast)
            else:
                Utils.updateScope(scope, s.mtype, ast.expr)
        elif not Checker.matchType(s.mtype, ret):
            raise TypeMismatchInStatement(ast)
        if type(ast.expr) is CallExpr:
            ret = self.visit(ast.expr, (scope, funcName))
        return (ast, ret)
    
    def visitDowhile(self, ast, param):
        scope, loop, funcName = param
        listLocalVar = [self.visit(i, scope) for i in ast.sl[0]]
        localScope = Checker.checkRedeclared([], listLocalVar)
        newScope = Utils.merge(scope, localScope)
        listStmt = []
        for i in ast.sl[1]:
            listStmt.append(self.visit(i, (newScope, True, funcName)))
            Utils.updateScopeToGlobal(scope, newScope)
        Checker.handleReturnStmts(listStmt)

        eType = None
        if type(ast.exp) is CallExpr:
            eType = Utils.getSymbol(scope, ast.exp).mtype
        else:
            eType = self.visit(ast.exp, (scope, funcName))
        if type(eType) is Unknown:
            Utils.updateScope(scope, BoolType(), ast.exp)
            self.visit(ast.exp, (scope, funcName))
        elif type(eType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        return (ast, None)

    def visitWhile(self, ast, param):
        scope, loop, funcName = param
        eType = None
        if type(ast.exp) is CallExpr:
            eType = Utils.getSymbol(scope, ast.exp).mtype
        else:
            eType = self.visit(ast.exp, (scope, funcName))
        if type(eType) is Unknown:
            Utils.updateScope(scope, BoolType(), ast.exp)
            self.visit(ast.exp, (scope, funcName))
        elif type(eType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        listLocalVar = [self.visit(i, scope) for i in ast.sl[0]]
        localScope = Checker.checkRedeclared([], listLocalVar)
        newScope = Utils.merge(scope, localScope)
        listStmt = []
        for i in ast.sl[1]:
            listStmt.append(self.visit(i, (newScope, True, funcName)))
            Utils.updateScopeToGlobal(scope, newScope)
        Checker.handleReturnStmts(listStmt)
        return (ast, None)

    def visitCallStmt(self, ast, param):
        scope, loop, funcName = param
        symbol = self.handleCall(ast, scope, funcName, 'function')
        s = Utils.getSymbol(scope, ast.method)
        if type(s.mtype) is Unknown:
            Utils.updateScope(scope, VoidType(), Id(s.name))
        elif type(s.mtype) is not VoidType:
            raise TypeMismatchInStatement(ast)
        return (ast, None)
    
    def handleCall(self, ast, scope, funcName, kind):
        symbol = Checker.checkUndeclared(scope, ast.method.name, Function())
        if len(symbol.param) != len(ast.param): 
            raise TypeMismatchInStatement(ast) if kind == 'function' else TypeMismatchInExpression(ast)   
        for i in range(len(ast.param)):
            sym = None
            if type(ast.param[i]) is CallExpr:
                sym = Utils.getSymbol(scope, ast.param[i]).mtype
            else:
                sym = self.visit(ast.param[i], (scope, funcName))
            if type(symbol.param[i]) is Unknown:
                if type(sym) in [VoidType, ArrayType]:
                    raise TypeMismatchInStatement(ast) if kind == 'function' else TypeMismatchInExpression(ast)
                elif type(sym) is Unknown:
                    raise TypeCannotBeInferred(ast)
                else:
                    Utils.updateTypeParam(scope, ast.method.name, sym, i)
            elif type(symbol.param[i]) is ArrayType:
                if type(sym) is not ArrayType:
                    raise TypeMismatchInStatement(ast) if kind == 'function' else TypeMismatchInExpression(ast)
                if type(symbol.param[i].eletype) is Unknown and type(sym.eletype) is Unknown:
                    raise TypeCannotBeInferred(ast)
                elif type(symbol.param[i].eletype) is Unknown and type(sym.eletype) is not Unknown:
                    Utils.updateTypeParam(scope, ast.method.name, sym, i)
                elif type(symbol.param[i].eletype) is not Unknown and type(sym.eletype) is Unknown:
                    Utils.updateScope(scope, symbol.param[i], ast.param[i])
                elif type(symbol.param[i].eletype) is not type(sym.eletype):
                    raise TypeMismatchInStatement(ast) if kind == 'function' else TypeMismatchInExpression(ast)
            else: 
                if type(sym) in [VoidType, ArrayType]:
                    raise TypeMismatchInStatement(ast) if kind == 'function' else TypeMismatchInExpression(ast)
                elif type(sym) is Unknown:
                    Utils.updateScope(scope, symbol.param[i], ast.param[i])
                elif type(symbol.param[i]) is not type(sym):
                    raise TypeMismatchInStatement(ast) if kind == 'function' else TypeMismatchInExpression(ast)
            if type(ast.param[i]) is CallExpr:
                self.visit(ast.param[i], (scope, funcName))
        Graph.add(funcName, ast.method.name)
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
