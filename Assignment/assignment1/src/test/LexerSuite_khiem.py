import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    ###################################################
    #   STRING TEST: 13 testcases
    def test_01_valid_string(self):
        """test valid string"""
        input = \
"""" This is a test !@#$%^^&*()?/|"
" 1234567890 \\' ASD" abc 
"KJFLDSK '" \\f asdasd "
"\\b\\f\\r\\n\\t\\'\\\\"
 """
        output = \
""" This is a test !@#$%^^&*()?/|, 1234567890 \\' ASD,abc,KJFLDSK '" \\f asdasd ,\\b\\f\\r\\n\\t\\'\\\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,101))

    def test_02_unclosed_string(self):
        """test unclosed string eof"""
        input = """" This is a test  asdsadasd \\f asdasd  """
        output = """Unclosed String:  This is a test  asdsadasd \\f asdasd  """
        self.assertTrue(TestLexer.checkLexeme(input,output,102))

    def test_03_unclosed_string_2(self):
        """test unclosed string has '" """
        input = """" This is a test  asdsadasd \\f asdasd '\""""
        output = """Unclosed String:  This is a test  asdsadasd \\f asdasd '\""""
        self.assertTrue(TestLexer.checkLexeme(input,output,103))

    def test_04_unclosed_string_3(self):
        """test unclosed string empty"""
        input = '"'
        output = """Unclosed String: """
        self.assertTrue(TestLexer.checkLexeme(input,output,104))

    def test_05_unclosed_string_4(self):
        """test unclosed string has newline"""
        input = '"abc\ndef"'
        output = """Unclosed String: abc"""
        self.assertTrue(TestLexer.checkLexeme(input,output,105))

    def test_06_unclosed_string_5(self):
        """test unclosed string has only newline"""
        input = '"\n"'
        output = """Unclosed String: """
        self.assertTrue(TestLexer.checkLexeme(input,output,106))

    def test_07_unclosed_string_6(self):
        """test unclosed string has multiple newlines"""
        input = '"\n\n\n\n\n\n"'
        output = 'Unclosed String: '
        self.assertTrue(TestLexer.checkLexeme(input,output,107))

    def test_08_unclosed_string_7(self):
        """test unclosed string"""
        input = '"abc\'" '
        output = 'Unclosed String: abc\'" '
        self.assertTrue(TestLexer.checkLexeme(input,output,108))

    def test_09_unclosed_string_8(self):
        """test unclosed string has '" and newline"""
        input = '"abc\'"\n'
        output = 'Unclosed String: abc\'"'
        self.assertTrue(TestLexer.checkLexeme(input,output,109))

    def test_10_unclosed_string_9(self):
        """test unclosed string has '" and multiple newlines"""
        input = '"abc\'"\n\n\n\n'
        output = 'Unclosed String: abc\'"'
        self.assertTrue(TestLexer.checkLexeme(input,output,110))

    def test_11_illegal_escape_quotes(self):
        """test illegal_escape string has \\" """
        input = '"abc\\""'
        output = 'Illegal Escape In String: abc\\"'
        self.assertTrue(TestLexer.checkLexeme(input,output,111))

    def test_12_illegal_escape_question(self):
        """test illegal esape has \\?"""
        input = '"abc\\? defg"'
        output = 'Illegal Escape In String: abc\\?'
        self.assertTrue(TestLexer.checkLexeme(input,output,112))

    def test_13_illegal_escape_question_2(self):
        """test illegal esape has \\?"""
        input = '"ab?c\\? defg"'
        output = 'Illegal Escape In String: ab?c\\?'
        self.assertTrue(TestLexer.checkLexeme(input,output,113))

    def test_14_string_no_beginning_quote(self):
        """test string has no beginning quote"""
        input = 'some string"'
        output = 'some,string,Unclosed String: '
        self.assertTrue(TestLexer.checkLexeme(input,output,114))

    def test_15_string_contain_slash_quote_double(self):
        """test string has \\ ' and " """
        input = r""" "\'"" """
        output = r'\',Unclosed String:  '
        self.assertTrue(TestLexer.checkLexeme(input,output,115))

    def test_16_string_contain_slash_quote_double_2(self):
        """test string has \\ ' and " """
        input = """ "\\'\" """
        output = r'\',<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input,output,116))

    def test_17_string_contains_illegal_escape_1(self):
        """test string which contains illegal escape: quote"""
        input = """" This is a test '" asdsadasd ' \\f asdasd " """
        output = """Illegal Escape In String:  This is a test '" asdsadasd ' """
        self.assertTrue(TestLexer.checkLexeme(input,output,117))

    def test_18_string_contains_illegal_escape_2(self):
        """test string which contains illegal escape: unidentified backslash"""
        input = """" This is a test '" asdsadasd \\h asdasd " """
        output = """Illegal Escape In String:  This is a test '" asdsadasd \\h"""
        self.assertTrue(TestLexer.checkLexeme(input,output,118))

    def test_19_string_contains_illegal_escape_3(self):
        """test string which contains illegal escape: lone backslash"""
        input = """" This is a test '" asdsadasd \\ asdasd " """
        output = """Illegal Escape In String:  This is a test '" asdsadasd \\ """
        self.assertTrue(TestLexer.checkLexeme(input,output,119))

    def test_20_string_contains_newline(self):
        """test string which contains newline character"""
        input = """" This is a test '" asdsa\ndasd \\ asdasd " """
        output = """Unclosed String:  This is a test '" asdsa"""
        self.assertTrue(TestLexer.checkLexeme(input,output,120))

    def test_21_empty_string(self):
        """test empty string"""
        input = """"" """
        output = """,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,121))

    def test_22_unclose_string_contains_quote(self):
        """test string which contains quote and double quote"""
        input = """" This is a test '" """
        output = """Unclosed String:  This is a test '" """
        self.assertTrue(TestLexer.checkLexeme(input,output,122))

    def test_23_string_contains_CR(self):
        """test string which contains carriage return"""
        input = """ "Somestring \r continue" """
        output = """Somestring 
 continue,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,123))

    def test_24_string_contains_CR_NL(self):
        """test string which contains carriage return and newline"""
        input = """ "Somestring \r\n continue" """
        output = """Unclosed String: Somestring 
