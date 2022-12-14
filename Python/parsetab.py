
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BREAK CLOSECORCHETE COMMA DIVIDE DO FI GORP GT GTE ID IF LPARENT LT LTE MINUS NE NUMBER OD ODD OPENCORCHETE PLUS PROC PROG RPARENT SEMMICOLOM SPACE TIMES UPDATE VAR WHILEprogram : PROGprogram : PROG variable proc GORPproc : proc procvariable : VAR variable variable : ID COMMA variable : ID SEMMICOLOM variable : variable variablevariable : ID ASSIGN NUMBER SEMMICOLOMproc : PROC ID arguments statement procarguments : LPARENT arguments RPARENTarguments : arguments argumentsarguments : ID COMMA arguments : IDproc : PROC ID LPARENT RPARENT OPENCORCHETE statement CLOSECORCHETEproc : OPENCORCHETE proc variable proc CLOSECORCHETEproc : PROC ID LPARENT RPARENT OPENCORCHETE if CLOSECORCHETEproc : ID LPARENT NUMBER COMMA NUMBER RPARENT SEMMICOLOMproc : ID LPARENT NUMBER COMMA NUMBER RPARENT statement : while if : IF condition  OPENCORCHETE statement CLOSECORCHETE  FIwhile : WHILE LPARENT ID LPARENT ID COMMA NUMBER RPARENT RPARENT DO do OD  condition : LPARENT ID LPARENT ID COMMA NUMBER RPARENT RPARENTdo :  OPENCORCHETE ID LPARENT ID COMMA NUMBER RPARENT CLOSECORCHETE statement : OPENCORCHETE ID LPARENT ID RPARENT SEMMICOLOM ID LPARENT ID RPARENT SEMMICOLOM ID LPARENT ID RPARENT CLOSECORCHETE statement : ID LPARENT ID COMMA NUMBER RPARENT'
    
