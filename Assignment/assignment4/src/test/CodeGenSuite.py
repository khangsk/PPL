import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test1_int(self):
        """Simple program: int main() {} """
        input = """
                    Function: main
                   Body:        
                        print(string_of_int(12111));
                   EndBody."""
        expect = "12111"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test2_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],([],[
    			CallStmt(Id("print"),[
                    CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
    	expect = "120"
    	self.assertTrue(TestCodeGen.test(input,expect,502))

    def test3_int(self):
        input = """
                    Var: x = 111;
                    Function: main
                   Body:        
                        Var: y = 12;
                        print(string_of_int(-12));
                        print(string_of_int(x));
                   EndBody."""
        expect = "-12111"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    
    def test4_bool(self):
        input = """
                    Function: main
                   Body:        
                        Var: y = True;
                        print(string_of_bool(y));
                   EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test5_float(self):
        input = """
                    Function: main
                   Body:        
                        Var: y = 123.0;
                        printStrLn(string_of_float(y));
                   EndBody."""
        expect = "123.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test6_string(self):
        input = """
                    Function: main
                   Body:        
                        Var: y = "Hello, Im Khang";
                        printStrLn(y);
                   EndBody."""
        expect = "Hello, Im Khang\n"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    
    def test7_unary(self):
        input = """
                    Function: main
                   Body:        
                        Var: y = 1;
                        y = -2;
                        printStrLn(string_of_int(y));
                   EndBody."""
        expect = "-2\n"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    
    def test8_unary(self):
        input = """
                    Function: main
                   Body:        
                        Var: y = 0.;
                        y = -.2.0;
                        printStrLn(string_of_float(y));
                   EndBody."""
        expect = "-2.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test9_unary(self):
        input = """
                    Function: main
                   Body:        
                        printStrLn(string_of_bool(!True));
                   EndBody."""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    
    def test10_binary(self):
        input = """
                    Function: main
                   Body:        
                        
                        printStrLn(string_of_bool(True || False));
                        printStrLn(string_of_bool(False || False));
                        print(string_of_bool(False || True));
                   EndBody."""
        expect = "true\nfalse\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    
    def test11_binary(self):
        input = """
                    Function: main
                   Body:        
                        
                        printStrLn(string_of_bool(True && False));
                        printStrLn(string_of_bool(True && True));
                        print(string_of_bool(False && True));
                   EndBody."""
        expect = "false\ntrue\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test12_binary(self):
        input = """
                    Function: main
                   Body:        
                        Var: x = 0;
                        x = x + 5;
                        x = x - 10;
                        x = x * -2;
                        printStrLn(string_of_int(x));
                        x = x + 1;
                        printStrLn(string_of_int(x));
                        x = x \\ 2;
                        printStrLn(string_of_int(x));
                        x = x % 3;
                        printStrLn(string_of_int(x));
                   EndBody."""
        expect = "10\n11\n5\n2\n"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    
    def test13_binary(self):
        input = """
                    Function: main
                   Body:        
                        Var: x = 0.;
                        x = x +. 5.;
                        x = x -. 10.;
                        x = x *. -.2.;
                        printStrLn(string_of_float(x));
                        x = x +. 1.;
                        printStrLn(string_of_float(x));
                        x = x \\. 2.;
                        printStrLn(string_of_float(x));
                   EndBody."""
        expect = "10.0\n11.0\n5.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test14_binary(self):
        input = """
                    Function: main
                   Body:        
                        print(string_of_bool(True && (1 + 2 >= 3) && (3 != 4)));

                   EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    
    def test15_binary(self):
        input = """
                    Function: main
                   Body:        
                        print(string_of_bool(False || (10 * 5 > 60) || (3 == 4)));

                   EndBody."""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test16_binary(self):
        input = """
                    Function: main
                   Body:        
                        print(string_of_bool(False || (10. *. 5. >=. 60.) || (3 == 4)));

                   EndBody."""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test17_binary(self):
        input = """
                    Function: main
                   Body:        
                        Var: x = True;
                        x = (3 == 3) && (10 != 9) && (100 > -10) && (-2 < 0) && (90 >= 90) && (-12 <= -12);
                        print(string_of_bool(x));

                   EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    
    def test18_binary(self):
        input = """
                    Function: main
                   Body:        
                        Var: x = True;
                        x = (10.12 =/= 9.5) && (10.5 >. 10.) && (-.2.0001 <. -.2.) && (90.1 >=. 90.1) && (-.12. <=. -.12.);
                        print(string_of_bool(x));

                   EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test19_if(self):
        input = """
                    Function: main
                   Body:        
                        Var: x = 5;
                        x = x - 1;
                        If (x < 0) Then print("Nho hon 0");
                        ElseIf (x == 0) Then print("Bang 0");
                        ElseIf (x == 1) Then print("stop");
                        Else
                            Var: y = 100;
                            x = x + y;
                            print(string_of_int(x));
                        EndIf.
                   EndBody."""
        expect = "104"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test20_if(self):
        input = """
                    Function: main
                   Body:        
                        Var: x = 0;
                        x = x - 1;
                        If (x < 0) Then print("Nho hon 0");
                        ElseIf (x == 0) Then print("Bang 0");
                        ElseIf (x == 1) Then print("stop");
                        Else
                            print(string_of_int(x));
                        EndIf.
                   EndBody."""
        expect = "Nho hon 0"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test21_if(self):
        input = """
                    Function: main
                   Body:        
                        Var: x = 2;
                        x = x - 1;
                        If (x < 0) Then print("Nho hon 0");
                        ElseIf (x == 0) Then print("Bang 0");
                        ElseIf (x == 1) Then 
                            Var: x = 123456, s = "1";
                            s = string_of_int(x);
                            print(s);
                        Else
                            print(string_of_int(x));
                        EndIf.
                   EndBody."""
        expect = "123456"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test22_while(self):
        input = """
                    Function: main
                   Body:        
                        Var: x = 5;
                        While (x >= 0) Do
                            print(string_of_int(x));
                            x = x - 1;
                        EndWhile.
                   EndBody."""
        expect = "543210"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    
    def test23_while(self):
        input = """
                    Var: x = 10;
                    Function: main
                   Body:        
                        Var: x = 10;
                        While (x >= 0) Do
                            Var: y = 2;
                            If (x % 2 == 0) Then
                                print(string_of_int(x));
                            Else
                                x = x - y;
                            EndIf.
                            x = x - 1;
                        EndWhile.
                   EndBody."""
        expect = "1062"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    
    def test24_while(self):
        input = """
                    Function: main
                   Body:        
                        Var: x = 5;
                        While (x >= 0) Do
                            Var: y = 1;
                            If (x > y) Then
                                print(string_of_int(x));
                            ElseIf (x == y) Then
                                Break;
                            Else
                                print(string_of_int(x));
                            EndIf.
                            x = x - 1;
                        EndWhile.
                   EndBody."""
        expect = "5432"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test25_do_while(self):
        input = """
                    Function: main
                   Body:        
                        Var: n = 10;
                        Do
                            If (n % 2 != 0) Then
                                print(string_of_int(n));
                            EndIf.
                            n = n - 1;
                        While (n >= 0) EndDo.
                   EndBody."""
        expect = "97531"
        self.assertTrue(TestCodeGen.test(input,expect,525))
    
    def test26_do_while(self):
        input = """
                    Function: main
                   Body:        
                        Var: n = 10;
                        Do
                            Var: x = 5, y = 4;
                            If ((n + x) % y == 0) Then
                                print(string_of_int(n));
                            EndIf.
                            n = n - 1;
                        While (n >= 0) EndDo.
                   EndBody."""
        expect = "73"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test27_for(self):
        input = """
                    Function: main
                   Body:        
                        Var: i = 0;
                        For (i = 0, i < 10, 1) Do
                            print(string_of_int(i));
                        EndFor.
                   EndBody."""
        expect = "0123456789"
        self.assertTrue(TestCodeGen.test(input,expect,527))
    
    def test28_for(self):
        input = """
                    Function: main
                   Body:        
                        Var: i = 0;
                        For (i = 0, i <= 10, 2) Do
                            print(string_of_int(i));
                        EndFor.
                   EndBody."""
        expect = "0246810"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test29_for(self):
        input = """
                    Function: main
                   Body:        
                        Var: i = 0;
                        For (i = 0, i <= 10, 1) Do
                            Var: x = 11;
                            If ((x + i) % 3 == 0) Then
                                print(string_of_int(i));
                            EndIf.
                            If (i > 8) Then
                                Break;
                            EndIf.
                        EndFor.
                   EndBody."""
        expect = "147"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test30(self):
        input = """
        Function: foo
        Body:
            print(string_of_int(1));
        EndBody.
        Function: main
        Body: 
            foo();
            print(string_of_int(120));
        EndBody."""
        expect = "1120"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test31(self):
        input = """
        Function: foo
        Body:
            Var: a = 1, b = 2;
            print(string_of_int(a + b));
        EndBody.
        Function: main
        Body: 
            print(string_of_int(0));
            foo();
            print(string_of_int(120));
        EndBody."""
        expect = "03120"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test32(self):
        input = """
        Function: foo
        Body:
            Var: a = 1, b = 2;
            print(string_of_int(a + b));
        EndBody.
        Function: main
        Body: 
            print(string_of_int(0));
            foo();
            foo1(2,3);
            print(string_of_int(120));
        EndBody.
        Function: foo1
        Parameter: x, y
        Body:
            print(string_of_int(x + y));
        EndBody.
        """
        expect = "035120"
        self.assertTrue(TestCodeGen.test(input,expect,532))
    
    def test33(self):
        """Simple program: int main() {} """
        input = """
        Function: foo1
        Parameter: x, y
        Body:
            print(string_of_int(x + y));
        EndBody.
        Function: foo
        Body:
            Var: a = 1, b = 2;
            print(string_of_int(a + b));
            foo1(2,3);
        EndBody.
        Function: main
        Body: 
            print(string_of_int(0));
            foo();
            print(string_of_int(120));
        EndBody.
        """
        expect = "035120"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    
    def test34(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            print(string_of_int(1));
            Return a + b;
        EndBody.
        Function: main
        Body: 
            Var: x = 10;
            x = x + foo(3, 4);
            print(string_of_int(x + 120));
        EndBody."""
        expect = "1137"
        self.assertTrue(TestCodeGen.test(input,expect,534))
    
    def test35(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Return a + b;
        EndBody.
        Function: main
        Body: 
            Var: x = 4;
            If (x > foo(3,4)) Then
                print(string_of_int(x));
            Else
                print(string_of_int(foo(3,5)));
            EndIf.
        EndBody."""
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test36(self):
        input = """
        Function: foo1
        Parameter: a, b
        Body:
            Return a * b;
        EndBody.
        Function: foo
        Parameter: a, b
        Body:
            Return a + b + foo1(4,5);
        EndBody.
        Function: main
        Body: 
            Var: x = 4;
            If (x > foo(3,4)) Then
                print(string_of_int(x));
            Else
                print(string_of_int(foo(3,5)));
            EndIf.
        EndBody."""
        expect = "28"
        self.assertTrue(TestCodeGen.test(input,expect,536))
    
    def test37(self):
        input = """
        Function: prime
        Parameter: n
        Body:
            If (n < 2) Then
                Return False;
            ElseIf ((n == 2) || (n == 3)) Then
                Return True;
            Else
                Var: i = 0;
                For (i = 2, i < n, 1) Do
                    If (n % i == 0) Then
                        Return False;
                    EndIf.
                EndFor.
                Return True;
            EndIf.
            Return True;
        EndBody.
        Function: main
        Body: 
            Var: x = 15, i = 0;
            For (i = 0, i < x, 1) Do
                If (prime(i)) Then
                    printStrLn(string_of_int(i));
                EndIf.
            EndFor.
        EndBody."""
        expect = "2\n3\n5\n7\n11\n13\n"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    
    def test38(self):
        input = """
        Function: even
        Parameter: n
        Body:
            If (n % 2 == 0) Then
                Return True;
            Else
                Return False;
            EndIf.
        EndBody.
        Function: main
        Body: 
            Var: x = 15, i = 0;
            For (i = 0, i < x, 1) Do
                If (!even(i)) Then
                    printStrLn(string_of_int(i));
                EndIf.
            EndFor.
        EndBody."""
        expect = "1\n3\n5\n7\n9\n11\n13\n"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test38(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            Return n +. 1.0;
        EndBody.
        Function: main
        Body: 
            Var: x = 5;
            While (check(x)) Do
                Var: y = 0.;
                y = y +. float_to_int(x);
                print(string_of_float(y));
                x = x - 1;
            EndWhile.
        EndBody.
        Function: check
        Parameter: x
        Body:
            If (x > 0) Then
                Return True;
            EndIf.
            Return False;
        EndBody."""
        expect = "5.04.03.02.01.0"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test39(self):
        input = """
        Var: x[3][3][2] = 
        {
            {
                {4, 5}, {8, 4}, {9, 7}
            }, 
            {
                {1, 0}, {4, 8}, {7, 6}
            }, 
            {
                {5, 5}, {9, 0}, {4, 2}
            }
        };
        Var: y[2] = {5, 7};
        Function: main
        Body: 
           print(string_of_int(x[2][1][0] * y[0]));
        EndBody.
        """
        expect = "45"
        self.assertTrue(TestCodeGen.test(input,expect,539))
    
    def test40(self):
        input = """
        Function: main
        Body: 
               Var: x[3][3][2] = 
        {
            {
                {4, 5}, {8, 4}, {9, 7}
            }, 
            {
                {1, 0}, {4, 8}, {7, 6}
            }, 
            {
                {5, 5}, {9, 0}, {4, 2}
            }
        };
            print(string_of_int(x[1][1][0]));
        EndBody.
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    
    
    def test41(self):
        input = """
        Var: x[3][3][2] = 
        {
            {
                {4, 5}, {8, 4}, {9, 7}
            }, 
            {
                {1, 0}, {4, 8}, {7, 6}
            }, 
            {
                {5, 5}, {9, 0}, {4, 2}
            }
        };
        Function: main
        Body: 
            Var: y[2] = {5, 7};
           print(string_of_int(x[2][1][0] * y[0]));
        EndBody.
        """
        expect = "45"
        self.assertTrue(TestCodeGen.test(input,expect,541))

    def test42(self):
        input = """
        Function: main
        Body: 
            Var: x[3] = {"Hoang", "Gia", "Khang"};
            Var: i = 0;
            For (i = 0, i < 3, 1) Do
                print(x[i]);
            EndFor.
        EndBody.
        """
        expect = "HoangGiaKhang"
        self.assertTrue(TestCodeGen.test(input,expect,542))

    def test43(self):
        input = """
        Function: main
        Body: 
            Var: x[3] = {5, 7, 9};
            print(string_of_int(x[1] + foo()[0]));
        EndBody.
        Function: foo
        Body:
            Var: y[2] = {1, 2};
            Return y;
        EndBody.
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,543))
    
    def test44(self):
        input = """
        Function: main
        Body: 
            Var: x[3] = {5, 7, 9};
            print(string_of_int(x[1] + foo(3, 4)[0]));
        EndBody.
        Function: foo
        Parameter: m, n
        Body:
            Var: y[2] = {1, 2};
            print(string_of_int(m*n));
            Return y;
        EndBody.
        """
        expect = "128"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    
    def test45(self):
        input = """
        Function: main
        Body: 
            Var: x[3] = {5, 7, 9};
            print(string_of_int(x[1] + foo1()));
        EndBody.
        Function: foo
        Body:
            Var: x[2] = {1, 2};
            Return x;
        EndBody.
        Function: foo1
        Body:
            Return foo()[1];
        EndBody.
        """
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    
    def test46(self):
        input = """
        Function: main
        Body: 
            Var: x[3] = {5, 7, 9};
            print(string_of_int(foo1(3)));
            print(string_of_int(x[1] + foo1(foo()[1])));
        EndBody.
        Function: foo
        Body:
            Var: x[2] = {1, 2};
            Return x;
        EndBody.
        Function: foo1
        Parameter: x
        Body:
            Return x;
        EndBody.
        """
        expect = "39"
        self.assertTrue(TestCodeGen.test(input,expect,546))

    def test47(self):
        input = """
        Function: foo
        Parameter: x
        Body:
            Var: t = 1;
            t = x;
            Return x;
        EndBody.
        Function: foo1
        Parameter: x
        Body:
            Return x + foo(5);
        EndBody.
        Function: main
        Body: 
            Var: a = True;
            print(string_of_int(foo1(4)));
            print(string_of_bool(a));
        EndBody.
        """
        expect = "9true"
        self.assertTrue(TestCodeGen.test(input,expect,547))

    def test48(self):
        input = """
        Function: foo
        Body:
            Return {1,2,3,4};
        EndBody.
        Function: main
        Body: 
            print(string_of_int(foo()[2]));
        EndBody.
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,548))
    
    def test49(self):
        input = """
        Function: foo
        Body:
            Return {1.,2.,3.,4.};
        EndBody.
        Function: main
        Body: 
            print(string_of_float(foo()[1]));
        EndBody.
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,549))

    def test50(self):
        input = """
        Function: foo
        Body: 
            Return {"Hoang", "Gia", "Khang"};
        EndBody.
        Function: main
        Body: 
            print(foo()[2]);
        EndBody.
        """
        expect = "Khang"
        self.assertTrue(TestCodeGen.test(input,expect,550))
    
    def test551(self):
        input = r"""
Function: main
    Body:
        Var: i = 0, a = 100;

        printLn();
        Do
            Var: a = 0;
            print(string_of_int(a));
            a = a + 1;
            i = i + 1;
        While i < 5 EndDo.
        printLn();
        printStrLn(string_of_int(a));
    EndBody.
"""
        expect = r"""
00000
100
"""
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    ##""" Do-While with Break """

    def test552(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        Do
            print(string_of_int(i));
            i = i + 1;
            Break;
        While i < 5 EndDo.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
0
1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test553(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        Do
            print(string_of_int(i));
            i = i + 1;
            If i == 3 Then
                Break;
            EndIf.
        While i < 5 EndDo.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
012
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    ##""" Do-While with Continue """

    def test554(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        Do
            print(string_of_int(i));
            i = i + 1;
            Continue;
        While i < 5 EndDo.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
01234
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test555(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        Do
            i = i + 1;
            If i < 3 Then
                Continue;
            EndIf.
            print(string_of_int(i));
        While i < 5 EndDo.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
345
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    ##""" For (simple) """

    def test556(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            print(string_of_int(i));
        EndFor.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
01234
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test557(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 0, 1) Do
            print(string_of_int(i));
        EndFor.
        printStrLn("No iteration");
    EndBody.
"""
        expect = r"""
No iteration
"""
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test558(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            Var: i = 3;
            print(string_of_int(i));
            i = i + 1;
        EndFor.
        printLn();
    EndBody.
"""
        expect = r"""
33333
"""
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test559(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 10, 1) Do
            print(string_of_int(i));
            i = i + 1;
        EndFor.
        printLn();
    EndBody.
"""
        expect = r"""
02468
"""
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test560(self):
        input = r"""
Function: main
    Body:
        Var: i = 0, step = 0;
        printLn();
        For (i = 0, i < 20, step) Do
            printStrLn(string_of_int(i));
            i = i + 1;
            step = step + 1;
        EndFor.
    EndBody.
"""
        expect = r"""
0
2
5
9
14
"""
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    ##""" For with Break """

    def test561(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            print(string_of_int(i));
            Break;
        EndFor.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
0
0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test562(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            print(string_of_int(i));
            If i == 3 Then
                Break;
            EndIf.
        EndFor.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
0123
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    ##""" For with Continue """

    def test563(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            print(string_of_int(i));
            Continue;
        EndFor.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
01234
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test564(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            If i < 3 Then
                Continue;
            EndIf.
            print(string_of_int(i));
        EndFor.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
34
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    #""" Return (simple) """

    def test565(self):
        input = r"""
Function: main
    Body:
        Var: condition = False;
        printLn();
        If condition Then
            printStrLn("Not return first");
        Else
            printStrLn("Return first");
            Return;
        EndIf.
        printStrLn("This line should not be printed");
    EndBody.
"""
        expect = r"""
Return first
"""
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    ##""" Array declaration """

    def test566(self):
        input = r"""
Var: a[1] = {1}, b[1] = {1.}, c[1] = {True}, d[1] = {"Hi!"};

Function: main
    Body:
        printLn();
        printStrLn(string_of_int(a[0]));
        printStrLn(string_of_float(b[0]));
        printStrLn(string_of_bool(c[0]));
        printStrLn(d[0]);
    EndBody.
"""
        expect = r"""
1
1.0
true
Hi!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test567(self):
        input = r"""
Var: a[2][2] = {{1,2},{3,4}};
Var: b[2][2] = {{1.,2.},{3.,4.}};
Var: c[2][2] = {{True,False},{False,True}};
Var: d[2][2] = {{"A","B"},{"C","D"}};

Function: main
    Body:
        printLn();
        printStrLn(string_of_int(a[1][1]));
        printStrLn(string_of_float(b[1][1]));
        printStrLn(string_of_bool(c[1][1]));
        printStrLn(d[1][1]);
    EndBody.
"""
        expect = r"""
4
4.0
true
D
"""
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test568(self):
        input = r"""
Var: a[1][1][1][1][1] = {{{{{1}}}}};
Var: b[1][1][1][1][1] = {{{{{1.}}}}};
Var: c[1][1][1][1][1] = {{{{{True}}}}};
Var: d[1][1][1][1][1] = {{{{{"Hi!"}}}}};

Function: main
    Body:
        printLn();
        printStrLn(string_of_int(a[0][0][0][0][0]));
        printStrLn(string_of_float(b[0][0][0][0][0]));
        printStrLn(string_of_bool(c[0][0][0][0][0]));
        printStrLn(d[0][0][0][0][0]);
    EndBody.
"""
        expect = r"""
1
1.0
true
Hi!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    #""" Array store """

    def test569(self):
        input = r"""
Var: a[1] = {1}, b[1] = {1.}, c[1] = {True}, d[1] = {"Hi!"};

Function: main
    Body:
        a[0] = 2;
        b[0] = 2.;
        c[0] = False;
        d[0] = "Hello!";
        printLn();
        printStrLn(string_of_int(a[0]));
        printStrLn(string_of_float(b[0]));
        printStrLn(string_of_bool(c[0]));
        printStrLn(d[0]);
    EndBody.
"""
        expect = r"""
2
2.0
false
Hello!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test570(self):
        input = r"""
Var: a[2][2] = {{1,2},{3,4}};
Var: b[2][2] = {{1.,2.},{3.,4.}};
Var: c[2][2] = {{True,False},{False,True}};
Var: d[2][2] = {{"A","B"},{"C","D"}};

Function: main
    Body:
        a[1][1] = 5;
        b[1][1] = 5.;
        c[1][1] = False;
        d[1][1] = "Hi!";
        printLn();
        printStrLn(string_of_int(a[1][1]));
        printStrLn(string_of_float(b[1][1]));
        printStrLn(string_of_bool(c[1][1]));
        printStrLn(d[1][1]);
    EndBody.
"""
        expect = r"""
5
5.0
false
Hi!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test571(self):
        input = r"""
Var: a[1][1][1][1][1] = {{{{{1}}}}};
Var: b[1][1][1][1][1] = {{{{{1.}}}}};
Var: c[1][1][1][1][1] = {{{{{True}}}}};
Var: d[1][1][1][1][1] = {{{{{"Hi!"}}}}};

Function: main
    Body:
        a[0][0][0][0][0] = 2;
        b[0][0][0][0][0] = 2.;
        c[0][0][0][0][0] = False;
        d[0][0][0][0][0] = "Hello!";
        printLn();
        printStrLn(string_of_int(a[0][0][0][0][0]));
        printStrLn(string_of_float(b[0][0][0][0][0]));
        printStrLn(string_of_bool(c[0][0][0][0][0]));
        printStrLn(d[0][0][0][0][0]);
    EndBody.
"""
        expect = r"""
2
2.0
false
Hello!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    ##""" Array assign """

    def test572(self):
        input = r"""
Var: a[1] = {1}, b[1] = {1.}, c[1] = {True}, d[1] = {"Hi!"};

Function: main
    Body:
        a = {2};
        b = {2.};
        c = {False};
        d = {"Hello!"};
        printLn();
        printStrLn(string_of_int(a[0]));
        printStrLn(string_of_float(b[0]));
        printStrLn(string_of_bool(c[0]));
        printStrLn(d[0]);
    EndBody.
"""
        expect = r"""
2
2.0
false
Hello!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test573(self):
        input = r"""
Var: a[2][2] = {{1,2},{3,4}};
Var: b[2][2] = {{1.,2.},{3.,4.}};
Var: c[2][2] = {{True,False},{False,True}};
Var: d[2][2] = {{"A","B"},{"C","D"}};

Function: main
    Body:
        a = {{11,12},{13,14}};
        b = {{11.,12.},{13.,14.}};
        c = {{False,True},{True,False}};
        d = {{"X","Y"},{"Z","T"}};
        printLn();
        printStrLn(string_of_int(a[1][1]));
        printStrLn(string_of_float(b[1][1]));
        printStrLn(string_of_bool(c[1][1]));
        printStrLn(d[1][1]);
    EndBody.
"""
        expect = r"""
14
14.0
false
T
"""
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test574(self):
        input = r"""
Var: a[1][1][1][1][1] = {{{{{1}}}}};
Var: b[1][1][1][1][1] = {{{{{1.}}}}};
Var: c[1][1][1][1][1] = {{{{{True}}}}};
Var: d[1][1][1][1][1] = {{{{{"Hi!"}}}}};

Function: main
    Body:
        a = {{{{{2}}}}};
        b = {{{{{2.}}}}};
        c = {{{{{False}}}}};
        d = {{{{{"Hello!"}}}}};
        printLn();
        printStrLn(string_of_int(a[0][0][0][0][0]));
        printStrLn(string_of_float(b[0][0][0][0][0]));
        printStrLn(string_of_bool(c[0][0][0][0][0]));
        printStrLn(d[0][0][0][0][0]);
    EndBody.
"""
        expect = r"""
2
2.0
false
Hello!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    ##""" Short circuit """

    def test575(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(False && (1 \ 0 == 0)));
    EndBody.
"""
        expect = r"""
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test576(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(True || (1 \ 0 == 0)));
    EndBody.
"""
        expect = r"""
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    # PART 2: INFERENCE

    # PART 3: COMPLEX PROGRAM

    def test577(self):
        input = r"""
** Selection sort **

Var: arr[10] = {1, 7, 8, 4, 2, 5, 9, 10, 6, 3};
Function: main
    Body:
        Var: i = 0;
        For (i = 0, i < 10, 1) Do
            Var: j = 0, minIndex = 0, temp = 0;
            ** Find min index **
            minIndex = i;
            For (j = i + 1, j < 10, 1) Do
                If arr[j] < arr[minIndex] Then
                    minIndex = j;
                EndIf.
            EndFor.
            ** Swap **
            temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        EndFor.

        print("\nSorted array:");
        For (i = 0, i < 10, 1) Do
            print(" ");
            print(string_of_int(arr[i]));
        EndFor.
        printLn();
    EndBody.
"""
        expect = r"""
Sorted array: 1 2 3 4 5 6 7 8 9 10
"""
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test578(self):
        input = r"""
** Find prime number **

Function: main
    Body:
        Var: i = 0, n = 50;
        print("\nPrime numbers that less than ");
        print(string_of_int(n));
        print(":");
        For (i = 2, i < n, 1) Do
            Var: isPrime = True, j = 2;
            ** Check if prime **
            For (j = 2, j < i - 1, 1) Do
                ** Early terminate **
                If j * j > i Then
                    Break;
                EndIf.
                If i % j == 0 Then
                    isPrime = False;
                    Break;
                EndIf.
            EndFor.
            ** Print if prime **
            If isPrime Then
                print(" ");
                print(string_of_int(i));
            EndIf.
        EndFor.
        printLn();
    EndBody.
"""
        expect = r"""
Prime numbers that less than 50: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
"""
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test579(self):
        input = r"""
** Find first positive missing value **

Var: arr[15] = {
    0, 3, 4, 100, 2,
    20, 1, 99, 7, 8,
    6, 2, 5, 10, 12
};

Function: main
    Body:
        Var: n = 15, hashTable[15] = {
            False,False,False,False,False,
            False,False,False,False,False,
            False,False,False,False,False
        };
        Var: i = 0, firstMissValue = 0;
        ** Iterate and save to hash table **
        For (i = 0, i < n, 1) Do
            If (arr[i] > n) || (arr[i] <= 0) Then
                Continue;
            EndIf.
            hashTable[arr[i] - 1] = True;
        EndFor.
        ** Find first miss value **
        firstMissValue = 1;
        While (firstMissValue <= n) && hashTable[firstMissValue - 1] Do
            firstMissValue = firstMissValue + 1;
        EndWhile.
        print("\nFirst positive missing value: ");
        printStrLn(string_of_int(firstMissValue));
    EndBody.
"""
        expect = r"""
First positive missing value: 9
"""
        self.assertTrue(TestCodeGen.test(input, expect, 579))
    
    def test80(self):
        input = """
                    Function: foo
                    Parameter: a[2][2]
                    Body:
                        print(string_of_float(a[1][1]));
                    EndBody.
                    Function: main
                    Body:
                        foo({{1., 2.},{3., 4.}});
                        print("h");
                    EndBody.
                """
        expect = "4.0h"
        self.assertTrue(TestCodeGen.test(input,expect,580))
    
    def test81(self):
        input = """
                    Function: foo
                    Parameter: a[2][2]
                    Body:
                        print(a[1][1]);
                    EndBody.
                    Function: main
                    Body:
                        foo({{"Hoang", "Gia"}, {"Khang", "CSE"}});
                    EndBody.
                """
        expect = "CSE"
        self.assertTrue(TestCodeGen.test(input,expect,581))
    
    def test82(self):
        input = """
                    Function: fact
                    Parameter: n
                    Body:
                        If (n == 1) Then
                            Return 1;
                        EndIf.
                        Return n * fact(n - 1);
                    EndBody.
                    Function: main
                    Body:
                        print(string_of_int(fact(5)));
                    EndBody.
                """
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,582))
    
    def test83_fibo(self):
        input = """
                    Function: fibonaci
                    Parameter: n
                    Body:
                        If (n == 0) Then
                            Return 0;
                        ElseIf (n == 1) Then
                            Return 1;
                        EndIf.
                        Return fibonaci(n - 1) + fibonaci(n - 2);
                    EndBody.
                    Function: main
                    Body:
                        print(string_of_int(fibonaci(5)));
                    EndBody.
                """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test84(self):
        input = """
                Function: foo
                Parameter: a[4], n
                Body:
                    While (n > 0) Do
                        n = n - 1;
                        printStrLn(string_of_int(a[n]));
                    EndWhile.
                EndBody.
                Function: main
                Body:
                    foo({5,4,8,9}, 4);
                EndBody.
                """
        expect = "9\n8\n4\n5\n"
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test85(self):
        input = """
            Function: foo
            Parameter: a[4], n
            Body:
                While (n > 0) Do
                    n = n - 1;
                    printStrLn(string_of_float(a[n]));
                EndWhile.
            EndBody.
            Function: main
            Body:
                foo({5.,4.,8.,9.}, 4);
            EndBody.
                """
        expect = "9.0\n8.0\n4.0\n5.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,585))

    def test86(self):
        input = """
                    Function: foo
                    Parameter: a[2][2]
                    Body:
                        print(a[1][1]);
                    EndBody.
                    Function: main
                    Parameter: x
                    Body:
                        x = 1;
                        foo({{"Hoang", "Gia"}, {"Khang", "CSE"}});
                        print(string_of_int(x));
                    EndBody.
                """
        expect = "CSE1"
        self.assertTrue(TestCodeGen.test(input,expect,586))

    def test87(self):
        input = r"""
            Function: prime_number
            Parameter: n
            Body:
                Var: i = 0;
                If n < 2 Then
                    Return False;
                EndIf.
                If (n == 2) || (n == 3) Then
                    Return True;
                EndIf.
                For (i = 2, i < n, 1) Do
                    If n % i == 0 Then
                        Return False;
                    EndIf.
                EndFor.
                Return True;
            EndBody.
            Function: main
            Body:
                Var: i = 0;
                For (i = 0, i < 100, 1) Do
                    If prime_number(i) Then
                        print(string_of_int(i));
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "2357111317192329313741434753596167717379838997"
        self.assertTrue(TestCodeGen.test(input,expect,587))

    def test88(self):
        input = r"""
            Function: main
            Body:
                Var: a___b = 12345;
                Var: b = True, c = 123.;
                If b Then
                    c = c +. 1.;
                    print(string_of_float(c));
                ElseIf !b Then
                    Return c;
                EndIf.
                Return float(a___b) + c;
            EndBody.
        """
        expect = "124.0"
        self.assertTrue(TestCodeGen.test(input,expect,588))
    
    def test89(self):
        input = r"""
            Var: arr[3][2] = {{1, 2}, {4, 5}, {3, 5}};
            Function: main
            Body:
                Var: p = 1, i = 0, j = 0;
                For (i = 0, i < 3, 1) Do
                    For (j = 0, j < 2, 1) Do
                        p = p * arr[i][j];
                    EndFor.
                EndFor.
                print(string_of_int(p));
            EndBody.
        """
        expect = "600"
        self.assertTrue(TestCodeGen.test(input,expect,589))
    
    def test90(self):
        input = r"""
            Var: string[3] = {"1.23", "0.e4", "12e2"};
            Function: main
            Body:
                Var: x[3] = {0., 0., 0.}, sum = 0., i = 0;
                For (i = 0, i < 3, 1) Do
                    x[i] = float_of_string(string[i]);
                    sum = sum +. x[i];
                EndFor.
                print(string_of_float(sum));
            EndBody.
        """
        expect = "1201.23"
        self.assertTrue(TestCodeGen.test(input,expect,590))

    def test91(self):
        input = r"""
            Var: string[3] = {"1.23", "0.e4", "12e2"};
            Function: main
            Body:
                Var: sum = 0, i = 0;
                For (i = 0, i < 3, 1) Do
                    sum = sum + int_of_float(float_of_string(string[i]));
                EndFor.
                print(string_of_int(sum));
            EndBody.
        """
        expect = "1201"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test92(self):
        input = r"""
            Function: main
            Body:
                Var: r = 10.;
                print("The tich hinh cau ban kinh r = ");
                print(string_of_float(r));
                print(" la: ");
                print(string_of_float(theTich(r)));
            EndBody.
            Function: theTich
            Parameter: r
            Body:
                Return (4. \. 3.) *. 3.14 *. r *. r *.r;
            EndBody.
        """
        expect = "The tich hinh cau ban kinh r = 10.0 la: 4186.667"
        self.assertTrue(TestCodeGen.test(input,expect,592))
    
    def test93(self):
        input = r"""
            Function: foo
            Parameter: a, b
            Body:
                printStrLn(string_of_float(float_to_int(a) *. b));
            EndBody.
            Function: main
            Body:
                Var: x = 5, y = 4.;
                foo(2 + x, 3. \. y);
                goo();
            EndBody.
            Function: goo
            Body:
                printStrLn("Nothing to print!!!");
            EndBody.
        """
        expect = "5.25\nNothing to print!!!\n"
        self.assertTrue(TestCodeGen.test(input,expect,593))

    def test94(self):
        input = r"""
            Function: main
            Body:
                If bool_of_string("True") Then
                    print("Dung roi");
                Else
                    print("Sai roi");
                EndIf.
            EndBody.
        """
        expect = "Dung roi"
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test95(self):
        input = """
                    Function: main
                    Parameter: x, c[2][2]
                    Body:
                        c = {{4,5},{6,7}};
                        print(string_of_int(c[1][0]));
                    EndBody.
                """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,595))
    
    def test92(self):
        input = r"""
            Function: main
            Body:
                
            EndBody.
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,592))
    
    def test92(self):
        input = r"""
            Function: main
            Body:
                
            EndBody.
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,592))
    
    def test92(self):
        input = r"""
            Function: main
            Body:
                
            EndBody.
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,592))
    
    # def test99(self):
    #     input = r"""
    #         Function: foo
    #         Parameter: a[5], b
    #         Body:
    #             Var: i = 0;
    #             While (i < 5) Do
    #                 a[i] = b +. 1.0 +. float_to_int(i);
    #                 i = i + 1;
    #             EndWhile.
    #             i = 0;
    #             While (i < 5) Do
    #                 print(string_of_float(a[i]));
    #                 i = i + 1;
    #             EndWhile.
    #         EndBody.
    #         Function: main
    #         Body:
    #             Var: a[5] = {0., 0., 0., 0., 0.}, b = 2.;
    #             foo(a, b);
    #         EndBody.
    #     """
    #     expect = "3.04.05.06.07.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,599))
    
    # def test100(self):
    #     input = r"""
    #         Function: main
    #         Body:
    #             Var: b[3][4] = {{2.3 , 5., 7.4, 4.}, {6., 17., 9.12, 30.}, {0., 10.3, 5., 2.4}}, a[6] = {1,2,3,4,5,6}, i = 0;
    #             a[3 + foo(2)] = a[int_of_float(b[2][3])] + 4;
    #             For (i = 0, i < 6, 1) Do
    #                 print(string_of_int(a[i]));
    #             EndFor.
    #         EndBody.
    #         Function: foo
    #         Parameter: a
    #         Body:
    #             Return a - 1;
    #         EndBody.
    #     """
    #     expect = "123476"
    #     self.assertTrue(TestCodeGen.test(input,expect,600))