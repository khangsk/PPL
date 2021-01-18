import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_glob_var_dec_part_1(self):
        input = """
        Var: a = 5, b; c = 3;
        """
        expect = "Error on line 2 col 23: c"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_glob_var_dec_part_2(self):
        input = """
        Var a = 5, b; 
        """
        expect = "Error on line 2 col 12: a"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_glob_var_dec_part_3(self):
        input = """
        Var: a = 5, b = {1,2}, ; 
        """
        expect = "Error on line 2 col 31: ;"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_glob_var_dec_part_4(self):
        input = """
        Var: a = 1 + 2;   
        """
        expect = "Error on line 2 col 19: +"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_glob_var_dec_part_5(self):
        input = """
        Var: a = "String", b;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_glob_var_dec_part_6(self):
        input = """
        Var: a = True, False;
        """
        expect = "Error on line 2 col 23: False"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_glob_var_dec_part_7(self):
        input = """
        Var: a, b, c
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_glob_var_dec_part_8(self):
        input = """
        Var: a == 1, b;
        """
        expect = "Error on line 2 col 15: =="
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_glob_var_dec_part_9(self):
        input = """
        Var: a = 1, b = ;
        """
        expect = "Error on line 2 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_glob_var_dec_part_10(self):
        input = """
        a = 1, b = 2;
        """
        expect = "Error on line 2 col 8: a"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    
    def test_glob_var_dec_part_11(self):
        input = """
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_glob_var_dec_part_12(self):
        input = """
        Var: b[2][5 = {{2,3,4},{4,5,6}};
        """
        expect = "Error on line 2 col 20: ="
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_glob_var_dec_part_13(self):
        input = """
        Var: b[2]["String"] = {{2,3,4},{4,5,6}};
        """
        expect = "Error on line 2 col 18: String"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_glob_var_dec_part_14(self):
        input = """
        Var: b[2][3] = {{2,3,4},{4,5,6};
        """
        expect = "Error on line 2 col 39: ;"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_glob_var_dec_part_15(self):
        input = """
        Var: b[2][3] = {{2,3,4} {4,5,6}};
        """
        expect = "Error on line 2 col 32: {"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_glob_var_dec_part_16(self):
        input = """
        Var: b[2][3] = {{2,3,4},{4,5,6}}
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_glob_var_dec_part_17(self):
        input = """
        Var b[2][3] = {{2,3,4},{4,5,6}};
        """
        expect = "Error on line 2 col 12: b"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_glob_var_dec_part_18(self):
        input = """
        Var: b[2][3] = {{2,3,"a"},{4,5,}};
        """
        expect = "Error on line 2 col 39: }"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_glob_var_dec_part_19(self):
        input = """
        Var: x = True;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_glob_var_dec_part_20(self):
        input = """
        Var: m = 1.2e-10, n[10] = {1,2,3};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_func_dec_part_21(self):
        input = """
        Function: main;
        """
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_func_dec_part_22(self):
        input = """
        Function: main
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_func_dec_part_23(self):
        input = """
        Function: main
        Body:
            fibonacci(x);
            Var: x = 5;
        EndBody.
        """
        expect = "Error on line 5 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_func_dec_part_24(self):
        input = """
        Function: main
        Body:
            Var: x = 5;
            Var: y = {{1,2,3,4}};
            fibonacci(x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    
    def test_func_dec_part_25(self):
        input = """
        Function: main
        Parameter: x = 2
        Body:
            Var: x = 5;
            Var: y = {{1,2,3,4}};
        EndBody.
        """
        expect = "Error on line 3 col 21: ="
        self.assertTrue(TestParser.checkParser(input,expect,225))
    
    def test_func_dec_part_26(self):
        input = """
        Function: main
        Parameter: x
        Body:
            Var: x = 5, 1.e-2;
        EndBody.
        """
        expect = "Error on line 5 col 24: 1.e-2"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_func_dec_part_27(self):
        input = """
        Function: main
        Parameter: x
        Body:
            Var: x = foo(2);
            Print();
        EndBody.
        """
        expect = "Error on line 5 col 21: foo"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    

    def test_func_dec_part_28(self):
        input = """
        Function: main
        Parameter: x
        Body:
            If n <= 1 Then
                If n == 0 Then
                    print("Hello World!");
            Else:
                Return False; 
        EndBody.
        """
        expect = "Error on line 8 col 16: :"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_func_dec_part_29(self):
        input = """
        Function: main
        Parameter: x
        Body:
            ** PPL
            * Nguyen ly ngon ngu lap trinh
            **
            Var: x = 1 +. 1;
        EndBody.
        """
        expect = "Error on line 8 col 23: +."
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_func_dec_part_30(self):
        input = """
        Funtion: main
        """
        expect = "F"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_expression_31(self):
        input = """
        Var: x = x + 1;
        """
        expect = "Error on line 2 col 17: x"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_expression_32(self):
        input = """
        Var: x = 2.E-1;
        Function: main
        Body:
            Var: y = 1;
            z = x + y;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_expression_33(self):
        input = """
        Function: foo
        Body:
            Var: x = True;
            x = x && (foo(1) || False);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_expression_34(self):
        input = """
        Function: print
        Parameter: arr[5], vec[5], x
        Body:
            x = !arr[0]; 
            print(arr[vec[1][x]]);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_expression_35(self):
        input = """
        Function: neg
        Parameter: x
        Body: 
            x = --(-x);
            Return -abs(x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_expression_36(self):
        input = """
        Function: main
        Body: 
            print(1 > 0 && 1.0 <. 0.0);
        EndBody.
        """
        expect = "Error on line 4 col 31: <."
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_expression_37(self):
        input = """
        Function: main
        Body: 
            print(foo(2) || 1.0 -. 0.5 == 0.5);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_expression_38(self):
        input = """
        Function: main
        Body: 
            foo("True")[1.0] = "He asked me: '"Where is John?'"";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_expression_39(self):
        input = """
        Function: goo
        Body: 
            x = -. 3.0 -. 3.0;
            Return x +. 1.0 *. 2.0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_expression_40(self):
        input = """
        Function: kang
        Body: 
            foo(1.e-1 \. 1e);
        EndBody.
        """
        expect = "Error on line 4 col 26: e"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_statement_41(self):
        input = """
        Function: star
        Body: 
            For (i = 0, i < 2, 1) Do
                Do Break; While (i != 1) 
                EndWhile.
            EndFor.
        EndBody.
        """
        expect = "Error on line 6 col 16: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_statement_42(self):
        input = """
        Var: x = {1,2};
        Function: a1
        Parameter: x
        Body: 
            If ! x[0] == 1 Then
                a1(x[0] + 1);
            ElseIf x[0] >. 1.0 Then
                Return False;
            Else
                Continue;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_statement_43(self):
        input = """
        Function: init
        Body: 
            If abs(foo(x))[1][1] =/= -1.e-2 Then
                For (i = 1, i <. 2.5, 1) Do
                    push(array, i);
                EndFor.
            EndIf.
            Return;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_statement_44(self):
        input = """
        Function: __str__
        Body: 
            Return str(self.string);
        EndBody.
        """
        expect = "_"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_statement_45(self):
        input = """
        Function: main
        Body: 
            If i == 0 Then
                While True print("Hello World!"); EndWhile.
            EndIf.
        EndBody.
        """
        expect = "Error on line 5 col 27: print"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_statement_46(self):
        input = """
        Function: main
        Body: 
            If i == 0 Then
                For (i = 0, i < 2, 1)
                    print("Hi!");
                EndFor.
            EndIf.
        EndBody.
        """
        expect = "Error on line 6 col 20: print"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_statement_47(self):
        input = """
        Function: main
        Body: 
            If True Then
                While True Do  
                    For (i = 0, i < 0, 0) Do
                    EndFor.
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "Error on line 8 col 16: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    
    def test_statement_48(self):
        input = """
        Function: main
        Body: 
            If True Then
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_statement_49(self):
        input = """
        Function: main
        Body: 
            While i
                Do print(x); While i 
                EndDo. 
            EndWhile.
        EndBody.
        """
        expect = "Error on line 6 col 16: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_statement_50(self):
        input = """
        Function: main
        Body: 
            For (i = 0, i < 5, 1) Do
                print(x);
                Var: x = 1;
            EndFor.
        EndBody.
        """
        expect = "Error on line 6 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_statement_51(self):
        input = """
        Function: main
        Body: 
            Var: x[1][2] = -1;
            Var: x = "Hello";
            x = "Hello!";
        EndBody.
        """
        expect = "Error on line 4 col 27: -"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_statement_52(self):
        input = """
        Function: main
        Body: 
            Var: foo(2)[2] = 2;
        EndBody.
        """
        expect = "Error on line 4 col 20: ("
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_statement_53(self):
        input = """
        Function: main
        Body: 
            Var: x;
            foo(2)[2] = 2;
            x = -1;
            print(a == 2);
            skip(!(1 + 1));
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_statement_54(self):
        input = """
        Function: main
        Body: 
            Var: arr[foo(2) +. 1.0] = arr[foo(1) +. 2.0];
        EndBody.
        """
        expect = "Error on line 4 col 21: foo"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_statement_55(self):
        input = """
        Function: main
        Parameter: arr[foo(1)], n 
        Body: 
            print(arr[foo(n)]);
        EndBody.
        """
        expect = "Error on line 3 col 23: foo"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_statement_56(self):
        input = """
        Function: main
        Parameter: n
        Body: 
            If False Then
                For i = 0, i < 2, 1 Then
                    print(n*i);
                EndFor. 
            EndIf.
        EndBody.
        """
        expect = "Error on line 6 col 20: i"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    
    
    def test_statement_57(self):
        input = """
        Function: main
        Parameter: x
        Body: 
            If 1 + 1 Then
                Break;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    
    def test_statement_58(self):
        input = """
        Function: main
        Parameter: a[5]
        Body: 
            For (i = 1 + foo(2), 1.0 <. 2.0, foo(2)[2]) Do
                ** This is a comment
                * multi-line.
                **
                While !1 > 2 Do
                    Iff Then
                        Var: x = {{1}};
                        ** Var declaration *
                    EndIf.
                EndWhile.
            EndFor.            
        EndBody.
        """
        expect = ""
        self.assertTrue(TestParser.checkParser(input,expect,258))
    
    def test_statement_59(self):
        input = """
        Function: main
        Body: 
            While i > 2 Do
                print("Hi");
                return;
            EndWhile.          
        EndBody.
        """
        expect = "Error on line 6 col 22: ;"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_statement_60(self):
        input = """
        Function: main
        Body: 
            If True Then
                If False Then
                    If True Then
                        If False Then
                    EndIf.
                EndIf.
            EndIf.   
        EndBody.
        """
        expect = "Error on line 11 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    
    def test_overall_61(self):
        input = """
        Var: a, b = 2.0, c;
        Function: main
        Body: 
            If True Then
                Var: x = 1;
                print(x);
            EndIf.   
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_overall_62(self):
        input = """
        Var: a, b = 2.0, c;
        Function: main
        Body: 
            While True Do
                Var: x;
                x = True;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_overall_63(self):
        input = """
        Var: a, b = 2.0, c;
        Function: main
        Body: 
            Var: a[1] = {1};
            For (i = 0, i < 1, 1) Do
                print(x);
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_overall_64(self):
        input = """
        Function: main
        Parameter: x
        Body: 
            If (True || False) Then
                Break;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    
    def test_overall_65(self):
        input = """
        Function: main
        Parameter: a[5]
        Body:   
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    
    def test_overall_66(self):
        input = """
        Function: main
        Body: 
            While i ! 2 Do
                print("Hi");
                Return;
            EndWhile.          
        EndBody.
        """
        expect = "Error on line 4 col 20: !"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_statement_67(self):
        input = """
        Function: main
        Body: 
            If True Then
                True
            EndIf.   
        EndBody.
        """
        expect = "Error on line 5 col 16: True"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    
    def test_overall_68(self):
        input = """
        Var: a, b = 2.0, c;
        Function: main
        Body: 
            If True Then
                Var: x = 1;
                print(x);
            EndIf.   
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_overall_69(self):
        input = """
        Var: a, b = 2.0, c;
        Function: main
        Body: 
            While true Do
                func[2];
            EndWhile.
        EndBody.
        """
        expect = "Error on line 6 col 23: ;"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_overall_70(self):
        input = """
        Var: a, b = {1}, c;
        Function: main
        Body: 
            Var: a[1] = {1};
            For (i = 0, i < 1) Do
                print(x);
            EndFor.
        EndBody.
        """
        expect = "Error on line 6 col 29: )"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_overall_71(self):
        input = """
        Var: x;
        Function: fact
        Parameter: n[2]
        Body:
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody.
        Function: main
        Body:
            x = 10;
            fact (x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    
    def test_overall_72(self):
        input = """
        Function: foo
        Body:
            for (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody.
        """
        expect = "Error on line 4 col 19: ="
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_overall_73(self):
        input = """
        Function: square
        Parameter: t
        Body:
            Return t * t;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_overall_74(self):
        input = """
        Function: main
        Body:
            If bool_of_string ("True") Then
                a = int_of_string (read ());
                b = float_of_int (a) +. 2.0;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    
    def test_overall_75(self):
        input = """
        Function: test
        Body:
            foo (2 + x, 4. \. y);
            goo ();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_overall_76(self):
        input = """
        Function: 
        Body:
            goo ();
        EndBody.
        """
        expect = "Error on line 3 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_overall_77(self):
        input = """
        Function: main
        Body:
            printLn();
            print(arg), printStrLn(arg);
            read();
        EndBody.
        """
        expect = "Error on line 5 col 22: ,"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_overall_78(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            While (i < 5)
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody.
        """
        expect = "Error on line 7 col 16: a"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    
    def test_overall_79(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            a[3 + foo(2)] = a[b[2][3]] + 4;
            a[True] = False;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    
    def test_overall_80(self):
        input = """
        Function: func
        Parameter: b
        Body:
            ();
        EndBody.
        """
        expect = "Error on line 5 col 12: ("
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_overall_81(self):
        input = """
        Function: loc
        Parameter: a
        Body:
            a;
        EndBody.
        """
        expect = "Error on line 5 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    
    def test_overall_82(self):
        input = """
        Body:
            merge();
        EndBody.
        """
        expect = "Error on line 2 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_overall_83(self):
        input = """
        Function: cover
        Parameter: **args**
        Body:
            print();
        EndBody.
        """
        expect = "Error on line 4 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_overall_84(self):
        input = """
        Function: delete
        Parameter:
        Body:
            While Do EndWhile.
        EndBody.
        """
        expect = "Error on line 4 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_overall_85(self):
        input = """
        Function: infix
        Parameter: a[5]
        Body:
            For (i = 0, i, 0) Do
                If a[i] == 1 Then
                ElseIf
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "Error on line 8 col 16: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_overall_86(self):
        input = """
        Function: swap
        Parameter: a, b
        Body:
            a, b = b, a;
        EndBody.
        """
        expect = "Error on line 5 col 13: ,"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_overall_87(self):
        input = """
        Function: cost
        Parameter: x
        Body:
            d(i) = d(x[i]) / d(t);
        EndBody.
        """
        expect = "/"
        self.assertTrue(TestParser.checkParser(input,expect,287))

        
    def test_overall_88(self):
        input = """
        Function: fee
        Parameter: x, a, b
        Body:
            a = (x, b);
        EndBody.
        """
        expect = "Error on line 5 col 18: ,"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_overall_89(self):
        input = """
        Function: go
        Parameter: x[n]
        Body:
            print(x[:]);
        EndBody.
        """
        expect = "Error on line 3 col 21: n"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_overall_90(self):
        input = """
        Function: main
        Var: x = 2;
        Body:
            call(x);
        EndBody.
        """
        expect = "Error on line 3 col 8: Var"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_overall_91(self):
        input = """
        Function: main
        Body:
            a[foo(2)] = foo(2)[a;];
        EndBody.
        """
        expect = "Error on line 4 col 32: ;"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_overall_92(self):
        input = """
        Function: main
        Body:
            match(!x) = "string\tstring"; 
        EndBody.
        """
        expect = "Error on line 4 col 22: ="
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_overall_93(self):
        input = """
        Function: main
        Body:
            If Continue Do
                Break;
            EndIf. 
        EndBody.
        """
        expect = "Error on line 4 col 15: Continue"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_overall_94(self):
        input = """
        Function: main
        Body:
            ElseIf x == 2 Then
                print(x);
            EndIf.
        EndBody.
        """
        expect = "Error on line 4 col 12: ElseIf"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    
    def test_overall_95(self):
        input = """
        Function: main
        Body:
            While (x - 2) != (x - 2) Do
                print(print(x));
            EndFor.
        EndBody.
        """
        expect = "Error on line 6 col 12: EndFor"
        self.assertTrue(TestParser.checkParser(input,expect,295))    

    def test_overall_96(self):
        input = """
        Function: 1
        Body:
            print(1);
        EndBody.
        """
        expect = "Error on line 2 col 18: 1"
        self.assertTrue(TestParser.checkParser(input,expect,296))  

    def test_overall_97(self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))    

    def test_overall_98(self):
        input = """
        Function: True;
        Body:
        EndBody.
        """
        expect = "Error on line 2 col 18: True"
        self.assertTrue(TestParser.checkParser(input,expect,298))    

    def test_overall_99(self):
        input = """
        Function: over
        Body:
            x = -. "s";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))    

    def test_overall_100(self):
        input = """
        Function: main;
        Body:
            h(a[3]) = a(h[2]);
        EndBody.
        """
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.checkParser(input,expect,300))    
    
    
    
    
    