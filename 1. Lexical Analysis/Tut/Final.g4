lexer grammar Final;

fragment LOWERCASE_LETTER   :  [a-z] ;
fragment DIGIT              :  [0-9] ;
fragment SIGN               :  [+-]? ;
fragment SCIENTIFIC         :  [e](SIGN)(DIGIT)+ ;
fragment DECIMAL_POINT      :  [.](DIGIT)+ ;
fragment EXP                : [Ee][+-]?[0-9]+;


REAL               :  [0-9]+'.'([0-9]+)?EXP?|[0-9]+EXP|([0-9]+)?'.'[0-9]+EXP?;
ID                 :  LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT)* ;
STRING             :  '\''(~'\''|('\'\''))+'\'';

WS                 :  [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines