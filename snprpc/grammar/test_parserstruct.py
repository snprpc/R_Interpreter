from snprpc.grammar.ParserStruct import *
from snprpc.grammar.R_Parser import *
from snprpc.grammar.Parser import *
from snprpc.grammar.Statement import *


# 单元测试——测试简单的语法匹配器1.0
# 测试 Concat 类
# 定义关键子的tag值 ‘RESERVED’
# 通过 Contat 定义简单的加法文法匹配器 parser1
# 通过运算符重载定义简单的加法文法匹配器 parser2
# 模拟词法分析器的输出 tokens
# 构建抽象语法树 ast
def unit_addGrammar():
    RESERVED = 'RESERVED'
    parser1 = Concat(Concat(Tag('INT'), Reserved('+', 'RESERVED')), Tag('INT'))
    parser2 = Tag('INT') + Reserved('+', RESERVED) + Tag('INT')
    tokens = [
              ['1', 'INT'],
              ['+', 'RESERVED'],
              ['4', 'INT']
             ]
    ast = parser1(tokens, 0)
    ast_result = ast.value
    print(ast_result)

# 单元测试——分句器1.0
# 通过定义 ‘;’ 文法匹配器对程序进行断句
# 通过完成的简单的算数运算文法分析器对输入 tokens 进行文法分析
# 构建抽象语法树 ast
def unit_Aesp():
    tokens = [['a', 'VARIABLE'],
              ['=', 'RESERVED'],
              ['1', 'INTEGER'],
              [';', 'RESERVED'],
              ['b', 'VARIABLE'],
              ['=', 'RESERVED'],
              ['a', 'VARIABLE'],
              ['+', 'RESERVED'],
              ['1', 'INTEGER'],
              [';', 'RESERVED']]
    ast = parse_result = R_parse(tokens)

# 单元测试 优先级测试1.0
def unit_precdence():
    tokens = [
                 ['a', 'VARIABLE'], ['=', 'RESERVED'], ['1', 'INTEGER'], [';', 'RESERVED'],
                 ['b', 'VARIABLE'], ['=', 'RESERVED'], ['1', 'INTEGER'], ['+', 'RESERVED'], ['a', 'VARIABLE'], ['*', 'RESERVED'], ['3', 'INTEGER'], [';', 'RESERVED']
             ]
    ast = R_parse(tokens)


# 单元测试 条件判断语句
def unit_if_stmt():
    tokens=[['a', 'VARIABLE'], ['=', 'RESERVED'], ['1', 'INTEGER'], [';', 'RESERVED'],
            ['b', 'VARIABLE'], ['=', 'RESERVED'], ['2', 'INTEGER'], [';', 'RESERVED'],
            ['if', 'RESERVED'], ['(', 'RESERVED'], ['a', 'VARIABLE'], ['>', 'RESERVED'], ['b', 'VARIABLE'], [')', 'RESERVED'],
            ['{', 'RESERVED'], ['a', 'VARIABLE'], ['=', 'RESERVED'], ['b', 'VARIABLE'], ['}', 'RESERVED'],
            ['else', 'RESERVED'], ['{', 'RESERVED'], ['b', 'VARIABLE'], ['=', 'RESERVED'], ['a', 'VARIABLE'], ['}', 'RESERVED'], [';', 'RESERVED']]
    ast = R_parse(tokens)
    return ast

# 单元测试 while循环语句
def unit_while_stmt():
    tokens = [
        ['a', 'VARIABLE'], ['=', 'RESERVED'], ['5', 'INTEGER'], [';', 'RESERVED'],
        ['result', 'VARIABLE'], ['=', 'RESERVED'], ['0', 'INTEGER'], [';', 'RESERVED'],
        ['while', 'RESERVED'], ['(', 'RESERVED'], ['a', 'VARIABLE'], ['>=', 'RESERVED'], ['0', 'INTEGER'], [')', 'RESERVED'],
        ['{', 'RESERVED'], ['result', 'VARIABLE'], ['=', 'RESERVED'], ['result', 'VARIABLE'], ['+', 'RESERVED'], ['a', 'VARIABLE'], [';', 'RESERVED'],
        ['a', 'VARIABLE'], ['=', 'RESERVED'], ['a', 'VARIABLE'], ['-', 'RESERVED'], ['1', 'INTEGER'], ['}', 'RESERVED'], [';', 'RESERVED']]
    ast = R_parse(tokens)
    return ast

# 单元测试 函数申明
def unit_func_claim():
    tokens = [['a', 'VARIABLE'], ['=', 'RESERVED'], ['0', 'INTEGER'], [';', 'RESERVED'],
              ['isodd', 'VARIABLE'], ['<-function', 'RESERVED'], ['(', 'RESERVED'], ['num', 'VARIABLE'], [')', 'RESERVED'],
              ['{', 'RESERVED'], ['if', 'RESERVED'], ['(', 'RESERVED'], ['num', 'VARIABLE'], ['%%', 'RESERVED'], ['2', 'INTEGER'], ['!=', 'RESERVED'], ['0', 'INTEGER'], [')', 'RESERVED'], ['{', 'RESERVED'], ['a', 'VARIABLE'], ['=', 'RESERVED'], ['1', 'INTEGER'], ['}', 'RESERVED'], [';', 'RESERVED'], ['a', 'VARIABLE'], ['=', 'RESERVED'], ['0', 'INTEGER'], ['}', 'RESERVED'], [';', 'RESERVED']]
    ast = R_parse(tokens)
    return ast

