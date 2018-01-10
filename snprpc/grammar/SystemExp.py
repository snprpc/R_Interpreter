from snprpc.grammar.Equality import Equality
from snprpc.Levent.LeInterpret.LeSimpleInterpreter import *
from snprpc.Levent.LeInterpret.create import create

class SystemExp(Equality):
    pass

class ReturnExp(SystemExp):

    def __init__(self, exp):
        self.right = exp

    def __repr__(self):
        return 'ReturnExp(%s)' % self.right

class BreakExp(SystemExp):
    def __repr__(self):
        return 'BreakExp()'


    def createAST(self, env):
        break1 = BREAK(env)
        break1.setContent()
        return break1

class NextExp(SystemExp):
    def __repr__(self):
        return 'NextExp()'

    def createAST(self, env):
        next1 = NEXT(env)
        next1.setContent()
        return next1

class PrintExp(SystemExp):

    def __init__(self, args):
        self.args = args

    def __repr__(self):
        return 'PrintExp(%s)' % self.args

    def createAST(self, env):
        create1 = create()
        call = CALL(env)
        argList = []
        tmp_list = self.args.createAST(env)
        tmp_list = reversed(tmp_list)
        for i in tmp_list:
            argList.append(i.createAST(env))
        call.setContent(create1.thing(env, 'print', 'VARIABLE'), argList)
        return call

class CExp(SystemExp):

    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return 'CExp(%s, %s)' % (self.name, self.args)

    def createAST(self, env):
        create1 = create()
        call = CALL(env)
        argList = []
        tmp_list = self.args.createAST(env)
        tmp_list = reversed(tmp_list)
        for i in tmp_list:
            argList.append(i.createAST(env))
        call.setContent(create1.thing(env, 'c', 'VARIABLE'), argList)
        assign = ASSIGN(env)
        assign.setContent(create1.thing(env, self.name, 'VARIABLE'),call)
        return assign


class PieExp(SystemExp):

    def __init__(self, args):
        self.args = args

    def __repr__(self):
        return 'PieExp(%s)' % self.args

    def createAST(self, env):
        create1 = create()
        call = CALL(env)
        argList = []
        tmp_list = self.args.createAST(env)
        tmp_list = reversed(tmp_list)
        for i in tmp_list:
            argList.append(i.createAST(env))
        call.setContent(create1.thing(env, 'pie', 'VARIABLE'), argList)
        return call
