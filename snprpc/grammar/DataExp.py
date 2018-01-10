from snprpc.grammar.Equality import Equality
from snprpc.Levent.LeEnv.LeEnvironment import *
from snprpc.Levent.LeFunctions.LeSystemFunction import *
from snprpc.Levent.LeInterpret.create import create
from snprpc.Levent.LeInterpret.LeMathematicInterpreter import *
from snprpc.Levent.LeInterpret.LeSimpleInterpreter import *


# 算数表达式类
class MathExp(Equality):
    pass

# 整形常量
class IntAexp(MathExp):
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return 'IntAexp(%d)' % self.i

    def child(self):
        return ['INTEGER', self.i]

    def getValue(self):
        return self.i

    def getType(self):
        return 'INTEGER'
    def createAST(self, env):
        create1 = create()
        return create1.num(env, 'INTEGER', self.i)

# 变量
class VarAexp(MathExp):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'VarAexp(%s)' % self.name

    def child(self):
        return ['VARIABLE', self.name]

    def getValue(self):
        return self.name

    def getType(self):
        return 'VARIABLE'
    def createAST(self, env):
        create1 = create()
        return create1.thing(env, self.name, 'VARIABLE')

# 字符串
class StrAexp(MathExp):
    def __init__(self, context):
        self.context = context

    def __repr__(self):
        return 'StrAexp(%s)' % self.context

    def getValue(self):
        return self.context

    def getType(self):
        return 'STRING'
    def child(self):
        return ['String', self.context]

    def createAST(self, env):
        create1 = create()
        return create1.thing(env, self.context, 'STRING')


class ArgsList(MathExp):
    def __init__(self, cur_arg, nxt_arg):
        self.cur_arg = cur_arg
        self.nxt_arg = nxt_arg
        # print("=====Args=====\t", self.cur_arg, self.nxt_arg)

    def __repr__(self):
        return 'ArgsList(%s, %s)' % (self.cur_arg, self.nxt_arg)

    def createAST(self, env):

        if self.nxt_arg == None:
            args_list = []
            args_list.append(self.cur_arg)
            return args_list
        else:
            args_list = self.nxt_arg.createAST(env)
            args_list.append(self.cur_arg)
            return args_list

# 二进制操作
class BinopAexp(MathExp):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
        # print("\n\033[1;47m\tBinopAexp\n\033[0m")
        # print("\n\t\t\033[1;32mop\t\t  left\t\t\t\t\t  right\n\033[0m")
        # print("\t   ", self.op, "\t\t", self.left.child(), "\t\t", self.right.child(), '\n')

    def __repr__(self):

        return 'BinopAexp(%s, %s, %s)' % (self.op, self.left, self.right)

    def child(self, children):
        children.left.child();
        children.right.child();

    def createAST(self, env):
        create1 = create()
        op = create1.op(env,
                       self.op,
                       self.left.createAST(env),
                       self.right.createAST(env))
        return op
