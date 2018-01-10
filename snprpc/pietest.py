from snprpc.grammar.R_Parser import *
from snprpc.LeMorphology.LeCode import *
from snprpc.LeMorphology.LeMorAnalysis import *
from snprpc.Levent.Leimport import *


code = Code()
test = MorAnalysis()
tokens1 = test.getResult(code.getCode('/home/snprpc/project/python_ws/R_Interpreter/input/PIE.R'))

ast = R_parse(tokens1)
if ast is None:
    print("None")
env = [LeEnvironment()]
node = ast.createAST(env)

print("""
pie_vec <- c(10,20,30,20,10,10)
pie(pie_vec
""")

for i in node:
    i.interpret()