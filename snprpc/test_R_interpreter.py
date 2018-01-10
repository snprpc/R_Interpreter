from snprpc.grammar.R_Parser import *
from snprpc.LeMorphology.LeCode import *
from snprpc.LeMorphology.LeMorAnalysis import *
from snprpc.Levent.Leimport import *


code = Code()
test = MorAnalysis()
tokens1 = test.getResult(code.getCode('/home/snprpc/project/python_ws/R_Interpreter/input/test.R'))
tokens = [['a', 'VARIABLE'], ['=', 'RESERVED'], ['3', 'INTEGER'], [';', 'RESERVED'], ['b', 'VARIABLE'], ['=', 'RESERVED'], ['a', 'VARIABLE'], ['+', 'RESERVED'], ['1', 'INTEGER'], [';', 'RESERVED'], ['e', 'VARIABLE'], ['=', 'RESERVED'], ['b', 'VARIABLE'], ['+', 'RESERVED'], ['1', 'INTEGER'], [';', 'RESERVED'], ['d', 'VARIABLE'], ['=', 'RESERVED'], ['e', 'VARIABLE'], ['-', 'RESERVED'], ['e', 'VARIABLE'], [';', 'RESERVED'], ['print', 'RESERVED'], ['(', 'RESERVED'], ['d', 'VARIABLE'], [')', 'RESERVED'], [';', 'RESERVED'], ['a', 'VARIABLE'], ['=', 'RESERVED'], ['2', 'INTEGER'], [';', 'RESERVED'], ['print', 'RESERVED'], ['(', 'RESERVED'], ['a', 'VARIABLE'], [')', 'RESERVED'], [';', 'RESERVED'], ['if', 'RESERVED'], ['(', 'RESERVED'], ['a', 'VARIABLE'], ['%%', 'RESERVED'], ['2', 'INTEGER'], ['==', 'RESERVED'], ['0', 'INTEGER'], [')', 'RESERVED'], ['{', 'RESERVED'], ['print', 'RESERVED'], ['(', 'RESERVED'], ['oushu', 'STRING'], [')', 'RESERVED'], ['}', 'RESERVED'], ['else', 'RESERVED'], ['{', 'RESERVED'], ['print', 'RESERVED'], ['(', 'RESERVED'], ['jishu', 'STRING'], [')', 'RESERVED'], ['}', 'RESERVED']]

#print(tokens)
ast = R_parse(tokens1)
# print(ast)
if ast is None:
    print("None")
env = [LeEnvironment()]
node = ast.createAST(env)
for i in node:
    i.interpret()
