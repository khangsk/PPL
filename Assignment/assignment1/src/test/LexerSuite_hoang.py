import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_lower_identifier1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc905Xx","""abc905Xx,<EOF>""",101))
    def test_lower_identifier2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc_1526Ab","""abc_1526Ab,<EOF>""",102))
    def test_lower_identifier3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("mddAsBBs12dsd 1AAabc mc123km","""mddAsBBs12dsd,1,Error Token A""",103))
    def test_keyword1(self):
        self.assertTrue(TestLexer.checkLexeme("Var Body Return","""Var,Body,Return,<EOF>""",104))
    def test_keyword2(self):
        self.assertTrue(TestLexer.checkLexeme("EndIf","""EndIf,<EOF>""",105))
    def test_keyword3(self):
        self.assertTrue(TestLexer.checkLexeme("ElseIf","""ElseIf,<EOF>""",106))  
    def test_keyword4(self):
        self.assertTrue(TestLexer.checkLexeme("EndWhile","""EndWhile,<EOF>""",107)) 
    def test_keyword5(self):
        self.assertTrue(TestLexer.checkLexeme("EndBody","""EndBody,<EOF>""",108))  
    def test_keyword6(self):
        self.assertTrue(TestLexer.checkLexeme("EndFor","""EndFor,<EOF>""",109))  
    def test_keyword7(self):
        self.assertTrue(TestLexer.checkLexeme("Returnhihi","""Return,hihi,<EOF>""",110))  
    def test_keyword9(self):
        self.assertTrue(TestLexer.checkLexeme("05Then","""0,5,Then,<EOF>""",111))  
    def test_keyword10(self):
        self.assertTrue(TestLexer.checkLexeme("0 5 Then","""0,5,Then,<EOF>""",112))  
    def test_keyword8(self):
        self.assertTrue(TestLexer.checkLexeme("EndDo","""EndDo,<EOF>""",113))
    def test_body_keyword(self):
        #fail
        self.assertTrue(TestLexer.checkLexeme("BoDy;","""Error Token B""",114))


    def test_integerlit1(self):
        self.assertTrue(TestLexer.checkLexeme("0000;","""0,0,0,0,;,<EOF>""",115))
    def test_integerlit2(self):
        self.assertTrue(TestLexer.checkLexeme("01954","""0,1954,<EOF>""",116))
    def test_integerHex(self):
        self.assertTrue(TestLexer.checkLexeme("0xFF","""0xFF,<EOF>""",117))
    def test_integerHex2(self):
        self.assertTrue(TestLexer.checkLexeme("0XABC;","""0XABC,;,<EOF>""",118))
    def test_integerHex3(self):
        self.assertTrue(TestLexer.checkLexeme("0Xabc;","""0,Error Token X""",119))   

    def test_integerOct1(self):
        self.assertTrue(TestLexer.checkLexeme("0o567","""0o567,<EOF>""",120))
    def test_integerOct2(self):
        self.assertTrue(TestLexer.checkLexeme("0O77","""0O77,<EOF>""",121))
    def test_integerOct3(self):
        self.assertTrue(TestLexer.checkLexeme("0O588","""0O5,88,<EOF>""",122))
    def test_integerOct4(self):
        #An integer literal is a sequence of one or more digits
        self.assertTrue(TestLexer.checkLexeme("0OaAb5","""0,Error Token O""",123))
    def test_floatlit(self):
        self.assertTrue(TestLexer.checkLexeme("12.23","""12.23,<EOF>""",124))
    def test_floatlit1(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e-3","""12.0e-3,<EOF>""",125))
    def test_floatlit2(self):
        self.assertTrue(TestLexer.checkLexeme("12e3","""12e3,<EOF>""",126))
    def test_floatlit6(self):
        #fail
        self.assertTrue(TestLexer.checkLexeme("12e","""12,e,<EOF>""",127))
    def test_floatlit3(self):
        self.assertTrue(TestLexer.checkLexeme("12000.","""12000.,<EOF>""",128))
    def test_floatlit4(self):
        self.assertTrue(TestLexer.checkLexeme(".5e26",""".,5e26,<EOF>""",129))
   
    def test_operator(self):
        self.assertTrue(TestLexer.checkLexeme("not.-.mod","""not,.,-.,mod,<EOF>""",130))
    def test_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("eend16=/=26","""eend16,=/=,26,<EOF>""",131))
    def test_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("!=kaka15","""!=,kaka15,<EOF>""",132))
    def test_operator3(self):
        self.assertTrue(TestLexer.checkLexeme("hoang\t","""hoang,<EOF>""",133))
    def test_operator4(self):
        self.assertTrue(TestLexer.checkLexeme(""""it's""","""Illegal Escape In String: it's""",134))
   
    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",135))
    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,136))
    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'\"c\\n def,<EOF>""",137))
    def test_random1(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: b[2][3] = {{2,3,4},{4,5,6}}""","""Var,:,b,[,2,],[,3,],=,{,{,2,,,3,,,4,},,,{,4,,,5,,,6,},},<EOF>""",138))
    def test_random2(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a = 5""","""Var,:,a,=,5,<EOF>""",139))
    def test_random3(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: c, d = 6, e, f; """,   """Var,:,c,,,d,=,6,,,e,,,f,;,<EOF>""",140))
    def test_random4(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: m, n[10];""",  """Var,:,m,,,n,[,10,],;,<EOF>""",141))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","""ab,Error Token ?""",142))

    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme("**this is comment 192**","""<EOF>""",143))
    def test_multi_comment(self):
        self.assertTrue(TestLexer.checkLexeme(r"""** This is a
