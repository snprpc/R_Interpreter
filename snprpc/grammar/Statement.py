from snprpc.grammar.Equality import Equality
from snprpc.Levent.LeEnv.LeEnvironment import *
from snprpc.Levent.LeFunctions.LeSystemFunction import *
from snprpc.Levent.LeInterpret.LeMathematicInterpreter import *
from snprpc.Levent.LeInterpret.LeSimpleInterpreter import *
from Leimport import *
from snprpc.Levent.LeInterpret.create import *

class Statement(Equality):
    pass


# 赋值表达式构造类
class AssignStatement(Statement):

    def __init__(self, name, aexp):
        self.name = name
        self.aexp = aexp
        # print('AssignStatement(%s, %s)' % (self.name, self.aexp.))

    def __repr__(self):
        return 'AssignStatement(%s, %s)' % (self.name, self.aexp)

    def createAST(self, env):
        create1 = create()
        # print(self.name)
        assign = create1.assign(env, create1.thing(env,self.name, 'VARIABLE'), self.aexp.createAST(env))
        return assign



# 复合表达式构造类
class CompoundStatement(Statement):
    def __init__(self, first, second):
        self.first = first
        self.second = second
        # print("first, second\t", self.first, ",", self.second)

    def __repr__(self):
        return 'CompoundStatement(%s, %s)' % (self.first, self.second)

    def createAST(self, env):

        return [self.first.createAST(env), self.second.createAST(env)]



# 参数列表
class ArgsStatement(Statement):
    def __init__(self, first, second):
        # first 表示第一个参数
        # second 表示第二个参数的对象
        self.first = first
        self.second = second

    def __repr__(self):
        return '\033[4;33m ArgsStatement(%s, %s) \033[0m' % (self.first, self.second)


# 函数声明构造类
class FunctionStatement(Statement):
    def __init__(self, name, args, body):
        self.name = name
        self.args = args
        self.body = body

    def createast(self):
        pass

    def __repr__(self):
        return 'FunctionStatement(%s, %s, %s)' % (self.name, self.args, self.body)

    def getHaooon(self, node):
        nodeList = []
        while isinstance(node, list):
            nodeList.insert(0, node[1])
            node = node[0]
        nodeList.insert(0, node)
        return nodeList

    def createAST(self, env):
        create1 = create()
        function = FUNCTION(env)
        args = ARGS(function.getEnv())
        # print(self.args.createAST(function.getEnv()))
        argsList = []
        newargs = reversed(self.args.createAST(function.getEnv()))
        for i in newargs:
            argsList.append(create1.thing(function.getEnv(),i,'VARIABLE'))
        args.setContent(argsList)
        # print(argsList,' hhahhahhhoooon')
        body = bodyFunction(function.getEnv())
        body.setContent(self.getHaooon(self.body.createAST(function.getEnv())))
        function.setContent(args, body)

        create1 = create()
        assign = ASSIGN(env)
        assign.setContent(create1.thing(env, self.name, 'VARIABLE'),function)

        return assign


# if结构构造类
class IfStatement(Statement):
    def __init__(self, condition, true_stmt, false_stmt):
        self.condition = condition
        self.true_stmt = true_stmt
        self.false_stmt = false_stmt

    def __repr__(self):
        return 'IfStatement(%s, %s, %s)' % (self.condition, self.true_stmt, self.false_stmt)

    def createAST(self, env):

        if self.false_stmt == None:
            create1 = create()
            if1 = IF(env)
            a = create1.true(env)
            if1.setContent(
                [self.condition.createAST(env)],
                [self.true_stmt.createAST(env)]
            )
            return if1
        else:
            create1 = create()
            if1 = IF(env)
            a = create1.true(env)
            if1.setContent(
                [self.condition.createAST(env), a],
                [self.true_stmt.createAST(env), self.false_stmt.createAST(env)]
            )
            return if1



# while结构构造类
class WhileStatement(Statement):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return 'WhileStatement(%s, %s)' % (self.condition, self.body)



# for 结构构造类
class ForStatement(Statement):
    def __init__(self, r_list, body):
        self.r_list = r_list
        self.body = body

    def __repr__(self):
        return '\nForStatement(%s, %s)' % (self.r_list, self.body)

    def getHaooon(self, node):
        nodeList = []
        while isinstance(node, list):
            nodeList.insert(0, node[1])
            node = node[0]
        nodeList.insert(0, node)
        return nodeList

    def createAST(self, env):
        for1 = FOR(env)
        env = for1.getEnv()
        in1 = IN(env)
        in1.setContent(self.r_list[0].createAST(env), self.r_list[1].createAST(env))
        for1.setContent(in1, self.getHaooon(self.body.createAST(env)))
        return for1

    # repeat 结构构造类
class RepeatStatement(Statement):
    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return 'RepeatStatement(%s)' % self.body

    def getHaooon(self, node):
        nodeList = []
        while isinstance(node, list):
            nodeList.insert(0, node[1])
            node = node[0]
        nodeList.insert(0, node)
        return nodeList

    def createAST(self,env):
        repeat = REPEAT(env)
        repeat.setContent(self.getHaooon(self.body.createAST(repeat.getEnv())))
        return repeat


# 函数调用语句
class FuncCallStatement(Statement):
    def __init__(self, name, args):
        self.name = name
        self.args = args

        # print("=====Func Call Statement=====")
        # print(self.args)

    def __repr__(self):
        return 'FuncCallStatement(%s, %s)' % (self.name, self.args)

    def createAST(self, env):
        create1 = create()
        call = CALL(env)
        newList = []
        for i in self.args.createAST(env):
            # print(i.getValue(),i.getType())
            newList.append(create1.thing(env,i.getValue(),i.getType()))
        reversed(newList)
        # print(newList,'haooon')
        call.setContent(create1.thing(env, self.name, 'VARIABLE'),newList)
        return call

