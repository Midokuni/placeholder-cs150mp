import ply.lex as lex
import sys

reserved = {
  'sizeof' : 'SIZEOF',
  'if' : 'IF',
  'else' : 'ELSE',
  'while' : 'WHILE',
  'return' : 'RETURN',
  'println' : 'PRINTLN',
  'print' : 'PRINT',
}

# List of token names.   This is always required
tokens = ['DELIMIT','STRING','QUOTE','NUMBER','ADD','SUB','MUL','DIV','LPAREN','RPAREN','POWER','LBRACKET','RBRACKET','MOD','EQUAL','NOT_EQUAL','LESS','GREATER','LESS_EQUAL','GREATER_EQUAL','NOT','LBRACE','RBRACE','ASSIGN','VARIABLE','COLON'] + list(reserved.values())

# Regular expression rules for simple tokens
t_ADD    = r'\+'
t_SUB   = r'-'
t_MUL  = r'\*'
t_DIV  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_POWER   = r'\^'
t_LBRACKET= r'\['
t_RBRACKET= r'\]'
t_MOD     = r'\%'
t_EQUAL   = r'\=\='
t_NOT_EQUAL = r'\!\='
t_LESS    = r'\<'
t_GREATER = r'\>'
t_LESS_EQUAL = r'\<\='
t_GREATER_EQUAL = r'\>\='
t_NOT = r'\!'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'\='
t_COLON = r':'
t_NUMBER = r'[0-9]+([\.][0-9]+)?'
t_QUOTE = r'\"'
t_DELIMIT = r'\n'

# A regular expression rule with some action code
# def t_NUMBER(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t

# Define a rule so we can track line numbers
# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)
#     return t

def t_VARIABLE(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  t.type = reserved.get(t.value,'VARIABLE')
  return t
def t_STRING(t):
  r'"(\.|[^\"])*"'
  return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
test = 0
while (test < 10){
  if (test % 2 == 0){
    println("Hello world")
  }
  test = test + 1
}
println(test)
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
