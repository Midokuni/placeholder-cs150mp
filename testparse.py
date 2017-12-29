import ply.yacc as yacc
from langlex import tokens

names = {"TESTICS":69}

def p_start(p):
	'''start : statement
			 | start statement'''
	p[0] = p[1]

def p_statement(p):
	'''statement : conditional DELIMIT'''
	p[0] = p[1]

def p_conditional(p):
	'''conditional : additive 
				   | IF LPAREN literal LESS literal RPAREN'''
	if (len(p) == 2):
		p[0] = p[1]
	else:
		if (p[3] < p[5]):
			print("LESS\n")
		else:
			print("GREATER\n")

def p_additive(p):
	'''additive : multiplicative
				| additive ADD multiplicative
				| additive SUB multiplicative'''
	if (len(p) == 2):
		p[0] = p[1]
	elif(p[2] == '+'):
		p[0] = p[1] + p[3]
	elif(p[2] == '-'):
		p[0] = p[1] - p[3]

def p_multiplicative(p):
	'''multiplicative : literal
					  | multiplicative MUL literal
					  | multiplicative DIV literal
					  | multiplicative MOD literal'''
	if (len(p) == 2):
		p[0] = p[1]
	elif(p[2] == '*'):
		p[0] = p[1] * p[3]
	elif(p[2] == '/'):
		p[0] = p[1] / p[3]
	elif(p[2] == '%'):
		p[0] = p[1] % p[3]

def p_literal(p):
	'''literal : identifier
				  | FLOAT
				  | INT
				  | STRING
				  | LPAREN additive RPAREN'''
	if (len(p) == 2):
		p[0] = p[1]
	else:
		p[0] = p[2]

def p_identifier(p):
	'''identifier : VARIABLE'''
	if (p[1] in names):
		p[0] = names[p[1]]
	else:
		print("ID NOT DER BOI")
		exit()


def file_main():
	parser = yacc.yacc()
	f = open("test.code")
	text = f.read()
	print (text)
	result = parser.parse(text, debug=1)
	print(result)
	f.close()

file_main()