* multi-line
* comment.
**""","""<EOF>""",144))
    def test_commentfail(self):
        self.assertTrue(TestLexer.checkLexeme("**this is comment fail****","""Unterminated Comment""",145))
    def test_seperator(self):
        self.assertTrue(TestLexer.checkLexeme(" 15()ab 26[]89 56a:ab 12.-* /.; 30-{}25*  ","""15,(,),ab,26,[,],89,56,a,:,ab,12.,-,*,Error Token /""",146))
    def test_floatlit5(self):
        #fail
        self.assertTrue(TestLexer.checkLexeme(".e26",""".,e26,<EOF>""",147))
    def test_noncomment(self):
        input = r""" *****"""
        expect = """*,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))
    def test_149(self):
        input = r""" *** **"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))

    def test_150(self):
        input = r""" 123596Aabc"""
        expect = """123596,Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))

    
    def test_151(self):
        input = r""" -50 """
        expect = """-,50,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))

    def test_152(self):
        input = r"""{15,True,-5,2.6}"""
        expect = """{,15,,,True,,,-,5,,,2.6,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))

    def test_153(self):
        input = r""""Tran" +"Danh" +"Hoang" """
        expect = """Tran,+,Danh,+,Hoang,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))

    def test_154(self):
        input = r"""hOang__1569356= hihi(9)[5]+16"""
        expect = """hOang__1569356,=,hihi,(,9,),[,5,],+,16,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))

    def test_155(self):
        input = r"""
            "hoang
            "
        """
        expect = """Unclosed String: hoang
"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))

    def test_156(self):
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
        expect = """Var,:,string,[,3,],=,{,1.23,,,0.e4,,,12e2,},;,Function,:,test,Body,:,Var,:,x,[,3,],,,sum,=,0.,;,For,(,i,=,0,,,i,<,3,,,1,),Do,x,[,i,],=,float,(,string,[,i,],),;,sum,=,sum,+,x,[,i,],;,EndFor,.,Return,sum,;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))

    def test_157(self):
        input = r""" 0x123abcd """
        expect = """0x123,abcd,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))

    """ Octal integer literal """

    def test_158(self):
        input = r"""Function: square
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                Return v;
            EndBody. """
        expect = """Function,:,square,Body,:,Var,:,r,=,10.,,,v,;,v,=,(,4.,\\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,Return,v,;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))

    def test_159(self):
        input = r"""Var: a, b, operator;
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
            EndBody."""
        expect = """Var,:,a,,,b,,,operator,;,Function,:,main,Body,:,input,(,a,),;,input,(,b,),;,input,(,operator,),;,If,operator,==,+,Then,Return,a,+,b,;,ElseIf,operator,==,-,Then,Return,a,-,b,;,ElseIf,operator,==,*,Then,Return,a,*,b,;,Else,Return,a,\\,b,;,EndIf,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 159))

    def test_160(self):
        input = r"""Var: arr[3][2] = {{1, 2}, {4, 5}, {3, 5}};
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
        expect = """Var,:,arr,[,3,],[,2,],=,{,{,1,,,2,},,,{,4,,,5,},,,{,3,,,5,},},;,Function,:,main,Body,:,Var,:,p,=,1,;,For,(,i,=,0,,,i,<,3,,,1,),Do,For,(,j,=,0,,,j,<,2,,,1,),Do,p,=,p,*,arr,[,i,],[,j,],;,EndFor,.,EndFor,.,writeln,(,p,),;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

    def test_161(self):
        input = r"""