"""
        self.assertTrue(TestLexer.checkLexeme(input,output,124))

    def test_25_string_contains_tabs(self):
        """test string which contains \\t"""
        input = """ "Somestring \t continue" """
        output = """Somestring \t continue,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,125))

    # IS THESE TWO POSSIBLE?
    def test_26_string_contains_backspace(self):
        """test string which contains \\b (back space)"""
        input = """ "Somestring \b continue" """
        output = """Somestring \b continue,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,126))

    def test_27_string_contains_form_feed(self):
        """test string which contains \\f (form feed)"""
        input = """ "Somestring \f continue" """
        output = """Somestring \f continue,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,127))


    ###################################################
    #   COMMENT BLOCK: 4 testcases
    def test_28_valid_block_comment(self):
        """test valid block comment"""
        self.assertTrue(TestLexer.checkLexeme("***dsa?dkjsah**abc**dkj!* *@#!@#%^^*%%&**","abc,<EOF>",128))

    def test_29_valid_empty_block_comment(self):
        """test valid empty block comment"""
        self.assertTrue(TestLexer.checkLexeme("****","<EOF>",129))

    def test_30_incomplete_block_comment_1(self):
        """test incomplete block comment 1"""
        self.assertTrue(TestLexer.checkLexeme("**abc","Unterminated Comment",130))

    def test_31_incomplete_block_comment_2(self):
        """test incomplete block comment 2"""
        self.assertTrue(TestLexer.checkLexeme("**abc*","Unterminated Comment",131))


    ###################################################
    #   IDENTIFIER: 8 testcases
    def test_32_lower_id(self):
        """test valid lower identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",132))

    def test_33_lower_upper_id(self):
        """test valid lower uppercase id"""
        self.assertTrue(TestLexer.checkLexeme("vaRiab","vaRiab,<EOF>",133))

    def test_34_lower_upper_digit_id(self):
        """test valid lower uppercase digit id"""
        self.assertTrue(TestLexer.checkLexeme("s0m3Th1ng123","s0m3Th1ng123,<EOF>",134))

    def test_35_lower_upper_digit_underscore_id(self):
        """test valid lower uppercase digit underscore id"""
        self.assertTrue(TestLexer.checkLexeme("s0m3Th1ng___123_Som3THiN6","s0m3Th1ng___123_Som3THiN6,<EOF>",135))

    def test_36_wrong_token(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme("ab?cde","ab,Error Token ?",136))

    def test_37_wrong_first_letter_upper_id(self):
        """test wrong id first upper letter of id"""
        self.assertTrue(TestLexer.checkLexeme("Wrong","Error Token W",137))
                      
    def test_38_wrong_first_letter_number_1(self):
        """test wrong id first number digit of id"""
        self.assertTrue(TestLexer.checkLexeme("9reat","9,reat,<EOF>",138))

    def test_39_wrong_first_letter_number_2(self):
        """test wrong id first letter underscore of id"""
        self.assertTrue(TestLexer.checkLexeme("_wrong","Error Token _",139))


    ###################################################
    #   INTLIT: 10 testcases
    def test_40_zero_check(self):
        """test zero integer"""
        self.assertTrue(TestLexer.checkLexeme("0","0,<EOF>",140))

    def test_41_valid_int_dec(self):
        """test valid decimal integer"""
        self.assertTrue(TestLexer.checkLexeme("123 456","123,456,<EOF>",141))

    def test_42_valid_int_hex(self):
        """test valid hex integer"""
        self.assertTrue(TestLexer.checkLexeme("0xABCDEF12 0X100","0xABCDEF12,0X100,<EOF>",142))

    def test_43_valid_int_oct(self):
        """test valid oct integer"""
        self.assertTrue(TestLexer.checkLexeme("0o123 0O777","0o123,0O777,<EOF>",143))

    def test_44_invalid_int_dec_extra_0(self):
        """test invalid decimal integer with extra 0"""
        self.assertTrue(TestLexer.checkLexeme("0123","0,123,<EOF>",144))

    def test_45_invalid_int_hex_extra_0(self):
        """test invalid hex integer with extra 0"""
        self.assertTrue(TestLexer.checkLexeme("0x0123","0,x0123,<EOF>",145))

    def test_46_invalid_int_oct_extra_0(self):
        """test invalid hex integer with extra 0"""
        self.assertTrue(TestLexer.checkLexeme("0o0123","0,o0123,<EOF>",146))

    def test_47_invalid_int_prefix(self):
        """test invalid integer with wrong prefix"""
        self.assertTrue(TestLexer.checkLexeme("0a123","0,a123,<EOF>",147))

    def test_48_invalid_int_hex_letter(self):
        """test invalid hex integer with wrong letter"""
        self.assertTrue(TestLexer.checkLexeme("0X123abc","0X123,abc,<EOF>",148))

    def test_49_invalid_int_oct_letter(self):
        """test invalid oct integer with wrong letter"""
        self.assertTrue(TestLexer.checkLexeme("0o678","0o67,8,<EOF>",149))

    def test_50_int_dec_oct_hex_letter_dense(self):
        """test close dec hex oct int letter"""
        self.assertTrue(TestLexer.checkLexeme("00x1200ABC0D0o123","0,0x1200ABC0D0,o123,<EOF>",150))

    def test_51_int_hex_letter_prefix_only(self):
        """test hex letter with prefix only"""
        self.assertTrue(TestLexer.checkLexeme("0x 0X","0,x,0,Error Token X",151))

    def test_52_int_oct_letter_prefix_only(self):
        """test oct letter with prefix only"""
        self.assertTrue(TestLexer.checkLexeme("0o 0O","0,o,0,Error Token O",152))

    def test_53_int_wrong_prefix_1(self):
        """test int letter with wrong prefix 1"""
        self.assertTrue(TestLexer.checkLexeme("0G123","0,Error Token G",153))

    def test_54_int_wrong_prefix_2(self):
        """test int letter with wrong prefix 2"""
        self.assertTrue(TestLexer.checkLexeme("99x123","99,x123,<EOF>",154))


    ###################################################
    #   FLOATLIT and BOOL: xx testcases
    def test_55_valid_float(self):
        """test valid float"""
        input = """12.0e3 12e3 12.e5 12.0e3 12000. 120000E-1"""
        output = """12.0e3,12e3,12.e5,12.0e3,12000.,120000E-1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,155))

    def test_56_valid_exp_float(self):
        """test valid float with exp"""
        input = """123e456 123.e5 12.0e3 120000e-1"""
        output = """123e456,123.e5,12.0e3,120000e-1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,156))

    def test_57_valid_point_float(self):
        """test valid float with point"""
        input = """12.0 12.123124125 12123213213.12321312321"""
        output = """12.0,12.123124125,12123213213.12321312321,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,157))

    def test_58_float_with_addition_0_1(self):
        """test float has extra 0s"""
        input = """00123.123"""
        output = """0,0,123.123,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,158))

    def test_59_float_with_addition_0_2(self):
        """test float has extra 0s"""
        input = """00123.123E-123"""
        output = """0,0,123.123E-123,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,159))

    def test_60_float_with_addition_0_3(self):
        """test float has extra 0s"""
        input = """00123."""
        output = """0,0,123.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,160))

    def test_61_float_with_exp_missing_exp_number(self):
        """test float missing decimal after exp"""
        input = """123e"""
        output = """123,e,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,161))

    def test_62_float_with_both_missing_exp_number(self):
        """test float with both point and e but missing e decimal"""
        input = """123.123e"""
        output = """123.123,e,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,162))

    def test_63_float_dec_without_int_part(self):
        """test float"""
        input = """.123"""
        output = """.,123,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,163))

    def test_64_float_exp_without_int_part(self):
        """test float"""
        input = """E123"""
        output = """Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input,output,164))

    def test_65_float_end_with_dot(self):
        """test float has dot at the end"""
        input = """123."""
        output = """123.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,165))

    def test_66_float_has_e0(self):
        """test float has exp 0"""
        input = """1.e-0 1.E0"""
        output = """1.e-0,1.E0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,166))

    def test_67_float_dense(self):
        """test floats close together"""
        input = """1.e-123.e321"""
        output = """1.e-123,.,e321,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,167))


    ###################################################################
    #   BOOL test

    def test_68_valid_bool(self):
        """test valid bool"""
        input = """TrueFalse"""
        output = """True,False,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,168))

    def test_69_bool_mix_with_id(self):
        """test bool value mix with id, bool first"""
        input = """Trueabcd"""
        output = """True,abcd,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,169))

    def test_70_bool_mix_with_id_2(self):
        """test bool value mix with id, id first"""
        input = """someidFalse"""
        output = """someidFalse,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,170))
    
    def test_71_bool_mix_with_bool(self):
        """test bool value mix with bools"""
        input = """TrueFalseFalseTrueTrueFalseTrue"""
        output = """True,False,False,True,True,False,True,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,171))


    ###################################################
    #   ARRAY TEST: 8 testcases
    def test_72_simple_array_lexer(self):
        """test simple array lexer"""
        input = """{1,2,3,4,5}"""
        output = """{,1,,,2,,,3,,,4,,,5,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,172))

    def test_73_empty_array_lexer(self):
        """test empty array lexer"""
        input = """{}"""
        output = """{,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,173))

    def test_74_array_in_array_lexer(self):
        """test array in array lexer"""
        input = """{{1,2,3},{3,2,1}}"""
        output = """{,{,1,,,2,,,3,},,,{,3,,,2,,,1,},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,174))

    def test_75_array_in_array_lexer(self):
        """test array in array lexer"""
        input = """{{1,2,3},{3,2,1}}"""
        output = """{,{,1,,,2,,,3,},,,{,3,,,2,,,1,},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,175))

    def test_76_array_with_various_type_lexer(self):
        """test array contains various types lexer"""
        input = """{{{{}}},   {1,2,3} ,1, 2,  "abc",99E-0,True}"""
        output = """{,{,{,{,},},},,,{,1,,,2,,,3,},,,1,,,2,,,abc,,,99E-0,,,True,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,176))

    def test_77_array_with_id_and_exp(self):
        """test array contains id and expression lexer"""
        input = """{id, funccall(param, param2), 1+2+3}"""
        output = """{,id,,,funccall,(,param,,,param2,),,,1,+,2,+,3,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,177))

    def test_78_array_with_unclosed_string(self):
        """test array contains unclosed string lexer"""
        input = """{"a","b","c'"","d}"""
        output = """{,a,,,b,,,c'",,,Unclosed String: d}"""
        self.assertTrue(TestLexer.checkLexeme(input,output,178))

    def test_79_array_with_unclosed_comment(self):
        """test array contains unclosed comment lexer"""
        input = """{1,2,3,**something** 4, **fail*}"""
        output = """{,1,,,2,,,3,,,4,,,Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input,output,179))


    ###################################################
    #   EXPRESSION test

    def test_80_expression_test_1(self):
        """expression lexer test 1"""
        input = r"""a = 1 + 2-3+  4;"""
        output = "a,=,1,+,2,-,3,+,4,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 180))

    def test_81_expression_test_2(self):
        """expression lexer test 2"""
        input = r"""b = 1.E-12  =/= a f(123);"""
        output = "b,=,1.E-12,=/=,a,f,(,123,),;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 181))

    def test_82_expression_test_3(self):
        """expression lexer test 3"""
        input = r"""a = 1 + 1.23 *. abc \. id[12[123][2][moreid]];"""
        output = "a,=,1,+,1.23,*.,abc,\.,id,[,12,[,123,],[,2,],[,moreid,],],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 182))

    def test_83_expression_test_4(self):
        """expression lexer test 4"""
        input = r"""b = 1.E-12 *. someThinG \ (-12.34) +. (!True) [False[moreid][more]]
