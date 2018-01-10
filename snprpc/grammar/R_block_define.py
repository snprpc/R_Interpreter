from snprpc.grammar.R_dictionary import *
from snprpc.grammar.DataExp import *
from snprpc.grammar.Statement import *
from snprpc.grammar.BoolExp import *
from snprpc.grammar.Parser import *
from snprpc.grammar.R_gram_struct import *
from functools import reduce


# ===================================================================
# ========================== 可复用通用句法 ==========================
# ===================================================================

def parser():
    # print("=====def parser=====")
    return Phrase(stmt_list())

# 分句器
def stmt_list():
    # print("=====def stmt list=====")
    separator = keyword(';') ^ (lambda x: lambda l, r: CompoundStatement(l, r))
    return Exp(stmt(), separator)
# 代码快结构匹配器
def code_block():
    # 大括号过滤器
    def process_group(parsed):
        ((_, p), _) = parsed
        # print("===== P =====\t", type(p))
        return p
    return keyword('{') + Lazy(stmt_list) + keyword('}') ^ process_group


def precedence(value_parser, precedence_levels, combine):

    def op_parser(precedence_level):
        return any_operator_in_list(precedence_level) ^ combine

    parser = value_parser * op_parser(precedence_levels[0])
    for precedence_level in precedence_levels[1:]:
        parser = parser * op_parser(precedence_level)
    return parser

def any_operator_in_list(ops):
    op_parsers = [keyword(op) for op in ops]
    parser = reduce(lambda l, r: l | r, op_parsers)
    return parser

# 操作、操作数匹配器
def process_binop(op):
    return lambda l, r: BinopAexp(op, l, r)

# ===================================================================
# ========================== 运算表达式相关句法 ==========================
# ===================================================================
class AexpBlock():

    universe

    # 运算表达式
    def aexp(self):
        # print("=====def aexp=====")
        return precedence(self.aexp_term(),
                          self.aexp_precedence_levels,
                          process_binop)

    def aexp_term():
        # print("=====def aexp term=====")
        return aexp_value() | aexp_group()

    def aexp_group():
        # print("=====def aexp group=====")
        def process_group(parsed):
            ((_, p), _) = parsed
            print("===== P =====\t", type(p))
            return p

        return keyword('(') + Lazy(aexp) + keyword(')') ^ process_group

    # 运算数构造器
    # 它将 num、var、string 解析器返回的值转变为实际的表达式
    def aexp_value():
        # print("=====def aexp value=====")
        return (num ^ (lambda i: IntAexp(i))) | \
               (var ^ (lambda v: VarAexp(v))) | \
               (string ^ (lambda s: StrAexp(s)))

    # 算数运算优先级表
    aexp_precedence_levels = [
        ['*', '/', '%%'],
        ['+', '-'],
    ]

# ===================================================================
# ========================== 逻辑运算相关句法 ==========================
# ===================================================================

# Boolean 表达式
def bexp():
    return precedence(bexp_term(),
                      bexp_precedence_levels,
                      process_logic)

def bexp_term():
    return bexp_not() | \
           bexp_relop() | \
           bexp_group()

def bexp_not():
    return keyword('not') + Lazy(bexp_term) ^ (lambda parsed: NotBexp(parsed[1]))

def bexp_relop():
    relops = ['<', '<=', '>', '>=', '==', '!=']
    return aexp() + any_operator_in_list(relops) + aexp() ^ process_relop

def bexp_group():
    def process_group(parsed):
        ((_, p), _) = parsed
        # print("===== P =====\t", type(p))
        return p
    return keyword('(') + Lazy(bexp) + keyword(')') ^ process_group


# 判断运算构造器
def process_relop(parsed):
    ((left, op), right) = parsed
    return RelopBexp(op, left, right)

# 逻辑运算构造器
def process_logic(op):
    if op == 'and':
        return lambda l, r: AndBexp(l, r)
    elif op == 'or':
        return lambda l, r: OrBexp(l, r)
    else:
        raise RuntimeError('unknown logic operator: ' + op)

# 逻辑运算优先级表
bexp_precedence_levels = [
    ['and'],
    ['or'],
]



# ===================================================================
# ========================== 函数调用相关句法 ==========================
# ===================================================================

# 函数调用参数列表
def call_args():

    # 括号过滤器
    def args_call_group(parsed):
        ((_, p), _) = parsed
        # print("===== P =====\t", type(p))
        return p
    return keyword('(') + Opt(Lazy(call_args_list)) + keyword(')') ^ args_call_group

def call_args_list():

    # 参数列表构造器
    def args_list_process(parsed):
        (cur_arg, nxt_arg) = parsed
        print("nxt_arg------------", nxt_arg)
        return ArgsList(cur_arg, nxt_arg)
    return r_data_type() + Opt(Lazy(extend_call_list)) ^ args_list_process

def extend_call_list():

    def args_next_process(parsed):
        (_, nxt_arg) = parsed
        return nxt_arg
    return keyword(',') + call_args_list() ^ args_next_process


# ===================================================================
# ========================== 函数调用相关句法 ==========================
# ===================================================================
# 申明函数 参数列表
def args():
    # 括号过滤器
    def args_def_process(parsed):
        ((_, p), _) = parsed
        print("===== P =====\t", type(p))
        return p
    return keyword('(') + Opt(Lazy(def_args_list)) + keyword(')') ^ args_def_process

def def_args_list():

    # 参数列表构造器
    def args_list_process(parsed):
        (cur_arg, nxt_arg) = parsed
        print("nxt_arg------------", nxt_arg)
        return ArgsList(cur_arg, nxt_arg)
    return var + Opt(Lazy(extend_def_list)) ^ args_list_process

def extend_def_list():

    def args_next_process(parsed):
        (_, nxt_arg) = parsed
        return nxt_arg
    return keyword(',') + def_args_list() ^ args_next_process

# ===================================================================
# ====================== return 系统调用相关句法 ======================
# ===================================================================

# 用于 return 返回
def fix_stmt():
    return aexp_value()

# ===============================================================
# ====================== for 循环结构相关句法 ======================
# ===============================================================

# for 结构迭代器匹配
def r_iterator():
    return keyword('(') + var + keyword('in') + var + keyword(')') ^ process_iterator_group

# for 结构迭代器括号过滤
def process_iterator_group(parsed):
    ((((_, var1), _), var2), _) = parsed
    return [var1, var2]

# =======================================================
# ====================== R 语言句法 ======================
# =======================================================
# R 数据类型
def r_data_type():
    return (num ^ (lambda i: IntAexp(i))) |\
           (var ^ (lambda v: VarAexp(v))) |\
           (string ^ (lambda s: StrAexp(s)))

# =======================================================
# ====================== R 语言句法 ======================
# =======================================================
# R 语言语法结构类型
def stmt():
    # print("=====def stmt=====")
    return assign_stmt() |\
           func_call() |\
           if_stmt()|\
           for_stmt() |\
           repeat_stmt() |\
           while_stmt() |\
           function_stmt() |\
           return_sys_stmt() | \
           break_sys_stmt() |\
           next_sys_stmt()