import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_unclose_string_1(self):
        input=''' "This is unclose string '''
        self.assertTrue(TestLexer.checkLexeme(input,"Unclosed String: This is unclose string ",101))

    def test_error_token_1(self):
        input = "Long9"
        self.assertTrue(TestLexer.checkLexeme(input,"Error Token L",102))

    def test_float_literal_1(self):
        input="12.0e3 12e3 12.e5 12.0e3 12000.120000e-1"
        self.assertTrue(TestLexer.checkLexeme(input,"12.0e3,12e3,12.e5,12.0e3,12000.120000e-1,<EOF>",103))

    def test_string_1(self):
        input=''' "He asked me: '"Where is John?'"" '''
        self.assertTrue(TestLexer.checkLexeme(input,'''He asked me: '"Where is John?'",<EOF>''',104))

    def test_array_literal_1(self):
        input=" {{1,2}} "
        self.assertTrue(TestLexer.checkLexeme(input,"{,{,1,,,2,},},<EOF>",105))

    def test_string_2(self):
        input="abc"
        self.assertTrue(TestLexer.checkLexeme(input,"abc,<EOF>",106))

    def test_kw_1(self):
        input="Var"
        self.assertTrue(TestLexer.checkLexeme(input,"Var,<EOF>",107))

    def test_error_token_2(self):
        input="ab?svn"
        self.assertTrue(TestLexer.checkLexeme(input,"ab,Error Token ?",108))

    def test_token_1(self):
        input="Var x;"
        self.assertTrue(TestLexer.checkLexeme(input,"Var,x,;,<EOF>",109))

    def test_illegal_string_1(self):
        input=""" "abc\\h def"  """
        self.assertTrue(TestLexer.checkLexeme(input,"""Illegal Escape In String: abc\\h""",110))

    def test_unclose_string_2(self):
        input=""" "abc def  """
        self.assertTrue(TestLexer.checkLexeme(input,"""Unclosed String: abc def  """,111))

    def test_string_3(self):
        input=""" "ab'"c\\n def"  """
        self.assertTrue(TestLexer.checkLexeme(input,"""ab'"c\\n def,<EOF>""",112))

    def test_error_comment_1(self):
        input=""" ** this is comment *  """
        self.assertTrue(TestLexer.checkLexeme(input,"""Unterminated Comment""",113))

    def test_unclose_string_3(self):
        input=""" "my name is '" hehehe '"  """
        self.assertTrue(TestLexer.checkLexeme(input,"""Unclosed String: my name is '" hehehe '"  """,114))

    def test_unclose_string_4(self):
        input= """
        " abc
        abc "
        """
        self.assertTrue(TestLexer.checkLexeme(input,"""Unclosed String:  abc""",115))

    def test_illegal_string_2(self):
        input= """
        "abc'abc"
        """
        self.assertTrue(TestLexer.checkLexeme(input,"""Illegal Escape In String: abc'a""",116))

    def test_array_literal_2(self):
        input= """{1, 2,3,  4}"""
        self.assertTrue(TestLexer.checkLexeme(input,"""{,1,,,2,,,3,,,4,},<EOF>""",117))

    def test_array_literal_3(self):
        input= """{ {  1,  2},  { 4, 5}, { 3, 5  } }"""
        self.assertTrue(TestLexer.checkLexeme(input,"""{,{,1,,,2,},,,{,4,,,5,},,,{,3,,,5,},},<EOF>""",118))

    def test_unclose_string_5(self):
        input= """ "abc\rdef" """
        self.assertTrue(TestLexer.checkLexeme(input,"""Unclosed String: abc""",119))

    def test_string_4(self):
        input= """ a\\.b """
        self.assertTrue(TestLexer.checkLexeme(input,"""a,\.,b,<EOF>""",120))

    def test_token_2(self):
        input= """ {  1, 2,3,     4 """
        self.assertTrue(TestLexer.checkLexeme(input,"""{,1,,,2,,,3,,,4,<EOF>""",121))

    def test_array_null(self):
        input= """{}"""
        self.assertTrue(TestLexer.checkLexeme(input,"""{,},<EOF>""",122))

    def test_comment_1(self):
        input= """** This is a single-line comment. **"""
        self.assertTrue(TestLexer.checkLexeme(input,"""<EOF>""",123))

    def test_comment_2(self):
        input= """
        ** This is a
        * multi-line
        * comment.
        **
        """
        self.assertTrue(TestLexer.checkLexeme(input,"""<EOF>""",124))

    def test_token_3(self):
        input= """{ 1;"""
        self.assertTrue(TestLexer.checkLexeme(input,"""{,1,;,<EOF>""",125))

    def test_string_contain_comment(self):
        input= """ "****" """
        self.assertTrue(TestLexer.checkLexeme(input,"""****,<EOF>""",126))

    def test_unclose_string_6(self):
        input= """ "abc"""
        self.assertTrue(TestLexer.checkLexeme(input,"""Unclosed String: abc""",127))

    def test_error_comment_2(self):
        input= """**"""
        self.assertTrue(TestLexer.checkLexeme(input,"""Unterminated Comment""",128))

    def test_comment_3(self):
        input= """****"""
        self.assertTrue(TestLexer.checkLexeme(input,"""<EOF>""",129))

    def test_int_literal_1(self):
        input= """0124"""
        self.assertTrue(TestLexer.checkLexeme(input,"""0,124,<EOF>""",130))

    def test_token_4(self):
        input= """0x098"""
        self.assertTrue(TestLexer.checkLexeme(input,"""0,x098,<EOF>""",131))

    def test_int_literal_2(self):
        input= """0O1234"""
        self.assertTrue(TestLexer.checkLexeme(input,"""0O1234,<EOF>""",132))

    def test_literal_1(self):
        input= """0o1280"""
        self.assertTrue(TestLexer.checkLexeme(input,"""0o12,80,<EOF>""",133))

    def test_error_token_3(self):
        input= """0O8111"""
        self.assertTrue(TestLexer.checkLexeme(input,"""0,Error Token O""",134))

    def test_float_literal_2(self):
        input= """0.e-9"""
        self.assertTrue(TestLexer.checkLexeme(input,"""0.e-9,<EOF>""",135))

    def test_id_1(self):
        input= """max_9_0000"""
        self.assertTrue(TestLexer.checkLexeme(input,"""max_9_0000,<EOF>""",136))

    def test_token_5(self):
        input= """0minX9"""
        self.assertTrue(TestLexer.checkLexeme(input,"""0,minX9,<EOF>""",137))

    def test_error_token_4(self):
        input= """Max_1000"""
        self.assertTrue(TestLexer.checkLexeme(input,"""Error Token M""",138))

    def test_token_6(self):
        input= """False098"""
        self.assertTrue(TestLexer.checkLexeme(input,"""False,0,98,<EOF>""",139))

    def test_token_7(self):
        input= """Falsefalse900"""
        self.assertTrue(TestLexer.checkLexeme(input,"""False,false900,<EOF>""",140))

    def test_token_8(self):
        input= """Var: x={1,     2,3, 4 }, y;"""
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,:,x,=,{,1,,,2,,,3,,,4,},,,y,;,<EOF>""",141))

    def test_token_9(self):
        input= """Var: x=-.0.90e-100,a[5];"""
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,:,x,=,-.,0.90e-100,,,a,[,5,],;,<EOF>""",142))

    def test_token_10(self):
        input= """Var: x=-9,a[100]=b;"""
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,:,x,=,-,9,,,a,[,100,],=,b,;,<EOF>""",143))

    def test_token_11(self):
        input= """{5.,   "cdf"}"""
        self.assertTrue(TestLexer.checkLexeme(input,"""{,5.,,,cdf,},<EOF>""",144))

    def test_string_5(self):
        input= """ "This is a inputing contain new line \\n" """
        self.assertTrue(TestLexer.checkLexeme(input,"""This is a inputing contain new line \\n,<EOF>""",145))

    def test_string_6(self):
        input= """ "This is a inputing contain backslash \\\\" """
        self.assertTrue(TestLexer.checkLexeme(input,"""This is a inputing contain backslash \\\\,<EOF>""",146))

    def test_token_12(self):
        input= """ If a >= x Then """
        self.assertTrue(TestLexer.checkLexeme(input,"""If,a,>=,x,Then,<EOF>""",147))

    def test_token_13(self):
        input= """ a = 0x98 + "long_nhat" """
        self.assertTrue(TestLexer.checkLexeme(input,"""a,=,0x98,+,long_nhat,<EOF>""",148))

    def test_token_14(self):
        input= """ a=-7+-9 """
        self.assertTrue(TestLexer.checkLexeme(input,"""a,=,-,7,+,-,9,<EOF>""",149))

    def test_token_15(self):
        input= """ True=!False """
        self.assertTrue(TestLexer.checkLexeme(input,"""True,=,!,False,<EOF>""",150))

    def test_error_token_5(self):
        input= """ Varr: X=9; """
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,r,:,Error Token X""",151))

    def test_token_16(self):
        input= """ Function: main_+ """
        self.assertTrue(TestLexer.checkLexeme(input,"""Function,:,main_,+,<EOF>""",152))

    def test_token_17(self):
        input= """ Parameter: "This is a inputing    " """
        self.assertTrue(TestLexer.checkLexeme(input,"""Parameter,:,This is a inputing    ,<EOF>""",153))

    def test_token_18(self):
        input= """ Var: x=0X9AFe_0 """
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,:,x,=,0X9AF,e_0,<EOF>""",154))

    def test_token_19(self):
        input= """ println(a+.2.) """
        self.assertTrue(TestLexer.checkLexeme(input,"""println,(,a,+.,2.,),<EOF>""",155))

    def test_token_20(self):
        input= """ Return true = False """
        self.assertTrue(TestLexer.checkLexeme(input,"""Return,true,=,False,<EOF>""",156))

    def test_token_21(self):
        input= """ a[2][3]={1,2.e-1,] """
        self.assertTrue(TestLexer.checkLexeme(input,"""a,[,2,],[,3,],=,{,1,,,2.e-1,,,],<EOF>""",157))

    def test_comment_4(self):
        input= """ ** This is a comment *** """
        self.assertTrue(TestLexer.checkLexeme(input,"""*,<EOF>""",158))

    def test_comment_5(self):
        input= """ ** This is a comment **** """
        self.assertTrue(TestLexer.checkLexeme(input,"""Unterminated Comment""",159))

    def test_token_22(self):
        input= """Var: a= "This is a inputing" ; """
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,:,a,=,This is a inputing,;,<EOF>""",160))

    def test_error_token_6(self):
        input= """Function: Break_; """
        self.assertTrue(TestLexer.checkLexeme(input,"""Function,:,Break,Error Token _""",161))

    def test_error_token_7(self):
        input= """Varr: X=6;"""
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,r,:,Error Token X""",162))

    def test_error_comment_3(self):
        input= """a=2**x;"""
        self.assertTrue(TestLexer.checkLexeme(input,"""a,=,2,Unterminated Comment""",163))

    def test_illegal_string_3(self):
        input= """ "Nguyen Long \\i Nhat" """
        self.assertTrue(TestLexer.checkLexeme(input,"""Illegal Escape In String: Nguyen Long \\i""",164))

    def test_token_23(self):
        input= """ {1,   "abc",]} """
        self.assertTrue(TestLexer.checkLexeme(input,"""{,1,,,abc,,,],},<EOF>""",165))

    def test_unclose_string_7(self):
        input= """input= "This is a inputing contain \\' """
        self.assertTrue(TestLexer.checkLexeme(input,"""input,=,Unclosed String: This is a inputing contain \\' """,166))

    def test_token_24(self):
        input= """If a =/= 0X9 then"""
        self.assertTrue(TestLexer.checkLexeme(input,"""If,a,=/=,0X9,then,<EOF>""",167))

    def test_token_25(self):
        input= """Var: arr[5] = {1,   2,3,   4,5;"""
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,:,arr,[,5,],=,{,1,,,2,,,3,,,4,,,5,;,<EOF>""",168))

    def test_error_comment_4(self):
        input= """foo(x+.1.x**)"""
        self.assertTrue(TestLexer.checkLexeme(input,"""foo,(,x,+.,1.,x,Unterminated Comment""",169))

    def test_token_26(self):
        input= """While x___9 % 0 == 0 Do"""
        self.assertTrue(TestLexer.checkLexeme(input,"""While,x___9,%,0,==,0,Do,<EOF>""",170))

    def test_error_token_8(self):
        input= """function: Main"""
        self.assertTrue(TestLexer.checkLexeme(input,"""function,:,Error Token M""",171))

    def test_unclose_string_8(self):
        input= """ "He said: '" My name is Long Nhat '" """
        self.assertTrue(TestLexer.checkLexeme(input,"""Unclosed String: He said: '" My name is Long Nhat '" """,172))

    def test_token_27(self):
        input= """x=x+foo(a,b+{1,      2});"""
        self.assertTrue(TestLexer.checkLexeme(input,"""x,=,x,+,foo,(,a,,,b,+,{,1,,,2,},),;,<EOF>""",173))

    def test_illegal_string_4(self):
        input= """Parameter: x="This is a string contain \\K and continue..." """
        self.assertTrue(TestLexer.checkLexeme(input,"""Parameter,:,x,=,Illegal Escape In String: This is a string contain \\K""",174))

    def test_string_literal_1(self):
        input= """ Var: input="This is a inputing contain \\' and \\b" """
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,:,input,=,This is a inputing contain \\' and \\b,<EOF>""",175))

    def test_token_28(self):
        input= """ Function: Breakx___; """
        self.assertTrue(TestLexer.checkLexeme(input,"""Function,:,Break,x___,;,<EOF>""",176))

    def test_error_token_9(self):
        input= """var: True=7.,X=01;"""
        self.assertTrue(TestLexer.checkLexeme(input,"""var,:,True,=,7.,,,Error Token X""",177))

    def test_token_29(self):
        input= """ Var: a=a\.4.,b=b\.5.; """
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,:,a,=,a,\.,4.,,,b,=,b,\.,5.,;,<EOF>""",178))

    def test_error_token_10(self):
        input= """ a=True?x+1:x; """
        self.assertTrue(TestLexer.checkLexeme(input,"""a,=,True,Error Token ?""",179))

    def test_token_30(self):
        input= """ 0o9; """
        self.assertTrue(TestLexer.checkLexeme(input,"""0,o9,;,<EOF>""",180))

    def test_comment_6(self):
        input= """ ** This is a comment \\n ** """
        self.assertTrue(TestLexer.checkLexeme(input,"""<EOF>""",181))

    def test_token_31(self):
        input= """ [{1,2     3}].x """
        self.assertTrue(TestLexer.checkLexeme(input,"""[,{,1,,,2,3,},],.,x,<EOF>""",182))

    def test_error_comment_5(self):
        input= """ *.**x; """
        self.assertTrue(TestLexer.checkLexeme(input,"""*.,Unterminated Comment""",183))

    def test_token_32(self):
        input= """ func(Break(x!=y)); """
        self.assertTrue(TestLexer.checkLexeme(input,"""func,(,Break,(,x,!=,y,),),;,<EOF>""",184))

    def test_token_33(self):
        input= """ if True Then x={{{{}}}}; """
        self.assertTrue(TestLexer.checkLexeme(input,"""if,True,Then,x,=,{,{,{,{,},},},},;,<EOF>""",185))

    def test_error_token_11(self):
        input= """ 270O1x; """
        self.assertTrue(TestLexer.checkLexeme(input,"""270,Error Token O""",186))

    def test_illegal_string_5(self):
        input= """ "This is a error string: Error here''"" """
        self.assertTrue(TestLexer.checkLexeme(input,"""Illegal Escape In String: This is a error string: Error here''""",187))

    def test_illegal_string_6(self):
        input= """ "This is a string \\" """
        self.assertTrue(TestLexer.checkLexeme(input,'''Illegal Escape In String: This is a string \\"''',188))

    def test_unclose_string_9(self):
        input= """ Var: input="My name is: '"K.I.D '"" " """
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,:,input,=,My name is: '"K.I.D '",Unclosed String:  """,189))

    def test_error_token_12(self):
        input= """ x=x+.1.E; """
        self.assertTrue(TestLexer.checkLexeme(input,"""x,=,x,+.,1.,Error Token E""",190))

    def test_token_34(self):
        input= """ x=2||y.; """
        self.assertTrue(TestLexer.checkLexeme(input,"""x,=,2,||,y,.,;,<EOF>""",191))

    def test_token_35(self):
        input= """ 0000x7; """
        self.assertTrue(TestLexer.checkLexeme(input,"""0,0,0,0x7,;,<EOF>""",192))

    def test_error_token_13(self):
        input= """ If x>=. True then X=0; """
        self.assertTrue(TestLexer.checkLexeme(input,"""If,x,>=.,True,then,Error Token X""",193))

    def test_error_token_14(self):
        input= """ Var: x={{;}} """
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,:,x,=,{,{,;,},},<EOF>""",194))

    def test_token_36(self):
        input= """ "" x=x+y; """
        self.assertTrue(TestLexer.checkLexeme(input,""",x,=,x,+,y,;,<EOF>""",195))

    def test_token_37(self):
        input= """ Var=foo(a[2][3]).; """
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,=,foo,(,a,[,2,],[,3,],),.,;,<EOF>""",196))

    def test_error_token_15(self):
        input= """ function__0*X; """
        self.assertTrue(TestLexer.checkLexeme(input,"""function__0,*,Error Token X""",197))

    def test_token_38(self):
        input= """ i__ said: "I love you" but she !love me """
        self.assertTrue(TestLexer.checkLexeme(input,"""i__,said,:,I love you,but,she,!,love,me,<EOF>""",198))

    def test_token_39(self):
        input= """ Varx__Break; """
        self.assertTrue(TestLexer.checkLexeme(input,"""Var,x__Break,;,<EOF>""",199))

    def test_token_40(self):
        input= """ While i!=0 Do work____ Done """
        self.assertTrue(TestLexer.checkLexeme(input,"""While,i,!=,0,Do,work____,Do,ne,<EOF>""",200))

    def test_token_41(self):
        input= """ ** this is a comment *a *a """
        self.assertTrue(TestLexer.checkLexeme(input,"""While,i,!=,0,Do,work____,Do,ne,<EOF>""",1000))











