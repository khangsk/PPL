// my ID: 1812535

grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : var_declare* func_declare* EOF ;
// GLOBAL VARIABLE
var_declare: VAR COLON list_var (COMMA list_var)* SEMI ;

list_var: variable (EQUAL literal)? ;

func_declare: FUNCTION COLON ID params_list? compound_stmt;

list_variable: variable (COMMA variable)* ;

variable: ID (LSB INT RSB)* ;

params_list: PARAMETER COLON list_variable ;

 //Array
array: LCB (literal (COMMA literal)*)? RCB ;

literal:  INT | FLOAT | BOOLEAN | STRING | array;

compound_stmt: BODY COLON var_declare* stmt* ENDBODY DOT ;

// STATEMENTS
stmt
    : assign_stmt
    | if_stmt
    | for_stmt
    | while_stmt
    | do_while_stmt
    | break_stmt
    | continue_stmt
    | call_stmt
    | return_stmt
    ;

assign_stmt: (ID | index_exp ) EQUAL exp SEMI ;

if_stmt: IF exp THEN var_declare* stmt* (ELSEIF exp THEN var_declare* stmt*)* (ELSE var_declare* stmt*)? ENDIF DOT ;

for_stmt: FOR LP ID EQUAL exp COMMA exp COMMA exp RP DO var_declare* stmt* ENDFOR DOT ;

while_stmt: WHILE exp DO var_declare* stmt* ENDWHILE DOT ;

do_while_stmt: DO var_declare* stmt* WHILE exp ENDDO DOT ;

break_stmt: BREAK SEMI ;

continue_stmt: CONTINUE SEMI ;

call_stmt: call_exp SEMI ;

return_stmt: RETURN exp? SEMI ;

call_exp: ID LP exps_list? RP ;



exps_list: exp (COMMA exp)* ;

exp: exp1 (EQU | NQU | LT | GT | LTE | GTE | NOT_EQUAL | LT_DOT | GT_DOT | LTE_DOT | GTE_DOT) exp1 | exp1 ;

exp1: exp1 (AND | OR) exp2 | exp2;

exp2: exp2 (ADD | ADD_DOT | SUB | SUB_DOT) exp3 | exp3;

exp3: exp3 (MUL | MUL_DOT | DIV | DIV_DOT | MOD) exp4 | exp4 ;

exp4: FACT exp4 | exp5 ;

exp5: (SUB | SUB_DOT) exp5 | exp6 ;

exp6: exp6 LSB exp RSB | exp7 ;

exp7: call_exp | operands ;

operands
    : literal
    | ID
    | call_exp
    | LP exp RP
    | operands LSB exp RSB
    ;

index_exp: operands LSB exp RSB ;

//IDENTIFIERS
ID: LOWER_CHAR (LOWER_CHAR | UPPER_CHAR | DIGIT | DASH)* ;
// LITERALS
 // Integer
INT: '0' | ([1-9] DIGIT*) | ('0' X [1-9A-F][0-9A-F]*) | ('0' O [1-7][0-7]*)  ;

 // Float
FLOAT: DIGIT+ (DECIMAL_PART? EXPONENT_PART | DECIMAL_PART EXPONENT_PART?) ;

 // Boolean
BOOLEAN: TRUE | FALSE ;

 // String
STRING: '"' (STR_CHAR)* '"'
    {
		s = str(self.text)
		self.text = s[1:-1]
	}
	;

// KEYWORDS
BODY: 'Body' ;
BREAK: 'Break' ;
CONTINUE: 'Continue' ;
DO: 'Do' ;
ELSE: 'Else' ;
ELSEIF: 'ElseIf' ;
ENDBODY: 'EndBody' ;
ENDIF: 'EndIf' ;
ENDFOR: 'EndFor' ;
ENDWHILE: 'EndWhile' ;
FOR: 'For' ;
FUNCTION: 'Function' ;
IF: 'If' ;
PARAMETER: 'Parameter' ;
RETURN: 'Return' ;
THEN: 'Then' ;
VAR: 'Var' ;
WHILE: 'While' ;
fragment TRUE: 'True' ;
fragment FALSE: 'False' ;
ENDDO: 'EndDo' ;

// OPERATORS
ADD: '+' ;
ADD_DOT: '+.' ;
SUB: '-' ;
SUB_DOT: '-.' ;
MUL: '*' ;
MUL_DOT: '*.' ;
DIV: '\\' ;
DIV_DOT: '\\.' ;
MOD: '%' ;
FACT: '!' ;
AND: '&&' ;
OR: '||' ;
EQU: '==' ;
NQU: '!=' ;
LT : '<' ;
GT : '>' ;
LTE: '<=' ;
GTE: '>=' ;
LT_DOT: '<.' ;
GT_DOT : '>.' ;
LTE_DOT: '<=.' ;
GTE_DOT: '>=.' ;
NOT_EQUAL: '=/=' ;
EQUAL: '=' ;

// SEPARATORS

LP: '(' ; 
RP: ')' ; 
LSB: '[' ; 
RSB: ']' ; 
COLON: ':' ; 
DOT: '.' ;
COMMA: ',' ; 
SEMI: ';' ; 
LCB: '{' ;
RCB: '}' ; 

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

COMMENT: '**' .*? '**' -> skip ; // skip comments

fragment DIGIT: [0-9] ;
fragment UPPER_CHAR: [A-Z] ;
fragment LOWER_CHAR: [a-z] ;
fragment DASH: '_' ;
fragment X: [xX] ;
fragment O: [oO] ;
fragment E: [eE] ;
fragment SIGN: [+-] ;
fragment DECIMAL_PART: DOT DIGIT* ;
fragment EXPONENT_PART: E SIGN? DIGIT+ ;
fragment STR_CHAR: ~[\n\r'\\"] | ESC_SEQ | '\'"' ;
fragment ESC_SEQ: '\\' [btnfr'\\] ;
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | '\''~["];

UNCLOSE_STRING: '"'STR_CHAR* ( [\n\r] | EOF)
    {
		s = str(self.text)
		if s[-1] in ['\n', '\r']:
			raise UncloseString(s[1:-1])
		else:
			raise UncloseString(s[1:])
	}
	;

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
    {
		s = str(self.text)
		raise IllegalEscape(s[1:])
	}
	;

UNTERMINATED_COMMENT: '**' .*?
    {
        raise UnterminatedComment()
    }
    ;

ERROR_CHAR: .
    {
		raise ErrorToken(self.text)
	}
	;

