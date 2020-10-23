import unittest

from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
      
    def test1_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test2_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test3_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test4_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test5_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test6_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test7_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))
    def test8_global_variable1(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var: a = 5;  ""","""Var,:,a,=,5,;,<EOF>""",108))
    def test9_global_variable2(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var: b[2][3] = {{2,3,4},{4,5,6}};  ""","""Var,:,b,[,2,],[,3,],=,{,{,2,,,3,,,4,},,,{,4,,,5,,,6,},},;,<EOF>""",109))
    def test10_global_variable3(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var: c, d = 6, e, f;  ""","""Var,:,c,,,d,=,6,,,e,,,f,;,<EOF>""",110))
    def test11_global_variable4(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var: m, n[10];  ""","""Var,:,m,,,n,[,10,],;,<EOF>""",111))
    def test12_single_comment(self):
        self.assertTrue(TestLexer.checkLexeme("** This is a single-line comment. **","""<EOF>""",112))
    def test13_multi_comment(self):
        self.assertTrue(TestLexer.checkLexeme(r"""** This is a
        * multi-line 
        * comment. 
        **""","""<EOF>""",113))
    def test14_unterminated_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is a single-line comment. ****as""","""Unterminated Comment""",114))
    def test15_unterminated_comment2(self):
        self.assertTrue(TestLexer.checkLexeme(r"""** This is a
        * multi-line 
        ** comment. 
        **""","""comment,.,Unterminated Comment""",115))
    def test16_comment(self):
        self.assertTrue(TestLexer.checkLexeme("*****","""*,<EOF>""",116))
    def test17_identifiers(self):
        self.assertTrue(TestLexer.checkLexeme(""" Hoang Gia Khang ""","""Error Token H""",117))
    def test18_identifiers2(self):
        self.assertTrue(TestLexer.checkLexeme(""" hoangGia Khang ""","""hoangGia,Error Token K""",118))
    def test19_identifiers3(self):
        self.assertTrue(TestLexer.checkLexeme(""" _khangasdas ""","""Error Token _""",119))
    def test20_identifiers4(self):
        self.assertTrue(TestLexer.checkLexeme(""" hoangGiakh1231231____FAsdf ""","""hoangGiakh1231231____FAsdf,<EOF>""",120))
    def test21_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(r""" Body Break Continue Do
        Else ElseIf EndBody EndIf EndFor EndWhile For Function 
        If Parameter Return Then 
        Var While True False EndDo ""","""Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,Function,If,Parameter,Return,Then,Var,While,True,False,EndDo,<EOF>""",121))
    def test22_Error_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(r""" Body Break Continue Do
        Else ElseIf EndBody EndIf EndFor EndWhile For Function 
        IF Parameter Return Then 
        Var While True False EndDo ""","""Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,Function,Error Token I""",122))
    def test23_float_array(self):
        self.assertTrue(TestLexer.checkLexeme(""" {2.0,3,4}  ""","""{,2.0,,,3,,,4,},<EOF>""",123))
    def test24_operators(self):
        self.assertTrue(TestLexer.checkLexeme("""+ +. - -. * *. \\ \\. % ! && || == != < > <= >= =/= <. >. <=. >=. ""","""+,+.,-,-.,*,*.,\\,\\.,%,!,&&,||,==,!=,<,>,<=,>=,=/=,<.,>.,<=.,>=.,<EOF>""",124))
    def test25_error_operators(self):
        self.assertTrue(TestLexer.checkLexeme("""+ +. - -. * *.  ? \\ \\. % ! &&""","""+,+.,-,-.,*,*.,Error Token ?""",125))
    def test26_error_separators(self):
        self.assertTrue(TestLexer.checkLexeme("""()[]:.,;{}""","""(,),[,],:,.,,,;,{,},<EOF>""",126))
    def test27_literal_interger_decimal(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0 10 0 5 123123123""","""0,10,0,5,123123123,<EOF>""",127))
    def test28_literal_interger_decimal(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0123456789""","""0,123456789,<EOF>""",128))
    def test29_literal_interger_hex(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0x12902""","""0x12902,<EOF>""",129))
    def test30_literal_interger_hex(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0XAAF231""","""0XAAF231,<EOF>""",130))
    def test31_not_literal_interger_hex(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0XAGF231""","""0XA,Error Token G""",131))
    def test32_not_literal_interger_hex(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0xgAF231""","""0,xgAF231,<EOF>""",132))
    def test33_literal_interger_oc(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0o5620""","""0o5620,<EOF>""",133))
    def test34_literal_interger_oc(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0O375283""","""0O3752,83,<EOF>""",134))
    def test35_not_literal_interger_oc(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0O98765""","""0,Error Token O""",135))
    def test36_not_literal_interger_oc(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0oABC123""","""0,oABC123,<EOF>""",136))
    def test37_literal_interger(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0 199 0xFF 0XABC 0o567 0O77""","""0,199,0xFF,0XABC,0o567,0O77,<EOF>""",137))
    def test38_float(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12.0e3 12e3 12.e5 12.0e3 12000. 120000e-1""","""12.0e3,12e3,12.e5,12.0e3,12000.,120000e-1,<EOF>""",138))
    def test39_float(self):
        self.assertTrue(TestLexer.checkLexeme("""000.0  0.  000E0  000.0E0  00.E0""","""000.0,0.,000E0,000.0E0,00.E0,<EOF>""",139))
    def test40_not_float(self):
        self.assertTrue(TestLexer.checkLexeme("""0.^0""","""0.,Error Token ^""",140))
    def test41_not_float(self):
        self.assertTrue(TestLexer.checkLexeme("""-2.E3""","""-,2.E3,<EOF>""",141))
    def test42_not_float(self):
        self.assertTrue(TestLexer.checkLexeme("""-5Abx0.^0""","""-,5,Error Token A""",142))
    def test43_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("""True False""","""True,False,<EOF>""",143))
    def test44_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("""TRUE""","""Error Token T""",144))
    def test45_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("""false FalsE""","""false,Error Token F""",145))
    def test46_array(self):
        self.assertTrue(TestLexer.checkLexeme("""{"hoang","gia","khang"}""","""{,hoang,,,gia,,,khang,},<EOF>""",146))
    def test47_array(self):
        self.assertTrue(TestLexer.checkLexeme("""{{1.e3,1.},{2.3,5e0}}""","""{,{,1.e3,,,1.,},,,{,2.3,,,5e0,},},<EOF>""",147))
    def test48_array(self):
        self.assertTrue(TestLexer.checkLexeme("""{1,2""","""{,1,,,2,<EOF>""",148))
    def test49_array(self):
        self.assertTrue(TestLexer.checkLexeme("""{True,False}""","""{,True,,,False,},<EOF>""",149))
    def test50_array(self):
        self.assertTrue(TestLexer.checkLexeme("""{true,False}""","""{,true,,,False,},<EOF>""",150))
    def test51_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Toi la Hoang Gia Khang!." ""","""Toi la Hoang Gia Khang!.,<EOF>""",151))
    def test52_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t" ""","""This is a string containing tab \\t,<EOF>""",152))
    def test53_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" ""","""He asked me: '"Where is John?'",<EOF>""",153))
    def test54_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me:  \\'Where is John?'"" ""","""He asked me:  \\'Where is John?'",<EOF>""",154))
    def test55_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: 'Where is John?'"" ""","""Illegal Escape In String: He asked me: 'W""",155))
    def test56_return_stmt(self):
        self.assertTrue(TestLexer.checkLexeme(""" Return True ; ""","""Return,True,;,<EOF>""",156))
    def test57_comment_in_array(self):
        self.assertTrue(TestLexer.checkLexeme("""{12 **  23asd&%^#$*()**, 3} ; ""","""{,12,,,3,},;,<EOF>""",157))
    def test58_assign_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("""k__HANmn = foo(g(x + 3) * 4) ;""","""k__HANmn,=,foo,(,g,(,x,+,3,),*,4,),;,<EOF>""",158))
    def test59_if_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("""
        If (a > b) && (!c) Then
            Return True;
        Else Return False;
        EndIf.""",
        """If,(,a,>,b,),&&,(,!,c,),Then,Return,True,;,Else,Return,False,;,EndIf,.,<EOF>""",159))
    def test60_for_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("""
        For (step = 10, step < 100, step * step) Do
            writeln(step);
        EndDo.""",
        """For,(,step,=,10,,,step,<,100,,,step,*,step,),Do,writeln,(,step,),;,EndDo,.,<EOF>""",160))
    def test61_while_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("""
        While n < 10 Do
            writeln(n * n + foo(n));
        EndWhile.""",
        """While,n,<,10,Do,writeln,(,n,*,n,+,foo,(,n,),),;,EndWhile,.,<EOF>""",161))
    def test62_Do_While_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Do
            i = i + 1;
            input(a[i]);
        While (i < 10) EndDo.""",
        """Do,i,=,i,+,1,;,input,(,a,[,i,],),;,While,(,i,<,10,),EndDo,.,<EOF>""",162))
    def test63_Break_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Do
            i = i + 1;
            input(a[i]);
            If (i == 6) Then
                Break ;
            EndIf.
        While (i < 10) EndDo.""",
        """Do,i,=,i,+,1,;,input,(,a,[,i,],),;,If,(,i,==,6,),Then,Break,;,EndIf,.,While,(,i,<,10,),EndDo,.,<EOF>""",163))
    def test64_Continue_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("""
            While n < 10 Do
                If n == 7 Then
                    Continue;
                ElseIf n > 7 Then
                    Break;
                EndIf.
                writeln(n * n + foo(n));
            EndWhile.""",
            """While,n,<,10,Do,If,n,==,7,Then,Continue,;,ElseIf,n,>,7,Then,Break,;,EndIf,.,writeln,(,n,*,n,+,foo,(,n,),),;,EndWhile,.,<EOF>""",164))
    def test65_Call_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("""
            Var: a, b = 10;
            a = foo(b * 3) + 10;
            writeln(a);""",
            """Var,:,a,,,b,=,10,;,a,=,foo,(,b,*,3,),+,10,;,writeln,(,a,),;,<EOF>""",165))
    def test66_return_stmt(self):
        self.assertTrue(TestLexer.checkLexeme("""
            Function: nothing
            Parameter: a, b
            Body:
                If a == b Then
                    Return 1;
                Else
                    Return 0;
                EndIf.
            EndBody.""",
            """Function,:,nothing,Parameter,:,a,,,b,Body,:,If,a,==,b,Then,Return,1,;,Else,Return,0,;,EndIf,.,EndBody,.,<EOF>""",166))
    def test67(self):
        self.assertTrue(TestLexer.checkLexeme("""
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
            EndBody.""",
            """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>""",167))
    def test68_illegal_esc(self):
        self.assertTrue(TestLexer.checkLexeme(""" "bfasdf\h" """, """Illegal Escape In String: bfasdf\h""",168))
    def test69_unterminated_comment(self):
        self.assertTrue(TestLexer.checkLexeme(""" **asdn899*(&(*US))***** """, """Unterminated Comment""",169))
    def test70_Unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Im Khang\n SK" """, """Unclosed String: Im Khang""",170))
    def test71(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Ho Chi Minh University\\n of \\t Technology" """, """Ho Chi Minh University\\n of \\t Technology,<EOF>""",171))
    def test72_illegal_esc(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Dai. Hoc. Bach' Khoa" """, """Illegal Escape In String: Dai. Hoc. Bach' """,172))
    def test73_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Thanh Pho'" Ho_ Chi???Minh" """, """Thanh Pho'" Ho_ Chi???Minh,<EOF>""",173))
    def test74_error_char(self):
        self.assertTrue(TestLexer.checkLexeme(""" th&anh """, """th,Error Token &""",174))
    def test75_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""*****""", """*,<EOF>""",175))
    def test76(self):
        self.assertTrue(TestLexer.checkLexeme(""" "What should i \\b \\f \\r \\n test now, huh?" """, """What should i \\b \\f \\r \\n test now, huh?,<EOF>""",176))
    def test77_illegal_esc(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Really \\t DON\'T know" """, """Illegal Escape In String: Really \\t DON'T""",177))
    def test78(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\ DenDi said: '"MMR is just a number'"" """, """\\\\ DenDi said: '"MMR is just a number'",<EOF>""",178))
    def test79_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "BKCSE """, """Unclosed String: BKCSE """,179))
    def test80_array(self):
        self.assertTrue(TestLexer.checkLexeme(""" {1,{1.e,3e},{{{}}}} """, """{,1,,,{,1.,e,,,3,e,},,,{,{,{,},},},},<EOF>""",180))
    def test81_comment_in_array(self):
        self.assertTrue(TestLexer.checkLexeme(""" {{123,**das** "SK",3}} """, """{,{,123,,,SK,,,3,},},<EOF>""",181))
    def test82_array(self):
        self.assertTrue(TestLexer.checkLexeme(""" {{{{{}{{2}}}}}} """, """{,{,{,{,{,},{,{,2,},},},},},},<EOF>""",182))
    def test83_array(self):
        self.assertTrue(TestLexer.checkLexeme(""" {{}{}} """, """{,{,},{,},},<EOF>""",183))
    def test84_error_keyword_var(self):
        self.assertTrue(TestLexer.checkLexeme(""" 
        Function: test
        Body:
            VaR: a = 1;
            writeln(a);
        EndBody. """, """Function,:,test,Body,:,Error Token V""",184))
    def test85(self):
        self.assertTrue(TestLexer.checkLexeme(""" 
        Function: test
        Body:
            Var: a = 1, b = 1.0;
            writeln(a \\. b);
        EndBody. """, """Function,:,test,Body,:,Var,:,a,=,1,,,b,=,1.0,;,writeln,(,a,\\.,b,),;,EndBody,.,<EOF>""",185))
    def test86_error_token(self):
        self.assertTrue(TestLexer.checkLexeme(""" a &&& b""", """a,&&,Error Token &""",186))
    def test87(self):
        self.assertTrue(TestLexer.checkLexeme(""" abc \\\\\\""", """abc,\\,\\,\\,<EOF>""",187))
    def test88(self):
        self.assertTrue(TestLexer.checkLexeme(""" 
        **The best football club 
            FC Barcelona**
        "abcd'a" ""","""Illegal Escape In String: abcd'a""",188))
    def test89_string_teencode(self):
        self.assertTrue(TestLexer.checkLexeme(""" "c0' c0ng m4`j s4't c0' ng4`ij n3n kjm" ""","""Illegal Escape In String: c0' """,189))
    def test90(self):
        self.assertTrue(TestLexer.checkLexeme(""" **"c0' c0ng m4`j s4't c0' \\h ng4`ij n3n kjm"** ""","""<EOF>""",190))
    def test91_unterminated_comment(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var: a = 0X7FA; **Python is a programming language* ""","""Var,:,a,=,0X7FA,;,Unterminated Comment""",191))
    def test92(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0 199 0xFF 0XABC 0o567 0O77 True FAlse""","""0,199,0xFF,0XABC,0o567,0O77,True,Error Token F""",192))
    def test93(self):
        self.assertTrue(TestLexer.checkLexeme("""++.-.- ""","""+,+.,-.,-,<EOF>""",193))
    def test94_array(self):
        self.assertTrue(TestLexer.checkLexeme("""{{-1.1, -0e123},{-"abc", -True}} ""","""{,{,-,1.1,,,-,0e123,},,,{,-,abc,,,-,True,},},<EOF>""",194))
    def test95_UNCLOSE_STRING(self):
        self.assertTrue(TestLexer.checkLexeme("""****   "Hello sir!""","""Unclosed String: Hello sir!""",195))
    def test96_ILLEGAL_ESCAPE(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Talented Engineering - 'Computer Science"  ""","""Illegal Escape In String: Talented Engineering - 'C""",196))
    def test97_url_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is my facebook: https://www.facebook.com/hgkhang"  ""","""This is my facebook: https://www.facebook.com/hgkhang,<EOF>""",197))
    def test98_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""
        **
        * nothing to say \t
        * I'm currently \h learning everything \\n
        **focusing""","""focusing,<EOF>""",198))
    def test99(self):
        self.assertTrue(TestLexer.checkLexeme(
            """Function: reverseString
            Parameter: num
            Body:
                For (i = num * 2, i < num * num, i + 1) Do
                    If i % 2 == 0 Then
                        writeln(i);
                    EndIf.
                EndFor.
            EndBody.""",
            """Function,:,reverseString,Parameter,:,num,Body,:,For,(,i,=,num,*,2,,,i,<,num,*,num,,,i,+,1,),Do,If,i,%,2,==,0,Then,writeln,(,i,),;,EndIf,.,EndFor,.,EndBody,.,<EOF>""",199))
    def test100_index_operator(self):
        self.assertTrue(TestLexer.checkLexeme("""
        a[3 + foo(2)] = a[b[2][3]] + 4;""",
        """a,[,3,+,foo,(,2,),],=,a,[,b,[,2,],[,3,],],+,4,;,<EOF>""",200))