from snprpc.grammar.R_Parser import *
from snprpc.LeMorphology.LeCode import *
from snprpc.LeMorphology.LeMorAnalysis import *
from snprpc.Levent.Leimport import *


code = Code()
test = MorAnalysis()
tokens1 = test.getResult(code.getCode('/home/snprpc/project/python_ws/R_Interpreter/input/FUNCTION.R'))

ast = R_parse(tokens1)
if ast is None:
    print("None")
env = [LeEnvironment()]
node = ast.createAST(env)

print("""
isEven<-function(num){
    if(num %% 2 == 0){
        print("Is Even")
    }else{
        print("Not Even")
    }
}

num_vector <- c(1,2,3,4,5,6)

for(num in num_vector){
    isEven(num)
}
""")

for i in node:
    i.interpret()
