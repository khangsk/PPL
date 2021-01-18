import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # Testcases 10x reserved for:
    # + identifiers
    # + keywords
    # + near-misses
    
    def test_lower_id(self):
        """test lower-case identifiers"""
        testcase = r"""i love you chu ca mo"""
        expect = r"""i,love,you,chu,ca,mo,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 100))
        
    def test_camel_id(self):
        """test camel-case identifiers"""
        testcase = r"""sHe lOvEs yOU chU cA mo"""
        expect = r"""sHe,lOvEs,yOU,chU,cA,mo,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 101))
        
    def test_alphanumeric_id(self):
        """test alphanumeric identifiers"""
        testcase = r"""ur m8 l0v3s u fr0m3000Up2AbOut9000"""
        expect = r"""ur,m8,l0v3s,u,fr0m3000Up2AbOut9000,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 102))
        
    def test_complex_id(self):
        """test weirdly-formed identifiers"""
        testcase = r"""thf p aP_z_P zxcvB11nm895f5fGh3jkwErtyuiop aWERT07IOPN___AS"""
        expect = r"""thf,p,aP_z_P,zxcvB11nm895f5fGh3jkwErtyuiop,aWERT07IOPN___AS,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 103))
    
    def test_id_among_ws(self):
        """test several identifiers seperated by weirdly-formed whitespace"""
        testcase = r"""	
        
        	thf
        p 
        
        aP_z_P		zxcvB11nm895f5fGh3jkwErtyuiop 	 aWERT07IOPN___AS"""
        expect = r"""thf,p,aP_z_P,zxcvB11nm895f5fGh3jkwErtyuiop,aWERT07IOPN___AS,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 104))

    def test_keyword(self):
        """test all reserved keywords"""
        testcase = r"""BodyBreakContinueDoElseElseIfEndBodyEndIfEndForEndWhileForFunctionIfParameterReturnThenVarWhileTrueFalseEndDo"""
        expect = r"""Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,Function,If,Parameter,Return,Then,Var,While,True,False,EndDo,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 105))
        
    def test_id_keyword(self):
        """test identifiers and keywords mixed together with skipped tokens thrown around"""
        testcase = r"""****	myVar
        urReturn	**ah*em**	our_EndDo	
        
        m8Function
        
        
        IfTrueThenbemyfriendplzEndIf  """
        expect = r"""myVar,urReturn,our_EndDo,m8Function,If,True,Then,bemyfriendplzEndIf,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 106))
        
    def test_near_miss_107(self):
        """test input closely resembling identifiers or keyword"""
        testcase = r"""IF false Then"""
        expect = r"""Error Token I"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 107))
    
    def test_near_miss_108(self):
        """test input closely resembling identifiers or keyword"""
        testcase = r"""
        		 Whikle	
                 
                 	"""
        expect = r"""Error Token W"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 108))
    
    def test_near_miss_109(self):
        """test input closely resembling identifiers or keyword"""
        testcase = r"""
            	**Then**Do**abc**	 Whil e	
                
                	****"""
        expect = r"""Do,Error Token W"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 109))
        
    # Testcases 11x reserved for:
    # + numeric literal
    # + near-misses
        
    def test_dec(self):
        """test decimal integer literals"""
        testcase = r""" 0   75114 2487 8954100 857460 512 00909"""
        expect = r"""0,75114,2487,8954100,857460,512,0,0,909,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 110))
        
    def test_oct(self):
        """test octal integer literals"""
        testcase = r"""	0o476 0O7777777777
        0o76543210"""
        expect = r"""0o476,0O7777777777,0o76543210,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 111))
        
    def test_hex(self):
        """test hexadecimal integer literals"""
        testcase = r""" 0XAF7468 0xFFFF0000 0xABCDEF0123456789
        0x1"""
        expect = r"""0XAF7468,0xFFFF0000,0xABCDEF0123456789,0x1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 112))
        
    def test_int(self):
        """test all kinds of integers"""
        testcase = r"""**0x*00o**
        00x1 0XFA0123
            0O170 4561324740	0o0
        """
        expect = r"""0,0x1,0XFA0123,0O170,4561324740,0,o0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 113))
    
    def test_non_scientific_float(self):
        """test float literals without exponent tail"""
        testcase = r""" 0.2 0. 794.13546
        0.0 196. .64"""
        expect = r"""0.2,0.,794.13546,0.0,196.,.,64,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 114))

    def test_scientific_float(self):
        """test float literals with exponent tail"""
        testcase = r"""0.e0 984E-4651451 000.00000e+0 599.e+-5"""
        expect = r"""0.e0,984E-4651451,000.00000e+0,599.,e,+,-,5,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 115))
        
    def test_near_miss_116(self):
        """test input closely resembling numeric literals"""
        testcase = r"""0000x0oO0O50xF12 00xA 0X0F"""
        expect = r"""0,0,0,0,x0oO0O50xF12,0,0xA,0,Error Token X"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 116))
        
    def test_near_miss_117(self):
        """test input closely resembling numeric literals"""
        testcase = r""".3E+7"""
        expect = r""".,3E+7,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 117))
    
    def test_near_miss_118(self):
        """test input closely resembling numeric literals"""
        testcase = r"""5e01 0o78e-3"""
        expect = r"""5e01,0o7,8e-3,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 118))
    
    def test_near_miss_119(self):
        """test input closely resembling numeric literals"""
        testcase = r"""0o640.7e0xFA 0xfa"""
        expect = r"""0o640,.,7e0,xFA,0,xfa,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 119))
        
    # Testcases 12x reserved for:
    # + string
    # + near-misses
        
    def test_inline_string(self):
        """test inline strings"""
        testcase = r""" "" "'""
        "\t" """
        expect = r""",'",\t,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 120))
        
    def test_multiline_string(self):
        """test multi-line string"""
        testcase = r"""	"!@#%$^&'"**(^(){Z] ****Pfoem
        " """
        expect = r"""Unclosed String: !@#%$^&'"**(^(){Z] ****Pfoem"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 121))
        
    def test_valid_escape_sequence(self):
        """test all valid escape sequences and '"" """
        testcase = r""" "\b\f\r\n\t\'\\'"" """""
        expect = r"""\b\f\r\n\t\'\\'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 122))
        
    def test_unclose_string(self):
        """test a string abruptly hit by an EOF mid-string"""
        testcase = r"""**0x*00o**
        "Sometimes, I do wonder how the hell I managed to survive 2 yrs of this uni."""
        expect = r"""Unclosed String: Sometimes, I do wonder how the hell I managed to survive 2 yrs of this uni."""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 123))
    
    def test_invalid_escape_sequence_124(self):
        """test a string containing invalid escape sequence"""
        testcase = r""" "\t\t\t\t\t\t\t\\n\\'a" """
        expect = r"""Illegal Escape In String: \t\t\t\t\t\t\t\\n\\'a"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 124))

    def test_invalid_escape_sequence_125(self):
        """test a string containing invalid escape sequence"""
        testcase = r""" "\t\t\t\t\b\t\t\\n\'a\f\o" """
        expect = r"""Illegal Escape In String: \t\t\t\t\b\t\t\\n\'a\f\o"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 125))
        
    def test_invalid_escape_sequence_126(self):
        """test a string containing invalid escape sequence"""
        testcase = r""" "0xFA\xFFF" """
        expect = r"""Illegal Escape In String: 0xFA\x"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 126))
        
    def test_invalid_escape_sequence_127(self):
        """test a string containing invalid escape sequence"""
        testcase = r""" "\/" """
        expect = r"""Illegal Escape In String: \/"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 127))
    
    def test_invalid_escape_sequence_128(self):
        """test a string containing invalid escape sequence"""
        testcase = r""" "A man once said: E:\ is where I hide my treasure trove." """
        expect = r"""Illegal Escape In String: A man once said: E:\ """
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 128))
    
    def test_invalid_escape_sequence_129(self):
        """test a string containing invalid escape sequence"""
        testcase = r""" "_(:3_| \)_" """
        expect = r"""Illegal Escape In String: _(:3_| \)"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 129))
        
    # Testcases 13x - 145 reserved for:
    # + array
    # + near-misses
        
    def test_empty_array(self):
        """test empty arrays"""
        testcase = r""" {} { } {
        }{}{**Empty**}"""
        expect = r"""{,},{,},{,},{,},{,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 130))
        
    def test_array_of_num(self):
        """test arrays of numeric values"""
        testcase = r"""{0O645, -0, 0x44} {** float ** -6e3, 7e-1, 7.5, 0.0 }"""
        expect = r"""{,0O645,,,-,0,,,0x44,},{,-,6e3,,,7e-1,,,7.5,,,0.0,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 131))
        
    def test_array_of_string(self):
        """test arrays of strings"""
        testcase = r"""{"", "\b", "'"", "abc\n\t\\h"} {"  "}"""
        expect = r"""{,,,,\b,,,'",,,abc\n\t\\h,},{,  ,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 132))
        
    def test_nested_array(self):
        """test nested arrays"""
        testcase = r"""{{{}, {}}, {{}, {}}, {{}, {}}} {{"2"}, {"quote"}, {"or"}, {"2"}, {"quote"}}"""
        expect = r"""{,{,{,},,,{,},},,,{,{,},,,{,},},,,{,{,},,,{,},},},{,{,2,},,,{,quote,},,,{,or,},,,{,2,},,,{,quote,},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 133))
    
    def test_array_of_diff_type(self):
        """test arrays with no consistent type"""
        testcase = r"""{456, -4., ** nested array **  {{{}}}     , "string theory"} {{}, ""}"""
        expect = r"""{,456,,,-,4.,,,{,{,{,},},},,,string theory,},{,{,},,,,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 134))

    def test_array_of_id(self):
        """test array contatining identifiers
            !!! since array was made into a production rule, this has become valid
        """
        testcase = r"""{pfoem, "made", this, "test", for, "absolutely", no, "reason"}"""
        expect = r"""{,pfoem,,,made,,,this,,,test,,,for,,,absolutely,,,no,,,reason,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 135))
        
    def test_array_of_keyword_id(self):
        """test arrays containing keywords or identifiers
            !!! since array was made into a production rule, this has become valid
        """
        testcase = r"""{{If}, uS2er, {Then}, chase_after_her} {"as 2nd chance is but an", {} , phrase} """
        expect = r"""{,{,If,},,,uS2er,,,{,Then,},,,chase_after_her,},{,as 2nd chance is but an,,,{,},,,phrase,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 136))
        
    def test_empty_element(self):
        """test arrays containing empty element
            !!! since array was made into a production rule, this has become valid
        """
        testcase = r"""{{, "words", ** I **, prayed}}"""
        expect = r"""{,{,,,words,,,,,prayed,},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 137))
    
    def test_weird_array_138(self):
        """test arrays containing weird combinations of tokens
            !!! since array was made into a production rule, this has become valid
        """
        testcase = r"""{.132e6, 0x0, 785l, true, ||, False}"""
        expect = r"""{,.,132e6,,,0,x0,,,785,l,,,true,,,||,,,False,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 138))
    
    def test_weird_array_139(self):
        """test arrays containing weird combinations of tokens
            !!! since array was made into a production rule, this has become valid
        """
        testcase = r""" {:3} """
        expect = r"""{,:,3,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 139))
        
    def test_unpaired_curly_bracket(self):
        """test arrays with incomplete or unexpected delimiters (unpaired curly brackets)
            !!! since array was made into a production rule, this has become valid
        """
        testcase = r"""{{7} {"""
        expect = r"""{,{,7,},{,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 140))
        
    def test_error_array_141(self):
        """test arrays containing errors"""
        testcase = r"""{"stronk, -0, 0x44} {" stonk"}"""
        expect = r"""{,stronk, -0, 0x44} {,stonk,Unclosed String: }"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 141))
        
    def test_error_array_142(self):
        """test arrays containing errors"""
        testcase = r"""{"bonk\cheems"} """
        expect = r"""{,Illegal Escape In String: bonk\c"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 142))
        
    def test_error_array_143(self):
        """test arrays containing errors"""
        testcase = r"""{1.E9} {0,E2} {2k}"""
        expect = r"""{,1.E9,},{,0,,,Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 143))
        
    def test_error_array_144(self):
        """test arrays containing errors"""
        testcase = r"""{"'Phu' they said, 'F u' I heard."}"""
        expect = r"""{,Illegal Escape In String: 'P"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 144))
        
    def test_error_array_145(self):
        """test arrays containing errors"""
        testcase = r""" {** a**b in python means a to the power of b **} """
        expect = r"""{,b,in,python,means,a,to,the,power,of,b,Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 145))
        
    # Testcases 146 - 155 reserved for:
    # + other symbols
    # + near-misses
    
    def test_rel_op(self):
        """test all relational operators with some near-misses mixed in"""
        testcase = r"""=/=<.>.<=.>=.==!=<><=>=<=> =\= <=> === =!"""
        expect = r"""=/=,<.,>.,<=.,>=.,==,!=,<,>,<=,>=,<=,>,=,\,=,<=,>,==,=,=,!,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 146))
        
    def test_ar_op(self):
        """test all arithmetic operators with some near-misses mixed in"""
        testcase = r"""+.-.*.\.+-*\\%!&&|| /."""
        expect = r"""+.,-.,*.,\.,+,-,*,\,\,%,!,&&,||,Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 147))
    
    def test_separator(self):
        """test all separators"""
        testcase = r"""}{[]),;(.:|"""
        expect = r"""},{,[,],),,,;,(,.,:,Error Token |"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 148))
    
    def test_sym(self):
        """test many mixed symbols with near-misses"""
        testcase = r""":: -> ... \\ ^"""
        expect = r""":,:,-,>,.,.,.,\,\,Error Token ^"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 149))
        
    def test_error_sym_150(self):
        """test error symbols"""
        testcase = r"""@special"""
        expect = r"""Error Token @"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 150))
        
    def test_error_sym_151(self):
        """test error symbols"""
        testcase = r"""a = True? 19: 02;"""
        expect = r"""a,=,True,Error Token ?"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 151))
        
    def test_error_sym_152(self):
        """test error symbols"""
        testcase = r"""$a = True? 19: 02;"""
        expect = r"""Error Token $"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 152))
        
    def test_error_sym_153(self):
        """test error symbols"""
        testcase = r"""** Don't comment Python-style ** # a = True? 19: 02;"""
        expect = r"""Error Token #"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 153))
        
    def test_error_sym_154(self):
        """test error symbols"""
        testcase = r"""** or C-style ** // a = True? 19: 02;"""
        expect = r"""Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 154))
        
    def test_error_sym_155(self):
        """test error symbols"""
        testcase = r"""** or do any C weird sh*t ** *&a = True? 19: 02;"""
        expect = r"""*,Error Token &"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 155))
    
    def test_int_float_op_156(self):
        """test integer and float operators"""
        testcase = r"""x = --.1 +.-.--. 7 =/= 7.*.7.8 \.7;"""
        expect = r"""x,=,-,-.,1,+.,-.,-,-.,7,=/=,7.,*.,7.8,\.,7,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 156))
     
    def test_int_float_op_157(self):
        """test integer and float operators"""
        testcase = r"""x = 7.>>.7 =/= 7 <> 7 <<. 7 ><.7 ==.7*.e;"""
        expect = r"""x,=,7.,>,>.,7,=/=,7,<,>,7,<,<.,7,>,<.,7,==,.,7,*.,e,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 157))
        
    def test_int_bool_op_158(self):
        """test integer and boolean operators"""
        testcase = r"""x = 7 !=!!!!!!--!=!9;"""
        expect = r"""x,=,7,!=,!,!,!,!,!,!,-,-,!=,!,9,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 158))
        
    def test_int_float_bool_op_159(self):
        """test integer, float and boolean operators"""
        testcase = r"""x = 7 ===/= 8.e-1.1 + !.9;"""
        expect = r"""x,=,7,==,=/=,8.e-1,.,1,+,!,.,9,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 159))
        
    # Testcases 16x-17x reserved for:
    # + randomly combined testcases

    def test_random_160(self):
        """test randomly"""
        testcase = r"""{{7} {, thf p aP_z_P zxcvB11x = 7 !=!!!!!!--!=!9;nm895f5fGh3jkwErtyuiop aWERT07IOPN___AS"""
        expect = r"""{,{,7,},{,,,thf,p,aP_z_P,zxcvB11x,=,7,!=,!,!,!,!,!,!,-,-,!=,!,9,;,nm895f5fGh3jkwErtyuiop,aWERT07IOPN___AS,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 160))
        
    def test_random_161(self):
        """test randomly"""
        testcase = r"""{{x = 7.>>.7 =/= 7 <> 7 <<. 7 ><.7 ==.7*.e;7} {"""
        expect = r"""{,{,x,=,7.,>,>.,7,=/=,7,<,>,7,<,<.,7,>,<.,7,==,.,7,*.,e,;,7,},{,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 161))
        
    def test_random_162(self):
        """test randomly"""
        testcase = r"""5e01 0o78e-3{{5e01 0o78e-37} {"""
        expect = r"""5e01,0o7,8e-3,{,{,5e01,0o7,8e-37,},{,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 162))
        
    def test_random_163(self):
        """test randomly"""
        testcase = r"""{{75e01 0o78e-3} {****	myVar
        urReturn	**ah*em**	our_EndDo	
        Ifx==yThenBreak;EndIf.
        m8Function
        
        
        IfTrueThenbemyfriendplzEndIf  """
        expect = r"""{,{,75e01,0o7,8e-3,},{,myVar,urReturn,our_EndDo,If,x,==,yThenBreak,;,EndIf,.,m8Function,If,True,Then,bemyfriendplzEndIf,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 163))
        
    def test_random_164(self):
        """test randomly"""
        testcase = r"""{{ur m8 l0v3s u fr0m3000Up2AbOut90007} {ur m8 l0v3s u fr0m3000Up2AbOut9000"""
        expect = r"""{,{,ur,m8,l0v3s,u,fr0m3000Up2AbOut90007,},{,ur,m8,l0v3s,u,fr0m3000Up2AbOut9000,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 164))
        
    def test_random_165(self):
        """test randomly"""
        testcase = r"""{{7ur m8 l0v3s u fr0m3000Up2AbOut9000}****	myVar
        urReturn	**ah*em**	our_EndDo	
        
        m8Function
        
        
        IfTrueThenbemyfriendplzEndIf   {"""
        expect = r"""{,{,7,ur,m8,l0v3s,u,fr0m3000Up2AbOut9000,},myVar,urReturn,our_EndDo,m8Function,If,True,Then,bemyfriendplzEndIf,{,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 165))
        
    def test_random_166(self):
        """test randomly"""
        testcase = r"""{{70000x0oO0O50xF120000x0oO0O50xF12 00xA 0X0F 00xA 0X0F} {"""
        expect = r"""{,{,70000,x0oO0O50xF120000x0oO0O50xF12,0,0xA,0,Error Token X"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 166))
        
    def test_random_167(self):
        """test randomly"""
        testcase = r"""{{7+.-.*.\.+-Ifx==yThenBreak;EndIf.*\\%!&&|| /.} {"""
        expect = r"""{,{,7,+.,-.,*.,\.,+,-,If,x,==,yThenBreak,;,EndIf,.,*,\,\,%,!,&&,||,Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 167))
        
    def test_random_168(self):
        """test randomly"""
        testcase = r"""{{{"bonk\c+.-Ifx==yThenBreak;EndIf..*.\.+-*\\%!&&|| /.heems"} 7} {"""
        expect = r"""{,{,{,Illegal Escape In String: bonk\c"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 168))
        
    def test_random_169(self):
        """test randomly"""
        testcase = r"""{{{1.E9} {0,E2} {2k}7} {"""
        expect = r"""{,{,{,1.E9,},{,0,,,Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 169))
        
    def test_random_170(self):
        """test randomly"""
        testcase = r"""do_sth("Do", 0, {77e2, 987.});{{0000x0oO0O50xF12 00xA 0X0F7} {"""
        expect = r"""do_sth,(,Do,,,0,,,{,77e2,,,987.,},),;,{,{,0,0,0,0,x0oO0O50xF12,0,0xA,0,Error Token X"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 170))
        
    def test_random_171(self):
        """test randomly"""
        testcase = r"""{{7}{"bonk\chdo_sth("Do", 0, {77e2, 987.});eems"}  {"""
        expect = r"""{,{,7,},{,Illegal Escape In String: bonk\c"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 171))
        
    def test_random_172(self):
        """test randomly"""
        testcase = r"""{{.3E+7{pfoem, "made", this, "test", for, "absolutely", no, "reason"}7} {"""
        expect = r"""{,{,.,3E+7,{,pfoem,,,made,,,this,,,test,,,for,,,absolutely,,,no,,,reason,},7,},{,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 172))
        
    def test_random_173(self):
        """test randomly"""
        testcase = r"""{{7}{1.E{pfoem, "made", this, "test", for, "absolutely", no, "reason"}9} {0,E2} {2k} {"""
        expect = r"""{,{,7,},{,1.,Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 173))
        
    def test_random_174(self):
        """test randomly"""
        testcase = r"""0.e0 984E-4651451 000.00000e+0 599.e+-5{{0.e0 984E-4651451 000.00000e+0 599.e+-57} {"""
        expect = r"""0.e0,984E-4651451,000.00000e+0,599.,e,+,-,5,{,{,0.e0,984E-4651451,000.00000e+0,599.,e,+,-,57,},{,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 174))
        
    def test_random_175(self):
        """test randomly"""
        testcase = r"""{{pfoem, "made", this, "test", for, "absolutely", no, "reason"}{7} .3E+7{"""
        expect = r"""{,{,pfoem,,,made,,,this,,,test,,,for,,,absolutely,,,no,,,reason,},{,7,},.,3E+7,{,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 175))
        
    def test_random_176(self):
        """test randomly"""
        testcase = r"""{{{.132e6, 0x0, 785l, do_sth("Do", 0, {77e2, 987.});truedo_sth("Do", 0, {77e2, 987.});+.-.*.\.+-*\\%!&&|| /., ||, False}7} {"""
        expect = r"""{,{,{,.,132e6,,,0,x0,,,785,l,,,do_sth,(,Do,,,0,,,{,77e2,,,987.,},),;,truedo_sth,(,Do,,,0,,,{,77e2,,,987.,},),;,+.,-.,*.,\.,+,-,*,\,\,%,!,&&,||,Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 176))
        
    def test_random_177(self):
        """test randomly"""
        testcase = r"""{{7{.132e6, 0x0,(a[a[True]+f(c)]+a)[a]=a[a]; 785l, true, ||, False}} {"""
        expect = r"""{,{,7,{,.,132e6,,,0,x0,,,(,a,[,a,[,True,],+,f,(,c,),],+,a,),[,a,],=,a,[,a,],;,785,l,,,true,,,||,,,False,},},{,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 177))
        
    def test_random_178(self):
        """test randomly"""
        testcase = r"""{{{.{pfoem, "made", this, "test", for, "absolutely", no, "reason"}132e6, 0x0, 785l, true, ||, False}7} {"""
        expect = r"""{,{,{,.,{,pfoem,,,made,,,this,,,test,,,for,,,absolutely,,,no,,,reason,},132e6,,,0,x0,,,785,l,,,true,,,||,,,False,},7,},{,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 178))
        
    def test_random_179(self):
        """test randomly"""
        testcase = r"""{{7{+.-.*.\.+-*\\%!&&|| /..132e6, 0x0, 785l, true, ||, False}} {"""
        expect = r"""{,{,7,{,+.,-.,*.,\.,+,-,*,\,\,%,!,&&,||,Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 179))

    def test_global_var_decl(self):
        """test global variable declaration part"""
        testcase = r"""Var: x0 = 12, x1 = {"a", "b", "c"};
        
        Var:y0 = 0xF, y1="abc";"""
        expect = r"""Var,:,x0,=,12,,,x1,=,{,a,,,b,,,c,},;,Var,:,y0,=,0xF,,,y1,=,abc,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 180))
        
    def test_func_decl(self):
        """test function declaration part"""
        testcase = r"""Function : testBody EndBody.
        Function: doCrazyStuff BodyEndBody."""
        expect = r"""Function,:,testBody,EndBody,.,Function,:,doCrazyStuff,Body,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 181))
        
    def test_parameter_decl(self):
        """test parameter declaration part"""
        testcase = r"""Function : test Parameter: a[5][3], b Body EndBody.
        Function: doCrazyStuff Parameter:BodyEndBody."""
        expect = r"""Function,:,test,Parameter,:,a,[,5,],[,3,],,,b,Body,EndBody,.,Function,:,doCrazyStuff,Parameter,:,Body,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 182))
        
    def test_local_var_decl(self):
        """test local variable declarations"""
        testcase = r"""Function : test BodyVar:aLocalPcovSheet;EndBody.
        Function: doCrazyStuff BodyVar:If1ThenVar:x={};EndBody. """
        expect = r"""Function,:,test,Body,Var,:,aLocalPcovSheet,;,EndBody,.,Function,:,doCrazyStuff,Body,Var,:,If,1,Then,Var,:,x,=,{,},;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 183))
        
    def test_assign_stmt(self):
        """test assignment statements"""
        testcase = r"""a=i; 1 + 1 = 2; array()[j]=a_ele; (1 == 2)[3]=4==.5;"""
        expect = r"""a,=,i,;,1,+,1,=,2,;,array,(,),[,j,],=,a_ele,;,(,1,==,2,),[,3,],=,4,==,.,5,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 184))
        
    def test_if_stmt(self):
        """test if statements"""
        testcase = r"""IfTrueThenFalse=TrueElseIfFalseThenTrue=FalseElse IfThenEndIf.EndIf."""
        expect = r"""If,True,Then,False,=,True,ElseIf,False,Then,True,=,False,Else,If,Then,EndIf,.,EndIf,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 185))
    
    def test_for_stmt(self):
        """test for statements"""
        testcase = r"""For(i=k,i<n,z)EndFor."""
        expect = r"""For,(,i,=,k,,,i,<,n,,,z,),EndFor,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 186))
        
    def test_while_stmt(self):
        """test while statements"""
        testcase = r"""While2==2DoEndWhile."""
        expect = r"""While,2,==,2,Do,EndWhile,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 187))
    
    def test_do_stmt(self):
        """test do while statements"""
        testcase = r"""DoVar:doVar;Whilebool_of_string("True")EndDo."""
        expect = r"""Do,Var,:,doVar,;,While,bool_of_string,(,True,),EndDo,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 188))
    
    def test_brk_cont(self):
        """test break statements"""
        testcase = r"""Break;Continue;"""
        expect = r"""Break,;,Continue,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 189))
        
    def test_call_stmt(self):
        """test call statements"""
        testcase = r"""do_sth("Do", 0, {77e2, 987.});"""
        expect = r"""do_sth,(,Do,,,0,,,{,77e2,,,987.,},),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 190))
        
    def test_return_stmt(self):
        """test return statements"""
        testcase = r"""Return;
        Return "a";
        Return {4, 4};"""
        expect = r"""Return,;,Return,a,;,Return,{,4,,,4,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 191))
        
    def test_cmplx_expr(self):
        """test complex expressions"""
        testcase = r"""If (f("True", True)) && (x =/= 2) Then x = !(-.g({1, 0}) ==. (7.*.73.)) ; EndIf."""
        expect = r"""If,(,f,(,True,,,True,),),&&,(,x,=/=,2,),Then,x,=,!,(,-.,g,(,{,1,,,0,},),==,.,(,7.,*.,73.,),),;,EndIf,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 192))
        
    def test_nested_stmt(self):
        """test nested statements"""
        testcase = r"""For(i=0,True,0)While(False)DoDoDoIfisNot Thena=0;EndIf.While(0)EndDo.While(f(2))EndDo.EndWhile.EndFor."""
        expect = r"""For,(,i,=,0,,,True,,,0,),While,(,False,),Do,Do,Do,If,isNot,Then,a,=,0,;,EndIf,.,While,(,0,),EndDo,.,While,(,f,(,2,),),EndDo,.,EndWhile,.,EndFor,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 193))
        
    def test_weird_init(self):
        """test weird initialization"""
        testcase = r"""Var:x[]=If True Then True Else {}, f()=func, a+b=3;
        Function: func
            Parameter: x=0
            Body
            EndBody."""
        expect = r"""Var,:,x,[,],=,If,True,Then,True,Else,{,},,,f,(,),=,func,,,a,+,b,=,3,;,Function,:,func,Parameter,:,x,=,0,Body,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 194))

    def test_weird_assign_stmt(self):
        """test weird assignment statements"""
        testcase = r"""(a[a[True]+f(c)]+a)[a]=a[a];"""
        expect = r"""(,a,[,a,[,True,],+,f,(,c,),],+,a,),[,a,],=,a,[,a,],;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 195))

    def test_mistake_196(self):
        """test common mistakes"""
        testcase = r"""Varr:im_okay;
        var:me_2;
        Va:but_im_not;"""
        expect = r"""Var,r,:,im_okay,;,var,:,me_2,;,Error Token V"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 196))
        
    def test_mistake_197(self):
        """test common mistakes"""
        testcase = r"""Function: tightBodyEndBody."""
        expect = r"""Function,:,tightBodyEndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 197))
    
    def test_mistake_198(self):
        """test common mistakes"""
        testcase = r"""Ifx==yThenBreak;EndIf."""
        expect = r"""If,x,==,yThenBreak,;,EndIf,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 198))
    
    def test_mistake_199(self):
        """test common mistakes"""
        testcase = r"""a=var&var|var;"""
        expect = r"""a,=,var,Error Token &"""
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 199))