=/= (foo(123) || goo(-234 && ((f()[1 + 3][-2.99e-123] + 56%7))));"""
        output = "b,=,1.E-12,*.,someThinG,\,(,-,12.34,),+.,(,!,True,),[,False,[,moreid,]" + \
                ",[,more,],],=/=,(,foo,(,123,),||,goo,(,-,234,&&,(,(,f,(,),[,1,+,3,]," + \
                "[,-,2.99e-123,],+,56,%,7,),),),),;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 183))

    def test_84_expression_test_5(self):
        """expression lexer test 5"""
        input = r"""a = 1+2+3 + "abcd";"""
        output = "a,=,1,+,2,+,3,+,abcd,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 184))

    def test_85_expression_test_6(self):
        """expression lexer test 6"""
        input = r"""a = 1+2-3.0 ** this is some comm** - foo(987 * 123) \. someid **will it work?**;"""
        output = "a,=,1,+,2,-,3.0,-,foo,(,987,*,123,),\.,someid,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 185))

    def test_86_expression_test_7(self):
        """expression lexer test 7"""
        input = r"""a = 123 < 321 < 999;"""
        output = "a,=,123,<,321,<,999,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 186))


    ###################################################
    #Various func test
    def test_87_string_unclosed_lexer(self):
        """test program with unclosed string"""
        input = \
"""Function: abc
    Body:
        s = "abcde
    Endbody."""
        output = "Function,:,abc,Body,:,s,=,Unclosed String: abcde"
        self.assertTrue(TestLexer.checkLexeme(input, output, 187))

    def test_88_func_with_comment_lexer(self):
        """Check simple func decl with comments in lexer"""
        input = \
"""** some comment **
Function: foo ** some more comment **
    Parameter: abc ** MuchM0re comment **
    Body:  ** LOTS of comment !@#$%^^&%&*() **
    EndBody **Here some too**. """
        output = "Function,:,foo,Parameter,:,abc,Body,:,EndBody,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 188))

    def test_89_complex_exp_test_lexer(self):
        """Some complex expression in lexer"""
        input = \
r"""Function: foo 
    Body: 
        a = 1 + 1.23 *. abc \. id[12[123][2][moreid]];
        b = 1.E-12 *. someThinG \ (-12.34) +. (!True) [False[moreid][more]]
