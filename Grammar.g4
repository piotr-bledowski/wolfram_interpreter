grammar Grammar;

program: statements+EOF;

matmul: MATRIX MULTIPLICATION MATRIX;
dot_product: VECTOR MULTIPLICATION VECTOR;

sin: SIN PAR_LEFT expression PAR_RIGHT;
cos: COS PAR_LEFT expression PAR_RIGHT;
sqrt: SQRT PAR_LEFT expression PAR_RIGHT;
root: ROOT PAR_LEFT expression COMMA NUMBER PAR_RIGHT;
log: LOG PAR_LEFT expression COMMA NUMBER PAR_RIGHT;

vector: BRACKET_OPEN expression (COMMA expression)* NUMBER BRACKET_CLOSE;
matrix: BRACKET_OPEN vector (COMMA vector)* BRACKET_CLOSE;

trig_func: sin | cos;

built_in_func: trig_func | sin | cos | sqrt | root | log;

expression: built_in_func | NUMBER;/* | expression (() built_in_func | NUMBER | expression)*;*/

exp_func: EXP PAR_LEFT expression PAR_RIGHT;
abs_func: ABS PAR_LEFT expression PAR_RIGHT;
ceil_func: CEIL PAR_LEFT expression PAR_RIGHT;
floor_func: FLOOR PAR_LEFT expression PAR_RIGHT;

arcsin_func: ARCSIN PAR_LEFT expression PAR_RIGHT;
arccos_func: ARCCOS PAR_LEFT expression PAR_RIGHT;
arctan_func: ARCTAN PAR_LEFT expression PAR_RIGHT;

sinh_func: SINH PAR_LEFT expression PAR_RIGHT;
cosh_func: COSH PAR_LEFT expression PAR_RIGHT;

factorial_func: expression FACTORIAL;
modulo_op: expression MOD expression;

params: param (COMMA param)* | empty;
param: VARIABLE | VARIABLE ASSIGNMENT expression;
empty: ;
statements: statement | statement statements;
statement: assignment_statement | expression | if_statement | for_statement | print_statement | func_statement;

assignment_statement: VARIABLE ASSIGNMENT expression;
func_statement: FUNCTION PAR_LEFT params PAR_RIGHT BRACE_LEFT statements BRACE_RIGHT;
if_statement: IF condition BRACE_LEFT statements BRACE_RIGHT | IF condition BRACE_LEFT statements BRACE_RIGHT else_statement;
else_statement: ELSE BRACE_LEFT statements BRACE_RIGHT;
for_statement: FOR VARIABLE ASSIGNMENT expression SEMICOLON expression SEMICOLON expression BRACE_LEFT statements BRACE_RIGHT;
print_statement: PRINT PAR_LEFT expression PAR_RIGHT;

condition: expression logic_op expression;

logic_op: EQUALS | NOT_EQUALS | LESS_THAN | GREATER_THAN | LESS_THAN_EQUALS | GREATER_THAN_EQUALS;

PLUS: '+';
MINUS: '-';
MULTIPLICATION: '*';
DIVISION: '/';
POWER: '^';
EQUALS: '=';
NOT_EQUALS: '<>';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_EQUALS: '<=';
GREATER_THAN_EQUALS: '>=';
ASSIGNMENT: ':=';
FACTORIAL: '!';
COMMA: ',';

SIN: 'sin';
COS: 'cos';
LOG: 'log';
SQRT: 'sqrt';
ROOT: 'root';

PAR_LEFT: '(';
PAR_RIGHT: ')';
BRACE_LEFT: '{';
BRACE_RIGHT: '}';
BRACKET_LEFT: '[';
BRACKET_RIGHT: ']';
SEMICOLON: ';';

VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;
FUNC: 'func';
IF: 'if';
ELSE: 'else';
PRINT: 'print';

NUMBER: [0-9].?[0-9]*;
