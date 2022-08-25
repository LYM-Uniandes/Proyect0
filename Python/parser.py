import ply.lex as lex
import ply.yacc as yacc
import re
import codecs
import os
import sys
from sys import stdin


# PALABRAS RESERVADAS DEL INTERPRETADOR

tokens = [ 'LPARENT', 'RPARENT', 'COMMA',
                'OPENCORCHETE', 'CLOSECORCHETE',
                 'PROG', 'VAR', 'PROC', "WHILE", "DO", "OD", "IF",
                  "FI", 'GORP', "NUMBER", "ID",
                  "ODD", "PLUS", "UPDATE", "MINUS", "TIMES", "NE", "LTE",
                  "GTE", "DIVIDE", "ASSIGN", "LT", "GT", "SEMMICOLOM", 
                  "BREAK", "SPACE"]


# LOOK A LIKE DE LAS PALABRAS RESERVADAS 

t_ignore = " \t"
t_PROG = 'PROG*'
t_VAR = 'var*'
t_PROC = 'PROC*'
t_WHILE = 'while*'
t_DO = 'do'
t_OD = 'od'
t_IF = 'if'
t_FI = 'fi'
t_GORP = 'GORP'
t_BREAK = r'\r\n'

# OPERADORES
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_UPDATE = r'\:='
t_OPENCORCHETE = r'{'
t_CLOSECORCHETE = r'}'


def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in tokens:
		t.value = t.value.upper()
		t.type = t.value

	return t
def t_SPACE(t):
    r'\s'
    pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
	r'\n'
	t.lexer.lineno += len(t.value)



# DETECCIÓN DE CARACTER ILEGAL EN EL ANALIZADOR LÉXICO

def t_error(t):
    print("caracter ilegal%s" %t.value[0])
    t.lexer.skip(1)
    
# Producciones
def p_progs(p):
	'''program : PROG'''
	print ("EL PROGRAMA INICIA CON PROG")

def p_progf(p):
	'''program : PROG variable proc GORP'''
	print ("EL PROGRAMA TERMINA CON GORP")

def p_progf2(p):
	'''program : PROG variable proc proc GORP'''
	print ("EL PROGRAMA TIENE UNA VARIABLE Y 2 FUNCIONES, TERMINA CON GORP \n EL PROGRAMA FUNCIONA CORRECTAMENTE")
# ASIGNACIÓN DE VARIABLES

def p_progf3(p):
	'''program : PROG variable proc proc proc GORP'''
	print ("EL PROGRAMA TIENE UNA VARIABLE Y 3 FUNCIONES, TERMINA CON GORP \n EL PROGRAMA FUNCIONA CORRECTAMENTE")
# ASIGNACIÓN DE VARIABLES
def p_variable(p):
    '''variable : VAR ID COMMA ID COMMA ID SEMMICOLOM'''   
    print("Inicializacion de Variables")

def p_variable1(p):
    '''variable : ID ASSIGN NUMBER SEMMICOLOM'''
    print("Se asigna una variable")
def p_PROC(p):
    '''proc : PROC ID LPARENT ID COMMA ID RPARENT statement proc'''
    print("Inicializacion de funcion")

def p_PROC1(p):
    '''proc : PROC ID LPARENT RPARENT OPENCORCHETE statement CLOSECORCHETE'''
    print("Se inicializa funcion sin parametro especifico")

def p_PROC2(p):
    '''proc : OPENCORCHETE proc variable proc CLOSECORCHETE'''
    print("Inicializacion de funcion #2")

def p_PROC3(p):
    '''proc : PROC ID LPARENT RPARENT OPENCORCHETE if CLOSECORCHETE'''
    print("Inicializacion de funcion #2")

def p_PROC4(p):
    '''proc : ID LPARENT NUMBER COMMA NUMBER RPARENT SEMMICOLOM'''
    print("Se inicializa una nueva función con parametros")
def p_PROC5(p):
    '''proc : ID LPARENT NUMBER COMMA NUMBER RPARENT '''
    print("Se inicializa una nueva función con parametros")
def p_statement1(p):
    '''statement : while'''
    print("Abre Ciclo While")

def p_statement2(p):
    '''statement : if'''
    print("inicio del IF")

def p_if(p):
    ''' if : IF condition  OPENCORCHETE statement CLOSECORCHETE  FI'''
    print("Este es el IF")

def p_While(p):
    '''while : WHILE LPARENT ID LPARENT ID COMMA NUMBER RPARENT RPARENT DO do OD '''
    print("While correcto")

def p_condition(p):
    ''' condition : LPARENT ID LPARENT ID COMMA NUMBER RPARENT RPARENT'''
def p_do(p):
    '''do :  OPENCORCHETE ID LPARENT ID COMMA NUMBER RPARENT CLOSECORCHETE '''
    print("do correcto")


def p_statement(p):
    '''statement : OPENCORCHETE ID LPARENT ID RPARENT SEMMICOLOM ID LPARENT ID RPARENT SEMMICOLOM ID LPARENT ID RPARENT CLOSECORCHETE'''
    print("Statement correcto")
#     if ( canWalk ( west ,1) ) { walk( west ,1) } fi
def p_statement2 (p):
    ''' statement : ID LPARENT ID COMMA NUMBER RPARENT'''
def p_error(p):
	print ("Error de sintaxis Linea: " +str(p.lineno) + str(p))
	#print ("Error en la linea "+str(p.lineno)

# LEER ARCHIVO .TXT

archivo = "file.txt"
fp = codecs.open(archivo, "r", "utf-8")
cadena = fp.read()
fp.close()




analizador = lex.lex()
analizador.input(cadena.strip())
while True:
    tok = analizador.token()
    if not tok : break
    print(tok)
    
parser = yacc.yacc()
result = parser.parse(cadena.strip())