=/= (foo(123) || goo(-234 && ((f()[1 + 3][-2.99e-123] + 56%7))));
    EndBody."""
        output = r"""Function,:,foo,Body,:,a,=,1,+,1.23,*.,abc,\.,id,[,12,[,123,]""" + \
                r""",[,2,],[,moreid,],],;,b,=,1.E-12,*.,someThinG,\,(,-,12.34,),+.,(,""" + \
                r"""!,True,),[,False,[,moreid,],[,more,],],=/=,(,foo,(,123,),||,goo,(,""" + \
                r"""-,234,&&,(,(,f,(,),[,1,+,3,],[,-,2.99e-123,],+,56,%,7,),),),),;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, output, 189))

    def test_90_some_wrong_id_lexer_mix(self):
        """Some unrecognized id lexer in function"""
        input = \
r"""Function: ThisNotTrue
    Body:
        Do
            Break;
        While True
        EndDo.
    EndBody."""
        output = "Function,:,Error Token T"
        self.assertTrue(TestLexer.checkLexeme(input, output, 190))

    def test_91_some_wrong_keyword_mix_1(self):
        """Some unrecognized keyword in function"""
        input = \
r"""Funtion: foo
    Body:
        Do
            Break;
        While True
        EndDo.
    EndBody."""
        output = "Error Token F"
        self.assertTrue(TestLexer.checkLexeme(input, output, 191))

    def test_92_some_wrong_id_mix(self):
        """Some unrecognized id in function"""
        input = \