_lr_action_items = {'PROG':([0,],[2,]),'$end':([1,2,16,],[0,-1,-2,]),'VAR':([2,3,4,6,11,12,13,15,20,26,28,42,48,56,60,61,64,],[4,4,4,4,4,-5,-6,-3,4,4,-8,-9,-15,-18,-14,-16,-17,]),'ID':([2,3,4,6,7,8,10,11,12,13,15,18,20,22,23,24,26,28,29,30,31,32,33,34,35,38,40,41,42,44,45,46,48,50,56,59,60,61,63,64,68,70,71,74,79,89,91,94,96,97,102,],[5,9,5,5,17,18,17,5,-5,-6,17,22,27,-13,30,22,9,-8,-12,-13,22,17,-19,43,22,22,17,49,17,51,52,-10,-15,58,-18,67,-14,-16,69,-17,52,-25,75,78,83,93,95,-21,98,99,-24,]),'PROC':([3,6,7,10,11,12,13,15,20,26,28,32,33,40,42,48,56,60,61,64,70,94,102,],[8,-7,8,8,-4,-5,-6,8,8,8,-8,8,-19,8,8,-15,-18,-14,-16,-17,-25,-21,-24,]),'OPENCORCHETE':([3,6,7,10,11,12,13,15,20,22,23,26,28,29,30,31,32,33,37,40,42,45,46,48,56,60,61,62,64,68,70,87,92,94,102,],[10,-7,10,10,-4,-5,-6,10,10,-13,34,10,-8,-12,-13,-11,10,-19,45,10,10,34,-10,-15,-18,-14,-16,68,-17,34,-25,91,-22,-21,-24,]),'COMMA':([5,9,22,25,27,30,49,67,78,99,],[12,12,29,39,12,29,57,72,82,101,]),'SEMMICOLOM':([5,9,21,27,56,66,86,],[13,13,28,13,64,71,89,]),'ASSIGN':([5,9,27,],[14,14,14,]),'GORP':([7,15,42,48,56,60,61,64,],[16,-3,-9,-15,-18,-14,-16,-17,]),'LPARENT':([9,17,18,22,23,24,27,29,30,31,35,36,38,43,46,51,52,55,69,75,93,95,],[19,19,24,-13,35,35,19,-12,41,35,35,44,35,50,-10,59,41,63,74,79,96,97,]),'NUMBER':([14,19,39,57,72,82,101,],[21,25,47,65,76,85,103,]),'CLOSECORCHETE':([15,33,40,42,48,53,54,56,60,61,64,70,73,81,94,100,102,104,],[-3,-19,48,-9,-15,60,61,-18,-14,-16,-17,-25,77,-20,-21,102,-24,105,]),'WHILE':([22,23,29,30,31,45,46,68,],[-13,36,-12,-13,-11,36,-10,36,]),'RPARENT':([22,24,29,31,38,46,47,58,65,76,80,83,85,88,98,103,],[-13,37,-12,-11,46,-10,56,66,70,80,84,86,88,92,100,104,]),'IF':([45,],[55,]),'FI':([77,],[81,]),'DO':([84,],[87,]),'OD':([90,105,],[94,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'variable':([2,3,4,6,11,20,26,],[3,6,11,6,6,26,6,]),'proc':([3,7,10,15,20,26,32,40,42,],[7,15,20,15,15,40,42,15,15,]),'arguments':([18,23,24,31,35,38,],[23,31,38,31,38,31,]),'statement':([23,45,68,],[32,53,73,]),'while':([23,45,68,],[33,33,33,]),'if':([45,],[54,]),'condition':([55,],[62,]),'do':([87,],[90,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROG','program',1,'p_progs','parser.py',86),
  ('program -> PROG variable proc GORP','program',4,'p_progf','parser.py',90),
  ('proc -> proc proc','proc',2,'p_proc4','parser.py',96),
  ('variable -> VAR variable','variable',2,'p_variable','parser.py',99),
  ('variable -> ID COMMA','variable',2,'p_variable2','parser.py',103),
  ('variable -> ID SEMMICOLOM','variable',2,'p_variable3','parser.py',107),
  ('variable -> variable variable','variable',2,'p_variable4','parser.py',111),
  ('variable -> ID ASSIGN NUMBER SEMMICOLOM','variable',4,'p_variable1','parser.py',115),
  ('proc -> PROC ID arguments statement proc','proc',5,'p_PROC','parser.py',118),
  ('arguments -> LPARENT arguments RPARENT','arguments',3,'p_arguments','parser.py',122),
  ('arguments -> arguments arguments','arguments',2,'p_arguments2','parser.py',125),
  ('arguments -> ID COMMA','arguments',2,'p_arguments3','parser.py',128),
  ('arguments -> ID','arguments',1,'p_arguments4','parser.py',131),
  ('proc -> PROC ID LPARENT RPARENT OPENCORCHETE statement CLOSECORCHETE','proc',7,'p_PROC1','parser.py',134),
  ('proc -> OPENCORCHETE proc variable proc CLOSECORCHETE','proc',5,'p_PROC2','parser.py',138),
  ('proc -> PROC ID LPARENT RPARENT OPENCORCHETE if CLOSECORCHETE','proc',7,'p_PROC3','parser.py',142),
  ('proc -> ID LPARENT NUMBER COMMA NUMBER RPARENT SEMMICOLOM','proc',7,'p_PROC4','parser.py',146),
  ('proc -> ID LPARENT NUMBER COMMA NUMBER RPARENT','proc',6,'p_PROC5','parser.py',149),
  ('statement -> while','statement',1,'p_statement1','parser.py',152),
  ('if -> IF condition OPENCORCHETE statement CLOSECORCHETE FI','if',6,'p_if','parser.py',160),
  ('while -> WHILE LPARENT ID LPARENT ID COMMA NUMBER RPARENT RPARENT DO do OD','while',12,'p_While','parser.py',164),
  ('condition -> LPARENT ID LPARENT ID COMMA NUMBER RPARENT RPARENT','condition',8,'p_condition','parser.py',168),
  ('do -> OPENCORCHETE ID LPARENT ID COMMA NUMBER RPARENT CLOSECORCHETE','do',8,'p_do','parser.py',170),
  ('statement -> OPENCORCHETE ID LPARENT ID RPARENT SEMMICOLOM ID LPARENT ID RPARENT SEMMICOLOM ID LPARENT ID RPARENT CLOSECORCHETE','statement',16,'p_statement','parser.py',175),
  ('statement -> ID LPARENT ID COMMA NUMBER RPARENT','statement',6,'p_statement2','parser.py',179),
]
