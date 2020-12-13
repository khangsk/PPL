import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallStmt(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_vardecl1(self):
        input = """Var: x = 5;
                    Var: x = 7;"""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_vardecl2(self):
        input = """Var: x[2][2] = {{1,2}, {3,4}, {1,2,{4}}};
                    Var: x = 7;"""
        expect = str(InvalidArrayLiteral(ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(4)])])))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_vardecl3(self):
        input = """Var: x = 4;
                Function: main
                Body:
                    Var: y;
                    y = x;
                    y = 5.6;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("y"),FloatLiteral(5.6))))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_array_cell1(self):
        input = """Var: x[1];
                Function: main
                Body:
                    x[0] = 2;
                    x[0] = 3.4;
                    Return x;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(0)]),FloatLiteral(3.4))))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_array_cell2(self):
        input = """Var: x[4] = {1, 2, 3 ,4};
                Function: main
                Body:
                    Var: z;
                    Var: m[4] = {1,2,3,4};
                    z = x[3];
                    m = foo();
                    Return x;
                EndBody.
                Function: foo
                Body:
                    Var: x;
                    x = main()[3];
                    Return {1,3,5};
                EndBody."""
        expect = str(TypeMismatchInStatement(Return(ArrayLiteral([IntLiteral(1),IntLiteral(3),IntLiteral(5)]))))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_array(self):
        input = """Function: main
                Body:
                    Var: x[4] = {2,3,4,5};
                    Var: y[4];
                    Var: z[4];
                    Var: t[4];
                    y = x;
                    x = y;
                    z = t;
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("z"),Id("t"))))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclared1(self):
        input = """Var: x[4] = {1, 2, 3, 4};
                Function: main
                Body:
                    Var: x = 5;
                    Var: x = 6;
                EndBody."""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_redeclared2(self):
        input = """Var: x[4] = {1, 2, 3, 4};
                Function: main
                Parameter: x
                Body:
                    Var: x = 5;
                EndBody."""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_redeclared3(self):
        input = """Var: x[4] = {1, 2, 3, 4};
                Function: main
                Parameter: x, y, z, x[5]
                Body:
                EndBody."""
        expect = str(Redeclared(Parameter(), "x"))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_redeclared4(self):
        input = """Var: main = 7;
                Function: main
                Parameter: x, y, z, main
                Body:
                EndBody."""
        expect = str(Redeclared(Function(), "main"))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_redeclared5(self):
        input = """
                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                EndBody.
                Function: foo
                Body:
                EndBody."""
        expect = str(Redeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_redeclared6(self):
        input = """
                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                    Var: x = 5;
                    Var: y = 6;
                    Var: z = True;
                    If z Then 
                        Var: z = 0;
                        Var: t = 7;
                        z = 5;
                        t = 6;
                    Else
                        Var: z = 1;
                        Var: t = 9;
                        Var: t = 6;
                        z = 6;
                        t = 7;
                    EndIf.
                EndBody."""
        expect = str(Redeclared(Variable(), "t"))
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_redeclared7(self):
        input = """
                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                    Var: x = 4;
                    For (x = 5, x < 100, 12) Do
                        Var: x = 6;
                        Var: x = 7;
                    EndFor.
                EndBody."""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_redeclared8(self):
        input = """
                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                    Var: x = 4;
                    While (x > 0) Do
                        Var: x = 7;
                        x = x - 1;
                    EndWhile.
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_redeclared9(self):
        input = """
                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                    Var: x = 4;
                    While (x > 0) Do
                        Var: x = 7;
                        Var: x = 9;
                        x = x - 1;
                    EndWhile.
                EndBody."""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_redeclared10(self):
        input = """
                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                    Var: x = 4;
                    Do
                        Var: x = 5;
                        x = x + 1;
                    While x > 2 EndDo.
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_redeclared11(self):
        input = """
                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                    Var: x = 4;
                    Do
                        Var: x = 5;
                        Var: x = 7;
                        x = x + 1;
                    While x > 2 EndDo.
                EndBody."""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_redeclared12(self):
        input = """
                Function: main
                Body:
                    print();
                EndBody.
                Function: read
                Body:
                EndBody."""
        expect = str(Redeclared(Function(), "read"))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_redeclared13(self):
        input = """
                Function: main
                Parameter: x, y, z[4][4]
                Body:
                    Var: s;
                    Var: x = 5;
                EndBody."""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_undeclared_function1(self):
        input = """
                Function: main
                Parameter: x, y, z[4][4]
                Body:
                    Var: s;
                    foo();
                EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_undeclared_function2(self):
        input = """
                Function: main
                Parameter: x, y, z[4][4]
                Body:
                    Var: s;
                    x();
                EndBody."""
        expect = str(Undeclared(Function(), "x"))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_undeclared_function3(self):
        input = """
                Function: main
                Parameter: x, y, z[4][4]
                Body:
                    Var: s;
                    z();
                EndBody."""
        expect = str(Undeclared(Function(), "z"))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_undeclared_function4(self):
        input = """
                Function: main
                Parameter: x, y, z[4][4]
                Body:
                    Var: s, t, m;
                    s = read();
                    t = 5;
                    t = int_of_float(5.6);
                    m = 5.7;
                    m = float_to_int(t);
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,428))
    
    def test_undeclared_function5(self):
        input = """
                Function: main
                Parameter: x, y, z[4][4]
                Body:
                    Var: s, t, m;
                    x = t + m + (t * s \\ (m - s + foo()) * 4);
                EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_undeclared_function6(self):
        input = """
                Function: main
                Parameter: x, y, z[4][4]
                Body:
                    Var: s, t, m;
                    x = t + m + (t * s \\ (m - s + foo()) * 4);
                EndBody.
                Function: foo
                Body:
                    Return 1;
                EndBody."""
                
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_undeclared_function7(self):
        input = """
                Function: main
                Parameter: x, y, z[4][4], foo
                Body:
                    Var: s, t, m;
                    x = t + m + (t * s \\ (m - s + foo()) * 4);
                EndBody.
                Function: foo
                Body:
                    Return 1;
                EndBody."""
                
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_undeclared_function8(self):
        input = """
                Function: main
                Parameter: x, y, z[4][4], foo[5][6]
                Body:
                    Var: s, t, m;
                    x = t + m + (t * s \\ (m - s + foo()) * 4);
                EndBody.
                Function: foo
                Body:
                    Return 1;
                EndBody."""
                
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_undeclared_function9(self):
        input = """
                Function: main
                Parameter: x, y
                Body:
                    Var: foo = 5;
                    foo();
                EndBody.
                Function: foo
                Body:
                EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_undeclared_identifier1(self):
        input = """
                Function: main
                Parameter: x, y
                Body:
                    foo();
                    foo = 1;
                EndBody.
                Function: foo
                Body:
                EndBody."""
        expect = str(Undeclared(Identifier(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_undeclared_identifier2(self):
        input = """
                Function: main
                Parameter: x, y
                Body:
                    foo();
                    foo = {{1}, {2}};
                EndBody.
                Function: foo
                Body:
                EndBody."""
        expect = str(Undeclared(Identifier(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_undeclared_identifier3(self):
        input = """
                Function: main
                Parameter: x, y
                Body:
                    foo();
                    x = x + (y + (1 + foo) + 3);
                EndBody.
                Function: foo
                Body:
                EndBody."""
        expect = str(Undeclared(Identifier(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_undeclared_identifier4(self):
        input = """
                Function: main
                Body:
                    Var: x;
                    x = foo(1, 2) + 2;
                    x = foo(1, z);
                EndBody.
                Function: foo
                Parameter: x, y
                Body:
                EndBody."""
        expect = str(Undeclared(Identifier(), "z"))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_undeclared_identifier5(self):
        input = """
                Function: main
                Body:
                    Var: x[5][6];
                    x[4][4] = 6;
                    x[z][3] = 7;
                EndBody."""
        expect = str(Undeclared(Identifier(), "z"))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_undeclared_identifier6(self):
        input = """
                Function: main
                Body:
                    Var: x[5][6];
                    x[4][4] = 6;
                    x[main][3] = 7;
                EndBody."""
        expect = str(Undeclared(Identifier(), "main"))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_undeclared_identifier7(self):
        input = """
                Function: main
                Body:
                    Var: x;
                    x = foo(1, 2) + 2;
                    x = foo(1, main);
                EndBody.
                Function: foo
                Parameter: x, y
                Body:
                EndBody."""
        expect = str(Undeclared(Identifier(), "main"))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_type_cannot_be_inferred1(self):
        input = """
                Function: main
                Body:
                    Var: x, y;
                    x = y;
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_type_cannot_be_inferred2(self):
        input = """
                Function: main
                Body:
                    Var: x[5][6], y;
                    x[1][2] = 5.6;
                    y = 5.7;
                    x[1][4] = y;
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_type_cannot_be_inferred3(self):
        input = """
                Function: main
                Body:
                    Var: x[5][6], y;
                    x[1][4] = y;
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id("x"),[IntLiteral(1),IntLiteral(4)]),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_type_cannot_be_inferred4(self):
        input = """
                Var: z[5][7];
                Function: main
                Body:
                    Var: x[5][6], y;
                    x[1][4] = z[1][2];
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id("x"),[IntLiteral(1),IntLiteral(4)]),ArrayCell(Id("z"),[IntLiteral(1),IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_type_cannot_be_inferred5(self):
        input = """
                Var: z[5][7];
                Function: main
                Body:
                    Var: x[5][6][7][8];
                    x[3][0][1][1] = 1;
                    x[1][4][1][1] = z[1][2];
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_type_cannot_be_inferred6(self):
        input = """
                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_type_cannot_be_inferred7(self):
        input = """
                Function: main
                Body:
                    Var: x;
                    foo(x);
                EndBody.
                Function: foo
                Parameter: x
                Body:
                EndBody."""
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_type_cannot_be_inferred8(self):
        input = """
                Function: main
                Body:
                    Var: x[5][6];
                    foo(x[3][2]);
                EndBody.
                Function: foo
                Parameter: x
                Body:
                EndBody."""
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[ArrayCell(Id("x"),[IntLiteral(3),IntLiteral(2)])])))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_type_cannot_be_inferred9(self):
        input = """
                Function: foo
                Parameter: x[5][6]
                Body:
                EndBody.
                Function: main
                Body:
                    Var: x[5][6];
                    foo(x);
                EndBody."""
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_type_cannot_be_inferred10(self):
        input = """
                Function: foo
                Parameter: x[5][6]
                Body:
                EndBody.
                Function: main
                Body:
                    Var: x[5][6];
                    x[0][0] = "abcd";
                    foo(x);
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_type_cannot_be_inferred11(self):
        input = """
                Function: foo
                Parameter: x[2][1]
                Body:
                EndBody.
                Function: main
                Body:
                    Var: x[2][1];
                    foo({{0}, {2}});
                    foo(x);
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test_type_cannot_be_inferred12(self):
        input = """
                Function: main
                Body:
                    Var: x[2][1];
                    x = foo();
                EndBody.
                Function: foo
                Body:
                    Return {{1}, {2}};
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_type_cannot_be_inferred13(self):
        input = """
                Function: main
                Body:
                    Var: x;
                    x = foo();
                EndBody.
                Function: foo
                Body:
                    Return 1;
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test_type_cannot_be_inferred14(self):
        input = """
                Function: foo
                Body:
                    Return {{1}, {2}};
                EndBody.
                Function: main
                Body:
                    Var: x[2][1];
                    x = foo();
                EndBody.
                """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_type_cannot_be_inferred15(self):
        input = """
                Function: foo
                Body:
                    Return {{1}, {2}};
                EndBody.
                Function: main
                Body:
                    Var: x;
                    x = foo()[1][0];
                EndBody.
                """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_type_cannot_be_inferred16(self):
        input = """
                Function: main
                Body:
                    Var: x;
                    x = foo()[0][1];
                EndBody.
                Function: foo
                Body:
                    Return {{1}, {2}};
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"),ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(0),IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_type_cannot_be_inferred17(self):
        input = """
                Function: main
                Body:
                    Var: x;
                    x = foo()[0][1] + 1;
                EndBody.
                Function: foo
                Body:
                    Return {{1}, {2}};
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"),BinaryOp("+",ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(0),IntLiteral(1)]),IntLiteral(1)))))
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_type_cannot_be_inferred18(self):
        input = """
                Function: main
                Body:
                    Var: x[2][1] = {{4}, {3}}, y;
                    x = foo();
                    y = foo()[0][0] + 1;
                EndBody.
                Function: foo
                Body:
                    Return {{1}, {2}};
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_type_cannot_be_inferred19(self):
        input = """
                Function: foo
                Parameter: x, y
                Body:
                    x = 4;
                    Return 5;
                EndBody.
                Function: main
                Body:
                    Var: x, y;
                    x = foo(x,y) + 1;
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"),BinaryOp("+",CallExpr(Id("foo"),[Id("x"),Id("y")]),IntLiteral(1)))))
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_type_cannot_be_inferred20(self):
        input = """
                Function: main
                Body:
                    Var: x[2][2], y[2][2];
                    x = y;
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_type_cannot_be_inferred21(self):
        input = """
                Function: main
                Body:
                    Var: x[2][2], y[2][2] = {{1,2}, {3,4}};
                    x = y;
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_type_cannot_be_inferred22(self):
        input = """
                Function: main
                Body:
                    Var: x;
                    Return x;
                EndBody."""
        expect = str(TypeCannotBeInferred(Return(Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_type_cannot_be_inferred23(self):
        input = """
                Function: main
                Body:
                    Var: x[5][6];
                    Return x;
                EndBody."""
        expect = str(TypeCannotBeInferred(Return(Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_type_cannot_be_inferred24(self):
        input = """
                Function: main
                Parameter: a[3]
                Body:
                    a = main({1,2,5});
                    Return a;
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("main"),[ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(5)])]))))
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_type_cannot_be_inferred25(self):
        input = """
                Function: main
                Parameter: a[1], y[1]
                Body:
                    Var: x;
                    y[0] = 1;
                    a[foo(x)] = y[x];
                EndBody.
                Function: foo
                Parameter: m
                Body:
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id("a"),[CallExpr(Id("foo"),[Id("x")])]),ArrayCell(Id("y"),[Id("x")]))))
        self.assertTrue(TestChecker.test(input,expect,515))

    def test_type_mismatch_in_statement1(self):
        input = """
                Var: x = 4;
                Function: main
                Body:
                    x = 5.5;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(5.5))))
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_type_mismatch_in_statement2(self):
        input = """
                Var: x = True;
                Function: main
                Body:
                    x = "abcd";
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),StringLiteral("abcd"))))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_type_mismatch_in_statement3(self):
        input = """
                Var: x = True;
                Function: main
                Body:
                    x = {True};
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),ArrayLiteral([BooleanLiteral(True)]))))
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_type_mismatch_in_statement4(self):
        input = """
                Var: x[2][1];
                Function: main
                Body:
                    x = 1;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_type_mismatch_in_statement5(self):
        input = """
                Var: x[2][1];
                Function: main
                Body:
                    x = {{1}};
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),ArrayLiteral([ArrayLiteral([IntLiteral(1)])]))))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_type_mismatch_in_statement6(self):
        input = """
                Var: x[2][1], y;
                Function: main
                Body:
                    x = {{1}, {2}};
                    y = {1, 2, 3};
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("y"),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))))
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_type_mismatch_in_statement7(self):
        input = """
                Var: x[2][1], y[3][1];
                Function: main
                Body:
                    x = {{1}, {2}};
                    y = x;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("y"),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_type_mismatch_in_statement8(self):
        input = """
                Var: x[2][1];
                Function: main
                Body:
                    Var: y = 1.5;
                    x = {{1}, {2}};
                    y = x[0][0];
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("y"),ArrayCell(Id("x"),[IntLiteral(0),IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(input,expect,469))
    
    def test_type_mismatch_in_statement9(self):
        input = """
                Var: x[2][1];
                Function: main
                Body:
                    Var: y[2][1];
                    x = {{1}, {2}};
                    y = x;
                    y[0][0] = 1.5;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("y"),[IntLiteral(0),IntLiteral(0)]),FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_type_mismatch_in_statement10(self):
        input = """
                Var: x[2][1];
                Function: main
                Body:
                    Var: y[2][1];
                    x = {{1}, {2}};
                    y = x[0][0];
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("y"),ArrayCell(Id("x"),[IntLiteral(0),IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_type_mismatch_in_statement11(self):
        input = """
                Var: x[2][1];
                Function: main
                Body:
                    Var: y[2][1];
                    x = {{1}, {2}};
                    x[0][0] = y;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(0),IntLiteral(0)]),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_type_mismatch_in_statement12(self):
        input = """
                Var: x[2][1] = {{True}, {False}};
                Function: main
                Body:
                    x = {{1}, {2}};
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])]))))
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_type_mismatch_in_statement13(self):
        input = """
                Function: main
                Body:
                    Var: x;
                    x = foo() + 1;
                    foo();
                EndBody.
                Function: foo
                Body:
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[])))
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_type_mismatch_in_statement14(self):
        input = """
                Function: foo
                Body:
                    Return {{1}, {2}};
                EndBody.
                Function: main
                Body:
                    Var: x = 1.5;
                    x = foo()[0][0];
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(0),IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_type_mismatch_in_statement15(self):
        input = """
                Function: foo
                Body:
                    Return {{1}, {2}};
                EndBody.
                Function: main
                Body:
                    Var: x = True;
                    foo()[0][0] = x;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(0),IntLiteral(0)]),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_type_mismatch_in_statement16(self):
        input = """
                Function: main
                Body:
                    Var: x, y[2][1] = {{2.3}, {4e1}};
                    x = foo() + 1;
                    y = foo();
                EndBody.
                Function: foo
                Body:
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("y"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_type_mismatch_in_statement17(self):
        input = """
                Function: main
                Body:
                    Var: x = True;
                    foo(4, 5);
                    foo(x, 4);
                EndBody.
                Function: foo
                Parameter: x, y
                Body:
                EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x"),IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_type_mismatch_in_statement18(self):
        input = """
                Function: main
                Body:
                    foo({1}, 5);
                EndBody.
                Function: foo
                Parameter: x, y
                Body:
                EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[ArrayLiteral([IntLiteral(1)]),IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_type_mismatch_in_statement19(self):
        input = """
                Function: main
                Body:
                    foo({1}, 5);
                EndBody.
                Function: foo
                Parameter: x[1], y
                Body:
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_type_mismatch_in_statement20(self):
        input = """
                Function: main
                Body:
                    foo(1, 5);
                EndBody.
                Function: foo
                Parameter: x[1], y
                Body:
                EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[IntLiteral(1),IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_type_mismatch_in_statement21(self):
        input = """
                Function: main
                Body:
                    Var: x[2][1];
                    If x[0][0] Then
                    ElseIf x[0][0] Then
                    Else
                    EndIf.
                    x[0][0] = 1;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(0),IntLiteral(0)]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_type_mismatch_in_statement22(self):
        input = """
                Function: main
                Body:
                    Var: x[2][1];
                    If main() Then
                    ElseIf main() Then
                    Else
                    EndIf.
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_type_mismatch_in_statement23(self):
        input = """
                Function: main
                Body:
                    Var: x[2][1], y = 5.5;
                    For (y = x[1][0], foo(), 1) Do
                        y = y + 1;
                    EndFor.
                EndBody.
                Function: foo
                Body:
                    Return True;
                EndBody."""
        expect = str(TypeMismatchInStatement(For(Id("y"),ArrayCell(Id("x"),[IntLiteral(1),IntLiteral(0)]),CallExpr(Id("foo"),[]),IntLiteral(1),([],[Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(1)))]))))
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_type_mismatch_in_statement24(self):
        input = """
                Function: main
                Body:
                    While foo() Do
                    Var: y = 1;
                        While y Do 
                            Return;
                        EndWhile.
                    EndWhile.
                EndBody.
                Function: foo
                Body:
                    Return True;
                EndBody."""
        expect = str(TypeMismatchInStatement(While(Id("y"),([],[Return(None)]))))
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_type_mismatch_in_statement25(self):
        input = """
                Function: main
                Body:
                    Var: x;
                    Do
                        x = x + 1;
                    While x > 100
                    EndDo.
                    Do
                    While x
                    EndDo.
                EndBody."""
        expect = str(TypeMismatchInStatement(Dowhile(([],[]),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_type_mismatch_in_statement26(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    If x > 5 Then Return 1;
                    ElseIf x > 6 Then Return 2.2;
                    Else Return True;
                    EndIf.
                EndBody."""
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(2.2))))
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_type_mismatch_in_statement27(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    If x > 5 Then Return;
                    ElseIf x > 6 Then Return 1;
                    Else Return True;
                    EndIf.
                EndBody."""
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_type_mismatch_in_statement28(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    If x > 5 Then Return 1;
                    ElseIf x > 6 Then Return;
                    Else Return True;
                    EndIf.
                EndBody."""
        expect = str(TypeMismatchInStatement(Return(None)))
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_type_mismatch_in_statement29(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    printLn();
                    x = printLn();
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("printLn"),[]))))
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_type_mismatch_in_statement30(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    print(x);
                    main(1);
                EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_type_mismatch_in_expression1(self):
        input = """
                Function: main
                Parameter: x, y
                Body:
                    x = x +. 1;
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_type_mismatch_in_expression2(self):
        input = """
                Function: main
                Parameter: x, y
                Body:
                    x = x + y + (x +. y);
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_type_mismatch_in_expression3(self):
        input = """
                Function: main
                Parameter: x, y
                Body:
                    x = x +. y + x;
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+",BinaryOp("+.",Id("x"),Id("y")),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_type_mismatch_in_expression4(self):
        input = """
                Function: main
                Parameter: x, y
                Body:
                    x = x +. (y + x);
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("y"),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_type_mismatch_in_expression5(self):
        input = """
                Function: main
                Parameter: x[2][2]
                Body:
                    x[1] = 0;
                EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_type_mismatch_in_expression6(self):
        input = """
                Function: main
                Parameter: x[2][2]
                Body:
                    x[1][2][3] = 0;
                EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_type_mismatch_in_expression7(self):
        input = """
                Function: main
                Parameter: x[2][2]
                Body:
                    x[foo()][foo()[1]] = 0;
                EndBody.
                Function: foo
                Body: 
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,501))

    def test_type_mismatch_in_expression8(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y[1];
                    y[main(main(True))] = 0;
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[BooleanLiteral(True)])))
        self.assertTrue(TestChecker.test(input,expect,502))

    def test_type_mismatch_in_expression9(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y[1][1];
                    y[main(main(1))][main(2)] = 0;
                    Return 1;
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,503))

    def test_type_mismatch_in_expression10(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y[1][1];
                    (y[0][0])[1] = 0;
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(ArrayCell(Id("y"),[IntLiteral(0),IntLiteral(0)]),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,504))

    def test_type_mismatch_in_expression11(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    (1 + 1)[1] = 0;
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(BinaryOp("+",IntLiteral(1),IntLiteral(1)),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,505))

    def test_type_mismatch_in_expression12(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    ({1})[0] = 0;
                    Return 1;
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,506))

    def test_type_mismatch_in_expression12(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    ({{1}, {2}})[0] = 0;
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])]),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,507))

    def test_type_mismatch_in_expression13(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    ({{1}, {2}})[0][0][0] = 0;
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])]),[IntLiteral(0),IntLiteral(0),IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,508))

    def test_type_mismatch_in_expression14(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    x = ({{1}, {2}})[0][0] || False;
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("||",ArrayCell(ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])]),[IntLiteral(0),IntLiteral(0)]),BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input,expect,509))

    def test_type_mismatch_in_expression15(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    x = ({{1}, {2}})[0 + 0 * 0 \\ 0][0];
                    Return 1;
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,510))

    def test_type_mismatch_in_expression16(self):
        input = """
                Function: main
                Parameter: x[1]
                Body:
                    x[x[x[x[0]]]] = 1;
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,511))

    def test_type_mismatch_in_expression17(self):
        input = """
                Function: main
                Parameter: x[1]
                Body:
                    x[x[x[x[0]]]] = True;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[ArrayCell(Id("x"),[ArrayCell(Id("x"),[ArrayCell(Id("x"),[IntLiteral(0)])])])]),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,512))

    def test_type_mismatch_in_expression18(self):
        input = """
                Function: main
                Parameter: x[1]
                Body:
                    Var: y = True;
                    y = x[x[x[x[0]]]];
                EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"),[ArrayCell(Id("x"),[ArrayCell(Id("x"),[ArrayCell(Id("x"),[IntLiteral(0)])])])])))
        self.assertTrue(TestChecker.test(input,expect,513))

    def test_type_mismatch_in_expression19(self):
        input = """
                Function: main
                Parameter: x[1], y[1]
                Body:
                    x[y[0]] = y[0];
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,514))

    def test_type_mismatch_in_expression20(self):
        input = """
                Function: main
                Parameter: x[1], y[1]
                Body:
                    x[0] = 1 + y[y[y[0]]];
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,515))

    def test_type_mismatch_in_expression21(self):
        input = """
                Function: main
                Parameter: x[1], y[1]
                Body:
                    If foo(foo(foo(1))) Then Return 1;
                    Else Return 2;
                    EndIf.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,516))

    def test_type_mismatch_in_expression22(self):
        input = """
                Function: foo
                Parameter: a, b, c
                Body:
                    c = "abc";
                EndBody.
                Function: main
                Parameter: x, y, z
                Body:
                    x = 1;
                    y = 1.1;
                    foo(x, y, z);
                    Return True;
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,517))

    def test_type_mismatch_in_expression23(self):
        input = """Function: main
                Body:
                    Var: x = 1;
                    x = foo(1,2);
                EndBody.
                Function: foo
                Parameter: x, y, z
                Body:
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,518))

    def test_type_mismatch_in_expression24(self):
        input = """Function: main
                Body:
                    Var: x = 1;
                    x = foo(1, 2, 3, 4);
                EndBody.
                Function: foo
                Parameter: x, y, z
                Body:
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,519))

    def test_type_mismatch_in_expression25(self):
        input = """Function: main
                Body:
                    Var: x, y, z;
                    x = -y;
                    z = 1.1;
                    z = x;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("z"),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect, 520))
    
    def test_type_mismatch_in_expression26(self):
        input = """Function: main
                Body:
                    Var: x, y, z;
                    x = -.y;
                    z = 1;
                    z = x;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("z"),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect, 521))

    def test_type_mismatch_in_expression27(self):
        input = """Function: main
                Body:
                    If foo(foo(foo(1))) Then
                    EndIf.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    Return True;
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect, 522))

    def test_type_mismatch_in_expression28(self):
        input = """Function: main
                Body:
                    Var: x[1];
                    x[foo(foo(foo(1)))] = 0;
                    x[foo(True)] = 1;
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[BooleanLiteral(True)])))
        self.assertTrue(TestChecker.test(input,expect, 523))

    def test_type_mismatch_in_expression29(self):
        input = """Function: main
                Body:
                    Var: x[1];
                    x[foo(foo(foo(1) + 1) + 1) + 1] = 0;
                    x[foo(1)] = 1;
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    Return 1;
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 524))

    def test_type_mismatch_in_expression30(self):
        input = """Function: main
                Body:
                    While foo(foo(foo(1))) Do
                    EndWhile.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    Return True;
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect, 525))

    def test_type_mismatch_in_expression31(self):
        input = """Function: main
                Body:
                    Do
                    While foo(foo(foo(1))) EndDo.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    Return True;
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect, 526))

    def test_type_mismatch_in_expression32(self):
        input = """Function: main
                Body:
                    Var: i;
                    For (i = 0, foo(foo(foo(1))), 1) Do
                    EndFor.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    Return True;
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect, 527))

    def test_type_mismatch_in_expression33(self):
        input = """Function: main
                Body:
                    Var: i;
                    For (i = 0, i < 100, foo(foo(foo(True)))) Do
                    EndFor.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    Return 1;
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[BooleanLiteral(True)])))
        self.assertTrue(TestChecker.test(input,expect, 528))

    def test_type_cannot_be_inferred27(self):
        input = """Function: main
                Body:
                    Var: i[1];
                    i[i[0]] = i[0];
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 529))

    def test_type_cannot_be_inferred28(self):
        input = """Function: main
                Body:
                    Var: i[1];
                    i[0] = i[i[0]];
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id("i"),[IntLiteral(0)]),ArrayCell(Id("i"),[ArrayCell(Id("i"),[IntLiteral(0)])]))))
        self.assertTrue(TestChecker.test(input,expect, 535))

    def test_type_cannot_be_inferred29(self):
        input = """Function: main
                Body:
                    Var: x[1], y[1], z;
                    z = 1 + foo({1});
                    x[foo(x)] = y[0];
                EndBody.
                Function: foo
                Parameter: x[1]
                Body:
                    Return 1;
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 530))
    
    def test_type_cannot_be_inferred30(self):
        input = """Function: main
                Body:
                    Var: x[1], y[1], z;
                    z = 1 + foo({1});
                    y[0] = x[foo(x)];
                EndBody.
                Function: foo
                Parameter: x[1]
                Body:
                    Return 1;
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id("y"),[IntLiteral(0)]),ArrayCell(Id("x"),[CallExpr(Id("foo"),[Id("x")])])))    )
        self.assertTrue(TestChecker.test(input,expect, 531))

    def test_type_cannot_be_inferred31(self):
        input = """Function: main
                Body:
                    Var: x[1], y[1];
                    x[x[0]] = y[0];
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 532))

    def test_type_cannot_be_inferred32(self):
        input = """Function: main
                Body:
                    Var: x[1], y[1];
                    x[0] = y[y[0]];
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id("x"),[IntLiteral(0)]),ArrayCell(Id("y"),[ArrayCell(Id("y"),[IntLiteral(0)])]))))
        self.assertTrue(TestChecker.test(input,expect, 534))

    def test_type_cannot_be_inferred26(self):
        input = """Function: main
                Body:
                    Var: x;
                    x = foo(foo(1) + 1);
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    Return x;
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"),CallExpr(Id("foo"),[BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(1)]),IntLiteral(1))]))))
        self.assertTrue(TestChecker.test(input,expect, 533))