Do
"""
        expect = """Do,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

    def test_162(self):
        input = r"""If"""
        expect = """If,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))

    def test_163(self):
        input = r""" Parameter"""
        expect = """Parameter,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))

    def test_164(self):
        input = r"""Function """
        expect = """Function,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))

    def test_165(self):
        input = r"""" !#$%&'()*+,-./^_`{|}~" """
        expect = """Illegal Escape In String:  !#$%&'("""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

    def test_166(self):
        input = r"""True"""
        expect = """True,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))

    def test_167(self):
        input = r""" False """
        expect = """False,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))

    def test_168(self):
        input = r""""0123456789" """
        expect = """0123456789,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))

    def test_169(self):
        input = r""""abcdefghijklmnopqrstuvwxyz" """
        expect = """abcdefghijklmnopqrstuvwxyz,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))

    def test_170(self):
        input = r""" "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  """
        expect = """ABCDEFGHIJKLMNOPQRSTUVWXYZ,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

    def test_171(self):
        input = r""" "\b\f\r\n\t\'\\" """
        expect = """\\b\\f\\r\\n\\t\\'\\\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 171))

    def test_172(self):
        input = """ "Hoang'"Tran'"Danh"
"""
        expect = """Hoang'\"Tran'\"Danh,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

    def test_173(self):
        input = r""" Hoang' """
        expect = """Error Token H"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

    def test_174(self):
        input = r""" "" """
        expect = """,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

    def test_175(self):
        input = r""" Hoan\g """
        expect = """Error Token H"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 175))

    def test_176(self):
        input = r"""hoang\1 """
        expect = """hoang,\\,1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

    def test_177(self):
        input = r""" hoang\+ """
        expect = """hoang,\\,+,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))

    def test_178(self):
        input = r""" hoang\ hihi"""
        expect = """hoang,\\,hihi,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test_179(self):
        input = r""" "hoang """
        expect = """Unclosed String: hoang """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))

    def test_180(self):
        input = r""" "hoanghi   
         """
        expect = """Unclosed String: hoanghi   
"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

    def test_181(self):
        input = r""" "hoang\t " """
        expect = """hoang\\t ,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))

    def test_182(self):
        input = r""" 15/26 """
        expect = """15,Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))

    def test_183(self):
        input = r""" hoang | tran """
        expect = """hoang,Error Token |"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))

    def test_184(self):
        input = r""" **tran * danh *hoang ** ** not a comment*hoang * """
        expect = """Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))

    def test_185(self):
        input = r"""" *** **"""
        expect = """Unclosed String:  *** **"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))

    def test_186(self):
        input = r""" "hoang|tran" """
        expect = """hoang|tran,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 186))

    def test_187(self):
        input = """ "55/26" """
        expect = """55/26,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))

    def test_188(self):
        input = r""" hoang\\tran"""
        expect = """hoang,\\,\\,tran,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))

    """ Error token """

    def test_189(self):
        input = r"""\hoang """
        expect = """\\,hoang,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))

    def test_190(self):
        input = r""" hoa\ng """
        expect = """hoa,\\,ng,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))

    def test_191(self):
        input = r""" 
        Function: main
    Body:
        a = !a > b || c + d * e[2];
    EndBody.
         """
        expect = """Function,:,main,Body,:,a,=,!,a,>,b,||,c,+,d,*,e,[,2,],;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))

    def test_192(self):
        input = r""" hoang \% hihi """
        expect = """hoang,\\,%,hihi,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))

    """ Free style """

    def test_193(self):
        input = r""" True & hoang """
        expect = """True,Error Token &"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))

    def test_194(self):
        input = r""" hoang % 2    """
        expect = """hoang,%,2,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))

    def test_195(self):
        input = r"""  [{[[[[[]]]]{}]]}]]}]]]{}]] """
        expect = """[,{,[,[,[,[,[,],],],],{,},],],},],],},],],],{,},],],<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))

    def test_196(self):
        input = r"""hoang======/= hihi"""
        expect = """hoang,==,==,==,Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))

    def test_197(self):
        input = r""" !==hoang"""
        expect = """!=,=,hoang,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))

    def test_198(self):
        input = r"""hoang-..1
"""
        expect = """hoang,-.,.,1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))

    def test_199(self):
        input = r""" hoang"tra\n"""
        expect = """hoang,Unclosed String: tra\\n"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))

    def test_200(self):
        input = r""" If expression Then statement-list
ElseIf expression Then statement-list
ElseIf expression Then statement-list
Else statement-list
EndIf.
 """
        expect = """If,expression,Then,statement,-,list,ElseIf,expression,Then,statement,-,list,ElseIf,expression,Then,statement,-,list,Else,statement,-,list,EndIf,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))
