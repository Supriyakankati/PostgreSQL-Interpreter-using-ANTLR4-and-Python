grammar Postgres;

// Parser Rules
prog: statement* EOF;

statement
    : create_stmt SEMI
    | insert_stmt SEMI
    | select_stmt SEMI
    ;

create_stmt : CREATE TABLE table_name '(' column_definition_list (',' table_constraint)* ')';

select_stmt : SELECT select_columns FROM table_name where_clause?;

select_columns : '*' | column_name_list;

where_clause : WHERE condition;

condition : expression (AND|OR) expression
          | expression;

expression : column_name '=' value
           | column_name '!=' value
           | column_name '>' value
           | column_name '<' value
           | column_name '>=' value
           | column_name '<=' value;

insert_stmt : INSERT INTO table_name insert_columns_and_values;

insert_columns_and_values
    : insert_columns VALUES insert_values
    | VALUES insert_values
    ;

insert_columns         : '(' column_name_list ')';
insert_values          : '(' value_list ')' (',' '(' value_list ')')*;

value_list             : value (',' value)*;

table_name             : IDENTIFIER;
column_definition_list : column_definition (',' column_definition)*;
column_definition      : column_name data_type (column_constraint)*;

column_name            : IDENTIFIER;
data_type              : basic_type | character_string_type | numeric_type | date_time_type | boolean_type | serial_type;

// Basic Data Types
basic_type             : INT | INTEGER | SMALLINT | BIGINT | REAL | DOUBLE | TEXT;

// Character String Types
character_string_type  : CHAR '(' NUMERIC_LITERAL ')'
                        | VARCHAR '(' NUMERIC_LITERAL ')'
                        | TEXT;

// Numeric Types
numeric_type           : NUMERIC '(' NUMERIC_LITERAL ',' NUMERIC_LITERAL ')'
                        | DECIMAL '(' NUMERIC_LITERAL ',' NUMERIC_LITERAL ')';

// Date and Time Types
date_time_type         : DATE | TIME | TIMESTAMP;

// Boolean Type
boolean_type           : BOOLEAN;

// Serial Type for auto-incremented fields
serial_type            : SERIAL;

column_constraint      : PRIMARY KEY | NOT NULL | UNIQUE;
table_constraint       : (CONSTRAINT IDENTIFIER)? (primary_key_constraint | unique_constraint);

primary_key_constraint : PRIMARY KEY '(' column_name_list ')';
unique_constraint      : UNIQUE '(' column_name_list ')';

column_name_list       : IDENTIFIER (',' IDENTIFIER)*;

value                  : literal;

literal                : STRING_LITERAL | NUMERIC_LITERAL | NULL | BOOLEAN_LITERAL | DATE_LITERAL;

// Lexer Rules
CREATE                : [C|c][R|r][E|e][A|a][T|t][E|e];
TABLE                 : [T|t][A|a][B|b][L|l][E|e];
SELECT                : [S|s][E|e][L|l][E|e][C|c][T|t];
FROM                  : [F|f][R|r][O|o][M|m];
WHERE                 : [W|w][H|h][E|e][R|r][E|e];
AND                   : [A|a][N|n][D|d];
OR                    : [O|o][R|r];
INSERT                : [I|i][N|n][S|s][E|e][R|r][T|t];
INTO                  : [I|i][N|n][T|t][O|o];
VALUES                : [V|v][A|a][L|l][U|u][E|e][S|s];
CONSTRAINT            : [C|c][O|o][N|n][S|s][T|t][R|r][A|a][I|i][N|n][T|t];
PRIMARY               : [P|p][R|r][I|i][M|m][A|a][R|r][Y|y];
KEY                   : [K|k][E|e][Y|y];
UNIQUE                : [U|u][N|n][I|i][Q|q][U|u][E|e];
NOT                   : [N|n][O|o][T|t];
NULL                  : [N|n][U|u][L|l][L|l];

// Data Types
INT                   : [I|i][N|n][T|t];
INTEGER               : [I|i][N|n][T|t][E|e][G|g][E|e][R|r];
SMALLINT              : [S|s][M|m][A|a][L|l][L|l][I|i][N|n][T|t];
BIGINT                : [B|b][I|i][G|g][I|i][N|n][T|t];
REAL                  : [R|r][E|e][A|a][L|l];
DOUBLE                : [D|d][O|o][U|u][B|b][L|l][E|e];
TEXT                  : [T|t][E|e][X|x][T|t];
CHAR                  : [C|c][H|h][A|a][R|r];
VARCHAR               : [V|v][A|a][R|r][C|c][H|h][A|a][R|r];
NUMERIC               : [N|n][U|u][M|m][E|e][R|r][I|i][C|c];
DECIMAL               : [D|d][E|e][C|c][I|i][M|m][A|a][L|l];
DATE                  : [D|d][A|a][T|t][E|e];
TIME                  : [T|t][I|i][M|m][E|e];
TIMESTAMP             : [T|t][I|i][M|m][E|e][S|s][T|t][A|a][M|m][P|p];
BOOLEAN               : [B|b][O|o][O|o][L|l][E|e][A|a][N|n];
SERIAL                : [S|s][E|e][R|r][I|i][A|a][L|l];

// Identifier and Literals
IDENTIFIER            : [a-zA-Z_][a-zA-Z0-9_]*;
NUMERIC_LITERAL       : [0-9]+;
STRING_LITERAL        : '\'' ('\'\'' | ~'\'')* '\''; // Handles escaping of single quotes
BOOLEAN_LITERAL       : [T|t][R|r][U|u][E|e] | [F|f][A|a][L|l][S|s][E|e];
DATE_LITERAL          : '\'' [0-9]{4} '-' [0-9]{2} '-' [0-9]{2} '\''; // Basic date format 'YYYY-MM-DD'

// Lexer Rules
SEMI                  : ';'+;
LINE_COMMENT          : '--' ~[\r\n]* -> skip;
BLOCK_COMMENT         : '/*' .*? '*/' -> skip;
WS                    : [ \t\r\n]+ -> skip;
