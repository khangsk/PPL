import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_redeclared_global_variable_1(self):
        """Complex program"""
        input = """
            Var: x,y,x=10;
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_global_variable_2(self):
        """Complex program"""
        input = """
            Var: x,y,z=10;
            Var: a,b=120000e-1,c="this is a string";
            Var: c;
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Variable(), 'c'))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_function_1(self):
        """Complex program"""
        input = """
            Var: x,y,z=10;
            Var: a,b=120000e-1,c="this is a string";
            Var: d;
            Function: d
                Parameter: x, y
                Body:
                EndBody.
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Function(), 'd'))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_function_2(self):
        """Complex program"""
        input = """
            Var: x,y,z=10;
            Var: a,b=120000e-1,c="this is a string";
            Var: d;
            Function: func_name
                Parameter: x, y
                Body:
                EndBody.
            Function: func_name
                Parameter: x, y
                Body:
                EndBody.
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Function(), 'func_name'))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_parameter_1(self):
        """Complex program"""
        input = """
            Function: func_name
                Parameter: x, y, z, x
                Body:
                EndBody.
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_function_name(self):
        """Complex program"""
        input = """
            Function: sub_func
                Parameter: x, y, z
                Body:
                EndBody.
            
            Function: sub_func_2
                Parameter: x, y, z
                Body:
                EndBody.
                
            Function: sub_func
                Parameter: x, y, z
                Body:
                EndBody.
                
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Function(), 'sub_func'))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_variable_in_function_1(self):
        """Complex program"""
        input = """
            Var: x,y,z;
            Function: sub_func
                Parameter: x, y, z
                Body:
                    Var: a,b,c,x;
                EndBody.
                
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclared_variable_in_function_2(self):
        """Complex program"""
        input = """
            Var: x,y,z,k;
            Function: sub_func
                Parameter: x, y, z
                Body:
                    Var: a,b,c;
                    Var: k,m,a; 
                EndBody.
                
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Variable(), 'a'))
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redeclared_variable_in_function_3(self):
        """Complex program"""
        input = """
            Var: x,y,z,k;
            Function: sub_func
            Parameter: x, y, z
                Body:
                    Var: sub_func;
                EndBody.
                
            Function: main
                Body:
                EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redeclared_in_ifStmt_1(self):
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
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclared_in_ifStmt_2(self):
        """Complex program"""
        input = """
            Function: func_name
            Parameter: k
                Body:
                    If 0==0 Then
                        Var: x;
                    ElseIf 1==1 Then
                        Var: y[1];
                        Break;
                    Else
                        Var: y;
                        Var: m, m[1][2][3] = "string";
                        Continue;
                    EndIf.
                EndBody.
                
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Variable(), 'm'))
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_redeclared_in_some_stmt(self):
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
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_redeclared_in_while_stmt(self):
        """Complex program"""
        input = """
            Function: phanTichSoNguyen
            Parameter: n
                Body:
                While n <=. 1 Do
                    Var: n[100];
                    Var: n;
                EndWhile.
                EndBody.
                
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Variable(), 'n'))
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_redeclared_in_dowhile_stmt(self):
        """Complex program"""
        input = """
            Var: x = { 1,    1.,   "", True};
            Function: test
            Body:
                Do
                    Var: x;
                    Var: y, x[100];
                While False EndDo.
            EndBody.
            
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_redeclared_builtin_function(self):
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
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_undeclared_id_in_assignStmt_1(self):
        """Complex program"""
        input = """
            Var: x;
            Function: sub_func
            Body:
                Var: y;
                x = 1;
                y = 2;
                z = 3;
            EndBody.

            Function: main
                Body:
                EndBody.
        """
        expect = str(Undeclared(Identifier(), 'z'))
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_undeclared_id_in_assignStmt_2(self):
        """Complex program"""
        input = """
            Function: main
                Body:
                    Var: x = 0x1;
                    x = 1 + 2 + 3;
                    main = 1;
                EndBody.
        """
        expect = str(Undeclared(Identifier(), 'main'))
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_undeclared_id_in_assignStmt_3(self):
        """Complex program"""
        input = """
            Function: main
                Body:
                    Var: x[1][2][3];
                    arr[1][1] = x;
                EndBody.
        """
        expect = str(Undeclared(Identifier(), 'arr'))
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_undeclared_id_in_assignStmt_4(self):
        """Complex program"""
        input = """
            Var: x;
            Function: main
                Body:
                    Var: y;
                    If (x > y) Then
                        x = 6;
                        y = 7;
                        Return True ;
                    Else 
                        z = 10;
                        Return False;
                    EndIf.
                EndBody.
        """
        expect = str(Undeclared(Identifier(), 'z'))
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_undeclared_id_in_forStmt(self):
        """Complex program"""
        input = """
            Var: x;
            Function: main
                Body:
                    Var: y;
                    For ( i=1,i<6,1) Do
                        If x < y Then
                            x = y;
                        EndIf.
                    EndFor.
                EndBody.
        """
        expect = str(Undeclared(Identifier(), 'i'))
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_undeclared_function_id_in_callStmt(self):
        """Complex program"""
        input = """
            Var: x;
            Function: main
                Body:
                    Var: y;
                    main();
                    foo();
                EndBody.
        """
        expect = str(Undeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_undeclared_function_id_in_main(self):
        """Complex program"""
        input = """
            Var: x;
            Function: sub_func
            Body:
                Var: y;
                x = 1;
                y = 2;
                x = x + y;
            EndBody.

            Function: main
                Body:
                    sub_func_2();
                EndBody.
        """
        expect = str(Undeclared(Function(), 'sub_func_2'))
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_undeclared_variable_id_in_main(self):
        """Complex program"""
        input = """
            Var: x;
            Function: foo
                Body:
                    Var: arr;
                EndBody.

            Function: main
                Body:
                    x = 0x9;
                    y = 1;
                EndBody.
        """
        expect = str(Undeclared(Identifier(), 'y'))
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_ambiguous_problem(self):
        """Complex program"""
        input = """
            Function: main
            Body:
                Var: main = 0;
                main();
                main = 1;
            EndBody.
        """
        expect = str(Undeclared(Function(), 'main'))
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_no_entry_point_1(self):
        """Complex program"""
        input = """
            Function: main_
            Body:
                Var: x;
                main_();
                x = 1;
            EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_main_func_between_function(self):
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
            EndBody.
            
            Function: main__
            Body:
                Var: x;
                main__();
                x = 1;
            EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_type_cannot_be_inferred_assignStmt(self):
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
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_invalid_type_in_stmt(self):
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
                Var: y = { 1,2,  3,4 ,5};
                x = y;
                x = 10;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), IntLiteral(10))))
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_invalid_variable_in_forStmt(self):
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
                Var: y = { 1,2,  3};
                For ( i=1,i<100,1) Do
                    If 1 < 2 Then
                        x = y;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = str(Undeclared(Identifier(), 'i'))
        self.assertTrue(TestChecker.test(input, expect, 428))
    '''
    '''
    def test_inferred_func_callStmt(self):
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
                Var: y = { 1,2,  3};
                Var: z = 1;
                z = z + foo();
                z = foo() + 0x9;
                k = 1; 
            EndBody.
        """
        expect = str(Undeclared(Identifier(), 'k'))
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_not_same_number_or_ARG_PAR(self):
        """Complex program"""
        input = """
            Function: foo
            Parameter: x,y
            Body:
                Var: z;
            EndBody.

            Function: main
            Body:
                Var: x[5];
                Var: y = { 1,2,  3};
                Var: z = 1,k;
                z = z + foo(1,2);
                z = foo(1,2.) + 0x9;
                k = 1; 
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [IntLiteral(1), FloatLiteral(2.)])))
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_invalid_func_call_simple(self):
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
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_cannot_inferred_in_call_expr(self):
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
                Var: x = 1, y;
                 x = foo(x,y);
            EndBody.
        """
        expect = str(TypeCannotBeInferred(CallExpr(Id('foo'), [Id('x'), Id('y')])))
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_donot_match_in_call_expr(self):
        """Complex program"""
        input = """
            Var: x = 1;
            Function: foo
            Parameter: x,y
            Body:
                Var: z;
                x = 1;
                y = 1.9999;
            EndBody.

            Function: main
            Body:
                Var: x = 1, y;
                 x = foo(1,100);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [IntLiteral(1), IntLiteral(100)])))
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_match_type_of_parameter_call_expr(self):
        """Complex program"""
        input = """
            Var: x = 1;
            Function: foo
            Parameter: x,y,   z
            Body:
                x = 1;
                y = 1.9999;
            EndBody.

            Function: main
            Body:
                Var: x = 1, y;
                 x = foo(1,1.1, "this is a string");
                 x = 1 + foo(1, 1.1, 1000);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [IntLiteral(1), FloatLiteral(1.1), IntLiteral(1000)])))
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_callStmt_not_return_voidType(self):
        """Complex program"""
        input = """
            Var: x = 1;
            Function: foo
            Parameter: x,y,   z
            Body:
                x = 1;
                y = 1.9999;
            EndBody.

            Function: main
            Body:
                Var: x = 1, y;
                 x = foo(1,1.1, "this is a string");
                 foo( 10000, 19.99999, "");
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'), [IntLiteral(10000), FloatLiteral(19.99999), StringLiteral("")])))
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_invalid_return_in_(self):
        """Complex program"""
        input = """
            Var: x = 1;
            Function: foo
            Parameter: x,y,   z
            Body:
                x = 1;
                y = 1.9999;
            EndBody.

            Function: main
            Body:
                Var: x = 1, y;
                 x = foo(1,1.1, "this is a string");
                 foo( 10000, 19.99999, "");
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'), [IntLiteral(10000), FloatLiteral(19.99999), StringLiteral("")])))
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_invalid_return_type_in_if_condition(self):
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
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If([(BinaryOp('+',Id('b'), IntLiteral(0)), [], [Return(Id('a'))])], ([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_invalid_condition_in_while(self):
        """Complex program"""
        input = """
            Var: x;
            Function: main
            Body:
                Var: y;
                While x +. y Do
        
                EndWhile.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(While(BinaryOp('+.',Id('x'), Id('y')), ([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """
                Function: main  
                   Body:
                        printStrLn();
                EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main 
                       Body:
                           printStrLn(read(4));
                       EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_use_func_before_declare(self):
        """More complex program"""
        input = """Function: main 
                       Body:
                           foo(1,2);
                       EndBody.
                    
                    Function: foo 
                    Parameter: x,y
                       Body:
                       EndBody.
                """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 442))


    def test_inferred_parameter_type(self):
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
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_inferred_parameter_type_2(self):
        """More complex program"""
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
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_use_func_before_decla(self):
        """More complex program"""
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
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_undecla_func(self):
        """More complex program"""
        input = """
                    Var: a;
                    Function: main 
                       Body:
                           goo();
                       EndBody.

                    Function: foo 
                       Body:
                            Return 1;
                       EndBody.
                """
        expect = str(Undeclared(Function(), 'goo'))
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_inferred(self):
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
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_array_literal_invalid(self):
        """More complex program"""
        input = """
                Var: x[3] = { 1,2,3 };
               Function: main
               Parameter: y, a
               Body:
                   x = 1;
               EndBody.
               """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_error_asignment_with_arrayliteral(self):
        """More complex program"""
        input = """
                Var: x[3] = { 1,2,3 };
               Function: main
               Parameter: y, a
               Body:
                    a = 1;
                    Return a;
               EndBody.
               
               Function: foo
               Parameter: a
               Body:
                   a = main(1,2);
                   x = { 1,2};
               EndBody.
               """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), ArrayLiteral([IntLiteral(1), IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_error_asignment_with_arrayliteral_2(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a
               Body:
                    a = 1;
                    Return a;
               EndBody.

               Function: foo
               Parameter: a
               Body:
                   a = main(1,2);
                   a = 1;
                   x = { 1,2};
               EndBody.
               """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), ArrayLiteral([IntLiteral(1), IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_func_return_array(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a
               Body:
                    Return x;
               EndBody.

               Function: foo
               Parameter: a[3][2]
               Body:
                   a = main(1,2);
               EndBody.
               """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_invalid_binary_op(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a
               Body:
                    Return x;
               EndBody.

               Function: foo
               Parameter: a
               Body:
                   a = 1; 
                   a = a + main(1,2);
               EndBody.
               """
        expect = str(TypeMismatchInExpression(BinaryOp('+', Id('a'), CallExpr(Id('main'), [IntLiteral(1), IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_invalid_in_for_stmt(self):
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
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_inferred_type_from_for_stmt(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a, i
               Body:
                    For ( i= 1 ,i<1000, i+1 ) Do
                    EndFor.
                    i = i + 1;
               EndBody.
               """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_invalid_index_expression_in_lhs(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a, i
               Body:
                    x[1] = 1;
               EndBody.
               """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('x'), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_invalid_index_expression_with_float_dimen(self):
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
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_invalid_index_expression(self):
        """More complex program"""
        input = """
                   Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
                  Function: main
                  Parameter: y, a, i
                  Body:
                        { {1,  3}, {1,4}}[1] = 1;
                  EndBody.
                  """
        expect = str(TypeMismatchInExpression(ArrayCell(ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(3)]), ArrayLiteral([IntLiteral(1), IntLiteral(4)])]), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_invalid_index_expression_with_funccallStmt(self):
        """More complex program"""
        input = """
                   Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
                  Function: main
                  Parameter: y, a, i
                  Body:
                        foo()[1] = 1;
                  EndBody.
                  
                  Function: foo
                  Body:
                        Return {1};
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_invalid_with_function_return_array(self):
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
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_valid_assign_with_array(self):
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
                        main(1,2,3)[2][2] = main(4,5,6)[3][2];
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_multi_func_return_array(self):
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
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'), []), [IntLiteral(1), IntLiteral(2)]), IntLiteral(100))))
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_inferred_para_type_in_binary_op(self):
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
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_inferred_ele_type_in_binary_op(self):
        """More complex program"""
        input = """
                   Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
                  Function: main
                  Parameter: y, a, i
                  Body:
                        a = 1 + foo()[2];
                  EndBody.

                  Function: foo
                  Body:
                        Return {1,2};
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 463))


    def test_invalid_return_array_type(self):
        """More complex program"""
        input = """
                   Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
                  Function: main
                  Parameter: y, a, i
                  Body:
                        a = 1.1 +. foo()[2];
                  EndBody.

                  Function: foo
                  Body:
                        Return {1,2};
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(ArrayLiteral([IntLiteral(1), IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_global_variable_duplicate_build_func_name(self):
        """More complex program"""
        input = """
                   Var: bool_of_string;
                  Function: main
                  Parameter: y, a, i
                  Body:
                        a = 1.1 +. foo()[2];
                  EndBody.

                  Function: foo
                  Body:
                        Return {1.1,2.2};
                  EndBody.
                  """
        expect = str(Redeclared(Variable(), 'bool_of_string'))
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_local_variable_duplicate_build_func_name(self):
        """More complex program"""
        input = """
                   Var: x;
                  Function: main
                  Parameter: y, a, i
                  Body:
                        Var: bool_of_string;
                        a = 1.1 +. foo()[2];
                  EndBody.

                  Function: foo
                  Body:
                        Return {1.1,2.2};
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_invalid_assign_stmt(self):
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
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_not_match_dimension_of_array(self):
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
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_index_is_not_int(self):
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
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_index_operator_with_not_array_type(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { True };
                  Function: main
                  Parameter: k, a, i
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
        expect = str(TypeMismatchInStatement(Assign(Id('x'), ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])]))))
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_call_stmt_with_param_is_array(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { True };
                  Function: main
                  Parameter: k, a, i
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
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_for_stmt_with_invalid_idx_variable(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { 1 };
                  Function: main
                  Parameter: k, a, i
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
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_for_stmt(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { 1 };
                  Function: main
                  Body:
                        Return y;
                  EndBody.

                  Function: foo
                  Body:
                        Var: y = 0x9;
                        Var: i = True;
                        For ( y = x[1][1][1], 1 < main()[1][2], y + main()[2][3] ) Do
                            y = 1;
                        EndFor.

                        Return;
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_invalid_type_condition_if_stmt(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { 1 };
                  Function: main
                  Body:
                        Return y;
                  EndBody.

                  Function: foo
                  Body:
                        Var: y = 0x9;
                        Var: i = True;
                        If main()[1][2] Then
                        EndIf.
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(If([(ArrayCell(CallExpr(Id('main'), []), [IntLiteral(1), IntLiteral(2)]), [],[])], ([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_inferred_type_from_if_stmt(self):
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
                        Var: x;
                        x = { {1,2} };
                        Return 1;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_inferred_para_type_from_if_stmt(self):
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
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_inferred_return_type_from_if_stmt(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z
                  Body:
                       If foo(2,3,4)[1][2] Then
                       EndIf. 
                  EndBody.

                  Function: foo
                  Parameter: k, a, i
                  Body:
                        k = k + a + i;
                        Return { {True,False}   };
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_inferred_type_from_while_stmt(self):
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
                        Var: x;
                        x = { {1,2} };
                        Return 1;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_inferred_para_type_from_while_stmt(self):
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
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_inferred_return_type_from_while_stmt(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z
                  Body:
                       While foo(2,3,4)[1][2] Do   
                       EndWhile. 
                  EndBody.

                  Function: foo
                  Parameter: k, a, i
                  Body:
                        k = k + a + i;
                        Return { {True,False}   };
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 480))


    def test_inferred_return_type_from_for_stmt(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z
                  Body:
                       For (x = 0, x < 10, foo(2.0,3,4)[1][2]) Do
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
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_complex_program_from_check_suite(self):
        """More complex program"""
        input = """
                  Function: fact
                  Parameter: n
                  Body:
                        If n == 0 Then
                            Var: x[1] = {False};
                            Return x[1];
                        ElseIf fact(1) Then
                            Var: y=9;
                        Else
                            Var: z;
                            Return fact(n - 1);
                        EndIf.
                  EndBody.
                  
                  Function: main
                  Parameter: x,y,z
                  Body:
                       For (x = 0, fact(0x9) , 1) Do
                            y = string_of_bool(fact(1));
                            y = "this is a string";
                       EndFor.
                  EndBody.
                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_inferred_type(self):
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
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_ambigous_inferred_in_expr(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x, y ,z
                  Body:
                       y = x || (x>z); 
                  EndBody.
                  """
        expect = str(TypeMismatchInExpression(BinaryOp( '||', Id('x'),BinaryOp( '>', Id('x'),Id('z')))))
        self.assertTrue(TestChecker.test(input, expect, 484))


    def test_inferred_return_type_from_param(self):
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
                  Parameter: x,y,z
                  Body:
                       fact(x,y, foo());
                       x = x + 9;
                       y = "False";
                  EndBody.
                  
                  Function: foo
                  Body:
                       Return 1;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_inferred_array_type_from_param(self):
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
                  Parameter: x,y,z
                  Body:
                       fact(x[1][2],y, foo(1,2)[2][3]);
                       x = { { 0x9, 0x6 } };
                       y = "False";
                  EndBody.

                  Function: foo
                  Parameter: x,y
                  Body:
                       x = 100 + y; 
                       Return { { "a", "b", "c" }, { "d", "e", "f" } };
                  EndBody.
                  
                  Function: goo
                  Body:
                       foo(100,200);
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'), [IntLiteral(100), IntLiteral(200)])))
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_inferred_type_from_param(self):
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
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_inferred_type_from_param_2(self):
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
                  EndBody.

                  """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_inferred_type_variable_from_arg(self):
        """More complex program"""
        input = """
                  Function: foo
                  Parameter: x,y
                  Body:
                      x = 1.1;
                      y = False;
                      Return { True };
                  EndBody.
                  
                  Function: main
                  Parameter: x, y
                  Body:
                      foo(x,y)[0] = False;
                      x = False;
                  EndBody.

                  """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_inferred_type_2(self):
        """More complex program"""
        input = """
                  Function: foo
                  Parameter: x,y
                  Body:
                      x = 1.1;
                      y = False;
                  EndBody.

                  Function: main
                  Parameter: x, y
                  Body:
                      foo(x,y);
                  EndBody.
                  
                  Function: goo
                  Body:
                      foo(1.1,1);
                  EndBody.

                  """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'), [FloatLiteral(1.1), IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_ambigous_undeclare_variable(self):
        """More complex program"""
        input = """
                  Function: foo
                  Parameter: x,y
                  Body:
                      Var: z;
                  EndBody.

                  Function: main
                  Parameter: x, y
                  Body:
                      z = 1;
                  EndBody.
                  """
        expect = str(Undeclared(Identifier(), 'z'))
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_ambigous_variable(self):
        """More complex program"""
        input = """
                  Var: x = { { { 1,2,3 } , { 2,3,4 } } , { { 1,2,3 } , { 2,3,4 } } };
                  Function: foo
                  Parameter: z, y
                  Body:
                      Return x;
                  EndBody.

                  Function: main
                  Parameter: x, y
                  Body:
                      x = foo(1,2);
                      x[1][2] = { {1,2} };
                  EndBody.
                  """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('x'), [IntLiteral(1), IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_ambigous_variable_2(self):
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
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_same_type_array(self):
        """More complex program"""
        input = """
                  Var: x = { { { 1,2,3 } , { 2,3,4 } } , { { 1,2,3 } , { 2,3,4 } } };
                  Function: main
                  Parameter: z, y
                  Body:
                      Var: a[1], b[2];
                      a = b;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Assign(Id('a'), Id('b'))))
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_same_type_array_2(self):
        """More complex program"""
        input = """
                  Var: x = { { { 1,2,3 } , { 2,3,4 } } , { { 1,2,3 } , { 2,3,4 } } };
                  Function: main
                  Parameter: z, y
                  Body:
                      Var: a[2][2][3];
                      a = x;
                      a[1][2][3] = True;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_multi_return_invalid(self):
        """More complex program"""
        input = """
                  Var: x = { { { 1,2,3 } , { 2,3,4 } } , { { 1,2,3 } , { 2,3,4 } } };
                  Function: main
                  Parameter: z, y
                  Body:
                      Var: a[2][2][3];
                      Var: b[1][2] = { {True,False}};
                      a = x;
                      a[1][2][3] = 0x9;
                      If b[1][1] Then
                         Return 1;
                      ElseIf b[1][2] Then
                         Return 1.1;
                      EndIf.
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_return_type(self):
        """More complex program"""
        input = """
                  Function: main
                  Body:
                      Var: x;
                      x = x + foo(); 
                  EndBody.
                  
                  Function: foo
                  Body:
                      Return "string"; 
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(StringLiteral("string"))))
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_redeclared_parameter(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z,main, x
                  Body:
                      
                  EndBody.

                  Function: foo
                  Body:
                      Return "string"; 
                  EndBody.
                  """
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_redeclared_function(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z,main
                  Body:

                  EndBody.

                  Function: foo
                  Body:
                      Return "string"; 
                  EndBody.
                  
                  Function: foo
                  Body:
                  EndBody.
                  """
        expect = str(Redeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_expr_with_undeclare_func(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z,main
                  Body:
                      x = 1;
                      x = main(1,2,3,4);
                  EndBody.
                  """
        expect = str(Undeclared(Function(), 'main'))
        self.assertTrue(TestChecker.test(input, expect, 500))

    def test_call_expr_with_undeclare_func_2(self):
        """More complex program"""
        input = """
                  Function: main
                  Parameter: x,y,z,int_of_float
                  Body:
                      x = 1;
                      x = int_of_float(1.1);
                  EndBody.
                  """
        expect = str(Undeclared(Function(), 'int_of_float'))
        self.assertTrue(TestChecker.test(input, expect, 501))

    def test_global_variable_same_name_built_in_func(self):
        """More complex program"""
        input = """
                  Var: int_of_float;
                  Function: main
                  Parameter: x,y,z
                  Body:
                      x = 1;
                      x = int_of_float(1.1);
                  EndBody.
                  """
        expect = str(Redeclared(Variable(), 'int_of_float'))
        self.assertTrue(TestChecker.test(input, expect, 502))







