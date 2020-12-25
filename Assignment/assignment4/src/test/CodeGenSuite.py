import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """
                    Function: main
                   Body:        
                        print(string_of_int(12111));
                   EndBody."""
        expect = "12111"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_int_ast(self):
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
                        print(string_of_int(y));
                        print(string_of_int(x));
                   EndBody."""
        expect = "12111"
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

    # def test3(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Function: foo
    #     Body:
    #         print(string_of_int(1));
    #     EndBody.
    #     Function: main
    #     Body: 
    #         foo();
    #         print(string_of_int(120));
    #     EndBody."""
    #     expect = "1 \n 120"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))