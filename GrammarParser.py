# Generated from Grammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,289,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,
        114,8,7,10,7,12,7,117,9,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,126,8,
        8,10,8,12,8,129,9,8,1,8,1,8,1,9,1,9,3,9,135,8,9,1,10,1,10,1,10,1,
        10,1,10,1,10,3,10,143,8,10,1,11,1,11,3,11,147,8,11,1,12,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,
        1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,
        1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,
        5,23,204,8,23,10,23,12,23,207,9,23,1,23,3,23,210,8,23,1,24,1,24,
        1,24,1,24,3,24,216,8,24,1,25,1,25,1,26,1,26,1,26,1,26,3,26,224,8,
        26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,232,8,27,1,28,1,28,1,28,1,
        28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,259,8,30,1,31,1,
        31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,
        35,1,35,0,0,36,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,0,1,1,0,6,
        11,271,0,72,1,0,0,0,2,76,1,0,0,0,4,80,1,0,0,0,6,85,1,0,0,0,8,90,
        1,0,0,0,10,95,1,0,0,0,12,102,1,0,0,0,14,109,1,0,0,0,16,121,1,0,0,
        0,18,134,1,0,0,0,20,142,1,0,0,0,22,146,1,0,0,0,24,148,1,0,0,0,26,
        153,1,0,0,0,28,158,1,0,0,0,30,163,1,0,0,0,32,168,1,0,0,0,34,173,
        1,0,0,0,36,178,1,0,0,0,38,183,1,0,0,0,40,188,1,0,0,0,42,193,1,0,
        0,0,44,196,1,0,0,0,46,209,1,0,0,0,48,215,1,0,0,0,50,217,1,0,0,0,
        52,223,1,0,0,0,54,231,1,0,0,0,56,233,1,0,0,0,58,237,1,0,0,0,60,258,
        1,0,0,0,62,260,1,0,0,0,64,265,1,0,0,0,66,277,1,0,0,0,68,282,1,0,
        0,0,70,286,1,0,0,0,72,73,5,33,0,0,73,74,5,3,0,0,74,75,5,33,0,0,75,
        1,1,0,0,0,76,77,5,34,0,0,77,78,5,3,0,0,78,79,5,34,0,0,79,3,1,0,0,
        0,80,81,5,15,0,0,81,82,5,20,0,0,82,83,3,22,11,0,83,84,5,21,0,0,84,
        5,1,0,0,0,85,86,5,16,0,0,86,87,5,20,0,0,87,88,3,22,11,0,88,89,5,
        21,0,0,89,7,1,0,0,0,90,91,5,18,0,0,91,92,5,20,0,0,92,93,3,22,11,
        0,93,94,5,21,0,0,94,9,1,0,0,0,95,96,5,19,0,0,96,97,5,20,0,0,97,98,
        3,22,11,0,98,99,5,14,0,0,99,100,5,32,0,0,100,101,5,21,0,0,101,11,
        1,0,0,0,102,103,5,17,0,0,103,104,5,20,0,0,104,105,3,22,11,0,105,
        106,5,14,0,0,106,107,5,32,0,0,107,108,5,21,0,0,108,13,1,0,0,0,109,
        110,5,35,0,0,110,115,3,22,11,0,111,112,5,14,0,0,112,114,3,22,11,
        0,113,111,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,
        0,116,118,1,0,0,0,117,115,1,0,0,0,118,119,5,32,0,0,119,120,5,36,
        0,0,120,15,1,0,0,0,121,122,5,35,0,0,122,127,3,14,7,0,123,124,5,14,
        0,0,124,126,3,14,7,0,125,123,1,0,0,0,126,129,1,0,0,0,127,125,1,0,
        0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,131,5,36,
        0,0,131,17,1,0,0,0,132,135,3,4,2,0,133,135,3,6,3,0,134,132,1,0,0,
        0,134,133,1,0,0,0,135,19,1,0,0,0,136,143,3,18,9,0,137,143,3,4,2,
        0,138,143,3,6,3,0,139,143,3,8,4,0,140,143,3,10,5,0,141,143,3,12,
        6,0,142,136,1,0,0,0,142,137,1,0,0,0,142,138,1,0,0,0,142,139,1,0,
        0,0,142,140,1,0,0,0,142,141,1,0,0,0,143,21,1,0,0,0,144,147,3,20,
        10,0,145,147,5,32,0,0,146,144,1,0,0,0,146,145,1,0,0,0,147,23,1,0,
        0,0,148,149,5,37,0,0,149,150,5,20,0,0,150,151,3,22,11,0,151,152,
        5,21,0,0,152,25,1,0,0,0,153,154,5,38,0,0,154,155,5,20,0,0,155,156,
        3,22,11,0,156,157,5,21,0,0,157,27,1,0,0,0,158,159,5,39,0,0,159,160,
        5,20,0,0,160,161,3,22,11,0,161,162,5,21,0,0,162,29,1,0,0,0,163,164,
        5,40,0,0,164,165,5,20,0,0,165,166,3,22,11,0,166,167,5,21,0,0,167,
        31,1,0,0,0,168,169,5,41,0,0,169,170,5,20,0,0,170,171,3,22,11,0,171,
        172,5,21,0,0,172,33,1,0,0,0,173,174,5,42,0,0,174,175,5,20,0,0,175,
        176,3,22,11,0,176,177,5,21,0,0,177,35,1,0,0,0,178,179,5,43,0,0,179,
        180,5,20,0,0,180,181,3,22,11,0,181,182,5,21,0,0,182,37,1,0,0,0,183,
        184,5,44,0,0,184,185,5,20,0,0,185,186,3,22,11,0,186,187,5,21,0,0,
        187,39,1,0,0,0,188,189,5,45,0,0,189,190,5,20,0,0,190,191,3,22,11,
        0,191,192,5,21,0,0,192,41,1,0,0,0,193,194,3,22,11,0,194,195,5,13,
        0,0,195,43,1,0,0,0,196,197,3,22,11,0,197,198,5,46,0,0,198,199,3,
        22,11,0,199,45,1,0,0,0,200,205,3,48,24,0,201,202,5,14,0,0,202,204,
        3,48,24,0,203,201,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,
        1,0,0,0,206,210,1,0,0,0,207,205,1,0,0,0,208,210,3,50,25,0,209,200,
        1,0,0,0,209,208,1,0,0,0,210,47,1,0,0,0,211,216,5,27,0,0,212,213,
        5,27,0,0,213,214,5,12,0,0,214,216,3,22,11,0,215,211,1,0,0,0,215,
        212,1,0,0,0,216,49,1,0,0,0,217,218,1,0,0,0,218,51,1,0,0,0,219,224,
        3,54,27,0,220,221,3,54,27,0,221,222,3,52,26,0,222,224,1,0,0,0,223,
        219,1,0,0,0,223,220,1,0,0,0,224,53,1,0,0,0,225,232,3,56,28,0,226,
        232,3,22,11,0,227,232,3,60,30,0,228,232,3,64,32,0,229,232,3,66,33,
        0,230,232,3,58,29,0,231,225,1,0,0,0,231,226,1,0,0,0,231,227,1,0,
        0,0,231,228,1,0,0,0,231,229,1,0,0,0,231,230,1,0,0,0,232,55,1,0,0,
        0,233,234,5,27,0,0,234,235,5,12,0,0,235,236,3,22,11,0,236,57,1,0,
        0,0,237,238,5,47,0,0,238,239,5,20,0,0,239,240,3,46,23,0,240,241,
        5,21,0,0,241,242,5,22,0,0,242,243,3,52,26,0,243,244,5,23,0,0,244,
        59,1,0,0,0,245,246,5,29,0,0,246,247,3,68,34,0,247,248,5,22,0,0,248,
        249,3,52,26,0,249,250,5,23,0,0,250,259,1,0,0,0,251,252,5,29,0,0,
        252,253,3,68,34,0,253,254,5,22,0,0,254,255,3,52,26,0,255,256,5,23,
        0,0,256,257,3,62,31,0,257,259,1,0,0,0,258,245,1,0,0,0,258,251,1,
        0,0,0,259,61,1,0,0,0,260,261,5,30,0,0,261,262,5,22,0,0,262,263,3,
        52,26,0,263,264,5,23,0,0,264,63,1,0,0,0,265,266,5,48,0,0,266,267,
        5,27,0,0,267,268,5,12,0,0,268,269,3,22,11,0,269,270,5,26,0,0,270,
        271,3,22,11,0,271,272,5,26,0,0,272,273,3,22,11,0,273,274,5,22,0,
        0,274,275,3,52,26,0,275,276,5,23,0,0,276,65,1,0,0,0,277,278,5,31,
        0,0,278,279,5,20,0,0,279,280,3,22,11,0,280,281,5,21,0,0,281,67,1,
        0,0,0,282,283,3,22,11,0,283,284,3,70,35,0,284,285,3,22,11,0,285,
        69,1,0,0,0,286,287,7,0,0,0,287,71,1,0,0,0,11,115,127,134,142,146,
        205,209,215,223,231,258
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'^'", "'='", 
                     "'<>'", "'<'", "'>'", "'<='", "'>='", "':='", "'!'", 
                     "','", "'sin'", "'cos'", "'log'", "'sqrt'", "'root'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "<INVALID>", 
                     "'func'", "'if'", "'else'", "'print'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MULTIPLICATION", "DIVISION", 
                      "POWER", "EQUALS", "NOT_EQUALS", "LESS_THAN", "GREATER_THAN", 
                      "LESS_THAN_EQUALS", "GREATER_THAN_EQUALS", "ASSIGNMENT", 
                      "FACTORIAL", "COMMA", "SIN", "COS", "LOG", "SQRT", 
                      "ROOT", "PAR_LEFT", "PAR_RIGHT", "BRACE_LEFT", "BRACE_RIGHT", 
                      "BRACKET_LEFT", "BRACKET_RIGHT", "SEMICOLON", "VARIABLE", 
                      "FUNC", "IF", "ELSE", "PRINT", "NUMBER", "MATRIX", 
                      "VECTOR", "BRACKET_OPEN", "BRACKET_CLOSE", "EXP", 
                      "ABS", "CEIL", "FLOOR", "ARCSIN", "ARCCOS", "ARCTAN", 
                      "SINH", "COSH", "MOD", "FUNCTION", "FOR" ]

    RULE_matmul = 0
    RULE_dot_product = 1
    RULE_sin = 2
    RULE_cos = 3
    RULE_sqrt = 4
    RULE_root = 5
    RULE_log = 6
    RULE_vector = 7
    RULE_matrix = 8
    RULE_trig_func = 9
    RULE_built_in_func = 10
    RULE_expression = 11
    RULE_exp_func = 12
    RULE_abs_func = 13
    RULE_ceil_func = 14
    RULE_floor_func = 15
    RULE_arcsin_func = 16
    RULE_arccos_func = 17
    RULE_arctan_func = 18
    RULE_sinh_func = 19
    RULE_cosh_func = 20
    RULE_factorial_func = 21
    RULE_modulo_op = 22
    RULE_params = 23
    RULE_param = 24
    RULE_empty = 25
    RULE_statements = 26
    RULE_statement = 27
    RULE_assignment_statement = 28
    RULE_func_statement = 29
    RULE_if_statement = 30
    RULE_else_statement = 31
    RULE_for_statement = 32
    RULE_print_statement = 33
    RULE_condition = 34
    RULE_logic_op = 35

    ruleNames =  [ "matmul", "dot_product", "sin", "cos", "sqrt", "root", 
                   "log", "vector", "matrix", "trig_func", "built_in_func", 
                   "expression", "exp_func", "abs_func", "ceil_func", "floor_func", 
                   "arcsin_func", "arccos_func", "arctan_func", "sinh_func", 
                   "cosh_func", "factorial_func", "modulo_op", "params", 
                   "param", "empty", "statements", "statement", "assignment_statement", 
                   "func_statement", "if_statement", "else_statement", "for_statement", 
                   "print_statement", "condition", "logic_op" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    MULTIPLICATION=3
    DIVISION=4
    POWER=5
    EQUALS=6
    NOT_EQUALS=7
    LESS_THAN=8
    GREATER_THAN=9
    LESS_THAN_EQUALS=10
    GREATER_THAN_EQUALS=11
    ASSIGNMENT=12
    FACTORIAL=13
    COMMA=14
    SIN=15
    COS=16
    LOG=17
    SQRT=18
    ROOT=19
    PAR_LEFT=20
    PAR_RIGHT=21
    BRACE_LEFT=22
    BRACE_RIGHT=23
    BRACKET_LEFT=24
    BRACKET_RIGHT=25
    SEMICOLON=26
    VARIABLE=27
    FUNC=28
    IF=29
    ELSE=30
    PRINT=31
    NUMBER=32
    MATRIX=33
    VECTOR=34
    BRACKET_OPEN=35
    BRACKET_CLOSE=36
    EXP=37
    ABS=38
    CEIL=39
    FLOOR=40
    ARCSIN=41
    ARCCOS=42
    ARCTAN=43
    SINH=44
    COSH=45
    MOD=46
    FUNCTION=47
    FOR=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MatmulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATRIX(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.MATRIX)
            else:
                return self.getToken(GrammarParser.MATRIX, i)

        def MULTIPLICATION(self):
            return self.getToken(GrammarParser.MULTIPLICATION, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_matmul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatmul" ):
                listener.enterMatmul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatmul" ):
                listener.exitMatmul(self)




    def matmul(self):

        localctx = GrammarParser.MatmulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_matmul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(GrammarParser.MATRIX)
            self.state = 73
            self.match(GrammarParser.MULTIPLICATION)
            self.state = 74
            self.match(GrammarParser.MATRIX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dot_productContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VECTOR(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.VECTOR)
            else:
                return self.getToken(GrammarParser.VECTOR, i)

        def MULTIPLICATION(self):
            return self.getToken(GrammarParser.MULTIPLICATION, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_dot_product

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDot_product" ):
                listener.enterDot_product(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDot_product" ):
                listener.exitDot_product(self)




    def dot_product(self):

        localctx = GrammarParser.Dot_productContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dot_product)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(GrammarParser.VECTOR)
            self.state = 77
            self.match(GrammarParser.MULTIPLICATION)
            self.state = 78
            self.match(GrammarParser.VECTOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIN(self):
            return self.getToken(GrammarParser.SIN, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_sin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSin" ):
                listener.enterSin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSin" ):
                listener.exitSin(self)




    def sin(self):

        localctx = GrammarParser.SinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(GrammarParser.SIN)
            self.state = 81
            self.match(GrammarParser.PAR_LEFT)
            self.state = 82
            self.expression()
            self.state = 83
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COS(self):
            return self.getToken(GrammarParser.COS, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_cos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCos" ):
                listener.enterCos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCos" ):
                listener.exitCos(self)




    def cos(self):

        localctx = GrammarParser.CosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(GrammarParser.COS)
            self.state = 86
            self.match(GrammarParser.PAR_LEFT)
            self.state = 87
            self.expression()
            self.state = 88
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SqrtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQRT(self):
            return self.getToken(GrammarParser.SQRT, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_sqrt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqrt" ):
                listener.enterSqrt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqrt" ):
                listener.exitSqrt(self)




    def sqrt(self):

        localctx = GrammarParser.SqrtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sqrt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(GrammarParser.SQRT)
            self.state = 91
            self.match(GrammarParser.PAR_LEFT)
            self.state = 92
            self.expression()
            self.state = 93
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROOT(self):
            return self.getToken(GrammarParser.ROOT, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = GrammarParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(GrammarParser.ROOT)
            self.state = 96
            self.match(GrammarParser.PAR_LEFT)
            self.state = 97
            self.expression()
            self.state = 98
            self.match(GrammarParser.COMMA)
            self.state = 99
            self.match(GrammarParser.NUMBER)
            self.state = 100
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOG(self):
            return self.getToken(GrammarParser.LOG, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_log

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog" ):
                listener.enterLog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog" ):
                listener.exitLog(self)




    def log(self):

        localctx = GrammarParser.LogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_log)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(GrammarParser.LOG)
            self.state = 103
            self.match(GrammarParser.PAR_LEFT)
            self.state = 104
            self.expression()
            self.state = 105
            self.match(GrammarParser.COMMA)
            self.state = 106
            self.match(GrammarParser.NUMBER)
            self.state = 107
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_OPEN(self):
            return self.getToken(GrammarParser.BRACKET_OPEN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def BRACKET_CLOSE(self):
            return self.getToken(GrammarParser.BRACKET_CLOSE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_vector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVector" ):
                listener.enterVector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVector" ):
                listener.exitVector(self)




    def vector(self):

        localctx = GrammarParser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(GrammarParser.BRACKET_OPEN)
            self.state = 110
            self.expression()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 111
                self.match(GrammarParser.COMMA)
                self.state = 112
                self.expression()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.match(GrammarParser.NUMBER)
            self.state = 119
            self.match(GrammarParser.BRACKET_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_OPEN(self):
            return self.getToken(GrammarParser.BRACKET_OPEN, 0)

        def vector(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.VectorContext)
            else:
                return self.getTypedRuleContext(GrammarParser.VectorContext,i)


        def BRACKET_CLOSE(self):
            return self.getToken(GrammarParser.BRACKET_CLOSE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_matrix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix" ):
                listener.enterMatrix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix" ):
                listener.exitMatrix(self)




    def matrix(self):

        localctx = GrammarParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(GrammarParser.BRACKET_OPEN)
            self.state = 122
            self.vector()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 123
                self.match(GrammarParser.COMMA)
                self.state = 124
                self.vector()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self.match(GrammarParser.BRACKET_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Trig_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sin(self):
            return self.getTypedRuleContext(GrammarParser.SinContext,0)


        def cos(self):
            return self.getTypedRuleContext(GrammarParser.CosContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_trig_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrig_func" ):
                listener.enterTrig_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrig_func" ):
                listener.exitTrig_func(self)




    def trig_func(self):

        localctx = GrammarParser.Trig_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_trig_func)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.sin()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.cos()
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


    class Built_in_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trig_func(self):
            return self.getTypedRuleContext(GrammarParser.Trig_funcContext,0)


        def sin(self):
            return self.getTypedRuleContext(GrammarParser.SinContext,0)


        def cos(self):
            return self.getTypedRuleContext(GrammarParser.CosContext,0)


        def sqrt(self):
            return self.getTypedRuleContext(GrammarParser.SqrtContext,0)


        def root(self):
            return self.getTypedRuleContext(GrammarParser.RootContext,0)


        def log(self):
            return self.getTypedRuleContext(GrammarParser.LogContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_built_in_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuilt_in_func" ):
                listener.enterBuilt_in_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuilt_in_func" ):
                listener.exitBuilt_in_func(self)




    def built_in_func(self):

        localctx = GrammarParser.Built_in_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_built_in_func)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.trig_func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.sin()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.cos()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.sqrt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                self.root()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 141
                self.log()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def built_in_func(self):
            return self.getTypedRuleContext(GrammarParser.Built_in_funcContext,0)


        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = GrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 18, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.built_in_func()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(GrammarParser.NUMBER)
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


    class Exp_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXP(self):
            return self.getToken(GrammarParser.EXP, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_exp_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_func" ):
                listener.enterExp_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_func" ):
                listener.exitExp_func(self)




    def exp_func(self):

        localctx = GrammarParser.Exp_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(GrammarParser.EXP)
            self.state = 149
            self.match(GrammarParser.PAR_LEFT)
            self.state = 150
            self.expression()
            self.state = 151
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Abs_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABS(self):
            return self.getToken(GrammarParser.ABS, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_abs_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbs_func" ):
                listener.enterAbs_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbs_func" ):
                listener.exitAbs_func(self)




    def abs_func(self):

        localctx = GrammarParser.Abs_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_abs_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(GrammarParser.ABS)
            self.state = 154
            self.match(GrammarParser.PAR_LEFT)
            self.state = 155
            self.expression()
            self.state = 156
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ceil_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CEIL(self):
            return self.getToken(GrammarParser.CEIL, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_ceil_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCeil_func" ):
                listener.enterCeil_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCeil_func" ):
                listener.exitCeil_func(self)




    def ceil_func(self):

        localctx = GrammarParser.Ceil_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ceil_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(GrammarParser.CEIL)
            self.state = 159
            self.match(GrammarParser.PAR_LEFT)
            self.state = 160
            self.expression()
            self.state = 161
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Floor_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOOR(self):
            return self.getToken(GrammarParser.FLOOR, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_floor_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloor_func" ):
                listener.enterFloor_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloor_func" ):
                listener.exitFloor_func(self)




    def floor_func(self):

        localctx = GrammarParser.Floor_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_floor_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(GrammarParser.FLOOR)
            self.state = 164
            self.match(GrammarParser.PAR_LEFT)
            self.state = 165
            self.expression()
            self.state = 166
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arcsin_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARCSIN(self):
            return self.getToken(GrammarParser.ARCSIN, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_arcsin_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArcsin_func" ):
                listener.enterArcsin_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArcsin_func" ):
                listener.exitArcsin_func(self)




    def arcsin_func(self):

        localctx = GrammarParser.Arcsin_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arcsin_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(GrammarParser.ARCSIN)
            self.state = 169
            self.match(GrammarParser.PAR_LEFT)
            self.state = 170
            self.expression()
            self.state = 171
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arccos_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARCCOS(self):
            return self.getToken(GrammarParser.ARCCOS, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_arccos_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArccos_func" ):
                listener.enterArccos_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArccos_func" ):
                listener.exitArccos_func(self)




    def arccos_func(self):

        localctx = GrammarParser.Arccos_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arccos_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(GrammarParser.ARCCOS)
            self.state = 174
            self.match(GrammarParser.PAR_LEFT)
            self.state = 175
            self.expression()
            self.state = 176
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arctan_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARCTAN(self):
            return self.getToken(GrammarParser.ARCTAN, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_arctan_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArctan_func" ):
                listener.enterArctan_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArctan_func" ):
                listener.exitArctan_func(self)




    def arctan_func(self):

        localctx = GrammarParser.Arctan_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arctan_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(GrammarParser.ARCTAN)
            self.state = 179
            self.match(GrammarParser.PAR_LEFT)
            self.state = 180
            self.expression()
            self.state = 181
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sinh_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINH(self):
            return self.getToken(GrammarParser.SINH, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_sinh_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinh_func" ):
                listener.enterSinh_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinh_func" ):
                listener.exitSinh_func(self)




    def sinh_func(self):

        localctx = GrammarParser.Sinh_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_sinh_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(GrammarParser.SINH)
            self.state = 184
            self.match(GrammarParser.PAR_LEFT)
            self.state = 185
            self.expression()
            self.state = 186
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cosh_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COSH(self):
            return self.getToken(GrammarParser.COSH, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_cosh_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosh_func" ):
                listener.enterCosh_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosh_func" ):
                listener.exitCosh_func(self)




    def cosh_func(self):

        localctx = GrammarParser.Cosh_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_cosh_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(GrammarParser.COSH)
            self.state = 189
            self.match(GrammarParser.PAR_LEFT)
            self.state = 190
            self.expression()
            self.state = 191
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factorial_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def FACTORIAL(self):
            return self.getToken(GrammarParser.FACTORIAL, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_factorial_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorial_func" ):
                listener.enterFactorial_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorial_func" ):
                listener.exitFactorial_func(self)




    def factorial_func(self):

        localctx = GrammarParser.Factorial_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factorial_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.expression()
            self.state = 194
            self.match(GrammarParser.FACTORIAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Modulo_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def MOD(self):
            return self.getToken(GrammarParser.MOD, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_modulo_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModulo_op" ):
                listener.enterModulo_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModulo_op" ):
                listener.exitModulo_op(self)




    def modulo_op(self):

        localctx = GrammarParser.Modulo_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_modulo_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.expression()
            self.state = 197
            self.match(GrammarParser.MOD)
            self.state = 198
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ParamContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def empty(self):
            return self.getTypedRuleContext(GrammarParser.EmptyContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = GrammarParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.param()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 201
                    self.match(GrammarParser.COMMA)
                    self.state = 202
                    self.param()
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.empty()
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


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(GrammarParser.VARIABLE, 0)

        def ASSIGNMENT(self):
            return self.getToken(GrammarParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = GrammarParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_param)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(GrammarParser.VARIABLE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(GrammarParser.VARIABLE)
                self.state = 213
                self.match(GrammarParser.ASSIGNMENT)
                self.state = 214
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_empty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)




    def empty(self):

        localctx = GrammarParser.EmptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_empty)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(GrammarParser.StatementsContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = GrammarParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_statements)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.statement()
                self.state = 221
                self.statements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_statement(self):
            return self.getTypedRuleContext(GrammarParser.Assignment_statementContext,0)


        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(GrammarParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(GrammarParser.For_statementContext,0)


        def print_statement(self):
            return self.getTypedRuleContext(GrammarParser.Print_statementContext,0)


        def func_statement(self):
            return self.getTypedRuleContext(GrammarParser.Func_statementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statement)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.assignment_statement()
                pass
            elif token in [15, 16, 17, 18, 19, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.expression()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.if_statement()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.for_statement()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                self.print_statement()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 6)
                self.state = 230
                self.func_statement()
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


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(GrammarParser.VARIABLE, 0)

        def ASSIGNMENT(self):
            return self.getToken(GrammarParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_assignment_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_statement" ):
                listener.enterAssignment_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_statement" ):
                listener.exitAssignment_statement(self)




    def assignment_statement(self):

        localctx = GrammarParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(GrammarParser.VARIABLE)
            self.state = 234
            self.match(GrammarParser.ASSIGNMENT)
            self.state = 235
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(GrammarParser.FUNCTION, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def params(self):
            return self.getTypedRuleContext(GrammarParser.ParamsContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def BRACE_LEFT(self):
            return self.getToken(GrammarParser.BRACE_LEFT, 0)

        def statements(self):
            return self.getTypedRuleContext(GrammarParser.StatementsContext,0)


        def BRACE_RIGHT(self):
            return self.getToken(GrammarParser.BRACE_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_func_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_statement" ):
                listener.enterFunc_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_statement" ):
                listener.exitFunc_statement(self)




    def func_statement(self):

        localctx = GrammarParser.Func_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(GrammarParser.FUNCTION)
            self.state = 238
            self.match(GrammarParser.PAR_LEFT)
            self.state = 239
            self.params()
            self.state = 240
            self.match(GrammarParser.PAR_RIGHT)
            self.state = 241
            self.match(GrammarParser.BRACE_LEFT)
            self.state = 242
            self.statements()
            self.state = 243
            self.match(GrammarParser.BRACE_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GrammarParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(GrammarParser.ConditionContext,0)


        def BRACE_LEFT(self):
            return self.getToken(GrammarParser.BRACE_LEFT, 0)

        def statements(self):
            return self.getTypedRuleContext(GrammarParser.StatementsContext,0)


        def BRACE_RIGHT(self):
            return self.getToken(GrammarParser.BRACE_RIGHT, 0)

        def else_statement(self):
            return self.getTypedRuleContext(GrammarParser.Else_statementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = GrammarParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_if_statement)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(GrammarParser.IF)
                self.state = 246
                self.condition()
                self.state = 247
                self.match(GrammarParser.BRACE_LEFT)
                self.state = 248
                self.statements()
                self.state = 249
                self.match(GrammarParser.BRACE_RIGHT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(GrammarParser.IF)
                self.state = 252
                self.condition()
                self.state = 253
                self.match(GrammarParser.BRACE_LEFT)
                self.state = 254
                self.statements()
                self.state = 255
                self.match(GrammarParser.BRACE_RIGHT)
                self.state = 256
                self.else_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(GrammarParser.ELSE, 0)

        def BRACE_LEFT(self):
            return self.getToken(GrammarParser.BRACE_LEFT, 0)

        def statements(self):
            return self.getTypedRuleContext(GrammarParser.StatementsContext,0)


        def BRACE_RIGHT(self):
            return self.getToken(GrammarParser.BRACE_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)




    def else_statement(self):

        localctx = GrammarParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(GrammarParser.ELSE)
            self.state = 261
            self.match(GrammarParser.BRACE_LEFT)
            self.state = 262
            self.statements()
            self.state = 263
            self.match(GrammarParser.BRACE_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GrammarParser.FOR, 0)

        def VARIABLE(self):
            return self.getToken(GrammarParser.VARIABLE, 0)

        def ASSIGNMENT(self):
            return self.getToken(GrammarParser.ASSIGNMENT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMICOLON)
            else:
                return self.getToken(GrammarParser.SEMICOLON, i)

        def BRACE_LEFT(self):
            return self.getToken(GrammarParser.BRACE_LEFT, 0)

        def statements(self):
            return self.getTypedRuleContext(GrammarParser.StatementsContext,0)


        def BRACE_RIGHT(self):
            return self.getToken(GrammarParser.BRACE_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)




    def for_statement(self):

        localctx = GrammarParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(GrammarParser.FOR)
            self.state = 266
            self.match(GrammarParser.VARIABLE)
            self.state = 267
            self.match(GrammarParser.ASSIGNMENT)
            self.state = 268
            self.expression()
            self.state = 269
            self.match(GrammarParser.SEMICOLON)
            self.state = 270
            self.expression()
            self.state = 271
            self.match(GrammarParser.SEMICOLON)
            self.state = 272
            self.expression()
            self.state = 273
            self.match(GrammarParser.BRACE_LEFT)
            self.state = 274
            self.statements()
            self.state = 275
            self.match(GrammarParser.BRACE_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(GrammarParser.PRINT, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_print_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_statement" ):
                listener.enterPrint_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_statement" ):
                listener.exitPrint_statement(self)




    def print_statement(self):

        localctx = GrammarParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(GrammarParser.PRINT)
            self.state = 278
            self.match(GrammarParser.PAR_LEFT)
            self.state = 279
            self.expression()
            self.state = 280
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def logic_op(self):
            return self.getTypedRuleContext(GrammarParser.Logic_opContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = GrammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.expression()
            self.state = 283
            self.logic_op()
            self.state = 284
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(GrammarParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(GrammarParser.NOT_EQUALS, 0)

        def LESS_THAN(self):
            return self.getToken(GrammarParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(GrammarParser.GREATER_THAN, 0)

        def LESS_THAN_EQUALS(self):
            return self.getToken(GrammarParser.LESS_THAN_EQUALS, 0)

        def GREATER_THAN_EQUALS(self):
            return self.getToken(GrammarParser.GREATER_THAN_EQUALS, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_logic_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_op" ):
                listener.enterLogic_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_op" ):
                listener.exitLogic_op(self)




    def logic_op(self):

        localctx = GrammarParser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





