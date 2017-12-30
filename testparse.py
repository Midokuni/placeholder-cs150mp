import ply.yacc as yacc
from langlex import tokens

names = {"TESTICS":69}

def p_start(p):
	'''start : repeat_ext_dec'''
	if(len(p) == 2):
		p[0] = p[1]

def p_repeat_ext_dec(p):
	'''repeat_ext_dec : external_declaration
	| repeat_ext_dec external_declaration'''
	if(len(p) == 2):
		p[0] = p[1]

def p_external_declaration(p):
	'''external_declaration : function_definition
	| declaration'''
	if(len(p) == 2):
		p[0] = p[1]

def p_function_definition(p):
	'''function_definition ::= type_specifier declarator repeat_declaration compound_statement'''
	if(len(p) == 2):
		p[0] = p[1]

def p_type_specifier(p):
	'''type_specifier : INT 
	| CHAR 
	| FLOAT'''
	if(len(p) == 2):
		p[0] = p[1]

def p_repeat_declaration(p):
	'''repeat_declaration ::= declaration
	| repeat_declaration declaration'''
	if(len(p) == 2):
		p[0] = p[1]
def p_declaration(p):
	'''declaration : type_specifier repeat_init_declarator DELIMIT '''
	if(len(p) == 2):
		p[0] = p[1]

def p_repeat_init_declarator(p):
	'''repeat_init_declarator : init_declarator
                | repeat_init_declarator init_declarator'''
	if(len(p) == 2):
		p[0] = p[1]

def p_init_declarator(p):
	'''init_declarator : declarator 
			| declarator ASSIGN initializer'''
	if(len(p) == 2):
		p[0] = p[1]
	#add declarator to the known names
	#names.add(p[1])

def p_declarator(p):
	'''declarator : direct_declarator'''
	p[0] = p[1]

def p_direct_declarator(p):
	'''direct_declarator : identifier
	| LPAREN declarator RPAREN
	| direct_declarator LBRACKET constant_expression RBRACKET
	| direct_declarator LBRACKET RBRACKET
	| direct_declarator LPAREN parameter_type_list RPAREN
	| direct_declarator LPAREN repeat_identifier RPAREN'''
	if(len(p) == 2):
		p[0] = p[1]
	elif(len(p)>4):
		p[0] = 3

def p_repeat_identifier(p):
	'''repeat_identifier : identifier 
	| repeat_identifier identifier'''
	if(len(p) == 2):
		p[0] = p[1]

def p_identifier(p):
	'''identifier : VARIABLE'''
	p[0] = p[1]

def p_constant_expression(p):
	'''constant_expression : conditional_expression'''
	p[0] = p[1]

def p_conditional_expression(p):
	'''conditional_expression : logicalor_expression'''
	p[0] = p[1]

def p_logicalor_expression(p):
	'''logicalor_expression : logicaland_expression
		| logicalor_expression OR logicaland_expression'''
	if(len(p) == 2):
		p[0] = p[1]
	else:
		if(p[1] or p[3]):
			print("TRUE")
		else:
			print("FALSE")

def p_logicaland_expression(p):
	'''logicaland_expression : inclusiveor_expression 
		| logicaland_expression AND exclusiveor_expression '''
	if(len(p) == 2):
		p[0] = p[1]
	else:
		if(p[1] and p[3]):
			print("TRUE")
		else:
			print("FALSE")

def p_exclusiveor_expression(p):
	'''exclusiveor_expression : equality_expression
	| exclusiveor_expression XOR equality_expression'''
	if(len(p) == 2):
		p[0] = p[1]
	else:
		if(p[1] ^ p[3]):
			print("TRUE")
		else:
			print("FALSE")

def p_equality_expression(p):
	'''equality_expression : relational_expression
	| equality_expression EQUAL relational_expression
	| equality_expression NOT_EQUAL relational_expression'''
	if(len(p) == 2):
		p[0] = p[1]
	else:
		if(p[1] == p[3] and p[2] == '=='):
			print("TRUE")
		elif(p[1] != p[3] and p[2] == '!='):
			print("TRUE")
		else:
			print("FALSE")