r"""Function: fo?o
    Body:
        Do
            Break;
        While True
        EndDo.
    EndBody."""
        output = "Function,:,fo,Error Token ?"
        self.assertTrue(TestLexer.checkLexeme(input, output, 192))

    def test_93_function_has_unclosed_comment(self):
        """Unterminated comment in function"""
        input = \
r"""Function: foo **This is valid**
    Body:
        Do
            Break; **This is invalid*
        While True
        EndDo.
    EndBody."""
        output = "Function,:,foo,Body,:,Do,Break,;,Unterminated Comment"
        self.assertTrue(TestLexer.checkLexeme(input, output, 193))

    def test_94_program_has_back_space(self):
        """Program has backspace in code"""
        input = \
"""Var: a,b,c;

Function: foo
    Body:
        Do
            Break\b;
        While True
        EndDo.
    EndBody."""
        output = "Var,:,a,,,b,,,c,;,Function,:,foo,Body,:,Do,Break,Error Token \b"
        self.assertTrue(TestLexer.checkLexeme(input, output, 194))

    def test_95_program_has_form_feed(self):
        """Program has form feed in code"""
        input = \
"""Var: a,b,c;

Function: foo \f
    Body:
        Do
            Break;
        While True
        EndDo.
    EndBody."""
        output = "Var,:,a,,,b,,,c,;,Function,:,foo,Error Token \f"
        self.assertTrue(TestLexer.checkLexeme(input, output, 195))

    def test_96_program_has_tab(self):
        """Program has tabs in code"""
        input = \
