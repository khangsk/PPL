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

    def test4_call_stmt(self):
        input = r"""
        Function: fact
        Parameter: b, c[1][2]
        Body:
            Var: a;
            a = 5;
            writeln(a[i], " is smaller than ", b);
        EndBody."""
        expect = "Program([FuncDecl(Id(fact)[VarDecl(Id(b)),VarDecl(Id(c),[IntLiteral(1),IntLiteral(2)])],([VarDecl(Id(a))][Assign(Id(a),IntLiteral(5)),CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( is smaller than ),Id(b)])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test5_only_if_stmt(self):
        input = """
        Function: fact
        Body:
            If a[i] > b Then 
                writeln(a[i], " is larger than ", b);
            EndIf.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(fact)[],([][If(BinaryOp(>,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( is larger than ),Id(b)])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test6_if_elseif_stmt(self):
        input = """
        Function: fact
        Body:
            If a[i] > b Then 
                writeln(a[i], " is larger than ", b);
            ElseIf a[i] == b Then 
                writeln(a[i], " equal ", b);
            EndIf.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(fact)[],([][If(BinaryOp(>,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( is larger than ),Id(b)])])ElseIf(BinaryOp(==,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( equal ),Id(b)])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test7_if_else_stmt(self):
        input = """
        Function: fact
        Body:
            If a[i] > b Then 
                writeln(a[i], " is larger than ", b);
            Else 
                writeln(a[i], " is smaller than ", b);
            EndIf.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(fact)[],([][If(BinaryOp(>,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( is larger than ),Id(b)])])Else([],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( is smaller than ),Id(b)])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test8_if_stmt(self):
        input = """
        Function: fact
        Body:
            If a[i] > b Then 
                writeln(a[i], " is larger than ", b);
            ElseIf a[i] == b Then 
                writeln(a[i], " equal ", b);
            Else 
                writeln(a[i], " is smaller than ", b);
            EndIf.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(fact)[],([][If(BinaryOp(>,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( is larger than ),Id(b)])])ElseIf(BinaryOp(==,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( equal ),Id(b)])])Else([],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( is smaller than ),Id(b)])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test9_if_stmt(self):
        input = """
        Function: fact
        Body:
            If a[i] > b Then 
                writeln(a[i], " is larger than ", b);
            ElseIf a[i] == b Then 
                writeln(a[i], " equal ", b);
            ElseIf a[i] && b Then 
                writeln(a[i]);
            ElseIf !a[i] Then 
                writeln(b);
            Else 
                writeln(a[i], " is smaller than ", b);
            EndIf.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(fact)[],([][If(BinaryOp(>,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( is larger than ),Id(b)])])ElseIf(BinaryOp(==,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( equal ),Id(b)])])ElseIf(BinaryOp(&&,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)])])])ElseIf(UnaryOp(!,ArrayCell(Id(a),[Id(i)])),[],[CallExpr(Id(writeln),[Id(b)])])Else([],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( is smaller than ),Id(b)])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test10_var_array(self):
        input = """Var: a[3] = {1,0,2};"""
        expect = "Program([VarDecl(Id(a),[IntLiteral(3)],ArrayLiteral(IntLiteral(1),IntLiteral(0),IntLiteral(2)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test11_var_array(self):
        input = """Var: a[3][2] = {{1,0XAF},{4,0},{0O6543,7}};
        """
        expect = "Program([VarDecl(Id(a),[IntLiteral(3),IntLiteral(2)],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(0XAF)),ArrayLiteral(IntLiteral(4),IntLiteral(0)),ArrayLiteral(IntLiteral(0O6543),IntLiteral(7))))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test12_while_stmt(self):
        input = """
        Function: abc
        Body:
            Var: i = 10;
            While (i > 1) Do
                writeln(i);
                i = i - 1;
            EndWhile.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(abc)[],([VarDecl(Id(i),IntLiteral(10))][While(BinaryOp(>,Id(i),IntLiteral(1)),[],[CallExpr(Id(writeln),[Id(i)]),Assign(Id(i),BinaryOp(-,Id(i),IntLiteral(1)))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test13_while_stmt(self):
        input = """
        Function: abc
        Body:
            While True Do
            EndWhile.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(abc)[],([][While(BooleanLiteral(true),[],[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test14_do_while_stmt(self):
        input = """
        Function: abc
        Body:
            Do
                Var: abc = False;
                writeln("nothing to print");
            While True EndDo.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(abc)[],([][Dowhile([VarDecl(Id(abc),BooleanLiteral(false))],[CallExpr(Id(writeln),[StringLiteral(nothing to print)])],BooleanLiteral(true))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test15_break_stmt(self):
        input = """
        Function: abc
        Body:
            Do
                Var: abc = False;
                Break;
                writeln("nothing to print");
            While True EndDo.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(abc)[],([][Dowhile([VarDecl(Id(abc),BooleanLiteral(false))],[Break(),CallExpr(Id(writeln),[StringLiteral(nothing to print)])],BooleanLiteral(true))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test16_continue_stmt(self):
        input = """
        Function: main
        Body:
            While True Do
                Continue;
                writeln("nothing to print");
            EndWhile.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(main)[],([][While(BooleanLiteral(true),[],[Continue(),CallExpr(Id(writeln),[StringLiteral(nothing to print)])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test17_return_stmt(self):
        input = """
        Function: main
        Body:
            Var: a = 1;
            a = a + 10;
            Return a;
        EndBody.
        """
        expect = "Program([FuncDecl(Id(main)[],([VarDecl(Id(a),IntLiteral(1))][Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(10))),Return(Id(a))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test18_return_stmt(self):
        input = """
        Function: main
        Body:
            Return;
        EndBody.
        """
        expect = "Program([FuncDecl(Id(main)[],([][Return()])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test19_for_stmt(self):
        input = """
        Function: main
        Parameter: a[10]
        Body:
            For (i = 1, i < 10, 1) Do
                writeln(a[i]);
            EndFor.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(main)[VarDecl(Id(a),[IntLiteral(10)])],([][For(Id(i),IntLiteral(1),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(1),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)])])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test20_for_stmt(self):
        input = """
        Function: main
        Parameter: a[10]
        Body:
            For (i = 1, i < 10, 1) Do
            EndFor.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(main)[VarDecl(Id(a),[IntLiteral(10)])],([][For(Id(i),IntLiteral(1),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(1),[],[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test21_index_exp(self):
        input = """
        Function: main
        Parameter: a[2][10]
        Body:
            For (i = 0, i < 2, 1) Do
                For (j = 0, j < 10, 1) Do
                    a[i][j] = a[i][j] * 10;
                    writeln(a[i][j]);
                EndFor.
            EndFor.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(main)[VarDecl(Id(a),[IntLiteral(2),IntLiteral(10)])],([][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(2)),IntLiteral(1),[],[For(Id(j),IntLiteral(0),BinaryOp(<,Id(j),IntLiteral(10)),IntLiteral(1),[],[Assign(ArrayCell(Id(a),[Id(i),Id(j)]),BinaryOp(*,ArrayCell(Id(a),[Id(i),Id(j)]),IntLiteral(10))),CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i),Id(j)])])])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test22_var(self):
        input = r"""
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, z;
        Var: m = 1, n[2] = {   2   ,   3   };"""
        expect = "Program([VarDecl(Id(a),IntLiteral(5)),VarDecl(Id(b),[IntLiteral(2),IntLiteral(3)],ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6)))),VarDecl(Id(c)),VarDecl(Id(d),IntLiteral(6)),VarDecl(Id(e)),VarDecl(Id(z)),VarDecl(Id(m),IntLiteral(1)),VarDecl(Id(n),[IntLiteral(2)],ArrayLiteral(IntLiteral(2),IntLiteral(3)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test23_funct_declare_part(self):
        input = r"""
        Var: x;
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact(n - 1);
                EndIf.
            EndBody.
        Function: main
        Body:
            x = 10;
            fact(x);
        EndBody."""
        expect = "Program([VarDecl(Id(x)),FuncDecl(Id(fact)[VarDecl(Id(n))],([][If(BinaryOp(==,Id(n),IntLiteral(0)),[],[Return(IntLiteral(1))])Else([],[Return(BinaryOp(*,Id(n),CallExpr(Id(fact),[BinaryOp(-,Id(n),IntLiteral(1))])))])]),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallExpr(Id(fact),[Id(x)])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test24(self):
        input = r"""
        Var: ajsd_123s = "Khang", u___12sA[2] = {  "Hoang" ,    "Gia"     };
        Var: a, b, c = 3.e3;
        Var: nothing;
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact(n - 1);
                EndIf.
            EndBody.
        **Test comment!!!**
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody."""
        expect = "Program([VarDecl(Id(ajsd_123s),StringLiteral(Khang)),VarDecl(Id(u___12sA),[IntLiteral(2)],ArrayLiteral(StringLiteral(Hoang),StringLiteral(Gia))),VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c),FloatLiteral(3.e3)),VarDecl(Id(nothing)),FuncDecl(Id(fact)[VarDecl(Id(n))],([][If(BinaryOp(==,Id(n),IntLiteral(0)),[],[Return(IntLiteral(1))])Else([],[Return(BinaryOp(*,Id(n),CallExpr(Id(fact),[BinaryOp(-,Id(n),IntLiteral(1))])))])]),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallExpr(Id(fact),[Id(x)])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test25(self):
        input = r"""
        Function: foo
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While (i < 5) Do
                    a[i] = b +. 1.0;
                    i = i + 1;
                EndWhile.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody."""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[IntLiteral(5)]),VarDecl(Id(b))],([VarDecl(Id(i),IntLiteral(0))][While(BinaryOp(<,Id(i),IntLiteral(5)),[],[Assign(ArrayCell(Id(a),[Id(i)]),BinaryOp(+.,Id(b),FloatLiteral(1.0))),Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])]),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallExpr(Id(fact),[Id(x)])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test26_for_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[5], b
            Body:
                For (i = 0, i < 10, 2) Do
                    writeln(a[i] + b);
                EndFor.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody."""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[IntLiteral(5)]),VarDecl(Id(b))],([][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[CallExpr(Id(writeln),[BinaryOp(+,ArrayCell(Id(a),[Id(i)]),Id(b))])])]),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallExpr(Id(fact),[Id(x)])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test27_assign_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[5], b
            Body:
                For (i = 0, i < 10, 2) Do
                    a[i] = b;
                EndFor.
            EndBody."""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[IntLiteral(5)]),VarDecl(Id(b))],([][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[Assign(ArrayCell(Id(a),[Id(i)]),Id(b))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test28_if_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[2], b
            Body:
                For (i = 0, i < 2, 1) Do
                    If a[i] > b Then writeln(a[i], " is larger than ", b);
                    ElseIf a[i] == b Then writeln(a[i], " equal ", b);
                    Else writeln(a[i], " is smaller than ", b);
                    EndIf.
                EndFor.
            EndBody."""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[IntLiteral(2)]),VarDecl(Id(b))],([][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(2)),IntLiteral(1),[],[If(BinaryOp(>,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( is larger than ),Id(b)])])ElseIf(BinaryOp(==,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( equal ),Id(b)])])Else([],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)]),StringLiteral( is smaller than ),Id(b)])])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test29_while_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[2], b
            Body:
                Var: i = 0;
                While (a[i] > b) Do
                    writeln(a[i]);
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[IntLiteral(2)]),VarDecl(Id(b))],([VarDecl(Id(i),IntLiteral(0))][While(BinaryOp(>,ArrayCell(Id(a),[Id(i)]),Id(b)),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)])]),Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test30_do_while_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[2], b
            Body:
                Var: i = 0;
                Do 
                    a[i] = a[i] +. 1.;
                While (a[i] > b) EndDo.
            EndBody."""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[IntLiteral(2)]),VarDecl(Id(b))],([VarDecl(Id(i),IntLiteral(0))][Dowhile([],[Assign(ArrayCell(Id(a),[Id(i)]),BinaryOp(+.,ArrayCell(Id(a),[Id(i)]),FloatLiteral(1.)))],BinaryOp(>,ArrayCell(Id(a),[Id(i)]),Id(b)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test31_break_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[10]
            Body:
                Var: i;
                For (i = 0, i < 10, 1) Do
                    writeln(a[i]);
                    If (a[10] > 5) Then
                        Break;
                    EndIf.
                EndFor.
            EndBody."""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[IntLiteral(10)])],([VarDecl(Id(i))][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(1),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)])]),If(BinaryOp(>,ArrayCell(Id(a),[IntLiteral(10)]),IntLiteral(5)),[],[Break()])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test32_continue_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[10]
            Body:
                Var: i;
                For (i = 0, i < 10, 1) Do
                    writeln(a[i]);
                    If (a[10] > 5) Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody."""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[IntLiteral(10)])],([VarDecl(Id(i))][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(1),[],[CallExpr(Id(writeln),[ArrayCell(Id(a),[Id(i)])]),If(BinaryOp(>,ArrayCell(Id(a),[IntLiteral(10)]),IntLiteral(5)),[],[Continue()])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test33_call_stmt(self):
        input = r"""
        Function: foo
            Parameter: x, y
            Body:
                writeln(foo(2 + x, 4. \. y) * goo());
            EndBody."""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(x)),VarDecl(Id(y))],([][CallExpr(Id(writeln),[BinaryOp(*,CallExpr(Id(foo),[BinaryOp(+,IntLiteral(2),Id(x)),BinaryOp(\.,FloatLiteral(4.),Id(y))]),CallExpr(Id(goo),[]))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    # def test34(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,334))
    # def test35(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))
    # def test36(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,336))
    # def test37(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,337))
    # def test38(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,338))
    # def test39(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,339))
    # def test40(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,340))
    # def test41(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,341))
    # def test42(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,342))
    # def test43(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,343))
    # def test44(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,344))
    # def test45(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,345))
    # def test46(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,346))
    # def test47(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,347))
    # def test48(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,348))
    # def test49(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,349))
    # def test50(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,350))
    # def test51(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,351))
    # def test52(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,352))
    # def test53(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,353))
    # def test54(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,354))
    # def test55(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,355))
    # def test56(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,356))
    # def test57(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,357))
    # def test58(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,358))
    # def test59(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,359))
    # def test60(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,360))
    # def test61(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,361))
    # def test62(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,362))
    # def test63(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,363))
    # def test64(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,364))
    # def test65(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,365))
    # def test66(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,366))
    # def test67(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,367))
    # def test68(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,368))
    # def test69(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,369))
    # def test70(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,370))
    # def test71(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,371))
    # def test72(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,372))
    # def test73(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,373))
    # def test74(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,374))
    # def test75(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,375))
    # def test76(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,376))
    # def test77(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,377))
    # def test78(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,378))
    # def test79(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,379))
    # def test80(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,380))
    # def test81(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,381))
    # def test82(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,382))
    # def test83(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,383))
    # def test84(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,384))
    # def test85(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,385))
    # def test86(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,386))
    # def test87(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,387))
    # def test88(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,388))
    # def test89(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,389))
    # def test90(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,390))
    # def test91(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,391))
    # def test92(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,392))
    # def test93(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,393))
    # def test94(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,394))
    # def test95(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,395))
    # def test96(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,396))
    # def test97(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,397))
    # def test98(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,398))
    # def test99(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,399))
    # def test400(self):
    #     input
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,400))
        