def p_relational_expression(p):
	'''relational_expression : additive_expression
	| relational_expression LESS additive_expression
	| relational_expression GREATER additive_expression
	| relational_expression LESS_EQUAL additive_expression
	| relational_expression GREATER_EQUAL additive_expression'''
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

def p_additive_expression(p):
	'''additive_expression : multiplicative_expression
				| additive_expression ADD multiplicative_expression
				| additive_expression SUB multiplicative_expression'''
	if (len(p) == 2):
		p[0] = p[1]
	elif(p[2] == '+'):
		p[0] = p[1] + p[3]
	elif(p[2] == '-'):
		p[0] = p[1] - p[3]

def p_multiplicative_expression(p):
	'''multiplicative_expression : unary_expression
					  | multiplicative_expression MUL unary_expression
					  | multiplicative_expression DIV unary_expression
					  | multiplicative_expression MOD unary_expression'''
	if (len(p) == 2):
		p[0] = p[1]
	elif(p[2] == '*'):
		p[0] = p[1] * p[3]
	elif(p[2] == '/'):
		p[0] = p[1] / p[3]
	elif(p[2] == '%'):
		p[0] = p[1] % p[3]

def p_unary_expression(p):
	'''unary_expression : postfix_expression
			 | SUB unary_expression
			 | NOT unary_expression'''
	if(len(p) == 2):
		p[0] = p[1]
	elif(p[1] == '-'):
		p[0] = -p[2]
	elif(p[1] == '!'):
		p[0] = not p[2]

def p_postfix_expression(p):
	'''postfix_expression : literal 
	   | postfix_expression LBRACKET expression RBRACKET
	   | postfix_expression LPAREN repeat_assignment_expression RPAREN'''
	if(len(p) == 2):
		p[0] = p[1]

def p_repeat_assignment_expression(p):
	'''repeat_assignment_expression : assignment_expression
	| repeat_assignment_expression assignment_expression'''
	if(len(p) == 2):
		p[0] = p[1]

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

def p_expression(p):
	'''expression : assignment_expression'''
	if(len(p) == 2):
		p[0] = p[1]

def p_assignemnt_expression(p):
	'''assignment_expression : conditional_expression
				  | postfix_expression ASSIGN assignment_expression'''
	if(lan(p) == 2):
		p[0] = p[1]

def p_parameter_type_list(p):
	'''parameter_type_list : parameter_list'''
	p[0] = p[1]

def p_parameter_list(p):
	'''parameter_list : parameter_declaration
	| parameter_list COMMA parameter_declaration'''
	if(len(p) == 2):
		p[0] = p[1]

def p_parameter_declaration(p):
	'''parameter_declaration : atleastone_type_specifier declarator
	| atleastone_type_specifier'''
	if(len(p) == 2):
		p[0] = p[1]

def p_atleastone_type_specifier(p):
	'''atleastone_type_specifier : type_specifier
		| atleastone_type_specifier type_specifier'''
	if(len(p) == 2):
		p[0] = p[1]

def p_initializer(p):
	'''initializer : assignment_expression'''
	p[0] = p[1]


def p_compound_statement(p):
	'''compound_statement : LBRACE repeat_declaration repeat_statement RBRACE'''

def p_repeat_statement(p):
	'''repeat_statement : statement
	| repeat_statement statement'''


def p_statement(p):
	'''statement : labeled_statement
			| expression_statement
			| selection_statement
			| iteration_statement
			| jump_statement'''
	p[0] = p[1]

def p_labeled_statement(p):
	'''labeled_statement : identifier COLON statement'''
	p[0] = p[1]

def p_expression_statement(p):
	'''expression_statement : 
			| expression'''
	if(len(p) == 2):
		p[0] = p[1]
def p_selection_statement(p):
	'''selection_statement : IF LPAREN statement RPAREN LBRACE statement RBRACE
			| IF LPAREN statement RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE'''
	p[0] = p[1]

def p_iteration_statement(p):
	'''iteration_statement : WHILE LPAREN expression RPAREN LBRACE statement RBRACE'''
	p[0] = p[1]

def p_jump_statement(p):
	'''jump_statement : RETURN expr'''
	p[0] = p[1]
def file_main():
	parser = yacc.yacc()
	f = open("test.code")
	text = f.read()
	print (text)
	result = parser.parse(text, debug=1)
	print(result)
	f.close()


file_main()
