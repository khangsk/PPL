import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    ######################################################################
    # ARRAY TEST: 7 testcases
    def test01_valid_normal_array(self):
        """Valid normal array"""
        input = """Var: x[123] = {1,2,3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test02_empty_array(self):
        """Check empty array"""
        input = """Var: x[0] = {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test03_array_contains_array(self):
        """Check array contains arrays"""
        input = \
"""Var: x[0] = {{}};
Var: y = {"asd", 0, {123, 12.3}, 1.23};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test04_array_contains_comment(self):
        """Check array contains comment"""
        input = """Var: x = {{1,2,3}, **asdkhasd!@#!@$!@** "abc"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test05_array_contains_id(self):
        """Check array contains id"""
        # FAILED WHEN SWITCH FROM ARRAY ELEM TO EXPR
        input = """Var: x[0] = {abc};"""
        expect = "Error on line 1 col 13: abc"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test06_unclosed_array(self):
        """Check unclosed array"""
        input = """Var: x[0] = {1,2,3 ;"""
        expect = "Error on line 1 col 19: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test07_array_with_ws(self):
        """Check array with various white space"""
        input = """Var: x[0] = {   1,  2,3 
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))


    ######################################################################
    # VAR DECL TEST: 14 testcases

    def test11_simple_var_decl(self):
        """Check simple var decl"""
        input = \
"""Var  :       anyid;
Var:a = 123.321e-123;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test12_multiple_var_decl(self):
        """Check var decl with multiple ids"""
        input = """Var  :       anyid, moreid,  mUchm0r31d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test13_single_var_decl_assign(self):
        """Check single var decl with assignment"""
        input = """Var:someid=True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test14_multiple_var_decl_assign(self):
        """Check multiple var decl, some has assignment"""
        input = """Var:someid, mor3Id= "SomeSTRING",   some_more_id,muchmoreID = 123.321e-2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test15_multiple_var_decl_ws(self):
        """Check multiple var decl, some has assignment with various white spaces"""
        input = """Var :         someid, mor3Id
        = "SomeSTRING"
        ,
    some_more_id,muchmoreID = {"str","s"},  lots_m0rE_1D = False;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test16_multiple_var_decl_ws_composites(self):
        """Check multiple var decl, add some composite ids"""
        input = """Var: someid[0][1][123][999], mor3Id[1000] = "SomeSTRING",
some_more_id[987],muchmoreID = 123.321e-2,  lots_m0rE_1D[123][123] = {12,3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test17_composite_var_no_dim(self):
        """Check composite id with no literal in brackets"""
        input = """Var: someid[] = {"w","h","oops"};"""
        expect = "Error on line 1 col 12: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test18_composite_var_wrong_dim(self):
        """Check composite id with wrong literal in dimension"""
        input = """Var: someid[1.23E-2] = {"w","h","oops"};"""
        expect = "Error on line 1 col 12: 1.23E-2"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test19_var_decl_wrong_keyword(self):
        """Check var decl with wrong keyword"""
        input = """vAr: someid;"""
        expect = "Error on line 1 col 0: vAr"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test20_var_decl_missing_comma(self):
        """Check var decl missing comma"""
        input = """Var someid;"""
        expect = "Error on line 1 col 4: someid"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test21_var_decl_no_id(self):
        """Check var decl without id"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test22_var_decl_missing_semi(self):
        """Check var decl missing semicolon"""
        input = """Var: someid = 123"""
        expect = "Error on line 1 col 17: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test23_var_decl_assign_exp(self):
        """Check var decl with expression assignment"""
        input = """Var: someid = 1+2+3;"""
        expect = "Error on line 1 col 15: +"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test24_var_decl_comment(self):
        """Check var decl with expression assignment"""
        input = """Var **some COMMENT**: ****someid = 3
        **more more**;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))


    ######################################################################
    # FUNC DECL TEST: 9 testcases

    def test31_simple_func_decl(self):
        """Check simple func decl"""
        input = \
"""Function: foo
    Body:
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test32_simple_func_decl_param(self):
        """Check simple func decl with some param"""
        input = \
"""Function: foo
    Parameter: a, b,c[123] ,d[123][234][0]  ,e
    Body:
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test33_simple_func_decl_param_no_id(self):
        """Check simple func decl with some param"""
        input = \
"""Function: foo
    Parameter:
    Body:
    EndBody."""
        expect = "Error on line 3 col 4: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test34_simple_func_decl_param_assign(self):
        """Check simple func decl with some params have assignment"""
        input = \
"""Function: foo
    Parameter: a, b = 123,c[123] ,d[123][234][0]  ,e
    Body:
    EndBody."""
        expect = "Error on line 2 col 20: ="
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test35_func_param_semi(self):
        """Check simple func decl param has semicolon"""
        input = \
"""Function: foo
    Parameter: abc;
    Body:
    EndBody."""
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test36_func_miss_dot(self):
        """Check simple func decl without dot at the end"""
        input = \
"""Function: foo
    Parameter: abc
    Body:
    EndBody"""
        expect = "Error on line 4 col 11: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test37_func_with_comment(self):
        """Check simple func decl with comments"""
        input = \
"""** some comment **
Function: foo ** some more comment **
    Parameter: abc ** MuchM0re comment **
    Body:  ** LOTS of comment !@#$%^^&%&*() **
    EndBody **Here some too**. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test38_multiple_func_decl(self):
        """Check multiple func decl"""
        input = """Function: foo Parameter: abc Body: EndBody. Function: foo Body: EndBody.
Function: goo Parameter: abc Body: EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test39_func_in_func_decl(self):
        """Check func decl inside func"""
        input = \
"""Function: foo 
    Body: 
        Function: goo
            Body:
            EndBody.
    EndBody."""
        expect = "Error on line 3 col 8: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test40_func_without_body(self):
        """Check func decl without body"""
        input = """Function: foo"""
        expect = "Error on line 1 col 13: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 240))


    ######################################################################
    # EXPRESSION TEST: 8 testcases

    def test41_simple_exp_test(self):
        """A simple expression"""
        input = \
r"""Function: foo 
    Body: 
        a = 1 + 2-3+  4;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test42_complex_exp_test(self):
        """Some more complex expression"""
        input = \
r"""Function: foo 
    Body: 
        a = 1 + 1.23 *. abc \. id[12[123][2][moreid]];
        b = 1.E-12 *. someThinG \ (-12.34) +. (!True) [False[moreid][more]]
=/= (foo(123) || goo(-234 && ((f()[1 + 3][-2.99e-123] + 56%7))));
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test43_double_exp(self):
        """Two expression in an assignment"""
        input = \
r"""Function: foo 
    Body: 
        b = 1.E-12  =/= a f(123);
    EndBody."""
        expect = "Error on line 3 col 26: f"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test44_exp_with_string(self):
        """Expression has string in it"""
        # ATTENTION
        input = \
r"""Function: foo 
    Body: 
        a = 1+2+3 + "abcd";
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test45_exp_with_comment(self):
        """Expression has some comments in it"""
        input = \
r"""Function: foo 
    Body: 
        a = 1+2-3.0 ** this is some comm** - foo(987 * 123) \. someid **will it work?**;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test46_exp_relation_association(self):
        """Expression has no association relation ops"""
        input = \
r"""Function: foo 
    Body: 
        a = 123 < 321 < 999;
    EndBody."""
        expect = "Error on line 3 col 22: <"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test47_exp_unary(self):
        """Expression has lots of unary ops"""
        input = \
r"""Function: foo 
    Body: 
        a = !-.--!!!--.--!!!!!!!(!!!!!!!(anyid * whoop(!!1)));
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))
    
    def test48_exp_binary_misplace_unary(self):
        """Expression has misplaced binary op at unary pos"""
        input = \
