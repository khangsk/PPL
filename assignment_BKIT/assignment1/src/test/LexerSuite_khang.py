import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("DuyKhang","Error Token D",101))
        self.assertTrue(TestLexer.checkLexeme("duyKhang","duyKhang,<EOF>",102))
        self.assertTrue(TestLexer.checkLexeme("duy0 Khang","duy0,Error Token K",103))
        self.assertTrue(TestLexer.checkLexeme("duy khAng_","duy,khAng_,<EOF>",104))
        self.assertTrue(TestLexer.checkLexeme("0DuyKhang","0,Error Token D",105))
        self.assertTrue(TestLexer.checkLexeme("_DuyKhang","Error Token _",106))
        self.assertTrue(TestLexer.checkLexeme("","<EOF>",107))

    def test_integers(self):
        '''test integers'''
        self.assertTrue(TestLexer.checkLexeme("""01230""","""0,1230,<EOF>""",108))
        self.assertTrue(TestLexer.checkLexeme("0 199 0xFF 0XABC 0o567 0O77","0,199,0xFF,0XABC,0o567,0O77,<EOF>",109))
        self.assertTrue(TestLexer.checkLexeme("-1","-,1,<EOF>",110))

    def test_floats(self):
        '''test floats'''
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12E3 12.e5 12000. 120000e-1","12.0e3,12E3,12.e5,12000.,120000e-1,<EOF>",111))
        self.assertTrue(TestLexer.checkLexeme("-00.01 1.e--1 ..12","-,00.01,1.,e,-,-,1,.,.,12,<EOF>",112))

    def test_booleans(self):
        """test booleans"""
        self.assertTrue(TestLexer.checkLexeme("True False Truefalse","True,False,True,false,<EOF>",113))
        self.assertTrue(TestLexer.checkLexeme("true fAlsE trueFalse","true,fAlsE,trueFalse,<EOF>",114))
    
    def test_legal_strings(self):
        """test strings"""
        self.assertTrue(TestLexer.checkLexeme(""" "" """,""",<EOF>""",115))
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\\ def \\t" ""","""abc\\\ def \\t,<EOF>""",116))
        self.assertTrue(TestLexer.checkLexeme(""" "@bc'"def\\'" ""","""@bc'"def\\',<EOF>""",117))
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\f def\\r\\n" ""","""abc\\f def\\r\\n,<EOF>""",118))
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",119))
        self.assertTrue(TestLexer.checkLexeme(""" "abcdef\\'"  ""","""abcdef\\',<EOF>""",120))
        

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",121))
        self.assertTrue(TestLexer.checkLexeme(""" "abc'def" ""","""Illegal Escape In String: abc'd""",122))

    def test_unclosed_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,123))
        self.assertTrue(TestLexer.checkLexeme(""" "abc"def" ""","""abc,def,Unclosed String:  """,124))
        self.assertTrue(TestLexer.checkLexeme(""" "abc'"def ""","""Unclosed String: abc'"def """,125))
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\'"" ""","""abc\\',Unclosed String:  """,126))

    def test_error_char(self):
        """test error char"""
        self.assertTrue(TestLexer.checkLexeme(""" 'abc'  ""","""Error Token '""",127))
        self.assertTrue(TestLexer.checkLexeme(""" "abc "'def'" "  ""","""abc ,Error Token '""",128))
        self.assertTrue(TestLexer.checkLexeme(""" "abc'"def" ""","""abc'"def,<EOF>""",129))

    def test_unterminated_comment(self):
        """test unterminated comment"""
        self.assertTrue(TestLexer.checkLexeme(""" *abc**  ""","""*,abc,Unterminated Comment""",130))
        self.assertTrue(TestLexer.checkLexeme(""" **abc*  ""","""Unterminated Comment""",131))
        self.assertTrue(TestLexer.checkLexeme(""" **** """, """<EOF>""",132))
        self.assertTrue(TestLexer.checkLexeme(""" 
        ** print is a function\nhello world\ni'm khang\n**  
        ""","""<EOF>""",133))
        self.assertTrue(TestLexer.checkLexeme(""" **abc ""","""Unterminated Comment""",134))
    
    def test_array(self):
        """test arrays"""
        self.assertTrue(TestLexer.checkLexeme(""" {{1},2,3}  ""","""{,{,1,},,,2,,,3,},<EOF>""",135))
        self.assertTrue(TestLexer.checkLexeme(""" {1, "String", }  ""","""{,1,,,String,,,},<EOF>""",136))
        self.assertTrue(TestLexer.checkLexeme(""" {{1},abc  ""","""{,{,1,},,,abc,<EOF>""",137))

    def test_literal(self):
        '''test illegal literals'''
        self.assertTrue(TestLexer.checkLexeme(""" 10x29 ""","""10,x29,<EOF>""",138))
        self.assertTrue(TestLexer.checkLexeme(""" 1o03 ""","""1,o03,<EOF>""",139))
        self.assertTrue(TestLexer.checkLexeme(""" "a\nb" ""","""Unclosed String: a""",140))
        self.assertTrue(TestLexer.checkLexeme(""" "a\bt" ""","""a\bt,<EOF>""",141))
        self.assertTrue(TestLexer.checkLexeme(""" 1E2.01 ""","""1E2,.,0,1,<EOF>""",142))
        self.assertTrue(TestLexer.checkLexeme(""" {"a'"bc"} ""","""{,a'"bc,},<EOF>""",143))
        self.assertTrue(TestLexer.checkLexeme(""" Truee ""","""True,e,<EOF>""",144))
        self.assertTrue(TestLexer.checkLexeme(""" """" abc """" ""","""abc,<EOF>""",145))
        self.assertTrue(TestLexer.checkLexeme(""" 0x0o11 ""","""0,x0o11,<EOF>""",146))
        self.assertTrue(TestLexer.checkLexeme(""" " **abc** " """,""" **abc** ,<EOF>""",147))
        self.assertTrue(TestLexer.checkLexeme(""" "{1,2,3}" ""","""{1,2,3},<EOF>""",148))
        self.assertTrue(TestLexer.checkLexeme(""" +-. ""","""+,-.,<EOF>""",149))
        self.assertTrue(TestLexer.checkLexeme(""" a & b ""","""a,Error Token &""",150))
        self.assertTrue(TestLexer.checkLexeme(""" ***** ""","""*,<EOF>""",151))
        self.assertTrue(TestLexer.checkLexeme(""" ** *** ""","""*,<EOF>""",152))
        self.assertTrue(TestLexer.checkLexeme(""" *** ** ""","""<EOF>""",153))
        self.assertTrue(TestLexer.checkLexeme(""" x = a \ b ""","""x,=,a,\,b,<EOF>""",154))
        self.assertTrue(TestLexer.checkLexeme(""" ** (** abc **) ** ""","""abc,<EOF>""",155))
        self.assertTrue(TestLexer.checkLexeme(""" "a' c" ""","""Illegal Escape In String: a' """,156))
        self.assertTrue(TestLexer.checkLexeme(""" "\\" """,'Illegal Escape In String: \\"',157))
        self.assertTrue(TestLexer.checkLexeme(""" {1**abc**2} ""","""{,1,2,},<EOF>""",158))
        self.assertTrue(TestLexer.checkLexeme(""" FFalse ""","""Error Token F""",159))
        self.assertTrue(TestLexer.checkLexeme(""" '"  ""","""Error Token '""",160))
        self.assertTrue(TestLexer.checkLexeme(""" {""}  ""","""{,,},<EOF>""",161))
        self.assertTrue(TestLexer.checkLexeme(""" 0x  ""","""0,x,<EOF>""",162))
        self.assertTrue(TestLexer.checkLexeme(""" {**abc*1}  ""","""{,Unterminated Comment""",163))
        self.assertTrue(TestLexer.checkLexeme(""" {*****} ""","""{,*,},<EOF>""",164))
        self.assertTrue(TestLexer.checkLexeme(""" {@}  ""","""{,Error Token @""",165))
        self.assertTrue(TestLexer.checkLexeme(""" "**abc"**  ""","""**abc,Unterminated Comment""",166))
        self.assertTrue(TestLexer.checkLexeme(""" ** \n **  ""","""<EOF>""",167))
        self.assertTrue(TestLexer.checkLexeme(""" x12.e5() ""","""x12,.,e5,(,),<EOF>""",168))
        self.assertTrue(TestLexer.checkLexeme(""" \\n ""","""\,n,<EOF>""",169))
        self.assertTrue(TestLexer.checkLexeme(""" {\\n,\n} ""","""{,\,n,,,},<EOF>""",170))
        self.assertTrue(TestLexer.checkLexeme(""" cout << x; ""","""cout,<,<,x,;,<EOF>""",171))
        self.assertTrue(TestLexer.checkLexeme(' "\\"" ','Illegal Escape In String: \\"',172))
        self.assertTrue(TestLexer.checkLexeme(""" 1.2 =/ = 2.1 ""","""1.2,=,Error Token /""",173))
        self.assertTrue(TestLexer.checkLexeme(""" x = 1\\n ""","""x,=,1,\,n,<EOF>""",174))
        self.assertTrue(TestLexer.checkLexeme(""" {Truefalse} ""","""{,True,false,},<EOF>""",175))
        self.assertTrue(TestLexer.checkLexeme(""" **"**a'"bc" ""","""a,Error Token '""",176))
        self.assertTrue(TestLexer.checkLexeme(""" "Error Token '"" ""","""Error Token '",<EOF>""",177))
        self.assertTrue(TestLexer.checkLexeme(""" <EOF> ""","""<,Error Token E""",178))
        self.assertTrue(TestLexer.checkLexeme(""" 12.e+5 ""","""12.e+5,<EOF>""",179))
        self.assertTrue(TestLexer.checkLexeme('"\n"','Unclosed String: ',180))

    def test_program_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" 
        for (i = 0, i < 10, 2) Do
            writeln(i);
        EndFor.  
        ""","""for,(,i,=,0,,,i,<,10,,,2,),Do,writeln,(,i,),;,EndFor,.,<EOF>""",181))
        
    def test_program_2(self):
        self.assertTrue(TestLexer.checkLexeme("""
        FOR (i = 0, i < 4, 1) DO 
        ENDFOR.
        ""","""Error Token F""",182))

    def test_program_3(self):
        self.assertTrue(TestLexer.checkLexeme("""
        If n == 0 Then
            Return 0;
        Elif n == 1 Then
            Return 1;
        Else 
            Return -1;
        EndIf.
        ""","""If,n,==,0,Then,Return,0,;,Error Token E""",183))

    def test_program_4(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            while (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody.
        ""","""Function,:,foo,Parameter,:,a,[,5,],,,b,Body,:,Var,:,i,=,0,;,while,(,i,<,5,),Do,a,[,i,],=,b,+.,1.0,;,i,=,i,+,1,;,EndWhile,.,EndBody,.,<EOF>""",184))
    
    def test_program_5(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        ""","""Var,:,a,=,5,;,Var,:,b,[,2,],[,3,],=,{,{,2,,,3,,,4,},,,{,4,,,5,,,6,},},;,Var,:,c,,,d,=,6,,,e,,,f,;,Var,:,m,,,n,[,10,],;,<EOF>""",185))
    
    def test_program_6(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Body:
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.
        ""","""Body,:,Var,:,r,=,10.,,,v,;,v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,EndBody,.,<EOF>""",186))

    def test_program_7(self):
        self.assertTrue(TestLexer.checkLexeme("""
        If bool_of_string ("True") Then
            a = int_of_string (read ());
            b = float_of_int (a) +. 2.0;
        EndIf.
        ""","""If,bool_of_string,(,True,),Then,a,=,int_of_string,(,read,(,),),;,b,=,float_of_int,(,a,),+.,2.0,;,EndIf,.,<EOF>""",187))

    def test_program_8(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Var: a[5] = {1,4,3,2,0};
        Var: b[2][3]={{1,2,3},{4,5,6}};
        ""","""Var,:,a,[,5,],=,{,1,,,4,,,3,,,2,,,0,},;,Var,:,b,[,2,],[,3,],=,{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},},;,<EOF>""",188))

    def test_program_9(self):
        self.assertTrue(TestLexer.checkLexeme("""
        If n == 0 & n !== 1 Then
            Return 0;
        ""","""If,n,==,0,Error Token &""",189))

    def test_program_10(self):
        self.assertTrue(TestLexer.checkLexeme("""
        BodyBreakContinueDoElseElseIfEndBodyEndIfEndForEndWhileFor
        ""","""Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,<EOF>""",190))
    
    def test_program_11(self):
        self.assertTrue(TestLexer.checkLexeme("""
        FunctionIfParameterReturnThenVarWhileTrueFalseEndDo=!&&||+-*
        ""","""Function,If,Parameter,Return,Then,Var,While,True,False,EndDo,=,!,&&,||,+,-,*,<EOF>""",192))

    def test_program_12(self):
        self.assertTrue(TestLexer.checkLexeme("""
        \\%==!=<><=>=+.-.*.\\.=/=<.>.<=.>=.()[]:.,;{}
        ""","""\,%,==,!=,<,>,<=,>=,+.,-.,*.,\.,=/=,<.,>.,<=.,>=.,(,),[,],:,.,,,;,{,},<EOF>""",192))

    def test_program_13(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Return "True";
        ""","""Return,True,;,<EOF>""",193))

    def test_program_14(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Return x.foo(1**2);
        ""","""Return,x,.,foo,(,1,Unterminated Comment""",194))

    def test_program_15(self):
        self.assertTrue(TestLexer.checkLexeme("""\\ day la chu thich""","""\,day,la,chu,thich,<EOF>""",195))

    def test_program_16(self):
        self.assertTrue(TestLexer.checkLexeme("""x := 2""","""x,:,=,2,<EOF>""",196))
    
    def test_program_17(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\m" ""","""Illegal Escape In String: \m""",197))

    def test_program_18(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'""  ""","""He asked me: '"Where is John?'",<EOF>""",198))

    
    def test_program_19(self):
        self.assertTrue(TestLexer.checkLexeme(""" 
        foo (2 + x, 4. \. y); 
        goo (); 
        ""","""foo,(,2,+,x,,,4.,\.,y,),;,goo,(,),;,<EOF>""",199))

    
    def test_program_20(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Break;
        ""","""Break,;,<EOF>""",200))