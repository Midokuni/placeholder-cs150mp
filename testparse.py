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
				   | IF LPAREN logicalor RPAREN'''
	p[0] = p[1]

def p_logicalor(p):
	'''logicalor : logicaland
				 | logicalor OR logicaland'''
	if (len(p) == 2):
		p[0] = p[1]
	else:
		if(p[1] or p[3]):
			print("TRUE")
		else:
			print("FALSE")

def p_logicaland(p):
	'''logicaland : equality
				 | logicaland OR equality'''
	if (len(p) == 2):
		p[0] = p[1]
	else:
		if(p[1] and p[3]):
			print("TRUE")
		else:
			print("FALSE")

def p_equality(p):
	'''equality : relational
				| equality EQUAL relational
				| equality NOT_EQUAL relational'''
	if (len(p) == 2):
		p[0] = p[1]
	else:
		if (p[2] == "=="):
			if(p[1] == p[3]):
				print("TRUE")
			else:
				print("FALSE")	
		elif (p[2] == "!="):
			if(p[1] != p[3]):
				print("TRUE")
			else:
				print("FALSE")

def p_relational(p):
	'''relational : additive 
				   | relational LESS additive
				   | relational GREATER additive
				   | relational LESS_EQUAL additive
				   | relational GREATER_EQUAL additive'''
	if (len(p) == 2):
		p[0] = p[1]
	else:
		if (p[2] == '<'):
			if (p[1] < p[3]):
				print("LESS")
			else:
				print("GREATER")
		elif (p[2] == '>'):
			if (p[1] > p[3]):
				print("GREATER")
			else:
				print("LESS")
		elif (p[2] == "<="):
			if (p[1] <= p[3]):
				print("LESS OR EQUAL")
			else:
				print("GREATER")
		elif (p[2] == ">="):
			if (p[1] >= p[3]):
				print("GREATER OR EQUAL")
			else:
				print("LESS")

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
