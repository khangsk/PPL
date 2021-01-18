import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # Testcases 20x - 265 reserved for:
    # + point test
    # + near-misses
    
    def test_empty(self):
        """test empty program"""
        testcase = r"""**Nguyen Thanh Nhan**"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 200))

    def test_global_var_decl(self):
        """test global var declarations"""
        testcase = r"""Var: nGuyeN, thANH, n__Ha__N, a[1][0], x0; Var: continue;"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 201))

    def test_global_var_init(self):
        """test global var initializations"""
        testcase = r"""Var: x=0, aBc=0xF, a_i=0O1, a[1][0] = {{}}, x0 = "x";
        Var: continue = True; Var: break = False;
        Var: i = a_i;"""
        expect = r"""Error on line 3 col 17: a_i"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 202))

    def test_empty_global_var_decl(self):
        """test empty global variable declaration"""
        testcase = r"""Var:**meant to be empty**;"""
        expect = r"""Error on line 1 col 25: ;"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 203))

    def test_wrong_global_var_decl(self):
        """test wrong global variable declaration"""
        testcase = r"""Var: a[-1];"""
        expect = r"""Error on line 1 col 7: -"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 204))

    def test_wrong_global_var_init_205(self):
        """test wrong global variable initialization"""
        testcase = r"""Var: o = {}, o = {{"{"}}};"""
        expect = r"""Error on line 1 col 24: }"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 205))

    def test_wrong_global_var_init_206(self):
        """test wrong global variable initialization"""
        testcase = r"""Var: a[1][3][3][0o7777][0xF] = {-x};"""
        expect = r"""Error on line 1 col 32: -"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 206))

    def test_wrong_global_var_init_207(self):
        """test wrong global variable initialization"""
        testcase = r"""Var: x = -2e3;"""
        expect = r"""Error on line 1 col 9: -"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 207))

    def test_parameter(self):
        """test parameter declarations"""
        testcase = r"""Function: a Parameter: a[0] Body:EndBody.Function: a Parameter: abc, cba, abc[0] Body:EndBody.
        Function: a Parameter: a,a,a[0] Body:EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 208))

    def test_empty_parameter(self):
        """test empty parameter declaration"""
        testcase = r"""Function: a Parameter: **meant to be empty** Body:EndBody."""
        expect = r"""Error on line 1 col 45: Body"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 209))

    def test_parameter_init(self):
        """test parameter initialization"""
        testcase = r"""Function: a Parameter: a,a,a[0]=0 Body:EndBody."""
        expect = r"""Error on line 1 col 31: ="""
        self.assertTrue(TestParser.checkParser(testcase, expect, 210))

    def test_local_var_decl_1(self):
        """test local varible declarations"""
        testcase = r"""Function: a Body:
        Var:a;
        Var:var;
        EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 211))

    def test_local_var_decl_2(self):
        """test local varible declarations"""
        testcase = r"""Function: a Body:IfTrueThenVar:a;Var:var;EndIf.EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 212))

    def test_local_var_init(self):
        """test local varible initializations"""
        testcase = r"""Function: a Body:Var:var = {"var"};IfTrueThenVar:a=0;Var:var="**meant 2 b string**";EndIf.EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 213))

    def test_wrong_local_var_decl_placement(self):
        """test local varible wrong placement"""
        testcase = r"""Function: a Body:Var:var = {"var"};IfTrueThenEndIf.Var:a=0;Var:var="**meant 2 b string**";EndBody."""
        expect = r"""Error on line 1 col 51: Var"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 214))

    def test_common_var_decl_mistake_215(self):
        """test common mistake when declare variable"""
        testcase = r"""Varr: x;"""
        expect = r"""Error on line 1 col 3: r"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 215))

    def test_common_var_decl_mistake_216(self):
        """test common mistake when declare variable"""
        testcase = r"""Function: a Body:Var:var = 0x0;IfTrueThenEndIf.Var:a=0;Var:var="**meant 2 b string**";EndBody."""
        expect = r"""Error on line 1 col 28: x0"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 216))

    def test_func_decl(self):
        """test function declarations"""
        testcase = r"""Function: a Body:Var:var = {"var"};IfTrueThenEndIf.Var:a=0;Var:var="**meant 2 b string**";EndBody."""
        expect = r"""Error on line 1 col 51: Var"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 217))

    def test_func_decl_before_var_decl(self):
        """test wrong function declaration placement"""
        testcase = r"""Function: a Body:Var:var = {"var"};IfTrueThenEndIf.Var:a=0;Var:var="**meant 2 b string**";EndBody.
        Var: a;"""
        expect = r"""Error on line 1 col 51: Var"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 218))

    def test_nested_func(self):
        """test function declaration within another function declaration"""
        testcase = r"""Function: a BodyFunction:a Body:EndBody.EndBody."""
        expect = r"""Error on line 1 col 16: Function"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 219))

    def test_nameless_func(self):
        """test function with no name"""
        testcase = r"""Function: **meant to be empty**
            Parameter: x;
            Body:
            EndBody."""
        expect = r"""Error on line 2 col 12: Parameter"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 220))

    def test_wrong_func_name(self):
        """test function with invalid name"""
        testcase = r"""Function: _helper_func
            Parameter: x;
            Body:
            EndBody."""
        expect = r"""_"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 221))

    def test_assign(self):
        """test assignment statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                i=-1 + int_of_float(1.);
                arr[i] = i;
                i = i ** 0 ** \ 0;
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 222))

    def test_assign_weird_lhs_223(self):
        """test assignment statements with weird left-hand side"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                (i + i)[i] = -.1.;
                (arr + i)[i == 0] = i;
                1[1] = i \. 0;
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 223))

    def test_assign_weird_lhs_224(self):
        """test assignment statements with weird left-hand side"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                function()[i] = -.1.;
                (arr =/= arr)["True"] = i;
                i + arr[i] = i;
            EndBody."""
        expect = r"""Error on line 6 col 18: +"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 224))

    def test_assign_weird_rhs_225(self):
        """test assignment statements with weird right-hand side"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                function()[i] = -.1. != !bool_of_string("True");
                i = i***i + i***i;
                i = i == arr[i + i >=. !arr() -. !6 || {"1"}] && i[i()][i()[i][(i)<i>--i]];
            EndBody."""
        expect = r"""Error on line 6 col 71: ["""
        self.assertTrue(TestParser.checkParser(testcase, expect, 225))

    def test_assign_weird_rhs_226(self):
        """test assignment statements with weird right-hand side"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                function()[i] = -.1. >=. !bool_of_string("True");
                i = i***i + i***i;
                i = i == arr[i + i >=. arr(0) -. !6 || {"1"}] && i[i()][i()[i][(i)]];
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 226))

    def test_assign_weird_rhs_227(self):
        """test assignment statements with weird right-hand side"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                function()[i] = -.1. == !bool_of_string("True");
                i = i***i == "***i***" == i***i;
                i = i == arr[+i >=. !arr() -. !6 || {"1"}] && i[i()][i({})[i][(i)<i>--i]];
            EndBody."""
        expect = r"""Error on line 6 col 28: ["""
        self.assertTrue(TestParser.checkParser(testcase, expect, 227))

    def test_if(self):
        """test if-then statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If True || False Then EndIf.
                If False && True && "True" || bool_of_string("False" +. 1.) Thenarr=arr;EndIf.
                If Then EndIf.
            EndBody."""
        expect = r"""Error on line 6 col 19: Then"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 228))

    def test_if_else(self):
        """test if-then-else statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If True || False ThenElseEndIf.
                If False && True && "True" || bool_of_string("False" +. 1.) ThenElsearr=arr;EndIf.
                Ifarr Thenarr=arr;Elsei=i*i;EndIf.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 229))

    def test_if_else_if(self):
        """test if-then-elseif statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If True || False ThenElseIf true ThenEndIf.
                If False && True && "True" || bool_of_string("False" +. 1.) ThenElseIf1ThenElsearr=arr;EndIf.
                Ifarr Thenarr=arr;ElseIfbut ThenElseIfor Theni=i*i;ElseEndIf.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 230))

    def test_nested_if_else_if(self):
        """test nested if statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                IfTrue||FalseThenIfTrueThenElseIfFalseThenElseEndIf.ElseIftrue ThenEndIf.
                If False && True && "True" || bool_of_string("False" +. 1.) ThenElseIf1ThenIf0ThenEndIf.Elsearr=arr;EndIf.
                Ifarr Thenarr=arr;ElseIfbut ThenElseIfor Theni=i*i;Else Ifi ThenElseIfarr ThenEndIf.EndIf.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 231))

    def test_weird_if_231(self):
        """test weird if statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If True
                Then
                ElseIf False
                Then
                Else If True == False
                Then
                Else
                EndIf.
            EndBody."""
        expect = r"""Error on line 12 col 12: EndBody"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 232))

    def test_weird_if_232(self):
        """test weird if statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If 1 == 2 || 2 == 2 || 3 == 1
                Then
                ElseIf False
                Then
                ElseIf True == False
                Then
                Else
                EndIf.EndIf.
            EndBody."""
        expect = r"""Error on line 4 col 31: =="""
        self.assertTrue(TestParser.checkParser(testcase, expect, 233))

    def test_weird_if_233(self):
        """test weird if statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If True
                Then
                If 0 Then EndIf.
                ElseIf False
                Then
                Else If True == False
                Then
                EndIf;EndIf.
            EndBody."""
        expect = r"""Error on line 11 col 21: ;"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 234))

    def test_for(self):
        """test for statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i=0, i < 1000, 1) Do
                    arr[i] = i;
                EndFor.
                
                For (i=i-1, i >= 0, -1)
                    print(i);
                EndFor.
            EndBody."""
        expect = r"""Error on line 9 col 20: print"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 235))

    def test_for_composite_count(self):
        """test for statement with composite count variable"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (arr={0}, True, {1}) Do
                    arr[i] = i;
                EndFor.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 236))

    def test_for_semi(self):
        """test for statement with semi-colon as separator"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i=0; True; 0) Do
                    arr[i] = i;
                EndFor.
            EndBody."""
        expect = r"""Error on line 4 col 24: ;"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 237))

    def test_nested_for(self):
        """test nested for statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i=0, i < 1000, 1) Do
                    Var: j = 0;
                    For (j = i, j < 1000, 1) Do
                        Var: k = j;
                    EndFor.
                EndFor.
            EndBody."""
        expect = r"""Error on line 7 col 33: j"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 238))

    def test_weird_for_239(self):
        """test weird for statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (brr[1]={0}, , {1}) Do
                    brr[i] = arr[i];
                    i = i + 1;
                EndFor.
            EndBody."""
        expect = r"""Error on line 4 col 24: ["""
        self.assertTrue(TestParser.checkParser(testcase, expect, 239))

    def test_weird_for_240(self):
        """test weird for statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For ( , , ) Do
                    arr[i] = i;
                    i = i + 1;
                EndFor.
            EndBody."""
        expect = r"""Error on line 4 col 22: ,"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 240))

    def test_weird_for_241(self):
        """test weird for statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For ( i = i * f(i, i * i), i < i * i, arr[i] ) Do
                    For (f(0, 0) = 0, True, 0)
                    
                    EndFor.
                EndFor.
            EndBody."""
        expect = r"""Error on line 5 col 26: ("""
        self.assertTrue(TestParser.checkParser(testcase, expect, 241))

    def test_while(self):
        """test while statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                WhileTrueDoEndWhile.
                WhileFalseDo**sth**sth();EndWhile.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 242))

    def test_while_no_do(self):
        """test while statement with no Do keyword"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                While True Do
                EndWhile.
                
                While False
                    **sth**
                    sth();
                EndWhile.
            EndBody."""
        expect = r"""Error on line 7 col 16: While"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 243))

    def test_nested_while(self):
        """test nested while statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                While True
                Do
                While False
                Do
                EndWhile.EndWhile.
                
                WhileFalseDoWhileFalseDoEndWhile.
                
                **sth**
                sth();
                
                EndWhile.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 244))

    def test_weird_while_245(self):
        """test weird while statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                While (True == !False) Do
                    WhileFalseDoWhileTrueDoEndWhile.
                EndWhile.
            EndBody."""
        expect = r"""Error on line 7 col 12: EndBody"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 245))

    def test_weird_while_246(self):
        """test weird while statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                While True DoDo
                While True
                    -i >= i
                EndDo.EndWhile.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 246))

    def test_do(self):
        """test do-while statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Do
                    arr[int_of_float(i)] = i;
                    i = i * i;
                While i <. i *. i
                EndDo.
                
                DoWhileFalseEndDo.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 247))

    def test_nested_do(self):
        """test nested do-while statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Do
                Var: j = 0;
                    Do
                        j = i;
                    While 0. \. j
                    EndDo.
                While 0 == 0x1-0X1
                EndDo.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 248))

    def test_weird_do_249(self):
        """test weird do-while statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                DoWhileTrueDoDoWhileFalseEndDo.EndWhile.WhileTrue=/=FalseEndDo.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 249))

    def test_weird_do_250(self):
        """test weird do-while statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                DoWhileTrueDoWhileFalseDoEndWhile.EndWhile.WhileTrue-.FalseEndDo.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 250))

    def test_break(self):
        """test break statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i = 0, i < 1000, 0O1) Do
                    Break;
                EndFor.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 251))

    def test_weird_break_252(self):
        """test weird break statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Break;
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 252))

    def test_weird_break_253(self):
        """test weird break statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i = 0, i < 1000, 0O1) Do
                    If True Then
                        Break;
                    Else
                        Continue;
                    EndIf.
                    
                    Break;
                EndFor.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 253))

    def test_continue(self):
        """test continue statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i = 0, i < 1000, 0O1) Do
                    Continue;
                EndFor.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 254))

    def test_weird_continue_255(self):
        """test weird continue statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Continue;
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 255))

    def test_weird_continue_256(self):
        """test weird continue statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i = 0, i < 1000, 0O1) Do
                    If True Then
                        Continue;
                    EndIf.
                    
                    Break;
                EndFor.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 256))

    def test_call(self):
        """test call statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                print("This is the first meaning full string");
                If True Then
                    print("isn\'t it");
                Else
                    do_sth_that_will_never_be_done(0, 0.0 + 1., False, "", {}, i);
                EndIf.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 257))

    def test_complex_call(self):
        """test complex call statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                do_sth_that_will_be_done(func1(0, 0., 0e0) + (2)[2] \. 0. == (i +. i * 2), {{"\\","//"}});
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 258))

    def test_weird_call_259(self):
        """test weird call statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                do_sth_that_will_be_done(func1(0, 0., 0e0) + (2)[2] \. 0. == (i +. i * 2), {{"\\","//"}});
                f__(g__(i__(True, (id())[2][True[False > 2]], 9 == (9 == 9) * 9), z()[z]));
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 259))

    def test_weird_call_260(self):
        """test weird call statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                f(True)(False);
            EndBody."""
        expect = r"""Error on line 4 col 23: ("""
        self.assertTrue(TestParser.checkParser(testcase, expect, 260))

    def test_empty_return(self):
        """test empty return statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Return;
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 261))

    def test_return(self):
        """test non-empty return statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Return 1;
                Return {};
                Return 2. +. -.2.;
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 262))

    def test_complex_return(self):
        """test complex return statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Return f(2) \ 2 =/= 2 * !(True || False);
                Return (True == False || (arr)[i*.i][i[i]]);
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 263))

    def test_weird_return_264(self):
        """test weird return statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Return arr = arr;
            EndBody."""
        expect = r"""Error on line 4 col 27: ="""
        self.assertTrue(TestParser.checkParser(testcase, expect, 264))

    def test_weird_return_265(self):
        """test weird return statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Return 2, 3;
            EndBody."""
        expect = r"""Error on line 4 col 24: ,"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 265))

    # The rest are reserved for:
    # + combined test
    # + common mistakes
    # + near-misses

    def test_parameter_repeat(self):
        """test parameter repeat"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Parameter: j, brr[1000]
            Body:
                
            EndBody."""
        expect = r"""Error on line 3 col 12: Parameter"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 266))

    def test_stmt_out_of_func(self):
        """test out-of-function statement"""
        testcase = r"""Var: a = 0.;
        a=a;"""
        expect = r"""Error on line 2 col 8: a"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 267))

    def test_func_in_func(self):
        """test nested functions"""
        testcase = r"""Function: function1
            Parameter: i, arr[1000]
            Body:
                Function: function2
                Parameter: j, brr[1000]
                Body:    
                EndBody.
            EndBody."""
        expect = r"""Error on line 4 col 16: Function"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 268))

    def test_multiple_scope_var(self):
        """test variable declarations across scopes"""
        testcase = r"""Var: x;
        Function: function
            Parameter: j, brr[1000]
            Body:
                Var: x=0;
                For (i=0,0,0) Do
                    Var:x=1;
                    Do
                        Var:x=2;
                    While1
                    EndDo.
                    If0Then
                        Var:x=3;
                    ElseIf0Then
                        Var:x=4;
                    Else
                        Var:x=5;
                    EndIf.
                EndFor.
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 269))

    def test_long_nested_stmt(self):
        """test nested statements"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                If True Then
                    For (i=0, i, -1) Do
                        Do While False EndDo.
                        While False Do Break; Var: k, l; EndWhile.
                    EndFor.
                EndIf.
            EndBody."""
        expect = r"""Error on line 7 col 46: Var"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 270))

    def test_complex_assign(self):
        """test complex assignment statement"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                ((a[2])[3][4])[s] = f(****) + g(o + 0o1, 0)[{2}[0]];
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 271))

    def test_operator_precedence_272(self):
        """test operator precedence"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = i * i + i \ --1 % i--i;
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 272))

    def test_operator_precedence_273(self):
        """test operator precedence"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = i *. -. -. 2. +. -. i \. i -. 0.E-8;
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 273))

    def test_operator_precedence_274(self):
        """test operator precedence"""
        testcase = r"""Function: main
            Parameter: j, brr[1000]
            Body:
                j = !i && i == i || !!i;
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 274))

    def test_operator_precedence_275(self):
        """test operator precedence"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = -.-.i +. brrr[5];
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 275))

    def test_operator_precedence_276(self):
        """test operator precedence"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = func(1)[2];
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 276))

    def test_operator_assoc_277(self):
        """test operator associativity"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = i + i + i;
                j = i * i * i;
                j = i \ i \ i;
                j = i - i - i;
                j = i % i % i;
                j = i *. i *. i;
                j = i +. i +. i;
                j = i -. i -. i;
                j = i \. i \. i;
                j = i || i || i;
                j = i && i && i;
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 277))

    def test_operator_assoc_278(self):
        """test operator associativity"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = --i;
                j = -.-.i;
                j = --.i;
                j = -.-i;
                j = !!i;
                j = -!-.1;
                j = !-i;
                j = !-.i;
                j = -.!i;
                j = !-.-!i;
                j = -!-i;
            EndBody."""
        expect = r"""Error on line 9 col 21: !"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 278))

    def test_operator_assoc_279(self):
        """test operator associativity"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = a()();
            EndBody."""
        expect = r"""Error on line 4 col 23: ("""
        self.assertTrue(TestParser.checkParser(testcase, expect, 279))

    def test_operator_assoc_280(self):
        """test operator associativity"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = i != i != i;
            EndBody."""
        expect = r"""Error on line 4 col 27: !="""
        self.assertTrue(TestParser.checkParser(testcase, expect, 280))

    def test_C_mistake_281(self):
        """test common mistake"""
        testcase = r"""Function: function()
            Body:
            EndBody."""
        expect = r"""Error on line 1 col 18: ("""
        self.assertTrue(TestParser.checkParser(testcase, expect, 281))

    def test_C_mistake_282(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = j = j;
            EndBody."""
        expect = r"""Error on line 4 col 22: ="""
        self.assertTrue(TestParser.checkParser(testcase, expect, 282))

    def test_C_mistake_283(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                For (;;) Do
                EndFor.
            EndBody."""
        expect = r"""Error on line 4 col 21: ;"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 283))

    def test_C_mistake_284(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                // Stupid comment
            EndBody."""
        expect = r"""/"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 284))

    def test_C_mistake_285(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                i = True ^ False;
            EndBody."""
        expect = r"""^"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 285))

    def test_python_mistake_286(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j, i = i, j;
            EndBody."""
        expect = r"""Error on line 4 col 17: ,"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 286))

    def test_python_mistake_287(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                # Another stupid comment
                j = i != i != i;
            EndBody."""
        expect = r"""#"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 287))
        
    def test_python_mistake_288(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                While True:
                EndWhile.
            EndBody."""
        expect = r"""Error on line 4 col 16: While"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 288))

    def test_python_mistake_289(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = i
            EndBody."""
        expect = r"""Error on line 5 col 12: EndBody"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 289))

    def test_python_mistake_290(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = i != i != i;
            EndBody."""
        expect = r"""Error on line 4 col 27: !="""
        self.assertTrue(TestParser.checkParser(testcase, expect, 290))

    def test_typo_291(self):
        """test common mistake"""
        testcase = r"""Var: x = 0x0;"""
        expect = r"""Error on line 1 col 10: x0"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 291))

    def test_typo_292(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = true;
            EndBody."""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 292))

    def test_typo_293(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                Var: _x = 0;
            EndBody."""
        expect = r"""_"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 293))

    def test_typo_294(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                If True Then
                Else If True Then
                End If.
            EndBody."""
        expect = r"""E"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 294))

    def test_typo_295(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                For (i = {}, i, i=i+1) Do
                EndFor.
            EndBody."""
        expect = r"""Error on line 4 col 33: ="""
        self.assertTrue(TestParser.checkParser(testcase, expect, 295))

    def test_typo_296(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = j ** 2;
            EndBody."""
        expect = r""""""
        self.assertTrue(TestParser.checkParser(testcase, expect, 296))

    def test_typo_297(self):
        """test common mistake"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = j / 2;
            EndBody."""
        expect = r"""/"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 297))

    def test_long_program_298(self):
        """test common mistake"""
        testcase = r"""Var: x;
        Var: y;
        Var: z;
        Function: function
            Parameter: j, brr[1000]
            Body:
                For (j = 0, j < 3; 1) Do
                    If (j == 0) && (j % 3 == 0) Then
                        x = brr[j];
                    ElseIf (j == 1) || (j % 2 == 1) Then
                        y = brr[j];
                        While (y % (j * j) != 0) Do
                            y = y + 1;
                        EndWhile.
                    Else
                        Var: k = 0xFFFFFFFF;
                        k = int_of_string(brr[j]);
                        z = k;
                EndFor.
            EndBody.
            
        Function: main
            Parameter: argv[1000], argc
            Body:
                function(argc, argv)
            EndBody."""
        expect = r"""Error on line 7 col 33: ;"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 298))

    def test_long_program_299(self):
        """test common mistake"""
        testcase = r"""Var: x = 0, y = 0, z = 0;
        Function: function
            Parameter: j, brr[1000]
            Body:
                For (j = 0, j < 3; 1) Do
                    If (j == 0) && (j % 3 == 0) Then
                        x = brr[j];
                    ElseIf (j == 1) || (j % 2 == 1) Then
                        y = brr[j];
                        While (y % (j * j) != 0) Do
                            y = y + 1;
                        EndWhile.
                    Else
                        Var: k = 0xFFFFFFFF;
                        k = int_of_string(brr[j]);
                        z = k;
                EndFor.
            EndBody.
            
        Function: super_print
            Parameter: str, n
            Body:
                For (i = 0, i < n, 1) Do
                    print(str);
                EndFor.
            EndBody.
            
        Function: main
            Parameter: argv[1000], argc
            Body:
                function(argc + 1, argv)
                Do
                    print("\n\r");
                    super_print("Hello World\n");
                While True
                EndDo.
            EndBody."""
        expect = r"""Error on line 5 col 33: ;"""
        self.assertTrue(TestParser.checkParser(testcase, expect, 299))