r"""Function: foo 
    Body: 
        a = +2;
    EndBody."""
        expect = "Error on line 3 col 12: +"
        self.assertTrue(TestParser.checkParser(input, expect, 248))


    ######################################################################
    # STATEMENT TEST: 

    ######################
    # VARIABLE DECLARATION TEST: 9 testcases
    def test51_simple_var_decl_in_func(self):
        """Function has some var decl inside"""
        input = \
r"""Function: foo 
    Body: 
        Var: a = 0.5e-9;
        Var: b, c, a , d[999], e[0][0], ids;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test52_var_decl_stmt_with_comment(self):
        """Function has some var decl mix with comments"""
        input = \
r"""Function: foo 
    Body: 
        Var: a **** ** comm** ;
        Var: b, c, a , d[ ** comm ** 999],
        ** this should be ok **      e[0][0], ids;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test53_var_decl_stmt_wrong_composite_dim_empty(self):
        """Var decl has wrong composite var: empty"""
        input = \
r"""Function: foo 
    Body: 
        Var: a[];
    EndBody."""
        expect = "Error on line 3 col 15: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test54_var_decl_stmt_wrong_composite_dim_wrongtype(self):
        """Var decl has wrong composite var: dim is not an int"""
        input = \
r"""Function: foo 
    Body: 
        Var: a[12e-21];
    EndBody."""
        expect = "Error on line 3 col 15: 12e-21"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test55_var_decl_stmt_outside_body(self):
        """Var decl outside of function body"""
        input = \