###################################################################

    def test_no_entry_point1(self):
        input = """"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect, 536))

    def test_no_entry_point2(self):
        input = """
                Var: main = 1;"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect, 537))

    def test_no_entry_point3(self):
        input = """
                Var: main = 1;
                Function: maIn
                Body:
                EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect, 538))

    def test_no_entry_point4(self):
        input = """
                Var: main = 1;
                Function: maIn
                Body:
                    Var: main = 2;
                EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect, 539))

    def test_not_in_loop1(self):
        input = """
                Function: main
                Body:
                    Break;
                EndBody."""
        expect = str(NotInLoop(Break()))
        self.assertTrue(TestChecker.test(input,expect, 540))
    
    def test_not_in_loop2(self):
        input = """
                Function: main
                Body:
                    Continue;
                EndBody."""
        expect = str(NotInLoop(Continue()))
        self.assertTrue(TestChecker.test(input,expect, 541))

    def test_not_in_loop3(self):
        input = """
                Function: main
                Body:
                    Var: i;
                    If i > 0 Then
                        Break;
                    EndIf.
                EndBody."""
        expect = str(NotInLoop(Break()))
        self.assertTrue(TestChecker.test(input,expect, 542))

    def test_not_in_loop4(self):
        input = """
                Function: main
                Body:
                    Var: i;
                    For (i = 0, i < 100, 1) Do
                        Break;
                    EndFor.
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 543))

    def test_not_in_loop5(self):
        input = """
                Function: main
                Body:
                    Var: i;
                    For (i = 0, i < 100, 1) Do
                    EndFor.
                    Continue;
                EndBody."""
        expect = str(NotInLoop(Continue()))
        self.assertTrue(TestChecker.test(input,expect, 544))

    def test_not_in_loop6(self):
        input = """
                Function: main
                Body:
                    Var: i;
                    For (i = 0, i < 100, 1) Do
                    EndFor.
                    While i > 1 Do
                    EndWhile.
                    Do 
                    While i > 1 EndDo.
                    Break;
                EndBody."""
        expect = str(NotInLoop(Break()))
        self.assertTrue(TestChecker.test(input,expect, 545))

    def test_not_in_loop7(self):
        input = """
                Function: main
                Body:
                    Var: i;
                    For (i = 0, i < 100, 1) Do
                        Continue;
                        While i > 1 Do
                            Do 
                                Continue;
                            While i > 1 EndDo.
                        Break;
                        EndWhile.
                    EndFor.
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 546))

    def test_not_in_loop8(self):
        input = """
                Function: main
                Body:
                    Var: i;
                    For (i = 0, i < 100, 1) Do
                        Continue;
                        While i > 1 Do
                            Do 
                                Continue;
                            While i > 1 EndDo.
                        Break;
                        EndWhile.
                    EndFor.
                    Continue;
                EndBody."""
        expect = str(NotInLoop(Continue()))
        self.assertTrue(TestChecker.test(input,expect, 547))

    def test_not_in_loop9(self):
        input = """
                Function: main
                Body:
                    Var: i;
                    For (i = 0, i < 100, 1) Do
                        Continue;
                        While i > 1 Do
                            Do 
                                Continue;
                            While i > 1 EndDo.
                        Break;
                        EndWhile.
                        While i > 2 Do
                        EndWhile.
                        Do
                            Continue;
                        While i > 2 EndDo.
                        While i > 2 Do
                        EndWhile.
                        Do
                        While i > 2 EndDo.
                        For (i = 0, i < 100, i) Do
                            Break; Continue;
                        EndFor.
                    EndFor.
                    For (i = 0, i < 100, i) Do
                        Continue; Continue;
                    EndFor.
                    While i > 2 Do
                        Break;
                        Break;
                        Continue;
                    EndWhile.
                    Do
                        Continue;
                    While i > 2 EndDo.
                EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 548))

    def test_not_in_loop10(self):
        input = """
                Function: main
                Body:
                    Var: i;
                    For (i = 0, i < 100, 1) Do
                        Continue;
                        While i > 1 Do
                            Do 
                                Continue;
                            While i > 1 EndDo.
                        Break;
                        EndWhile.
                        While i > 2 Do
                        EndWhile.
                        Do
                        While i > 2 EndDo.
                        While i > 2 Do
                        EndWhile.
                        Do
                        While i > 2 EndDo.
                        For (i = 0, i < 100, i) Do
                        EndFor.
                    EndFor.
                    For (i = 0, i < 100, i) Do
                    EndFor.
                    While i > 2 Do
                    EndWhile.
                    Do
                    While i > 2 EndDo.
                    Break;
                EndBody."""
        expect = str(NotInLoop(Break()))
        self.assertTrue(TestChecker.test(input,expect, 549))
    
    def test_invalid_array_literal1(self):
        input = """
        Function: main
        Body:
            Var: x[4] = {1,2,3, {4}};
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),ArrayLiteral([IntLiteral(4)])])))
        self.assertTrue(TestChecker.test(input,expect, 550))

    def test_invalid_array_literal2(self):
        input = """
        Function: main
        Body:
            Var: x[4] = {{1},{2},{3, {4}}, {4}};
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([IntLiteral(3),ArrayLiteral([IntLiteral(4)])])))
        self.assertTrue(TestChecker.test(input,expect, 551))

    def test_invalid_array_literal3(self):
        input = """
        Function: main
        Body:
            Var: x[4][2] = {{1, 2},{2, 1},{3, 1.5}, {4, 3}};
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([IntLiteral(3),FloatLiteral(1.5)])))
        self.assertTrue(TestChecker.test(input,expect, 552))

    def test_invalid_array_literal4(self):
        input = """
        Function: main
        Body:
            Var: x[4][2] = {{1, 2},{2.4, 1.5},{True, False}, {4, 3}};
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([FloatLiteral(2.4),FloatLiteral(1.5)]),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False)]),ArrayLiteral([IntLiteral(4),IntLiteral(3)])])))
        self.assertTrue(TestChecker.test(input,expect, 553))

    def test_invalid_array_literal5(self):
        input = """
        Function: main
        Body:
            Var: x[4][2][1] = {{{1}, {3}},{{2}, {1}},{{3}, {True}}, {{4}, {3}}};
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([ArrayLiteral([IntLiteral(3)]),ArrayLiteral([BooleanLiteral(True)])])))
        self.assertTrue(TestChecker.test(input,expect, 554))

    def test_invalid_array_literal6(self):
        input = """
        Function: main
        Body:
            Var: x[4][2][1] = {{{1}, {3}},{{2}, {1}},{{3}, {1}}, {{4}, {3}}};
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 555))

    def test_invalid_array_literal7(self):
        input = """
        Function: main
        Body:
            Var: x[0] = {};
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([])))
        self.assertTrue(TestChecker.test(input,expect, 556))

    def test_invalid_array_literal8(self):
        input = """
        Function: main
        Body:
            Var: x[2][0] = {{}, {}};
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([])))
        self.assertTrue(TestChecker.test(input,expect, 557))

    def test_function_not_return1(self):
        input = """
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 558))

    def test_function_not_return2(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i > 5 Then
                Return 1;
            EndIf.
        EndBody.
        """
        expect = str(FunctionNotReturn("main"))
        self.assertTrue(TestChecker.test(input,expect, 559))

    def test_function_not_return3(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i > 5 Then
                Return 1;
            Else
                Return 2;
            EndIf.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 560))

    def test_function_not_return4(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i > 5 Then
                Return 1;
            ElseIf i > 6 Then
                i = i + 1;
            Else
                Return 2;
            EndIf.
        EndBody.
        """
        expect = str(FunctionNotReturn("main"))
        self.assertTrue(TestChecker.test(input,expect, 561))

    def test_function_not_return5(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i > 5 Then
                Return;
            ElseIf i > 6 Then
                i = i + 1;
            EndIf.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 562))

    def test_function_not_return6(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i > 5 Then
                Return 1;
            ElseIf i > 6 Then
                i = i + 1;
            EndIf.
            Return 2;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 563))
    
    def test_function_not_return7(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i > 5 Then
                Return 1;
            ElseIf i > 6 Then
                i = i + 1;
            EndIf.
            If i > 2 Then
                Return 1;
            Else
                Return 2;
            EndIf.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 564))

    def test_function_not_return8(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i > 5 Then
                Return 3.7;
            ElseIf i > 6 Then
                i = i + 1;
            EndIf.
            For (i = 1, i < 100, i) Do
                Return 2.3;
            EndFor.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 565))

    def test_function_not_return9(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i > 5 Then
                Return 3.7;
            ElseIf i > 6 Then
                i = i + 1;
            EndIf.
            For (i = 1, i < 100, i) Do
            EndFor.
            i = i + 1;
        EndBody.
        """
        expect = str(FunctionNotReturn("main"))
        self.assertTrue(TestChecker.test(input,expect, 566))

    def test_function_not_return10(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i > 5 Then
                Return 3.7;
            ElseIf i > 6 Then
                If i > 6 Then
                    Return 7.8;
                Else
                    If i > 100 Then
                        Return 9.0;
                    ElseIf i > 1000 Then
                        Return 9.1;
                    Else
                        Return 9.2;
                    EndIf.
                EndIf.
            Else
                Return 1.1;
            EndIf.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 567))

    def test_function_not_return11(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i > 5 Then
                Return 3.7;
            ElseIf i > 6 Then
                If i > 6 Then
                    Return 7.8;
                Else
                    If i > 100 Then
                        Return 9.0;
                    ElseIf i > 1000 Then
                        Return 9.1;
                    EndIf.
                EndIf.
            Else
                Return 1.1;
            EndIf.
        EndBody.
        """
        expect = str(FunctionNotReturn("main"))
        self.assertTrue(TestChecker.test(input,expect, 568))

    def test_function_not_return12(self):
        input = """
        Function: main
        Body:
            Var: x;
            x = x + foo();
        EndBody.
        Function: foo
        Body:
        EndBody.
        """
        expect = str(FunctionNotReturn("foo"))
        self.assertTrue(TestChecker.test(input,expect, 574))

    def test_function_not_return13(self):
        input = """
        Function: foo
        Body:
        EndBody.
        Function: main
        Body:
            Var: x;
            x = x + foo();
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("x"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect, 575))

    def test_unreachable_function1(self):
        input = """
        Function: main
        Body:
        EndBody.
        Function: foo
        Body:
        EndBody.
        """
        expect = str(UnreachableFunction("foo"))
        self.assertTrue(TestChecker.test(input,expect, 569))

    def test_unreachable_function2(self):
        input = """
        Function: main
        Body:
        EndBody.
        Function: foo
        Body:
            foo();
        EndBody.
        """
        expect = str(UnreachableFunction("foo"))
        self.assertTrue(TestChecker.test(input,expect, 570))

    def test_unreachable_function3(self):
        input = """
        Function: main
        Body:
        EndBody.
        Function: foo1
        Body:
            foo();
        EndBody.
        Function: foo
        Body:
            foo1();
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 571))

    def test_unreachable_function4(self):
        input = """
        Function: main
        Body:
            Var: foo = 1;
        EndBody.
        Function: foo
        Body:
        EndBody.
        """
        expect = str(UnreachableFunction("foo"))
        self.assertTrue(TestChecker.test(input,expect, 572))

    def test_unreachable_function5(self):
        input = """
        Function: main
        Body:
            Var: x;
            x = x + foo();
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 573))

    def test_unreachable_function6(self):
        input = """
        Function: main
        Body:
            While foo() > 5
            Do
            EndWhile.
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 576))

    def test_unreachable_statement1(self):
        input = """
        Function: main
        Body:
            Var: x;
            Return;
            x = 1;
        EndBody."""
        expect = str(UnreachableStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect, 577))

    def test_unreachable_statement2(self):
        input = """
        Function: main
        Body:
            Var: x;
            Return 1;
            x = 1;
        EndBody."""
        expect = str(UnreachableStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect, 578))

    def test_unreachable_statement3(self):
        input = """
        Function: main
        Body:
            Var: x;
            If x > 5 Then
                Return;
                x = x + 1;
            Else
                Return ;
            EndIf.
        EndBody."""
        expect = str(UnreachableStatement(Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))))
        self.assertTrue(TestChecker.test(input,expect, 579))

    def test_unreachable_statement4(self):
        input = """
        Function: main
        Body:
            Var: x;
            If x > 5 Then
                Return;
            Else
                Return ;
            EndIf.
            x = x + 1;
        EndBody."""
        expect = str(UnreachableStatement(Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))))
        self.assertTrue(TestChecker.test(input,expect, 580))

    def test_unreachable_statement5(self):
        input = """
        Function: main
        Body:
            Var: x;
            For (x = 0, x < 100, x) Do
                Return;
            EndFor.
            x = x + 2;
        EndBody."""
        expect = str(UnreachableStatement(Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))))
        self.assertTrue(TestChecker.test(input,expect, 581))

    def test_unreachable_statement6(self):
        input = """
        Function: main
        Body:
            Var: x;
            For (x = 0, x < 100, x) Do
                If x > 50 Then
                    Return;
                EndIf.
            EndFor.
            x = x + 2;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 582))

    def test_unreachable_statement7(self):
        input = """
        Function: main
        Body:
            Var: x;
            For (x = 0, x < 100, x) Do
                If x > 50 Then
                    Return;
                EndIf.
                While x > 1 Do
                    Break;
                    Return;
                EndWhile.
            EndFor.
            x = x + 2;
        EndBody."""
        expect = str(UnreachableStatement(Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))))
        self.assertTrue(TestChecker.test(input,expect, 583))

    def test_index_out_of_range1(self):
        input = """
        Function: main
        Body:
            Var: x[0];
            x[0] = 1;
        EndBody."""
        expect = str(IndexOutOfRange(ArrayCell(Id("x"),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect, 584))

    def test_index_out_of_range2(self):
        input = """
        Function: main
        Body:
            Var: x[5];
            x[-1] = 1;
        EndBody."""
        expect = str(IndexOutOfRange(ArrayCell(Id("x"),[UnaryOp("-",IntLiteral(1))])))
        self.assertTrue(TestChecker.test(input,expect, 585))

    def test_index_out_of_range3(self):
        input = """
        Function: main
        Body:
            Var: x[5];
            x[2 + 3] = 1;
        EndBody."""
        expect = str(IndexOutOfRange(ArrayCell(Id("x"),[BinaryOp("+",IntLiteral(2),IntLiteral(3))])))
        self.assertTrue(TestChecker.test(input,expect, 586))

    def test_index_out_of_range4(self):
        input = """
        Function: main
        Body:
            Var: x[5];
            x[2 * 3 - 2] = 1;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 587))

    def test_index_out_of_range5(self):
        input = """
        Function: main
        Body:
            Var: x[5];
            x[11 % 5] = 1;
            x[12 % 5] = 1;
            x[13 % 5] = 1;
            x[14 % 5] = 1;
            x[15 % 5] = 1;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 588))

    def test_index_out_of_range6(self):
        input = """
        Function: main
        Body:
            Var: x[5], y = 100;
            x[y + 1] = 1;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 589))

    def test_index_out_of_range7(self):
        input = """
        Function: main
        Body:
            Var: x[5];
            x[24 \\ 5] = 1;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 590))

    def test_index_out_of_range8(self):
        input = """
        Function: main
        Body:
            Var: x[5];
            x[25 \\ 5 - 1 + 1] = 1;
        EndBody."""
        expect = str(IndexOutOfRange(ArrayCell(Id("x"),[BinaryOp("+",BinaryOp("-",BinaryOp("\\",IntLiteral(25),IntLiteral(5)),IntLiteral(1)),IntLiteral(1))])))
        self.assertTrue(TestChecker.test(input,expect, 591))

    def test_built_in_function1(self):
        input = """
        Function: main
        Body:
            Var: x = 1;
            Var: y = 2.5;
            Var: z = "234";
            Var: t = True;
            x = int_of_float(1.4);
            y = float_to_int(2);
            z = string_of_int(234);
            x = int_of_string("10ab");
            y = float_of_string("4.4");
            z = string_of_float(3.3);
            z = string_of_bool(t);
            t = bool_of_string(z);
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 592))

    def test_deep_inference1(self):
        input = """
        Function: main
        Body:
            Var: x[1], y[1], z[1], t[1], w[1];
            x[y[z[t[w[0]]]]] = True;
            x[0] = False;
            y[0] = 1;
            z[0] = 1;
            w[0] = 1;
            Return t;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 593))

    def test_deep_inference2(self):
        input = """
        Function: main
        Body:
            Var: x[1], y[1], z[1], t[1], w[1];
            Return x[y[z[t[w[x[0]]]]]];
        EndBody."""
        expect = str(TypeCannotBeInferred(Return(ArrayCell(Id("x"),[ArrayCell(Id("y"),[ArrayCell(Id("z"),[ArrayCell(Id("t"),[ArrayCell(Id("w"),[ArrayCell(Id("x"),[IntLiteral(0)])])])])])]))))
        self.assertTrue(TestChecker.test(input,expect, 594))

    
    




    


    def test_random2(self):
        input = """Function: main
                    Parameter: x
                   Body:
                        Var: a[3];
                        a[a[2]]=True;
                   EndBody."""
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("a"),[ArrayCell(Id("a"),[IntLiteral(2)])]),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect, 598))

    def test_random1(self):
        input = """Function: foo
                   Parameter: x
                   Body: 
                        Return 1;
                   EndBody.
                   Function: fan
                   Parameter: x
                   Body: 
                        Return True;
                   EndBody.
                    Function: main
                    Parameter: x
                   Body:
                        main(foo(fan(2)));
                   EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect, 599))

    

    


    
        

    


    


