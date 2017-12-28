import ply.yacc as yacc
from langlex import tokens

def p_start(p):
	'''start : externaldeclarationrep'''
	p[0] = p[1]

def p_externaldeclarationrep(p):
	'''externaldeclarationrep : 
								| externaldeclarationrep externaldeclaration'''
	if (len(p) == 2):
		p[0] = p[1]
	#else:

def p_externaldeclaration(p):
	'''externaldeclaration : functiondefinition
							| declaration'''
	p[0] = p[1]

def p_functiondefinition(p):
	'''functiondefinition : declarator declarationrep compoundstatement'''

def p_declarationrep(p):
	'''declarationrep : 
						| declarationrep declaration'''

def p_declarator(p):
	'''declarator : directdeclarator'''
	p[0] = p[1]

def p_directdeclarator(p):
	'''directdeclarator : VARIABLE
						| LPAREN declarator RPAREN
						| directdeclarator LBRACKET constantexpression RBRACKET
						| directdeclarator LBRACKET RBRACKET
						| directdeclarator LPAREN parametertypelist RPAREN
						| directdeclarator LPAREN identifierrep RPAREN'''

def p_identifierrep(p):
	'''identifierrep : 
					 | identifierrep VARIABLE'''

def p_constantexpression(p):
	'''constantexpression : conditionalexpression'''
	p[0] = p[1]

def p_conditionalexpression(p):
	'''conditionalexpression : logicalor'''
	p[0] = p[1]

def p_logicalor(p):
	'''logicalor : logicaland
				 | logicalor OR logicaland'''
	if (len(p) == 2):
		p[0] = p[1]
	#else:

def p_logicaland(p):
	'''logicaland : equality
				  | logicaland AND equality'''
	if (len(p) == 2):
		p[0] = p[1]

def p_equality(p):
	'''equality : relational
				| equality EQUAL relational
				| equality NOT_EQUAL relational'''
	if (len(p) == 2):
		p[0] = p[1]

def p_relational(p):
	'''relational : additive
				  | relational LESS additive
				  | relational GREATER additive
				  | relational LESS_EQUAL additive
				  | relational GREATER_EQUAL additive'''
	if (len(p) == 2):
		p[0] = p[1]

def p_additive(p):
	'''additive : multiplicative
				| additive ADD multiplicative
				| additive SUB multiplicative'''
	if (len(p) == 2):
		p[0] = p[1]

def p_multiplicative(p):
	'''multiplicative : unaryexpression
					  | multiplicative MUL unaryexpression
					  | multiplicative DIV unaryexpression
					  | multiplicative MOD unaryexpression'''
	if (len(p) == 2):
		p[0] = p[1]

def p_unaryexpression(p):
	'''unaryexpression : postfixexpression
					   | SIZEOF unaryexpression'''
	if (len(p) == 2):
		p[0] = p[1]

def p_postfixexpression(p):
	'''postfixexpression : primaryexpression'''
#					   	 | postfixexpression LBRACKET expression RBRACKET
#					   	 | postfixexpression LPAREN assignmentrep RPAREN'''
	if (len(p) == 2):
		p[0] = p[1]

# def p_assignmentrep(p):
# 	'''assignmentrep : 
#					 | assignmentrep assignment'''

def p_primaryexpression(p):
	'''primaryexpression : VARIABLE
						 | FLOAT
						 | INT
						 | STRING
						 | LPAREN expression RPAREN'''

# def p_expression(p):
# 	'''expression : assignmentexpression
# 				  | expression COMMA assignmentexpression'''

# def p_assignmentexpression(p):
# 	'''assignmentexpression : conditionalexpression
# 							| unaryexpression ASSIGN assignmentexpression'''




#def p_multiplicative"


def file_main():
	parser = yacc.yacc()
	f = open('test.code')
	result = parser.parse(f)
	return result