r"""Function: foo 
        Var: id;
    Body: 
    EndBody."""
        expect = "Error on line 2 col 8: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test56_var_decl_stmt_not_at_the_beginning(self):
        """Var decl not at the beginning of body"""
        input = \
r"""Function: foo 
    Body: 
        Var: this, should[12];
        this = that;
        Var: be, failed;
    EndBody."""
        expect = "Error on line 5 col 8: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test57_var_decl_has_assignment(self):
        """Var decl has id assignment"""
        input = \
r"""Function: foo 
    Body: 
        Var: someid = moreid;
    EndBody."""
        expect = "Error on line 3 col 22: moreid"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test58_var_decl_assign_negative_num(self):
        """Var decl has expression assignment"""
        input = \
r"""Function: foo 
    Body: 
        Var: someid = -123.;
    EndBody."""
        expect = "Error on line 3 col 22: -"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test59_var_decl_has_expr_assign(self):
        """Var decl has negative number assignment"""
        input = \
r"""Function: foo 
    Body: 
        Var: someid = 1 + 2 \. 3.0;
    EndBody."""
        expect = "Error on line 3 col 24: +"
        self.assertTrue(TestParser.checkParser(input, expect, 259))


    ######################
    # ASSIGNMENT TEST: 6 testcases

    def test61_simple_valid_assignment(self):
        """Test simple assignment"""
        input = \
r"""Var : a,b = 9,c;

Function: foo 
    Body: 
        Var: someid;
        someid = False;
        a = 1 * 2 + 3 \ 4;
    EndBody.

Function: somefunc 
    Body: 
        Var: somemoreid[123] = {1,2,3};
        somemoreid = {123};
        c = b \. 9;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test62_assignment_with_undeclared_ids(self):
        """Test assignment involves undeclared ids"""
        input = \
r"""Function: foo 
    Body: 
        someid = 123 * 123 + foo() - oo || whoop(a > b[-1.], c, d);
        somemoreid[9] = 123 * 123 + foo() - oo || whoop(a > b[-1.], c, d);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test63_assignment_with_index_ops(self):
        """Test assignment involves index operator at left hand side"""
        input = \
r"""Function: foo 
    Body: 
        123[9[8][7]] = 123 * 123[abc] + foo() - oo || whoop(a > b[False], c, d);
        arr[123456 *. 654321] = 123 * 123 + foo() - oo || whoop(a > b, c, d);
        more_arr[ foo() || 123456 *. 654321] = 123 * 123 + foo() - oo || whoop(a > b, c, d);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test64_assignment_left_hand_side(self):
        """Test assignment with number left hand side"""
        input = \
r"""Function: foo 
    Body: 
        123 = 123;
    EndBody."""
        expect = "Error on line 3 col 12: ="
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test65_assignment_left_hand_side(self):
        """Test assignment with string left hand side"""
        input = \
r"""Function: foo 
    Body: 
        "abcd" = 123;
    EndBody."""
        expect = "Error on line 3 col 15: ="
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test66_assignment_left_hand_side(self):
        """Test assignment with string left hand side"""
        input = \
r"""Function: foo 
    Body: 
        "abcd" = 123;
    EndBody."""
        expect = "Error on line 3 col 15: ="
        self.assertTrue(TestParser.checkParser(input, expect, 266))


    ######################
    # IF TEST: 9 testcases

    def test71_simple_if_test(self):
        """Test simple if"""
        input = \
r"""Function: foo 
    Body:
        If (something) Then
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test72_simple_if_elif_test(self):
        """Test simple if and else if"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        If (something) Then
            something = 1 + 2 * 3 \. 4;
        ElseIf something < more Then
            more = more * more;
        ElseIf (((something || more))) Then
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test73_simple_if_elif_else_test(self):
        """Test simple if and else if and else"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        If something Then
        ElseIf (something < more) Then
        Else
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test74_simple_if_else_test(self):
        """Test simple if and else"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        If (something) Then
        Else
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test75_nested_if_test(self):
        """Test nested if"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        If (something) Then
            If (True) Then
            EndIf.
        ElseIf (something < more) Then
            If (False) Then
            ElseIf (True) Then
            EndIf.
        Else
            If (something) Then
            ElseIf (something < more) Then
            Else
            EndIf.
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test76_if_no_condition(self):
        """Test if without condition"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        If  Then
            do_something();
        EndIf.
    EndBody."""
        expect = "Error on line 4 col 12: Then"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test77_if_no_then(self):
        """Test if without condition"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        If (True)
            do_something();
        EndIf.
    EndBody."""
        expect = "Error on line 5 col 12: do_something"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test78_elif_begin(self):
        """Test if begin with elseif"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        ElseIf (True)
            do_something();
        EndIf.
    EndBody."""
        expect = "Error on line 4 col 8: ElseIf"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test79_if_multiple_else(self):
        """Test if with multiple else"""
        input = \
