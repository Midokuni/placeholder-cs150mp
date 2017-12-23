import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'ADD',
   'SUB',
   'MUL',
   'DIV',
   'LPAREN',
   'RPAREN',
   'POWER',
   'LBRACKET',
   'RBRACKET',
   'SIZEOF',
   'MOD',
   'EQUAL',
   'NOT_EQUAL',
   'LESS',
   'GREATER',
   'LESS_EQUAL',
   'GREATER_EQUAL',
   'NOT',
   'IF',
   'ELSE',
   'WHILE',
   'RETURN',
   'LBRACE',
   'RBRACE',
   'ASSIGN',
   'VARIABLE',
)

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
t_SIZEOF    = "sizeof"
t_IF = "if"
t_ELSE = "else"
t_WHILE = "while"
t_RETURN = "return"
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)




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
if (app_le <= 14){
  14 = 13
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)