# Generated from c:\Users\KHANG\Desktop\PPL\5. AST\ASTGenExercises\cau4\src\main\mc\parser\MC.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\5\2\20\n\2\3\3\3\3\3\3\7\3\25\n\3\f\3\16\3\30\13\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\7\4\37\n\4\f\4\16\4\"\13\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\5\5*\n\5\3\5\2\2\6\2\4\6\b\2\2\2,\2\17")
        buf.write("\3\2\2\2\4\26\3\2\2\2\6\33\3\2\2\2\b)\3\2\2\2\n\13\5\4")
        buf.write("\3\2\13\f\7\7\2\2\f\r\5\4\3\2\r\20\3\2\2\2\16\20\5\4\3")
        buf.write("\2\17\n\3\2\2\2\17\16\3\2\2\2\20\3\3\2\2\2\21\22\5\6\4")
        buf.write("\2\22\23\7\b\2\2\23\25\3\2\2\2\24\21\3\2\2\2\25\30\3\2")
        buf.write("\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\31\3\2\2\2\30\26\3")
        buf.write("\2\2\2\31\32\5\6\4\2\32\5\3\2\2\2\33 \5\b\5\2\34\35\7")
        buf.write("\t\2\2\35\37\5\b\5\2\36\34\3\2\2\2\37\"\3\2\2\2 \36\3")
        buf.write("\2\2\2 !\3\2\2\2!\7\3\2\2\2\" \3\2\2\2#*\7\4\2\2$*\7\3")
        buf.write("\2\2%&\7\5\2\2&\'\5\2\2\2\'(\7\6\2\2(*\3\2\2\2)#\3\2\2")
        buf.write("\2)$\3\2\2\2)%\3\2\2\2*\t\3\2\2\2\6\17\26 )")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "<INVALID>", "'^'", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "BOOLIT", "INTLIT", "LB", "RB", "COMPARE", 
                      "EXPONENT", "ANDOR", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_exp = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_operand = 3

    ruleNames =  [ "exp", "term", "factor", "operand" ]

    EOF = Token.EOF
    BOOLIT=1
    INTLIT=2
    LB=3
    RB=4
    COMPARE=5
    EXPONENT=6
    ANDOR=7
    SEMI=8
    WS=9
    ERROR_CHAR=10
    UNCLOSE_STRING=11
    ILLEGAL_ESCAPE=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.TermContext)
            else:
                return self.getTypedRuleContext(MCParser.TermContext,i)


        def COMPARE(self):
            return self.getToken(MCParser.COMPARE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp




    def exp(self):

        localctx = MCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_exp)
        try:
            self.state = 13
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.term()
                self.state = 9
                self.match(MCParser.COMPARE)
                self.state = 10
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.FactorContext)
            else:
                return self.getTypedRuleContext(MCParser.FactorContext,i)


        def EXPONENT(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.EXPONENT)
            else:
                return self.getToken(MCParser.EXPONENT, i)

        def getRuleIndex(self):
            return MCParser.RULE_term




    def term(self):

        localctx = MCParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 15
                    self.factor()
                    self.state = 16
                    self.match(MCParser.EXPONENT) 
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 23
            self.factor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.OperandContext)
            else:
                return self.getTypedRuleContext(MCParser.OperandContext,i)


        def ANDOR(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.ANDOR)
            else:
                return self.getToken(MCParser.ANDOR, i)

        def getRuleIndex(self):
            return MCParser.RULE_factor




    def factor(self):

        localctx = MCParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.operand()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.ANDOR:
                self.state = 26
                self.match(MCParser.ANDOR)
                self.state = 27
                self.operand()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def BOOLIT(self):
            return self.getToken(MCParser.BOOLIT, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_operand




    def operand(self):

        localctx = MCParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operand)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(MCParser.INTLIT)
                pass
            elif token in [MCParser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(MCParser.BOOLIT)
                pass
            elif token in [MCParser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(MCParser.LB)
                self.state = 36
                self.exp()
                self.state = 37
                self.match(MCParser.RB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





