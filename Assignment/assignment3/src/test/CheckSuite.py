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

    def test47_inferred_parameter_type(self):
        input = """Function: main 
                       Body:
                           foo(1,2);
                       EndBody.

                    Function: foo 
                    Parameter: x,y
                       Body:
                            x = x + y;
                            Return 1;
                       EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test48_inferred_parameter_type(self):
        """More complex program"""
        input = """Function: main 
                       Body:
                           foo(1,2);
                       EndBody.

                    Function: foo 
                    Parameter: x,y
                       Body:
                            x = 1.1;
                            y = 2;
                       EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test49_func_return_array(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a
               Body:
                    foo(x);
                    Return x;
               EndBody.

               Function: foo
               Parameter: a[3][2]
               Body:
                   a = main(1,2);
                   Return 1;
               EndBody.
               """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test50(self):
        """More complex program"""
        input = """
                Function: foo
                Parameter: a,b
                Body:
                    If a > b Then
                        If a > 0 Then
                            If b > 0 Then
                                Return 1;
                            Else
                                b = b + 10;
                            EndIf.
                        Else
                            Return 1;
                        EndIf.
                    EndIf. 
                    Return;
                EndBody.
                Function: main
                Body:
                    foo(5,2);
                EndBody.
               """
        expect = str(TypeMismatchInStatement(Return(None)))
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test51(self):
        """More complex program"""
        input = """
                Function: foo
                Parameter: a,b
                Body:
                    If a > b Then
                        If a > 0 Then
                            If b > 0 Then
                                Return 1;
                            Else
                                b = b + 10;
                            EndIf.
                        Else
                            Return True;
                        EndIf.
                    EndIf. 
                    Return;
                EndBody.
                Function: main
                Body:
                    foo(5,2);
                EndBody.
               """
        expect = str(TypeMismatchInStatement(Return(BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test52(self):
        """More complex program"""
        input = """
                Function: foo
                Parameter: a,b
                Body:
                    If a > b Then
                        Var: i;
                        For (i = 2, i < 10, i + 1) Do
                            Var: s;
                            s = string_of_int(i);
                            printStr(s);
                        EndFor.
                    ElseIf a < b Then
                        i = 1;
                        Return i;
                    EndIf. 
                    Return;
                EndBody.
                Function: main
                Body:
                    foo(5,2);
                EndBody.
               """
        expect = str(Undeclared(Identifier(), 'i'))
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test53(self):
        """More complex program"""
        input = """
                Function: foo
                Parameter: a,b
                Body:
                    If a > b Then
                        Var: i;
                        For (i = 2, i < 10, i + 1) Do
                            Var: s;
                            s = string_of_int(i);
                            printStr(s);
                        EndFor.
                    ElseIf a < b Then
                        Var: i = 0;
                        While i < 5 Do
                            Var: s;
                            s = string_of_int(i);
                            printStrLn(s);
                        EndWhile.
                    EndIf. 
                    Return b;
                EndBody.
                Function: main
                Body:
                    foo(5,2);
                EndBody.
               """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[IntLiteral(5), IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test54(self):
        """More complex program"""
        input = """
                Function: foo
                Parameter: a[2][2],b
                Body:
                    a[1] = 1;
                    a[1][1] = b + 2;
                    Return b;
                EndBody.
                Function: main
                Body:
                    foo(5,2);
                EndBody.
               """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test55(self):
        """More complex program"""
        input = """
                Function: main
                Body:
                    Var: x;
                    foo(5,x);
                EndBody.
                Function: foo
                Parameter: x,y
                Body:
                EndBody.
               """
        expect = str(TypeCannotBeInferred(CallStmt(Id('foo'),[IntLiteral(5),Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test56(self):
        """More complex program"""
        input = """
                Function: main
                Body:
                    Var: x;
                    x = 1 + 2;
                    foo(5,x);
                EndBody.
                Function: foo
                Parameter: x,y
                Body:
                    Return True;
                EndBody.
               """
        expect = str(TypeMismatchInStatement(Return(BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test57(self):
        """More complex program"""
        input = """
                Function: foo
                Parameter: x,y
                Body:
                    x = 2;
                    y = 1;
                    Return;
                EndBody.
                Function: main
                Body:
                    Var: x;
                    x = 1 + 2;
                    foo(5.1,x);
                EndBody.
               """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[FloatLiteral(5.1), Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test58(self):
        """More complex program"""
        input = """
                 Function: main
                Body:
                    Var: x;
                    x = 1 + 2;
                    foo(5.1,x);
                EndBody.
                Function: foo
                Parameter: x,y
                Body:
                    x = 2;
                    y = 1;
                    Return;
                EndBody.
                
               """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test59(self):
        input = """ 
            Function: main
            Parameter: x, y ,z
            Body:
            y = x || (x > z);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('>',Id('x'),Id('z'))))
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    def test60(self):
        input = """ 
        Function: foo
            Parameter: x
            Body:
            x=1.1;
            Return { True };
            EndBody.
        Function: main
            Parameter: x, y
            Body:
            foo(x)[0] = x || (x>y);
            EndBody.

        """
        expect = str(TypeMismatchInExpression(BinaryOp('||',Id('x'),BinaryOp('>',Id('x'),Id('y')))))
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test61(self):
        input = """ 
        Function: main
        Parameter: x, y
        Body:
            y = 1;
            foo(1.1, y);
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
            y = 1;
            x = y;
        Return { True };
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test62_ambigous_variable_2(self):
        """More complex program"""
        input = """
                  Var: x[2][2][3] = { { { 1,2,3 } , { 2,3,4 } } , { { 1,2,3 } , { 2,3,4 } } };
                  Function: foo
                  Parameter: z, y
                  Body:
                      Return x;
                  EndBody.

                  Function: main
                  Parameter: x, y
                  Body:
                      x = foo(1,2);
                      x[1][2][3] = False;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),CallExpr(Id('foo'),[IntLiteral(1), IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test63_ambigous_variable_2(self):
        """More complex program"""
        input = """
                  Var: x[2][2][3] = { { { 1,2,3 } , { 2,3,4 } } , { { 1,2,3 } , { 2,3,4 } } };
                  Function: foo
                  Parameter: z, y
                  Body:
                      Return x;
                  EndBody.

                  Function: main
                  Parameter: x[2][2][3], y
                  Body:
                      x = foo(1,2);
                      x[0][0][0] = False;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'), [IntLiteral(0), IntLiteral(0), IntLiteral(0)]), BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test64_redeclared_in_ifStmt_1(self):
        """Complex program"""
        input = """
            Function: func_name
                Body:
                    If 1>2 Then
                        Var: x;
                        Return True ;
                    Else 
                        Var: x;
                        Var: y[1], y;
                        Return False;
                    EndIf.
                EndBody.
                
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Variable(), 'y'))
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test65_redeclared_in_some_stmt(self):
        """Complex program"""
        input = """
            Function: func_name
            Parameter: k
                Body:
                    If 0==0 Then
                        Var: x;
                    ElseIf 1==1 Then
                        Var: y[1];
                    Else
                        Var: y;
                        Var: m, n[1][2][3] = "string";
                    EndIf.
                    k = 0x9;
                    For ( k=2,0<1, 1+1 ) Do
                        Var: y,m,n;
                        Var: k, n[1][2][100];
                    EndFor.
                EndBody.
                
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Variable(), 'n'))
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test66_redeclared_builtin_function(self):
        """Complex program"""
        input = """
            Function: int_of_float
            Body:
            EndBody.

            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Function(), 'int_of_float'))
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test67_type_cannot_be_inferred_assignStmt(self):
        """Complex program"""
        input = """
            Function: main_
            Body:
                Var: x;
                main_();
                x = 1;
            EndBody.

            Function: main
            Body:
                Var: x;
                x = 1;
                x = 1.;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), FloatLiteral(1.))))
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test68_invalid_variable_in_forStmt(self):
        """Complex program"""
        input = """
            Function: main_
            Body:
                Var: x;
                main_();
                x = 1;
            EndBody.

            Function: main
            Body:
                Var: x[5];
                Var: y[3] = { 1,2,  3};
                For ( i=1,i<100,1) Do
                    If 1 < 2 Then
                        x = y;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = str(Undeclared(Identifier(), 'i'))
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test69_inferred_func_callStmt(self):
        """Complex program"""
        input = """
            Function: foo
            Body:
                Var: x;
                x = 1;
            EndBody.

            Function: main
            Body:
                Var: x[5];
                Var: y[3] = { 1,2,  3};
                Var: z = 1;
                z = z + foo();
                z = foo() + 0x9;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+', Id('z'),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test70_invalid_func_call_simple(self):
        """Complex program"""
        input = """
            Var: x = 1;
            Function: foo
            Parameter: x,y
            Body:
                Var: z;
            EndBody.

            Function: main
            Body:
                 x = foo(1);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test71_match_type_of_parameter_call_expr(self):
        """Complex program"""
        input = """
            Var: x = 1;
            Function: foo
            Parameter: x,y,   z
            Body:
                x = 1;
                y = 1.9999;
                Return y;
            EndBody.

            Function: main
            Body:
                Var: x = 1.1, y;
                 x = foo(1,1.1, "this is a string");
                 x = 1 + foo(1, 1.1, 1000);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'), [IntLiteral(1), FloatLiteral(1.1), IntLiteral(1000)]))))
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test72_invalid_return_type_in_if_condition(self):
        """Complex program"""
        input = """
            Var: a,b;
            Function: foo
            Parameter: x,y,   z
            Body:
                Return;
            EndBody.

            Function: main
            Body:
                If b + 0 Then 
                    Return a; 
                EndIf.
                foo(1,2,3);
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If([(BinaryOp('+',Id('b'), IntLiteral(0)), [], [Return(Id('a'))])], ([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test73_inferred(self):
        """More complex program"""
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
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test74_error_asignment_with_arrayliteral_2(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a
               Body:
                    a = 1.;
                    Return a;
               EndBody.

               Function: foo
               Parameter: a
               Body:
                   a = main(1,2.);
                   a = a + 2;
               EndBody.
               """
        expect = str(TypeMismatchInExpression(BinaryOp('+',Id('a'),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test75_invalid_in_for_stmt(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a, i
               Body:
                    For ( i= 1.1 ,i<1000, i+1 ) Do
                    EndFor.
               EndBody.
               """
        expect = str(TypeMismatchInStatement(For(Id('i'), FloatLiteral(1.1), BinaryOp("<", Id("i"), IntLiteral(1000)), BinaryOp("+", Id("i"), IntLiteral(1)), ([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test76_inferred_type_from_for_stmt(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a, i
               Body:
                    For ( i= 1 ,i<1000, i+1 ) Do
                        a =  a + x[i][i+1];
                    EndFor.
                    i = i + 1;
               EndBody.
               """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test77_invalid_index_expression_with_float_dimen(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a, i
               Body:
                    x[1][1.1] = 1;
               EndBody.
               """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('x'), [IntLiteral(1), FloatLiteral(1.1)])))
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test78_invalid_with_function_return_array(self):
        """More complex program"""
        input = """
                   Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
                  Function: main
                  Parameter: y, a, i
                  Body:
                        Return x;
                  EndBody.

                  Function: foo
                  Body:
                        main(1,2,3)[2] = 1;
                  EndBody.
                  """
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id('main'), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), [IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test79_multi_func_return_array(self):
        """More complex program"""
        input = """
                   Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
                  Function: main
                  Parameter: y, a, i
                  Body:
                        foo()[2][3] = 0.9;
                        Return x;
                  EndBody.

                  Function: foo
                  Body:
                        Return { { 1.1,2.2, 4.4 }, { 2.2,3.3, 9.9}   }; 
                  EndBody.
                  
                  Function: goo
                  Body:
                        foo()[1][2] = 100;
                  EndBody.
                  """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(2), IntLiteral(3)]),FloatLiteral(0.9))))
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test80_inferred_para_type_in_binary_op(self):
        """More complex program"""
        input = """
                   Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
                  Function: main
                  Parameter: y, a, i
                  Body:
                        a = 1 + foo();
                  EndBody.

                  Function: foo
                  Body:
                        Return 1.1;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test81_invalid_assign_stmt(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { True };
                  Function: main
                  Parameter: k, a, i
                  Body:
                        Var: bool_of_string;
                        x[1][1][1] = y[2][1];
                        y[1][1] = z[0];
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('y'),[IntLiteral(1), IntLiteral(1)]), ArrayCell(Id('z'), [IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test82_not_match_dimension_of_array(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { True };
                  Function: main
                  Parameter: k, a, i
                  Body:
                        Var: bool_of_string;
                        x[1][1] = y[2][1];
                  EndBody.
                  """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('x'),[IntLiteral(1), IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test83_index_is_not_int(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { True };
                  Function: main
                  Parameter: k, a, i
                  Body:
                        Var: bool_of_string;
                        x[1.1][1][1] = y[2][1];
                  EndBody.
                  """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('x'),[FloatLiteral(1.1), IntLiteral(1), IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test84_index_operator_with_not_array_type(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { True };
                  Function: main
                  Parameter: k[2][2][2], a[3][2], i[1]
                  Body:
                        Var: bool_of_string;
                        k[1] = 1;
                        Return k;
                  EndBody.
                  
                  Function: foo
                  Body:
                        Var: x;
                        x = main( {1}, 2, 3);
                        x = { {1,2} };
                  EndBody.
                  """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('k'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test85_call_stmt_with_param_is_array(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { True };
                  Function: main
                  Parameter: k[2][2][2], a[3][2], i[1]
                  Body:
                        k = x;
                        a = y;
                        i = z;
                  EndBody.

                  Function: foo
                  Body:
                        Var: x;
                        main( { { { 100,200 } , {200,300} },  { { 300,400 } , {400,500} } } , { {100,200} , {200,300} , {3,4} } , { False });
                        Return x;
                  EndBody.
                  """
        expect = str(TypeCannotBeInferred(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test86_for_stmt_with_invalid_idx_variable(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { 1 };
                  Function: main
                  Parameter: k[2][2][2], a[3][2], i[1]
                  Body:
                        k = x;
                        a = y;
                        i = z;
                  EndBody.

                  Function: foo
                  Body:
                        Var: x = 0x9;
                        Var: i = True;
                        main( { { { 100,200 } , {200,300} },  { { 300,400 } , {400,500} } } , { {100,200} , {200,300} , {3,4} } , { 100 });
                        For ( i=2,1<z[1], x+1 ) Do
                            x = 1;
                        EndFor.
                        
                        Return x;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(For(Id('i'), IntLiteral(2), BinaryOp('<', IntLiteral(1), ArrayCell(Id('z'), [IntLiteral(1)])), BinaryOp('+', Id('x'), IntLiteral(1)), ([], [Assign(Id('x'), IntLiteral(1))]))))
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test87_for_stmt(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { 1 };
                  Function: main
                  Body:
                        foo();
                        Return y;
                  EndBody.

                  Function: foo
                  Body:
                        Var: y = 0x9;
                        Var: i = True;
                        For ( y = x[1][1][1], 1 < main()[1][1], y + main()[2][0] ) Do
                            y = True;
                        EndFor.

                        Return;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test88_invalid_type_condition_if_stmt(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {True,False} , {True,False} , {True,True} }, z[1] = { 1 };
                  Function: main
                  Body:
                    foo();
                        Return y;
                  EndBody.

                  Function: foo
                  Body:
                        Var: y = 0x9;
                        Var: i = True;
                        If main()[1][1] Then
                            Return 1;
                        EndIf.
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test89_inferred_type_from_if_stmt(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: k
                  Body:
                       If foo(1,2,3) Then
                       ElseIf k Then
                       EndIf. 
                  EndBody.
                  
                  Function: foo
                  Parameter: k, a, i
                  Body:
                        Var: x[1][2];
                        x = { {1,2} };
                        Return 1;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test90_inferred_para_type_from_if_stmt(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z
                  Body:
                       If x Then
                       ElseIf y Then
                       ElseIf z Then
                       EndIf. 
                  EndBody.

                  Function: foo
                  Parameter: k, a, i
                  Body:
                        main(True,False,1);
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'), [BooleanLiteral(True), BooleanLiteral(False), IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test91_inferred_return_type_from_if_stmt(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z
                  Body:
                       If foo(2,3,4) Then
                       EndIf. 
                  EndBody.

                  Function: foo
                  Parameter: k, a, i
                  Body:
                        k = k + a + i;
                        i = i +. 1.;
                        Return True;
                  EndBody.
                  """
        expect = str(TypeMismatchInExpression(BinaryOp('+.',Id('i'),FloatLiteral(1.))))
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test92_inferred_type_from_while_stmt(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: k
                  Body:
                       While foo(1,2,3) Do   
                       EndWhile.
                       
                       While k Do   
                       EndWhile.
                        
                  EndBody.

                  Function: foo
                  Parameter: k, a, i
                  Body:
                        Var: x[1][2];
                        x = { {1,2} };
                        Return 1;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test93_inferred_para_type_from_while_stmt(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z
                  Body:
                       While x Do   
                       EndWhile. 
                       
                       While y Do   
                       EndWhile.
                       
                       While z Do   
                       EndWhile.
                  EndBody.

                  Function: foo
                  Parameter: k, a, i
                  Body:
                        main(True,False,1);
                  EndBody.
                  """
        expect = str(
            TypeMismatchInStatement(CallStmt(Id('main'), [BooleanLiteral(True), BooleanLiteral(False), IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test94_inferred_return_type_from_while_stmt(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z
                  Body:
                       While foo(2,3,4) Do   
                       EndWhile. 
                  EndBody.

                  Function: foo
                  Parameter: k, a, i
                  Body:
                        k = k + a + i;
                        Return { {True,False}   };
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(ArrayLiteral([ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False)])]))))
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test95_inferred_return_type_from_for_stmt(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z
                  Body:
                       For (x = 0, x < 10, foo(2.0,3,4)) Do
                            y = float_of_int(x);
                       EndFor.
                       Return y;
                  EndBody.

                  Function: foo
                  Parameter: k, a, i
                  Body:
                        k = main(1,2.1,3);
                        k = k +. 1.1;
                        Return { {"a","b"}   };
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(ArrayLiteral([ArrayLiteral([StringLiteral('a'), StringLiteral('b')])]))))
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test96_complex_program_from_check_suite(self):
        """More complex program"""
        input = """
                  Function: fact
                  Parameter: n
                  Body:
                        If n == 0 Then
                            Var: x[1] = {False};
                            Return x[0];
                        ElseIf fact(1) Then
                            Var: y=9;
                        Else
                            Var: z;
                            Return fact(n - 1);
                        EndIf.
                        Return True;
                  EndBody.
                  
                  Function: main
                  Parameter: x,y,z
                  Body:
                       For (x = 0, fact(0x9) , 1) Do
                            y = string_of_bool(fact(1));
                            y = False;
                       EndFor.
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Assign(Id('y'),BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test97_inferred_type(self):
        """More complex program"""
        input = """
                  Function: fact
                  Parameter: m,n
                  Body:
                        m = 1;
                        n = "string";
                  EndBody.

                  Function: main
                  Parameter: x,y,z
                  Body:
                       fact(x,y);
                       x = x + 9;
                       y = False;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test98_inferred_array_type_from_param(self):
        """More complex program"""
        input = """
                  Function: fact
                  Parameter: m,n,p
                  Body:
                        m = 1;
                        n = "string";
                        p = string_of_int(m);
                  EndBody.

                  Function: main
                  Parameter: x[2][3],y,z
                  Body:
                       fact(x[1][2],y, foo(1,2));
                       y = "False";
                  EndBody.

                  Function: foo
                  Parameter: x,y
                  Body:
                       x = 100 + y; 
                       Return "HIHI";
                  EndBody.
                  
                  Function: goo
                  Body:
                       foo(100,200);
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'), [IntLiteral(100), IntLiteral(200)])))
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test99_inferred_type_from_param(self):
        """More complex program"""
        input = """
                  Function: fact
                  Parameter: m,n,p
                  Body:
                        m = 1;
                        n = "string";
                        p = string_of_int(m);
                        Return p;
                  EndBody.

                  Function: main
                  Parameter: x,y,z
                  Body:
                       foo(fact(100,"a","b"), 1);
                  EndBody.

                  Function: foo
                  Parameter: x,y
                  Body:
                       y = 0x9; 
                       x = 1;
                  EndBody.

                  """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test100_inferred_type_from_param_2(self):
        """More complex program"""
        input = """
                  Function: fact
                  Parameter: m,n,p
                  Body:
                        m = 1;
                        n = "string";
                        p = string_of_int(m);
                        Return { { 1.1, 1.2 } , { 1.3, 1.4 }, { 1.5, 1.6 } };
                  EndBody.

                  Function: main
                  Parameter: x,y,z
                  Body:
                       foo(fact(100,"a","b")[2][1], 1);
                  EndBody.

                  Function: foo
                  Parameter: x,y
                  Body:
                       y = 0x9; 
                       x = 1.1 +. 1.2;
                       Return y;
                  EndBody.

                  """
        expect = str(TypeMismatchInStatement(Return(Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 500))
    
    def test501_order_infer_4(self):
        """More complex program"""
        input = """
                  Function: foo
                  Parameter: x
                  Body:
                      If foo(int_of_string(string_of_bool(foo(1)))) Then
                        Return True;
                      EndIf.
                      Return False;
                  EndBody.

                  Function: main
                  Body:
                    Var: a;
                    a = foo(3);
                  EndBody.

                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 501))
    def test502_order_infer_4(self):
        """More complex program"""
        input = """
                  Function: foo
                  Parameter: x
                  Body:
                        foo(4.2);
                        x = 5.1;
                      Return;
                  EndBody.

                  Function: main
                  Body:
                    foo(2.1);
                  EndBody.

                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 502))

    def test103_order_infer_4(self):
        """More complex program"""
        input = """Function: foo1
                  Parameter: x
                  Body:
                        Return x +. foo1(1. *. foo1(foo1(foo1(x))) +. foo(2.));
                  EndBody.
                  Function: main
                  Body:
                    Var: x;
                    
                    x = foo1(2.) +. foo(2.);
                  EndBody.
                    Function: foo
                  Parameter: x
                  Body:
                        x = foo(4.2);
                      Return x;
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 503))

    def test104_order_infer_4(self):
        """More complex program"""
        input = """Function: foo1
                  Parameter: x
                  Body:
                    Var: i, j;
                        For (i = 1, foo1(foo1(True)), 1) Do
                            For (i = 1, foo1(False), 1) Do
                                printStr(string_of_int(i));
                            EndFor.
                        EndFor.
                        j = float_of_int(i);
                        Return foo(foo(True));
                  EndBody.
                  Function: main
                  Body:
                    Var: x;
                    
                    x = foo1(True) && foo(True);
                  EndBody.
                    Function: foo
                  Parameter: x
                  Body:
                        x = foo(False);
                      Return x;
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 504))

    def test105_order_infer_4(self):
        """More complex program"""
        input = """Function: foo1
                  Parameter: x
                  Body:
                    Var: i, j;
                        Do
                            i = 1;
                        While foo1(foo1(True)) EndDo.
                        Return foo(foo(True));
                  EndBody.
                  Function: main
                  Body:
                    Var: x;
                    
                    x = foo1(True) && foo(True);
                  EndBody.
                    Function: foo
                  Parameter: x
                  Body:
                        x = foo(False);
                      Return x;
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 505))

    def test106_order_infer_4(self):
        """More complex program"""
        input = """Function: foo1
                  Parameter: x
                  Body:
                    Var: i, j;
                        While foo1(foo1(True)) Do
                            i = 1;
                        EndWhile.
                        Return foo(foo(True));
                  EndBody.
                  Function: main
                  Body:
                    Var: x;
                    
                    x = foo1(True) && foo(True);
                  EndBody.
                    Function: foo
                  Parameter: x
                  Body:
                        x = foo(False);
                      Return x;
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 506))

    def test_order_infer_4(self):
        """More complex program"""
        input = """
                  Function: foo
                  Parameter: x
                  Body:
                      Return True && foo(foo(True));
                  EndBody.

                  Function: main
                  Body:
                  Var: a;
                        a=foo(True);
                  EndBody.

                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 508))
    # def test50(self):
    #     input = """
    #     Function: foo
    #     Body:
    #        Var: x;
    #        x = main() + 1;
    #        If x > 1 Then
    #             Return 1;
    #             x = x + 1;
    #         Else
    #          x = 0;
    #          EndIf.

    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: x;
    #         x = foo() + 1;
    #         kkk();
    #         Return 1;
    #     EndBody.
    #     Function: kkk
    #     Body:
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))))
    #     self.assertTrue(TestChecker.test(input,expect,450))

    # def test100(self):
    #     input = """
    #     Var: x[2][2] = {{1,2},{3,4}};
    #     Function: main
    #     Body:
    #         Var: n;
    #        x[n][3\\4+1*2-10%4+2] = 1;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id("b"),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))))
    #     self.assertTrue(TestChecker.test(input,expect,500))