r"""Function: foo
    Body:
        If (True)
            do_somemore();
        Else
        Else
        Else
        EndIf.
    EndBody."""
        expect = "Error on line 4 col 12: do_somemore"
        self.assertTrue(TestParser.checkParser(input, expect, 279))


    ######################
    # FOR TEST: 8 testcases

    def test81_simple_for_test(self):
        """Test simple for"""
        input = \
r"""Function: foo 
    Body:
        Var: x;
        For (x = 1, x < 10, 1) Do
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))


    def test82_for_with_stmt_test(self):
        """Test for contains some stmt"""
        input = \
r"""Function: foo 
    Body:
        Var: x;
        For (x = 1, x < 10, 1) Do
            a = 123;
            b = b + 123;
            do_something();
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test83_nested_for_test(self):
        """Test nested for"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        For (something = 123 * 321 + 999, 123 * 1.2e2, False) Do
            For (more = 123 * 321 + 999, 123 * 1.2e2, False) Do
                more = more + something;
            EndFor.
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test84_for_no_condition(self):
        """Test for without condition"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        For Do
            do_something();
        EndFor.
    EndBody."""
        expect = "Error on line 4 col 12: Do"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test85_for_composite_condition_var(self):
        """Test for with composite condition var"""
        input = \
r"""Function: foo
    Body:
        For (a[1] = 123, 1, 1) Do
        EndFor.
    EndBody."""
        expect = "Error on line 3 col 14: ["
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test86_for_no_condition_parentheses(self):
        """Test for with no parentheses"""
        input = \
r"""Function: foo
    Body:
        For a = 123, 1, 1 Do
        EndFor.
    EndBody."""
        expect = "Error on line 3 col 12: a"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test87_for_no_do(self):
        """Test for missing do keyword"""
        input = \
r"""Function: foo
    Body:
        For (a = 123, 1, 1)
        EndFor.
    EndBody."""
        expect = "Error on line 4 col 8: EndFor"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test88_for_no_var_assignment(self):
        """Test for missing first assignment"""
        input = \
r"""Function: foo
    Body:
        For (, 1, 1)
        EndFor.
    EndBody."""
        expect = "Error on line 3 col 13: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 288))


    ######################
    # WHILE TEST: 6 testcases

    def test91_simple_while_test(self):
        """Test simple while"""
        input = \
r"""Function: foo 
    Body:
        While True Do
        EndWhile.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))


    def test92_while_with_stmt_test(self):
        """Test while contains some stmt"""
        input = \
r"""Function: foo 
    Body:
        Var: x;
        While (x < 10) Do
            a = 123;
            b = b + 123;
            do_something();
        EndWhile.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test93_nested_while_test(self):
        """Test nested while"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        While (something > more) Do
            While (abc + 123 \ 321) Do
                more = more + something;
                do_something();
            EndWhile.
        EndWhile.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test94_while_no_condition(self):
        """Test while without condition"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        While Do
            do_something();
        EndWhile.
    EndBody."""
        expect = "Error on line 4 col 8: While"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test95_while_parentheses_no_condition(self):
        """Test while with no condition, only parentheses"""
        input = \
