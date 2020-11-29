import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    
    def test1_read_func(self):
        input = """Function: main
                   Body: 
                        read(0);
                   EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("read"),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test2_printLn_func(self):
        input = """Function: main
                   Body: 
                        printLn("khang");
                   EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printLn"),[StringLiteral("khang")])))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test3_printStr_func(self):
        input = """Function: main
                   Body: 
                        printStr();
                   EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStr"),[])))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test4_printStrLn_func(self):
        input = """Function: main
                   Body: 
                        printStrLn(123);
                   EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[IntLiteral(123)])))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test5_int_of_float(self):
        input = """Function: main
                   Body: 
                        Var: a = 1.1;
                        a = int_of_float(123.0);
                   EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('a'), CallExpr(Id("int_of_float"),[FloatLiteral(123.0)]))))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test6_float_of_int(self):
        input = """Function: main
                   Body: 
                        Var: a = 1.1;
                        a = float_of_int(12.0);
                   EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("float_of_int"),[FloatLiteral(12.0)])))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test7_int_of_string(self):
        input = """Function: main
                   Body: 
                        Var: a = 1.1;
                        a = int_of_string(12.0);
                   EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("int_of_string"),[FloatLiteral(12.0)])))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test8_string_of_int(self):
        input = """Function: main
                   Body: 
                        Var: a;
                        a = string_of_int(True);
                   EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("string_of_int"),[BooleanLiteral(True)])))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test9_float_of_string(self):
        input = """Function: main
                   Body: 
                        Var: a;
                        a = float_of_string("12.");
                        a = 1;
                   EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('a'), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test10_string_of_float(self):
        input = """Function: main
                   Body: 
                        Var: a;
                        a = string_of_float(True);
                   EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("string_of_float"),[BooleanLiteral(True)])))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test11_bool_of_string(self):
        input = """Function: main
                   Body: 
                        Var: a, b;
                        a = bool_of_string("True");
                        b = a + "123";
                   EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp(('+'), Id('a'), StringLiteral('123'))))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test12_string_of_bool(self):
        input = """Function: main
                   Body: 
                        Var: a;
                        a = string_of_bool("True");
                   EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("string_of_bool"),[StringLiteral("True")])))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test13_undeclared_function(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test14_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,414))
    
    def test15_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test16_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallStmt(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test17_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test18_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test19_undeclared_function(self):
        """Simple program: main"""
        input = """Var: a[2][2] = {{1,2},{3,4}};"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,419))

    def test20_redeclared_function_main(self):
        input = """Var: main;
                    Function: main
                   Body: 
                   EndBody."""
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test21_no_entry_point(self):
        input = """Function: foo
                   Body: 
                    main();
                   EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test22(self):
        input = """Var: foo;
                    Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test23(self):
        input = """Var: foo;
                    Function: main
                   Body: 
                        foo();
                   EndBody.
                   Function: foo
                   Body:
                   EndBody."""
        expect = str(Redeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test24(self):
        input = """Var: main;
                    Function: foo
                    Body:
                    EndBody.
                """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,424))

    def test25(self):
        input = """
        Function: main
        Parameter: a, b
        Body:
            a = b;
        EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test26(self):
        input = """
        Function: main
        Parameter: a, b
        Body:
            a[b] = 1;
        EndBody.
                """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[Id('b')])))
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test27(self):
        input = """
        Var: x = 1;
        Function: main
        Parameter: a, b[1]
        Body:
            a = True;
            b[0] = x;
            b[0] = a;
        EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('b'),[IntLiteral(0)]), Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test28(self):
        input = """
        Var: x = 1;
        Function: main
        Parameter: a, b
        Body:
            a = 1;
            a = True;
        EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,428))
    
    def test29(self):
        input = """
        Function: foo
        Body:
        EndBody.
         Function: main
        Parameter: a, b
        Body:
            a = 1;
            a = foo();
            b = foo();
            b = True;
        EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test30(self):
        input = """Var: x;
                    Function: main
                   Body: 
                        x = 1;
                        x = foo(1);
                        
                   EndBody.
                   
                   Function: foo
                   Parameter: k
                   Body:
                        k = 1.1;
                        printStrLn(k);
                   EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("k"),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,430))

    def test31(self):
        input = """Var: x;
                    Function: main
                   Body: 
                        x = 1;
                        x = foo(1);
                        xx();
                   EndBody.
                   Function: xx
                   Parameter: a
                   Body:
                        foo(1);
                    EndBody.
                   Function: foo
                   Parameter: k
                   Body:
                        printStrLn(k);
                   EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("xx"),[])))
        self.assertTrue(TestChecker.test(input,expect,431))

    def test32(self):
        input = """
        Var: a = 1;
        Function: main
        Parameter: b
        Body:
            b = True;
            a = b;
        EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test33(self):
        input = """
        Var: a;
        Function: foo
        Body:
            Return 1;
        EndBody.
        Function: main
        Body:
            a = foo();
            a = "sk";
        EndBody.
        
                """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),StringLiteral("sk"))))
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test34(self):
        input = """
        
        Var: a;
        Function: main
        Body:
            a = foo();
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        
        """
        expect = str(TypeCannotBeInferred(Assign(Id('a'),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test35(self):
        input = """
        Var: a;
        Function: main
        Parameter: b
        Body:
            Var: b;
        EndBody.
        """
        expect = str(Redeclared(Variable(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test36(self):
        input = """
        Var: x[2][2] = {{1,2},{3,2}}, a;
        Function: foo
        Body:
            Return x;
        EndBody.
        Function: main
        Body:
            Var: a;
            a = foo()[1][1];
            a = 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test37(self):
        input = """
        Function: main
        Parameter: b, b[5][6]
        Body:
            
        EndBody.
        """
        expect = str(Redeclared(Parameter(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test38_call_stmt(self):
        input = """Function: main
                   Body: 
                        foo(1, 2);
                   EndBody.
                   Function: foo
                   Parameter: a, b
                   Body:
                        Return a;
                   EndBody."""
        expect = str(TypeMismatchInStatement(Return(Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test39_if_stmt(self):
        input = """Function: main
                   Body: 
                        Var: x;
                        If x Then
                            x = 1;
                        EndIf.
                   EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('x'), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test40(self):
        input = """
        Function: foo
        Parameter: a
        Body:
            a = 1;
            Return a;
        EndBody.
        Function: main
        Parameter: b
        Body:
            foo();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[])))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test41(self):
        input = """
        Function: foo
        Parameter: a
        Body:
            a = 1;
            Return;
        EndBody.
        Function: main
        Parameter: b
        Body:
            main();
            foo();
            Return b;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[])))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test42(self):
        input = """
        Function: main
        Parameter: y, a, x
        Body:
            y = a + foo(x);
        EndBody.
        Function: foo
        Parameter: a
        Body:
            Return;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(CallExpr(Id('foo'),[Id('x')])))
        self.assertTrue(TestChecker.test(input,expect,442))
    
    def test43(self):
        input = """
        Function: main
        Parameter: y, a, x
        Body:
            x = 1;
            y = a + foo(x);
        EndBody.
        Function: foo
        Parameter: a
        Body:
            a = False;
            Return a;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'), BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input,expect,443))
    
    def test44(self):
        input = """
        Var: a[2][2];
        Function: main
        Parameter: b[2][2]
        Body:
           a[1][1] = 1.1;
           b = a;
           b = {{1,2},{3,4}};
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("b"),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))))
        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test45(self):
        input = """
        Var: a;
        Function: main
        Parameter: b
        Body:
            While a Do
                b = a && True;
            EndWhile.
            b = 1 + 2;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("b"), BinaryOp("+", IntLiteral(1), IntLiteral(2)))))
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test46(self):
        input = """
            Var: a[2] = {"Hoang", "Gia"};
            Function: main
            Parameter: x, y
            Body:
                x = read();
                y = int_of_string(x);
                If y == 0 Then
                    printStr(x);
                ElseIf y == 1 Then
                    printStrLn(a[1]);
                Else
                    printLn(a[0]);
                EndIf.
                Return 0;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('printLn'), [ArrayCell(Id('a'),[IntLiteral(0)])])))
        self.assertTrue(TestChecker.test(input,expect,446))
    
    # def test47(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: n;
    #         foo()[n][2] = 1;
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return {1,2};
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id("b"),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))))
    #     self.assertTrue(TestChecker.test(input,expect,447))

    # # # def test_inferred_parameter_type_2(self):
    # # #     """More complex program"""
    # # #     input = """Function: main 
    # # #                    Body:
    # # #                        foo(1,2);
    # # #                    EndBody.

    # # #                 Function: foo 
    # # #                 Parameter: x,y
    # # #                    Body:
    # # #                         x = x + y;
    # # #                         Return 1;
    # # #                    EndBody.
    # # #             """
    # # #     expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
    # # #     self.assertTrue(TestChecker.test(input, expect, 444))

    # # # def test_inferred_parameter_type(self):
    # # #     """More complex program"""
    # # #     input = """Function: main 
    # # #                    Body:
    # # #                        foo(1,2);
    # # #                    EndBody.

    # # #                 Function: foo 
    # # #                 Parameter: x,y
    # # #                    Body:
    # # #                         x = 1.1;
    # # #                         y = 2;
    # # #                    EndBody.
    # # #             """
    # # #     expect = str(TypeMismatchInStatement(Assign(Id('x'), FloatLiteral(1.1))))
    # # #     self.assertTrue(TestChecker.test(input, expect, 443))
    # # # def test_func_return_array(self):
    # # #     """More complex program"""
    # # #     input = """
    # # #             Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
    # # #            Function: main
    # # #            Parameter: y, a
    # # #            Body:
    # # #                 Return x;
    # # #            EndBody.

    # # #            Function: foo
    # # #            Parameter: a[3][2]
    # # #            Body:
    # # #                a = main(1,2);
    # # #            EndBody.
    # # #            """
    # # #     expect = str()
    # # #     self.assertTrue(TestChecker.test(input, expect, 451))

    # # def test45(self):
    # #     input = """
    # #     Function: foo
    # #     Body:
    # #        Var: x;
    # #        x = main() + 1;
    # #        If x > 1 Then
    # #             Return 1;
    # #             x = x + 1;
    # #         Else
    # #          x = 0;
    # #          EndIf.

    # #     EndBody.
    # #     Function: main
    # #     Body:
    # #         Var: x;
    # #         x = foo() + 1;
    # #         kkk();
    # #         Return 1;
    # #     EndBody.
    # #     Function: kkk
    # #     Body:
    # #     EndBody.
    # #     """
    # #     expect = str(UnreachableStatement(Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))))
    # #     self.assertTrue(TestChecker.test(input,expect,445))

    # #  def test46(self):
    # #     input = """
    # #     Var: x[2][2] = {{1,2},{3,4}};
    # #     Function: main
    # #     Body:
    # #         Var: n;
    # #        x[n][3\\4+1*2-10%4+2] = 1;
    # #     EndBody.
    # #     """
    # #     expect = str(TypeMismatchInStatement(Assign(Id("b"),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))))
    # #     self.assertTrue(TestChecker.test(input,expect,446))