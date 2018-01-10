from snprpc.grammar.R_Parser import *
from snprpc.LeMorphology.LeCode import *
from snprpc.LeMorphology.LeMorAnalysis import *
from snprpc.Levent.Leimport import *


code = Code()
test = MorAnalysis()
tokens1 = test.getResult(code.getCode('/home/snprpc/project/python_ws/R_Interpreter/input/IF.R'))

ast = R_parse(tokens1)
if ast is None:
    print("None")
env = [LeEnvironment()]
node = ast.createAST(env)

print("""
a = 2
if(a %% 2 == 0){
    print("even")
}else{
    print("odd")
}
""")

for i in node:
    i.interpret()