r"""Function: foo
    Body:
        While () Do
        EndWhile.
    EndBody."""
        expect = "Error on line 3 col 8: While"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test96_while_no_do(self):
        """Test while missing do keyword"""
        input = \
r"""Function: foo
    Body:
        While a == 123
        EndWhile.
    EndBody."""
        expect = "Error on line 3 col 8: While"
        self.assertTrue(TestParser.checkParser(input, expect, 296))


    ######################
    # DO WHILE TEST: 6 testcases

    def test301_simple_dowhile_test(self):
        """Test simple do while"""
        input = \
r"""Function: foo 
    Body:
        Do While abc
        EndDo.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 301))

    def test302_dowhile_with_stmt_test(self):
        """Test do while contains some stmt"""
        input = \
r"""Function: foo 
    Body:
        Var: x;
        Do
            a = 123;
            b = b + 123;
            do_something();
        While x < 10 
        EndDo.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 302))

    def test303_nested_dowhile_test(self):
        """Test nested do while"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        Do
            Do
                more = more + something;
                do_something();
            While (abc + 123 \ 321)
            EndDo.
        While (something > more)
        EndDo.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 303))

    def test304_dowhile_no_condition(self):
        """Test do while without condition"""
        input = \
r"""Function: foo 
    Parameter: something, more
    Body:
        Do
            do_something();
        While 
        EndDo.
    EndBody."""
        expect = "Error on line 7 col 8: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 304))

    def test305_dowhile_parentheses_no_condition(self):
        """Test do while with no condition, only parentheses"""
        input = \
r"""Function: foo
    Body:
        Do
        While ()
        EndWhile.
    EndBody."""
        expect = "Error on line 4 col 15: )"
        self.assertTrue(TestParser.checkParser(input, expect, 305))

    def test306_do_while_no_while(self):
        """Test do while missing while keyword"""
        input = \
r"""Function: foo
    Body:
        Do a = 123;
        EndDo.
    EndBody."""
        expect = "Error on line 4 col 8: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 306))


    ######################
    # BR, CONT TEST: 3 testcases

    def test311_br_and_cont_in_if_loop_stmt(self):
        """Test br cont in if loop stmt"""
        input = \
r"""Function: foo
    Body:
        Break;
        Continue;
        For (qbc = 321, (True || False), 123) Do
            Break;
            Continue;
        EndFor.

        While False Do
            If (abc) Then
                Break
                ;
            ElseIf def Then
                Continue   ;
            Else Break;
            EndIf.
        EndWhile.

        Do 
            Break;
            Continue;
        While True
        EndDo.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 311))

    def test312_br_missing_semi(self):
        """Test break stmt missing semicolon"""
        input = \
r"""Function: foo
    Body:
        Do
            Break
        While True
        EndDo.
    EndBody."""
        expect = "Error on line 5 col 8: While"
        self.assertTrue(TestParser.checkParser(input, expect, 312))

    def test313_cont_missing_semi(self):
        """Test continue stmt missing semicolon"""
        input = \
r"""Function: foo
    Body:
        Do
            Continue
        While True
        EndDo.
    EndBody."""
        expect = "Error on line 5 col 8: While"
        self.assertTrue(TestParser.checkParser(input, expect, 313))


    ######################
    # CALL TEST: 4 testcases

    def test321_simple_call_test(self):
        """Test simple call"""
        input = \
r"""Function: foo
    Body:
        foo();
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 321))

    def test322_simple_call_with_param(self):
        """Test simple call with paramenters"""
        input = \
r"""Function: foo
    Body:
        foo((((123*.321))), abcd, efgh * ij[a[b[1]][2]][3]);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 322))

    def test323_call_with_no_semi(self):
        """Test call without semicolon"""
        input = \
r"""Function: foo
    Body:
        foo((((123*.321))), abcd, efgh * ij[a[b[1]][2]][3])
    EndBody."""
        expect = "Error on line 4 col 4: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 323))

    def test324_call_missing_parentheses(self):
        """Test call without parentheses"""
        input = \
r"""Function: foo
    Body:
        foo;
    EndBody."""
        expect = "Error on line 3 col 11: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 324))


    ######################
    # RET TEST: 4 testcases

    def test331_ret_stmt_check(self):
        """Test return stmt everywhere"""
        input = \
