import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test1_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test2_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test3_var_integer_decimal(self):
        input = """Var: a = 1, b=2123, c=0;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test4_var_integer_hex(self):
        input = """Var: abc =  0XF123,    x___asdyz = 0xA398;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test5_var_integer_hex2(self):
        input = """Var: abc,    x___asdyz = 0xA398, x, khang, hoang = 0X3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test6_var_integer_hex_err(self):
        input = """Var: abc = 0xA398,    x___asdyz = 0XG123;"""
        expect = "X"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test7_var_integer_hex_err2(self):
        input = """Var: = 0xA398;"""
        expect = "Error on line 1 col 5: ="
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test8_var_integer_oct(self):
        input = """Var: fasdf898a   =0O772, dsf__2 = 0o21371;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test9_var_integer_oct2(self):
        input = """Var: dsf__2 = 0o21371, a, khang = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test10_var_integer_oct_err(self):
        input = """Var: hoang = 0O23F;"""
        expect = "F"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test11_var_float(self):
        input = """Var: a = 112.0e3, b___1, c=12.;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test12_var_string(self):
        input = """Var: a = "hoang gia khang", b___1, c=12.;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test13_var(self):
        input = r"""
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, z;
        Var: m = 1, n[2] = {   2   ,   3   };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test14_funct_declare_part(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test15_funct_declare_part_full(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test16_funct_declare_part_error_Then(self):
        input = r"""
        Var: x;
        Function: fact
            Parameter: n
            Body:
                If n == 0 then
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
        expect = "Error on line 6 col 26: then"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test17_funct_declare_and_comment(self):
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
        **Test comment!!!**
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test18_string_array(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test19(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test20(self):
        input = """Var: FF"""
        expect = "F"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test21_For_stmt(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test22_assign_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[5], b
            Body:
                For (i = 0, i < 10, 2) Do
                    a[i] = b;
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test22_if_stmt(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test24_if_error(self):
        input = r"""
        Function: foo
            Parameter: a[2], b
            Body:
                For (i = 0, i < 2, 1) Do
                    If a[i] > b Then writeln(a[i], " is larger than ", b);
                    **Error '='**
                    ElseIf a[i] = b Then writeln(a[i], " equal ", b);
                    EndIf.
                EndFor.
            EndBody."""
        expect = "Error on line 8 col 32: ="
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test25_while_stmt(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test26_while_missing_do(self):
        input = r"""
        Function: foo
            Parameter: a[2], b
            Body:
                Var: i = 0;
                **While have no "Do"**
                While (a[i] > b)
                    writeln(a[i]);
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = "Error on line 8 col 20: writeln"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test27_do_while_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[2], b
            Body:
                Var: i = 0;
                Do 
                    a[i] = a[i] +. 1.;
                While (a[i] > b) EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test28_break_stmt(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test29_continue_stmt(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test30_call_stmt(self):
        input = r"""
        Function: foo
            Parameter: x, y
            Body:
                writeln(foo(2 + x, 4. \. y) * goo());
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test31_return_stmt(self):
        input = r"""
        Function: compare
            Parameter: x, y
            Body:
                If (x > y) Then
                    Return True ;
                Else Return False;
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test32_type_coercions(self):
        input = r"""
        Function: compare
            Parameter: a, b
            Body:
                If bool_of_string("True") Then
                    a = int_of_string(read());
                    b = float_of_string(a) +. 2.0;
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test33(self):
        input = r"""
        Function: printDivivsors
            Parameter: n
            Body:
                For (i = 1, i <= n, 1) Do
                    If (n % i == 0) Then
                        writeln(i);
                    EndIf.
                EndFor.
            EndBody.
        Function: main
            Body:
                Var: x;
                input(x);
                printDivivsors(x);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test34(self):
        input = r"""
        Function: power_rep
            Parameter: base, exp
            Body:
                Var: a = 2;
                If (exp == 0) Then
                    Return 1;
                EndIf.
                For (i = 0, i < exp - 1, 1) Do
                    base = base * a;
                EndFor.
                Return base;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test35(self):
        input = r"""
        Function: power_recur
            Parameter: base, exp
            Body:
                If (exp == 0) Then
                    Return 1;
                EndIf.
                Return base * power_recur(base, exp - 1);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test36(self):
        input = r"""
        Function: power_rep
            Parameter: base, exp
            Body:
                Var: a = 2;
                If (exp == 0) Then
                    Return 1;
                EndIf.
                For (i = 0, i < exp - 1, 1) Do
                    base = base * a;
                EndFor.
                Return base;
            EndBody.
        Function: power_recur
            Parameter: base, exp
            Body:
                If (exp == 0) Then
                    Return 1;
                EndIf.
                Return base * power_recur(base, exp - 1);
            EndBody.
        Function: main
            Parameter: base, exp
            Body:
                base = input();
                exp = input();
                writeln(power_rep(base, exp));
                writeln(power_recur(base, exp));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test37_wrong_pos_of_var(self):
        input = r"""
        Function: power_rep
            Parameter: base, exp
            Body:
                If (exp == 0) Then
                    Return 1;
                EndIf.
                For (i = 0, i < exp - 1, 1) Do
                    base = base * a;
                EndFor.
                Var: a = 2;
                Return base;
            EndBody.
        """
        expect = "Error on line 11 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test38(self):
        input = r"""
        Function: main
            Body:
                Var: answer, length, jump_max, arr[10], a , j;
                For (i = 0, i < length, 1) Do
                    arr[i] = input();
                EndFor.
                For (j = 0, j < length, 1) Do
                    If (a + jump_max >= arr[i]) && (a + jump_max < arr[i + 1]) Then
                        a = arr[i];
                        answer = answer + 1;
                    EndIf.
                EndFor.
                If (j != length - 1) Then
                    answer = -1;
                EndIf.
                If (a + jump_max >= arr[length - 1]) Then
                    answer = answer + 1;
                Else answer = -1;
                EndIf.
	            writeln(answer);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test39(self):
        input = r"""
        Function: longest_substr
            Parameter: str
            Body:
                Var: count = 0, check = False;
                For (i = 0, i < length(str), 1) Do
                    For (j = 0, j < length(str), 1) Do
                        If (str[i] == str[j]) && (i != j) Then
                            check = True;
                            Break;
                        EndIf.
                        If (check) Then
                            check = False;
                        EndIf.
                        Continue;
                    EndFor.
                    count = count + 1;
                EndFor.
                Return count;     
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test40(self):
        input = r"""
        Function: foo
            Parameter: str
            Body:
                Var: count = 0, check = False;
                For (i = 0, i < length(str), 1) Do
                    If !str[i] Then
                        count = count + 1;
                        writeln(str[i]);
                    EndIf.
                EndFor.
                Return count;     
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test41(self):
        input = r"""
        Function: uoc_chung_lon_nhat
            Parameter: a, b
            Body:
                If (a == b) Then
                    Return a;
                EndIf.
	            If (a > b) Then
		            a = a % b;
                EndIf.
	            If (a == 0) Then
                    Return b;
                EndIf.
	            Return uoc_chung_lon_nhat(b, a);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test42_error_expression(self):
        input = r"""
        Function: longest_substr
            Parameter: str
            Body:
                Var: count = 0, check = False;
                For (i = 0, i < length(str), 1) Do
                    For (j = 0, j < length(str), 1) Do
                        **Error is here (!=)**
                        If (str[i] == str[j] && i != j) Then
                            check = True;
                            Break;
                        EndIf.
                        If (check) Then
                            check = False;
                        EndIf.
                        Continue;
                    EndFor.
                    count = count + 1;
                EndFor.
                Return count;     
            EndBody.
        """
        expect = "Error on line 9 col 50: !="
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test43(self):
        input = r"""
        Function: square_num
            Parameter: x
            Body:
                If x == 1 Then
                    Return 1;
                Else 
                    Return sqrt(x + square_num(x - 1));
                EndIf.
            EndBody.
        Function: main
            Body:
                Var: x = 10;
                writeln(square_num(x));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test44(self):
        input = r"""
        Function: reverseString
            Parameter: initialString
            Body:
                If (initialString == nullptr) Then
                    Return;
                EndIf.
                If (strlen(initialString) == 1) Then
                    writeln(initialString[0]);
                    Return;
                EndIf.
                writeln(initialString[strlen(initialString) - 1]);
                initialString[strlen(initialString) - 1] = 0;
                reverseString(initialString);
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test45(self):
        input = r"""
        Function: reverseString
            Parameter: initialString
            Body:
                initialString = "khang
            EndBody."""
        expect = "khang"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test46_for_stmt(self):
        input = r"""
        Function: reverseString
            Parameter: num
            Body:
                For (i = num * 2, i < num * num, i + 1) Do
                    If i % 2 == 0 Then
                        writeln(i);
                    EndIf.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test47(self):
        input = r"""
            Var: arr[5][6]=1.e790,b,c=2;
            Var: x;
            Function: tEST_function_Name_1
                Parameter: x[100]
                Body:
                    Do 
                        x=x + foo(267+a[6]+. 1.0);
                        x=x%2;
                        If (i>=9) Then
                            writeln(a+7);
                        EndIf.
                    While i<=27 EndDo .
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test48(self):
        input = r"""
            Function: tEST_function_Name_2
                Parameter: x,a[69],b[1][2][3]
                Body:
                    For (i=1, goo(2+a[6]) < i,2>goo(9)) Do
                        If arr[7] >= foo(3) Then
                            Break;
                        EndIf.
                    EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test49(self):
        input = r"""
            Function: reverseString
            Parameter: num
            Body:
                For (i = num * 2, i < num * num, i + 1) Do
                    Var: a = 1;
                    If i % 2 == 0 Then
                        writeln(a * i);
                    EndIf.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test50_var_wrong_pos(self):
        input = r"""
            Function: test
            Parameter: num
            Body:
                For (i = num * 2, i < num * num, i + 1) Do
                    If i % 2 == 0 Then
                        writeln(a * i);
                    EndIf.
                    Var: a = 1;
                EndFor.
            EndBody."""
        expect = "Error on line 9 col 20: Var"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test51_var_wrong_pos(self):
        input = r"""
            Function: test
            Parameter: num
            Var: test = 100;
            Body:
                For (i = num * 2, i < num * num, i + 1) Do
                    Var: a = 1;
                    If i % 2 == 0 Then
                        writeln(a * i);
                    EndIf.
                EndFor.
            EndBody."""
        expect = "Error on line 4 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test52_name_fucntion_error(self):
        input = r"""
            Function: _test
            Parameter: num
            Body:
                return false;
            EndBody."""
        expect = "_"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test53_var(self):
        input = r"""
            Var: a = True, b = {1,2}, c = {{True, False}, {1.e2, 1e3}};
            Function: test
            Parameter: num
            Body:
                Return False;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test54_var(self):
        input = r"""
            Var: a = True, b = {1,2}, c = {{True, False}, {1.e2, 2e2}};
            Function: test
            Parameter: num
            Body:
                Var: sum = 0;
                For (i = num, i < sqr(num), 2) Do
                    sum = sum + i * i;
                EndFor.
                Return sum;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test55_var(self):
        input = r"""
            Var: a = -1.23;
            """
        expect = "Error on line 2 col 21: -"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test56(self):
        input = r"""
            Function: test
            Parameter: num
            Body:
                Var: sum = 0;
                For (i = num, i < sqr(num), 2) Do
                    sum = 123[1[1][1][1][1][1][1][1]][i];
                EndFor.
                Return sum;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test57(self):
        input = r"""
            Function: main
            Body:
                Var: arr[10];
                For (i = 0, i < 10, 1) Do
                    For (j = i + 1, j < 10, 1) Do
                        If (arr[i] < arr[j]) Then
                            Var: temp;
                            temp = arr[i];
                            arr[i] = arr[j];
                            arr[j] = temp;
                        EndIf.
                    EndFor.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))
    def test58(self):
        input = r"""
            Function: main
            Body:
                Var: i, n;
                Do
                    writeln("Input n: ");
                    input(n);
                    If (n <= 0) Then
                        writeln("Input again, N must be larger than 0");
                    EndIf.
                While (n <= 0) EndDo.
                i = 1;
                While (i <= n) Do
                    If (n % i == 0) Then
                        writeln(i);
                        i = i + 1;
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))
    def test59(self):
        input = r"""
            Function: main
            Body:
                For (i = 1, i <= 10, 1) Do
                    For (j = 2, j <= 9, 1) Do
                        writeln(i, j, i * j);
                    EndFor.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))
    def test60(self):
        input = """
            Function: prime_number
            Parameter: n
            Body:
                If (n < 2) Then
                    Return False;
                ElseIf (n > 2) Then
                    If (n % 2 == 0) Then
                        Return False;
                    EndIf.
                    For (i = 3, i <= sqrt(n), 2) Do
                        If (n % i == 0) Then
                            Return False;
                        EndIf.
                    EndFor.
                EndIf.
                Return True;
            EndBody.
            Function: main
            Body:
                Var: n;
                input(n);
                If prime_number(n) Then
                    writeln(n, "is prime number");
                Else
                    writeln(n, "is not prime number");
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))
    def test61(self):
        input = """
            Function: main
            Body:
                Var: a[10], max;
                For (i = 0, i < 10, 1) Do
                    input(a[i]);
                EndFor.
                max = a[0];
                For (i = 0, i < 10, 1) Do
                    If max < a[i] Then
                        max = a[i];
                    EndIf.
                EndFor.
                writeln("Max number in array is: ", max);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))
    def test62_complex_exp_test(self):
        """Some more complex simple expression"""
        input = r"""
        Function: foo 
        Body: 
            a = 1 + 1.23 *. abc \. id[12[123][2][moreid]];
            b = 1.E-12  =/= foo(123);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))
    def test63_comment(self):
        input = r"""
            **
            * A
            &
            * %\\s
            * 3'
            **
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))
    def test64(self):
        input = r"""
            Var: a = {{{1, 2}},{{{}}},{{{{{{{{{{}}}}}}}}}}};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))
    def test65_sign_operand(self):
        input = r"""
            Function: foo
            Body:
                a = 1 -;
            EndBody.
        """
        expect = "Error on line 4 col 23: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 265))
    def test66_sign_operand(self):
        input = r"""
            Function: foo
            Body:
                a = -1;
                Return a * 190;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))
    def test67_logical(self):
        input = r"""
            Function: foo
            Body:
                a = !1;
                b = !True;
                Return a * 190;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))
    def test68_operators(self):
        input = r"""
            Function: foo
            Body:
                a = a * 1;
                b = 12. * 3.e3;
                c = 0x123 \ 3;
                Return;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))
    def test69_relational(self):
        input = r"""
            Function: foo
            Body:
                If a =/= b Then
                    Return False;
                ElseIf a >=. b Then
                    Return True;
                ElseIf a <=. b Then
                    Return True;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))
    def test70_relational(self):
        input = r"""
            Function: foo
            Body:
                If (a == b) && (a != c) || (a > b) || (a < c)   Then
                    Return True;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))
    def test71_relational(self):
        input = r"""
            Function: foo
            Body:
                If (a >. b) && (a <. b) || (a <= d) && (a >= e)  Then
                    Return True;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))
    def test72_coercions(self):
        input = r"""
            Function: foo
            Body:
                Var: s = "123";
                n = int(s);
                Return n * 10;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))
    def test73_function_in_function(self):
        input = r"""
            Function: foo
            Body:
                Var: s = "123";
                n = int(s);
                Function: a
                Body:
                    Return True;
                EndBody.
            EndBody.
        """
        expect = "Error on line 6 col 16: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 273))
    def test74_Body_in_Body(self):
        input = r"""
            Function: foo
            Body:
                Var: s = "123";
                n = int(s);
                Body:
                    Return True;
                EndBody.
            EndBody.
        """
        expect = "Error on line 6 col 16: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 274))
    def test75_while_stmt_missing_do(self):
        input = r"""
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
        expect = "Error on line 7 col 20: a"
        self.assertTrue(TestParser.checkParser(input, expect, 275))
    def test76_coercions(self):
        input = r"""
            Var: string[3] = {"1.23", "0.e4", "12e2"};
            Function: test
            Body:
                Var: x[3], sum = 0.;
                For (i = 0, i < 3, 1) Do
                    x[i] = float(string[i]);
                    sum = sum + x[i];
                EndFor.
                Return sum;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))
    def test77_misssing_function(self):
        input = r"""
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
            EndBody.
        """
        expect = "Error on line 2 col 12: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 277))
    def test78_var_declaration(self):
        input = r"""
            Function: square
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                Return v;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))
    def test79_a_operator_p(self):
        input = r"""
            Var: a, b, operator;
            Function: main
            Body:  
                input(a);
                input(b);
                input(operator);
                If operator == "+" Then
                    Return a + b;
                ElseIf operator == "-" Then
                    Return a - b;
                ElseIf operator == "*" Then
                    Return a * b;
                Else
                    Return a \ b;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))
    def test80(self):
        input = r"""
            Var: arr[3][2] = {{1, 2}, {4, 5}, {3, 5}};
            Function: main
            Body:
                Var: p = 1;
                For (i = 0, i < 3, 1) Do
                    For (j = 0, j < 2, 1) Do
                        p = p * arr[i][j];
                    EndFor.
                EndFor.
                writeln(p);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))
    def test81_error_logical_operator(self):
        input = r"""
            Function: main
            Body:
                a = 1!;
            EndBody.
        """
        expect = "Error on line 4 col 21: !"
        self.assertTrue(TestParser.checkParser(input, expect, 281))
    def test82_Var_declare_wrong(self):
        input = r"""
            Function: main
            Body:
                Var: a = b;
            EndBody.
        """
        expect = "Error on line 4 col 25: b"
        self.assertTrue(TestParser.checkParser(input, expect, 282))
    def test83_missing_body(self):
        input = r"""
            Function: main
            Return 1;
        """
        expect = "Error on line 3 col 12: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 283))
    def test84_no_stmt_in_body(self):
        input = r"""
            Function: main
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))
    def test85_coercion(self):
        input = r"""
            Function: main
            Body:
                Var: s = "this is a string containing tab \t", a = "0XFA1B23";
                s = s + string(a);
                writeln(s);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))
    def test86_wrong_operator(self):
        input = r"""
            Function: main
            Body:
                Var: a = 0XFA1B23;
                Var: b = 1;
                a = a *+ b;
                writeln(a);
            EndBody.
        """
        expect = "Error on line 6 col 23: +"
        self.assertTrue(TestParser.checkParser(input, expect, 286))
    def test87_sign_operand(self):
        input = r"""
            Function: main
            Body:
                Var: a = 0XFA1B23;
                Var: b = 1;
                a = a *- b;
                a = a*.-b;
                writeln(a);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))
    def test88(self):
        input = r"""
            Function: abc
            Body:
                a = !((!b && c) + 1) || check(d);
                Return a;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))
    def test89_precedence(self):
        input = r"""
            Function: main
            Body:
                Var: a, b = 5;
                input(a);
                If (a > b && a < 10) Then
                    Return True;
                Else
                    Return False;
                EndIf.
            EndBody.
        """
        expect = "Error on line 6 col 31: <"
        self.assertTrue(TestParser.checkParser(input, expect, 289))
    def test90_mul_and_add(self):
        input = r"""
            Function: main
            Body:
                Var: a, b = 5;
                input(a);
                If !(a + b * 10) Then
                    Return True;
                Else
                    Return False;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))
    def test91_function_call(self):
        input = r"""
            Function: main
            Body:
                Return a(b(c(d(e(f(1123 + True + fo(z(f(f)))))))));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))
    def test92_wrong_exp_while(self):
        input = r"""
            Function: main
            Body:
                While a > 0 Do
                EndWhile.
                While If a > 0 Then Do
                EndWhile.
            EndBody.
        """
        expect = "Error on line 6 col 22: If"
        self.assertTrue(TestParser.checkParser(input, expect, 292))
    def test93_parameter_cant_init_value(self):
        input = r"""
            Function: main
            Parameter: a ** = 3 **, b = "error";
            Body:
            EndBody.
        """
        expect = "Error on line 3 col 38: ="
        self.assertTrue(TestParser.checkParser(input, expect, 293))
    def test94_coercion_float(self):
        input = r"""
            Function: main
            Body:
                Var: a___b = 12345;
                Var: b = True, c = 123.;
                If b Then
                    c = c +. 1.;
                ElseIf !b Then
                    Return c;
                EndIf.
                Return float(a___b) + c;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))
    def test95(self):
        input = r"""
            Var: a = "Hoang Gia Khang";
            Function: check
            Parameter: b
            Body:
                If (a == b) Then
                    Return True;
                EndIf.
                Return False;
            EndBody.
            Function: main
            Body:
                Var: s, k, result;
                input(s);
                input(k);
                result = string(s) + string(k);
                If check(result) Then
                    writeln(result);
                Else
                    writeln("Nothing");
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))
    def test96_error_var(self):
        input = r"""
            Function: main
            Body:
                Var: a = b = 1;
            EndBody.
        """
        expect = "Error on line 4 col 25: b"
        self.assertTrue(TestParser.checkParser(input, expect, 296))
    def test97_assign_stmt(self):
        input = r"""
            Function: main
            Body:
                Var: a, b;
                input(a, b);
                c = a == b;
                d = c+-1.23*.-3e4;
                writeln(d);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))
    def test98_call_stmt(self):
        input = r"""
            Function: main
            Body:
                foo(3 +x[i] * y(3,z(4)));
                If !foo Then
                    Return False;
                EndIf.
                For (i = 0, i < 100, 2) Do
                    writeln(sqrt(i) * test[3][foo(4)]);
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))
    def test99_all(self):
        input = r"""
            Function: prime_number
            Parameter: n
            Body:
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
                Var: a[100];
                For (i = 0, i < 100, 1) Do
                    input(a[i]);
                    If prime_number(a[i]) && (a[i] % 2 != 0) Then
                        writeln(a[i]);
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))
    def test100_all(self):
        input = r"""
            Var: a = 5;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: c, d = 6, e, f;
            Var: m, n[10];
            Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
            EndBody.
            Function: main
            Body:
            ** This is a single-line comment. **
            ** This is a
            * multi-line
            * comment.
            **
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                If bool_of_string ("True") Then
                    a = int_of_string (read ());
                    b = float_of_int (a) +. 2.0;
                EndIf.
                For (i = 0, i < 10, 2) Do
                    writeln(i);
                EndFor.
                x = 10;
                fact (x);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))