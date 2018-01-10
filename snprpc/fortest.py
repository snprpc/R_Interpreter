from snprpc.grammar.R_Parser import *
from snprpc.LeMorphology.LeCode import *
from snprpc.LeMorphology.LeMorAnalysis import *
from snprpc.Levent.Leimport import *


code = Code()
test = MorAnalysis()
tokens1 = test.getResult(code.getCode('/home/snprpc/project/python_ws/R_Interpreter/input/FOR.R'))

ast = R_parse(tokens1)
if ast is None:
    print("None")
env = [LeEnvironment()]
node = ast.createAST(env)

print("""
fruit_vector <- c("apple","banana","pear","orange")

for(fruit in fruit_vector){
    print(fruit)
}

num = 5
repeat{
    print("REPEAT")
    num = num - 1
    if(num==0){
        break
    }
}
""")

for i in node:
    i.interpret()