"""Var: a,b,c;\t
\t
Function: foo \t
    Body:\t\t\t\t\t
        Do
            Break;\t
        While True\t
        EndDo.
    EndBody."""
        output = "Var,:,a,,,b,,,c,;,Function,:,foo,Body,:,Do,Break,;,While,True,EndDo,.,EndBody,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 196))

    def test_97_program_has_CR(self):
        """Program has carriage return in code"""
        input = \
"""Var: a,b,c;\r
\r
Function: foo \r
    Body:\r\r\r\r\r
        Do
            Break;\r
        While True\r
        EndDo.
    EndBody."""
        output = "Var,:,a,,,b,,,c,;,Function,:,foo,Body,:,Do,Break,;,While,True,EndDo,.,EndBody,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 197))


    ###################################################

    def test_98_dense_code_check(self):
        """Test no space code"""
        input = r"Var:a,b=123;Function:foo123 Parameter:a[99]Body:Var:x;" + \
                r"abc=321;WhileTrueDoEndWhile.If123ThenFor(abc=999,(13||31)&&" + \
                r"True-False,f())DoVar:def;EndFor.ElseVar:ghi;EndIf.EndBody."
        output = r"Var,:,a,,,b,=,123,;,Function,:,foo123,Parameter,:,a,[,99,]" + \
                r",Body,:,Var,:,x,;,abc,=,321,;,While,True,Do,EndWhile,.,If,123,Then," + \
                r"For,(,abc,=,999,,,(,13,||,31,),&&,True,-,False,,,f,(,),),Do,Var,:,def,;" + \
                r",EndFor,.,Else,Var,:,ghi,;,EndIf,.,EndBody,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 198))

    def test_99_sign_check(self):
        """Test sign"""
        input = r"""++.-.*-*.\\..||&&===/==><>=<=>=.<=.!;[](){}"""
        output = r"""+,+.,-.,*,-,*.,\,\.,.,||,&&,==,=/=,=,>,<,>=,<=,>=.,<=.,!,;,[,],(,),{,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, output, 199))

    def test_100_keywords_check(self):
        """Test keywords"""
        input = r"""VarFunctionParameterBodyEndBodyIfThenElseIfElseEndIfForDoEnd""" + \
                r"""ForEndDoWhileEndWhileBreakContinueReturn"""
        output = r"""Var,Function,Parameter,Body,EndBody,If,Then,ElseIf,Else,EndIf,For""" + \
                r""",Do,EndFor,EndDo,While,EndWhile,Break,Continue,Return,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, output, 200))


##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################


#     # various test
#     def test998_simple_exp_test(self):
#         """A simple expression"""
#         input = """!\\.+-=\\%><=.*.
#         \\.-.+.=/="""
#         output = "???"
#         self.assertTrue(TestLexer.checkLexeme(input, output, 998))


#     def test999_simple_exp_test(self):
#         """A simple expression"""
#         input = \
# """        b = 1.E-12  =/= foo(123);"""
#         output = "???"
#         self.assertTrue(TestLexer.checkLexeme(input, output, 999))

#     def test_integer(self):
#         """test integers"""
#         self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

#     def test_illegal_escape(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

#     def test_unterminated_string(self):
#         """test unclosed string"""
#         self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

#     def test_normal_string_with_escape(self):
#         """test normal string with escape"""
#         self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))