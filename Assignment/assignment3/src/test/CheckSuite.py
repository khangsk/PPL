from main.bkit.utils.AST import ArrayCell
from main.bkit.checker.StaticError import NoEntryPoint, Redeclared, TypeCannotBeInferred, TypeMismatchInExpression
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

    # # def test_diff_numofparam_stmt(self):
    # #     """Complex program"""
    # #     input = """Function: main  
    # #                Body:
    # #                     printStrLn();
    # #                 EndBody."""
    # #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    # #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # # def test_diff_numofparam_expr(self):
    # #     """More complex program"""
    # #     input = """Function: main 
    # #                 Body:
    # #                     printStrLn(read(4));
    # #                 EndBody."""
    # #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    # #     self.assertTrue(TestChecker.test(input,expect,402))

    # # def test_undeclared_function_use_ast(self):
    # #     """Simple program: main """
    # #     input = Program([FuncDecl(Id("main"),[],([],[
    # #         CallExpr(Id("foo"),[])]))])
    # #     expect = str(Undeclared(Function(),"foo"))
    # #     self.assertTrue(TestChecker.test(input,expect,403))

    # # def test_diff_numofparam_expr_use_ast(self):
    # #     """More complex program"""
    # #     input = Program([
    # #             FuncDecl(Id("main"),[],([],[
    # #                 CallStmt(Id("printStrLn"),[
    # #                     CallExpr(Id("read"),[IntLiteral(4)])
    # #                     ])]))])
    # #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    # #     self.assertTrue(TestChecker.test(input,expect,404))

    # # def test_diff_numofparam_stmt_use_ast(self):
    # #     """Complex program"""
    # #     input = Program([
    # #             FuncDecl(Id("main"),[],([],[
    # #                 CallStmt(Id("printStrLn"),[])]))])
    # #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    # #     self.assertTrue(TestChecker.test(input,expect,405))

    #  #  def test_undeclared_function(self):
    # #     """Simple program: main"""
    # #     input = """Var: a[2][2] = {{1,2},{3,4}};"""
    # #     expect = str(Undeclared(Function(),"foo"))
    # #     self.assertTrue(TestChecker.test(input,expect,406))

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
    
    def test14(self):
        input = """
        Function: main
        Parameter: a, b
        Body:
            a[3] = 1;
        EndBody.
                """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[Id('b')])))
        self.assertTrue(TestChecker.test(input,expect,414))
    
    # def test11_call_stmt(self):
    #     input = """Function: main
    #                Body: 
    #                     foo(1, 2);
    #                EndBody.
    #                Function: foo
    #                Parameter: a, b
    #                Body:
    #                EndBody."""
    #     expect = str(Redeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,411))