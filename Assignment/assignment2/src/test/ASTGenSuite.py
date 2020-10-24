import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test2_array_program(self):
        input = """Var:x = 1, y;
        Var: a[2] = 3, b[4];"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("y"),[],None),VarDecl(Id("a"),[IntLiteral(2)],IntLiteral(3)),VarDecl(Id("b"),[IntLiteral(4)],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test3_array_program(self):
        input = """Var: abc[1][2][3] = 4;"""
        expect = Program([VarDecl(Id("abc"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)],IntLiteral(4))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    # def test4_call_stmt(self):
    #     input = r"""
    #     Function: fact
    #     Parameter: b, c[1][2]
    #     Body:
    #         Var: a;
    #         a = 5;
    #         writeln(a[i], " is smaller than ", b);
    #     EndBody."""
    #     expect = Program([])
        # [FuncDecl(Id("fact")[VarDecl(Id("b")),VarDecl(Id("c"),[IntLiteral(1),IntLiteral(2)])],([][]))
        # self.assertTrue(TestAST.checkASTGen(input,expect,304))
    # def test5_only_if_stmt(self):
    #     input = """
    #     Function: fact
    #     Body:
    #         If a[i] > b Then 
    #             writeln(a[i], " is larger than ", b);
    #         EndIf.
    #     EndBody.
    #     """
    #     expect = Program([])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,305))
    # def test6_if_elseif_stmt(self):
    #     input = """
    #     Function: fact
    #     Body:
    #         If a[i] > b Then 
    #             writeln(a[i], " is larger than ", b);
    #         ElseIf a[i] == b Then 
    #             writeln(a[i], " equal ", b);
    #         EndIf.
    #     EndBody.
    #     """
    #     expect = Program([])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,306))
    # def test7_if_else_stmt(self):
    #     input = """
    #     Function: fact
    #     Body:
    #         If a[i] > b Then 
    #             writeln(a[i], " is larger than ", b);
    #         Else 
    #             writeln(a[i], " is smaller than ", b);
    #         EndIf.
    #     EndBody.
    #     """
    #     expect = Program([])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,307))
    # def test8_if_stmt(self):
    #     input = """
    #     Function: fact
    #     Body:
    #         If a[i] > b Then 
    #             writeln(a[i], " is larger than ", b);
    #         ElseIf a[i] == b Then 
    #             writeln(a[i], " equal ", b);
    #         Else 
    #             writeln(a[i], " is smaller than ", b);
    #         EndIf.
    #     EndBody.
    #     """
    #     expect = Program([])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,308))
    # def test9_if_stmt(self):
    #     input = """
    #     Function: fact
    #     Body:
    #         If a[i] > b Then 
    #             writeln(a[i], " is larger than ", b);
    #         ElseIf a[i] == b Then 
    #             writeln(a[i], " equal ", b);
    #         ElseIf a[i] && b Then 
    #             writeln(a[i]);
    #         ElseIf !a[i] Then 
    #             writeln(b);
    #         Else 
    #             writeln(a[i], " is smaller than ", b);
    #         EndIf.
    #     EndBody.
    #     """
    #     expect = Program([])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test10_var_array(self):
        input = """Var: a[3] = {1,0,2};"""
        expect = Program([VarDecl(Id("a"),[IntLiteral(3)],ArrayLiteral([IntLiteral(1),IntLiteral(0),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test11_var_array(self):
        input = """Var: a[3][2] = {{1,0XAF},{4,0},{0O6543,7}};
        """
        expect = Program([VarDecl(Id("a"),[IntLiteral(3),IntLiteral(2)],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral("0XAF")]),ArrayLiteral([IntLiteral(4),IntLiteral(0)]),ArrayLiteral([IntLiteral("0O6543"),IntLiteral(7)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    # def test12_while_stmt(self):
    #     input = """
    #     Function: abc
    #     Body:
    #         Var: i = 10;
    #         While (i > 1) Do
    #             writeln(i);
    #             i = i - 1;
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = Program([VarDecl(Id("a"),[IntLiteral(3),IntLiteral(2)],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral("0XAF")]),ArrayLiteral([IntLiteral(4),IntLiteral(0)]),ArrayLiteral([IntLiteral("0O6543"),IntLiteral(7)])]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,312))
    # def test13_while_stmt(self):
    #     input = """
    #     Function: abc
    #     Body:
    #         While True Do
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = Program([])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,313))
    # def test14_do_while_stmt(self):
    #     input = """
    #     Function: abc
    #     Body:
    #         Do
    #             Var: abc = False;
    #             writeln("nothing to print");
    #         While True EndDo.
    #     EndBody.
    #     """
    #     expect = Program([])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,314))
    # def test15_break_stmt(self):
    #     input = """
    #     Function: abc
    #     Body:
    #         Do
    #             Var: abc = False;
    #             Break;
    #             writeln("nothing to print");
    #         While True EndDo.
    #     EndBody.
    #     """
    #     expect = Program([])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,315))
    # def test16_continue_stmt(self):
    #     input = """
    #     Function: main
    #     Body:
    #         While True Do
    #             Continue;
    #             writeln("nothing to print");
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = Program([])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,316))
    # def test17_return_stmt(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: a = 1;
    #         a = a + 10;
    #         Return a;
    #     EndBody.
    #     """
    #     expect = Program([])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,317))
    # def test18_return_stmt(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Return;
    #     EndBody.
    #     """
    #     expect = Program([])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,318))
    