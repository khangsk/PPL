import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test2_array_program(self):
        """Simple program: int main() {} """
        input = """Var:x = 1, y;
        Var: a[2] = 3, b[4]"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("y"),[],None),VarDecl(Id("a"),[IntLiteral(2)],IntLiteral(3)),VarDecl(Id("b"),[IntLiteral(4)],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test3_array_program(self):
        """Simple program: int main() {} """
        input = """Var: abc[1][2][3] = 4"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("y"),[],None),VarDecl(Id("a"),[IntLiteral(2)],IntLiteral(3)),VarDecl(Id("b"),[IntLiteral(4)],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

 
   