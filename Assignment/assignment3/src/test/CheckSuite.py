from main.bkit.utils.AST import ArrayCell, BooleanLiteral, CallExpr, CallStmt, IntLiteral, StringLiteral
from main.bkit.checker.StaticError import InvalidArrayLiteral, NoEntryPoint, Parameter, Redeclared, TypeCannotBeInferred, TypeMismatchInExpression, TypeMismatchInStatement, Variable
import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
   
    # def test_undeclared_function(self):
    #     """Simple program: main"""
    #     input = """Function: main
    #                Body: 
    #                     foo();
    #                EndBody."""
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """Complex program"""
    #     input = """Function: main  
    #                Body:
    #                     printStrLn();
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main 
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"),[],([],[
    #         CallStmt(Id("foo"),[])]))])
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_undeclared_function(self):
    #     """Simple program: main"""
    #     input = """Var: a[2][2] = {{1,2},{3,4}};"""
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test7_redeclared_function_main(self):
    #     input = """Function: main
    #                Body: 
    #                EndBody.
    #                Function: main
    #                Body:
    #                EndBody."""
    #     expect = str(Redeclared(Function(),"main"))
    #     self.assertTrue(TestChecker.test(input,expect,407))
    
    # def test8_no_entry_point(self):
    #     input = """Function: foo
    #                Body: 
    #                 main();
    #                EndBody."""
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input,expect,407))
    # def test9(self):
    #     input = """Var: foo;
    #                 Function: main
    #                Body: 
    #                     foo();
    #                EndBody."""
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,409))
    
    # def test10(self):
    #     input = """Var: foo;
    #                 Function: main
    #                Body: 
    #                     foo();
    #                EndBody.
    #                Function: foo
    #                Body:
    #                EndBody."""
    #     expect = str(Redeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,410))
    
    # def test11(self):
    #     input = """Var: main;
    #             """
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input,expect,411))
    # def test12(self):
    #     input = """
    #     Function: main
    #     Parameter: a, b
    #     Body:
    #         a = b;
    #     EndBody.
    #             """
    #     expect = str(TypeCannotBeInferred(Assign(Id('a'),Id('b'))))
    #     self.assertTrue(TestChecker.test(input,expect,412))
    
    # def test13(self):
    #     input = """
    #     Function: main
    #     Parameter: a, b
    #     Body:
    #         a[b] = 1;
    #     EndBody.
    #             """
    #     expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[Id('b')])))
    #     self.assertTrue(TestChecker.test(input,expect,413))
    
    # def test14(self):
    #     input = """
    #     Var: x = 1;
    #     Function: main
    #     Parameter: a, b[1]
    #     Body:
    #         a = True;
    #         b[1] = x;
    #         b[0] = a;
    #     EndBody.
    #             """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('b'),[IntLiteral(0)]), Id('a'))))
    #     self.assertTrue(TestChecker.test(input,expect,414))

    # def test15(self):
    #     input = """
    #     Var: x = 1;
    #     Function: main
    #     Parameter: a, b
    #     Body:
    #         a = 1;
    #         a = True;
    #     EndBody.
    #             """
    #     expect = str(TypeMismatchInStatement(Assign(Id('a'),BooleanLiteral(True))))
    #     self.assertTrue(TestChecker.test(input,expect,415))
    
    # def test16(self):
    #     input = """
    #     Function: foo
    #     Body:
    #     EndBody.
    #      Function: main
    #     Parameter: a, b
    #     Body:
    #         a = 1;
    #         a = foo();
    #         b = foo();
    #         b = True;
    #     EndBody.
    #             """
    #     expect = str(TypeMismatchInStatement(Assign(Id('b'),BooleanLiteral(True))))
    #     self.assertTrue(TestChecker.test(input,expect,416))

    # def test17(self):
    #     input = """Var: x;
    #                 Function: main
    #                Body: 
    #                     x = 1;
    #                     x = foo(1);
    #                     xx();
    #                EndBody.
    #                Function: xx
    #                Parameter: a
    #                Body:
    #                     foo(1);
    #                 EndBody.
    #                Function: foo
    #                Parameter: k
    #                Body:
    #                     printStrLn(k);
    #                EndBody."""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("xx"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,417))

    # def test18(self):
    #     input = """
    #     Var: a = 1;
    #     Function: main
    #     Parameter: b
    #     Body:
    #         b = True;
    #         a = b;
    #     EndBody.
    #             """
    #     expect = str(TypeMismatchInStatement(Assign(Id('a'),Id('b'))))
    #     self.assertTrue(TestChecker.test(input,expect,418))

    # def test19(self):
    #     input = """
    #     Var: a;
    #     Function: foo
    #     Body:
    #         Return 1;
    #     EndBody.
    #     Function: main
    #     Body:
    #         a = foo();
    #         a = "sk";
    #     EndBody.
        
    #             """
    #     expect = str(TypeMismatchInStatement(Assign(Id('a'),StringLiteral("sk"))))
    #     self.assertTrue(TestChecker.test(input,expect,419))
    
    # def test20(self):
    #     input = """
        
    #     Var: a;
    #     Function: main
    #     Body:
    #         a = foo();
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return 1;
    #     EndBody.
        
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('a'),CallExpr(Id('foo'),[]))))
    #     self.assertTrue(TestChecker.test(input,expect,420))

    # def test21(self):
    #     input = """
    #     Var: a;
    #     Function: main
    #     Parameter: b
    #     Body:
    #         Var: b;
    #     EndBody.
    #     """
    #     expect = str(Redeclared(Variable(), 'b'))
    #     self.assertTrue(TestChecker.test(input,expect,421))


    # def test22(self):
    #     input = """
    #     Var: x[2] = {{1,2},{3,2.1}}, a;
    #     Function: foo
    #     Body:
           
    #         Return x;
    #     EndBody.
    #     Function: main
    #     Body:
           
    #     EndBody.
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),FloatLiteral(2.1)])])))
    #     self.assertTrue(TestChecker.test(input,expect,422))

    # def test23(self):
    #     input = """
    #     Function: main
    #     Parameter: b, b[5][6]
    #     Body:
            
    #     EndBody.
    #     """
    #     expect = str(Redeclared(Parameter(), 'b'))
    #     self.assertTrue(TestChecker.test(input,expect,423))
    
    # def test24_call_stmt(self):
    #     input = """Function: main
    #                Body: 
    #                     foo(1, 2);
    #                EndBody.
    #                Function: foo
    #                Parameter: a, b
    #                Body:
    #                     Return a;
    #                EndBody."""
    #     expect = str(TypeMismatchInStatement(Return(Id('a'))))
    #     self.assertTrue(TestChecker.test(input,expect,424))

    # def test25(self):
    #     input = """
    #     Function: foo
    #     Parameter: a
    #     Body:
    #         a = 1;
    #         Return a;
    #     EndBody.
    #     Function: main
    #     Parameter: b
    #     Body:
    #         foo();
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[])))
    #     self.assertTrue(TestChecker.test(input,expect,425))

    # def test26(self):
    #     input = """
    #     Function: foo
    #     Parameter: a
    #     Body:
    #         a = 1;
    #         Return;
    #     EndBody.
    #     Function: main
    #     Parameter: b
    #     Body:
    #         main();
    #         foo();
    #         Return b;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[])))
    #     self.assertTrue(TestChecker.test(input,expect,426))

    # def test27(self):
    #     input = """
    #     Function: main
    #     Parameter: y, a, x
    #     Body:
    #         y = a + foo(x);
    #     EndBody.
    #     Function: foo
    #     Parameter: a
    #     Body:
    #         Return;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(CallExpr(Id('foo'),[Id('x')])))
    #     self.assertTrue(TestChecker.test(input,expect,427))
    
    # def test28(self):
    #     input = """
    #     Function: main
    #     Parameter: y, a, x
    #     Body:
    #         x = 1;
    #         y = a + foo(x);
    #     EndBody.
    #     Function: foo
    #     Parameter: a
    #     Body:
    #         a = False;
    #         Return a;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(Id('a'))))
    #     self.assertTrue(TestChecker.test(input,expect,428))
    
    # def test29(self):
    #     input = """
    #     Var: a[2][2];
    #     Function: main
    #     Parameter: b[2][2]
    #     Body:
    #        a[1][1] = 1.1;
    #        b = a;
    #        b = {{1,2},{3,4}};
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id("b"),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))))
    #     self.assertTrue(TestChecker.test(input,expect,429))

    # def test29(self):
    #     input = """
    #     Var: a[2][2];
    #     Function: main
    #     Parameter: b[2][2]
    #     Body:
    #        a[1][1] = 1.1;
    #        b = a;
    #        b = {{1,2},{3,4}};
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id("b"),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))))
    #     self.assertTrue(TestChecker.test(input,expect,429))

    def test30(self):
        input = """
        Function: foo
        Body:
           Var: x;
           x = main() + 1;
           If x > 1 Then
                Return 1;
                x = x + 1;
            Else
             x = 0;
             EndIf.

        EndBody.
        Function: main
        Body:
            Var: x;
            x = foo() + 1;
            kkk();
            Return 1;
        EndBody.
        Function: kkk
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("b"),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))))
        self.assertTrue(TestChecker.test(input,expect,430))
    



    