r"""Function: foo
    Body:
        Return;
        Return True;
        For (qbc = 321, (True || False), 123) Do
            Return;
            Return (999);
        EndFor.

        While False Do
            If (abc) Then
                Return
                ;
            ElseIf def Then
                Return "somes tring"   ;
            Else Break;
            EndIf.
        EndWhile.

        Do 
            Return xas\a\.h*.c+.n \ "string";
            Return;
        While True
        EndDo.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 331))

    def test332_ret_missing_semi(self):
        """Test return stmt missing semicolon"""
        input = \
r"""Function: foo
    Body:
        Do
            Return
        While True
        EndDo.
    EndBody."""
        expect = "Error on line 5 col 8: While"
        self.assertTrue(TestParser.checkParser(input, expect, 332))

    def test333_ret_multiple_expr(self):
        """Test return stmt have multiple expressions"""
        input = \
r"""Function: foo
    Body:
        Do
            Return abc (999 + 1) "oops" "failed";
        While True
        EndDo.
    EndBody."""
        expect = "Error on line 4 col 33: oops"
        self.assertTrue(TestParser.checkParser(input, expect, 333))

    def test334_return_statement(self):
        """Test return some statement"""
        input = \
r"""Function: foo
    Body:
        Do
            Return Continue;;
        While True
        EndDo.
    EndBody."""
        expect = "Error on line 4 col 19: Continue"
        self.assertTrue(TestParser.checkParser(input, expect, 334))

    
    ######################################################################
    # SOME COMBINATION: 8 testcases

    def test341_lone_semicolon(self):
        """Test lone semicolons"""
        input = \
r"""Function: foo
    Body:
        ;
    EndBody."""
        expect = "Error on line 3 col 8: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 341))

    def test342_empty_file(self):
        """Test empty file"""
        input = ""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 342))

    def test343_expr_alone(self):
        """Test expression alone in body"""
        input = \
r"""Function: foo 
    Body: 
        a == 1;
    EndBody."""
        expect = "Error on line 3 col 10: =="
        self.assertTrue(TestParser.checkParser(input, expect, 343))

    def test344_do_dowhile_combination(self):
        """Test do and dowhile combine"""
        input = \
r"""Function: foo 
    Body: 
        Do While True Do EndWhile. While True EndDo.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 344))

    def test345_wrong_order_vardecl_funcdecl(self):
        """Test var decl in various scope"""
        input = \
r"""Var: a = 0,b,c;
Function: foo 
    Body: 
    EndBody.
Var: d;
Function: goo 
    Body: 
    EndBody."""
        expect = "Error on line 5 col 0: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 345))

    def test346_multiple_var_decl_hierachy(self):
        """Test var decl in various scope"""
        input = \
r"""Var: a = 0,b,c;

Function: foo 
    Body: 
        Var: a,b = True,c;
        do_something();

        For (it=0, 0, 0) Do
            Var: d,e,f;
            do_something();

            While (abcd) Do
                Var: g,h,i;
                do_something();

                If True Then
                    Var: o,f,f;
                    do_something();
                ElseIf d Then
                    Var: f,f;
                    do_something();
                Else
                    Var: d,o,w,n;
                    do_something();
                EndIf.
            EndWhile.
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 346))

    def test347_illegal_numeric_pass(self):
        """Test illegal numeric identifier"""
        input = \
r"""Function: foo 
    Body: 
        a = 0123 + 123;
    EndBody."""
        expect = "Error on line 3 col 13: 123"
        self.assertTrue(TestParser.checkParser(input, expect, 347))

    def test348_dense_code_check(self):
        """Test no space code"""
        input = r"""Var:a,b=123;Function:foo123 Parameter:a[99]Body:Var:x;""" + \
                r"""abc=321;WhileTrueDoEndWhile.If123ThenFor(abc=999,(13||31)""" + \
                r"""&&True-False,f())DoVar:def;EndFor.ElseVar:ghi;EndIf.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 348))


#     def testnext(self):
#         input = \
# """Function: abc
#     Body:
#             For (i=x+7,i<a[2][3], 6) Do
#                 writeLn(i);
#             EndFor.
#     EndBody."""
#         expect = "..."
#         self.assertTrue(TestParser.checkParser(input, expect, 204))