# 单元测试 for循环
def unit_for_stmt():
    tokens = [['a', 'VARIABLE'], ['=', 'RESERVED'], ['abcde', 'STRING'], [';', 'RESERVED'],
              ['b', 'VARIABLE'], ['=', 'RESERVED'], ['0', 'INTEGER'], [';', 'RESERVED'],
              ['for', 'RESERVED'], ['(', 'RESERVED'], ['i', 'VARIABLE'], ['in', 'RESERVED'], ['a', 'VARIABLE'], [')', 'RESERVED'],
              ['{', 'RESERVED'], ['b', 'VARIABLE'], ['=', 'RESERVED'], ['b', 'VARIABLE'], ['+', 'RESERVED'], ['1', 'INTEGER'], ['}', 'RESERVED'], [';', 'RESERVED']]
    ast = R_parse(tokens)
    return ast

# 单元测试 函数调用
def unit_func_call():
    tokens = [['a', 'VARIABLE'], ['=', 'RESERVED'], ['0', 'INTEGER'], [';', 'RESERVED'],
              ['isodd', 'VARIABLE'], ['<-function', 'RESERVED'], ['(', 'RESERVED'], ['num', 'VARIABLE'], [')', 'RESERVED'],
              ['{', 'RESERVED'],
              ['if', 'RESERVED'], ['(', 'RESERVED'], ['num', 'VARIABLE'], ['%%', 'RESERVED'], ['2', 'INTEGER'], ['!=', 'RESERVED'], ['0', 'INTEGER'], [')', 'RESERVED'],
              ['{', 'RESERVED'], ['a', 'VARIABLE'], ['=', 'RESERVED'], ['1', 'INTEGER'], ['}', 'RESERVED'], [';', 'RESERVED'], ['a', 'VARIABLE'], ['=', 'RESERVED'], ['0', 'INTEGER'], ['}', 'RESERVED'], [';', 'RESERVED'],
              ['isodd', 'VARIABLE'], ['(', 'RESERVED'], ['2', 'INTEGER'], [',', 'RESERVED'], ['num2', 'VARIABLE'], [')', 'RESERVED'], [';', 'RESERVED']]
    ast = R_parse(tokens)
    return ast

# 单元测试 return 语句
def unit_return_sys():
    tokens = [['a', 'VARIABLE'], ['=', 'RESERVED'], ['0', 'INTEGER'], [';', 'RESERVED'],
              ['isodd', 'VARIABLE'], ['<-function', 'RESERVED'], ['(', 'RESERVED'], ['num1', 'VARIABLE'], [')', 'RESERVED'],
              ['{', 'RESERVED'], ['if', 'RESERVED'], ['(', 'RESERVED'], ['num', 'VARIABLE'], ['%%', 'RESERVED'], ['2', 'INTEGER'], ['!=', 'RESERVED'], ['0', 'INTEGER'], [')', 'RESERVED'],
              ['{', 'RESERVED'], ['return', 'RESERVED'], ['1', 'INTEGER'], ['}', 'RESERVED'], [';', 'RESERVED'],
              ['return', 'RESERVED'], ['0', 'INTEGER'], ['}', 'RESERVED'], [';', 'RESERVED'],
              ['isodd', 'VARIABLE'], ['(', 'RESERVED'], ['2', 'INTEGER'], [')', 'RESERVED'], [';', 'RESERVED']]
    ast = R_parse(tokens)
    return ast

# 单元测试 repeat循环
def unit_repeat_stmt():
    tokens = [['a', 'VARIABLE'], ['=', 'RESERVED'], ['0', 'INTEGER'], [';', 'RESERVED'],
              ['repeat', 'RESERVED'], ['{', 'RESERVED'], ['a', 'VARIABLE'], ['=', 'RESERVED'], ['a', 'VARIABLE'], ['+', 'RESERVED'], ['1', 'INTEGER'], [';', 'RESERVED'],
              ['if', 'RESERVED'], ['(', 'RESERVED'], ['a', 'VARIABLE'], ['>', 'RESERVED'], ['5', 'INTEGER'], [')', 'RESERVED'],
              ['{', 'RESERVED'], ['a', 'VARIABLE'], ['=', 'RESERVED'], ['0', 'INTEGER'], ['}', 'RESERVED'], ['}', 'RESERVED'], [';', 'RESERVED']]

    ast = R_parse(tokens)
    return ast

# 单元测试 break、next 关键字
# 单元测试 repeat循环
def unit_breakandnext_stmt():
    tokens = [['a', 'VARIABLE'], ['=', 'RESERVED'], ['0', 'INTEGER'], [';', 'RESERVED'],
              ['repeat', 'RESERVED'], ['{', 'RESERVED'], ['a', 'VARIABLE'], ['=', 'RESERVED'], ['a', 'VARIABLE'], ['+', 'RESERVED'], ['1', 'INTEGER'], [';', 'RESERVED'],
              ['next', 'RESERVED'], [';', 'RESERVED'],
              ['if', 'RESERVED'], ['(', 'RESERVED'], ['a', 'VARIABLE'], ['>', 'RESERVED'], ['5', 'INTEGER'], [')', 'RESERVED'],
              ['{', 'RESERVED'], ['break', 'RESERVED'], ['}', 'RESERVED'], ['}', 'RESERVED'], [';', 'RESERVED']]

    ast = R_parse(tokens)
    return ast

# 单元测试 c函数声明
def unit_c_sys():
    tokens = [['c_test', 'VARIABLE'], ['<-c', 'RESERVED'], ['(', 'RESERVED'], ['a', 'STRING'], [',', 'RESERVED'], ['b', 'STRING'], [',', 'RESERVED'], ['c', 'STRING'], [')', 'RESERVED']]
    ast = R_parse(tokens)
    return ast