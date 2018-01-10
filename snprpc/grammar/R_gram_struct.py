from snprpc.grammar.SystemExp import *
from snprpc.grammar.R_block_define import *

# 赋值语句
def assign_stmt():
    # print("=====def assign stmt=====")

    def process(parsed):
        ((name, _), exp) = parsed
        return AssignStatement(name, exp)

    return var + keyword('=') + aexp() ^ process

# 函数调用
def func_call():
    def process(parsed):
        (name, exp) = parsed
        return FuncCallStatement(name, exp)

    return var + call_args() ^ process

# if 结构
def if_stmt():
    def process(parsed):
        (((_, condition), true_stmt), false_parsed) = parsed
        # print("===== condition =====\t", condition)
        if false_parsed:
            (_, false_stmt) = false_parsed
        else:
            false_stmt = None
        return IfStatement(condition, true_stmt, false_stmt)
    return keyword('if') + bexp() + code_block() + Opt(keyword('else') + code_block()) ^ process

# while 结构
def while_stmt():
    def process(parsed):
        ((_, condition), body) = parsed
        return WhileStatement(condition, body)
    return keyword('while') + bexp() + code_block() ^ process

# 函数申明
def function_stmt():
    def process(parsed):
        (((name, _), arg_list), body) = parsed
        return FunctionStatement(name, arg_list, body)

    return var + keyword('<-function') + args() + code_block() ^ process

# for 结构
def for_stmt():
    def process(parsed):
        ((_, r_iter_list), body) = parsed
        return ForStatement(r_iter_list, body)

    return keyword('for') + Lazy(r_iterator) + code_block() ^ process

# repeat 结构
def repeat_stmt():
    def process(parsed):
        (_, body) = parsed
        return RepeatStatement(body)

    return keyword('repeat') + code_block() ^ process

# return 系统操作匹配器
def return_sys_stmt():

    def process(parsed):
        (_, exp) = parsed
        return ReturnExp(exp)

    return keyword('return') + Lazy(fix_stmt) ^ process

# print 系统操作匹配器
def print_sys_stmt():
    def process(parsed):
        (_, args) = parsed
        return PrintExp(args)

    return keyword('print') + call_args() ^ process

# next 系统操作匹配器
def next_sys_stmt():

    def process(parsed):
        _ = parsed
        return NextExp()

    return keyword('next') ^ process


# break 系统操作匹配器
def break_sys_stmt():

    def process(parsed):
        _ = parsed
        return BreakExp()

    return keyword('break') ^ process
