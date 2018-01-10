from snprpc.grammar.test_parserstruct import *

# 单元测试1.0
# 条件判断语句解析
print("\n====================单元测试1.0——条件盘判断结构====================\n")
ast = unit_if_stmt()

# 单元测试1.0
# while 循环语句解析
print("\n====================单元测试1.0——while循环结构====================\n")
ast = unit_while_stmt()

# 单元测试1.0
# 函数声明
print("\n====================单元测试1.0——函数声明====================\n")
ast = unit_func_claim()

# 单元测试1.0
# for 循环语句解析
print("\n====================单元测试1.0——for循环结构====================\n")
ast = unit_for_stmt()

# 单元测试1.0
# 函数调用语句解析
print("\n====================单元测试1.0——函数调用语句====================\n")
ast = unit_func_call()

# 单元测试1.0
# return 系统函数解析
print("\n====================单元测试1.0——return系统函数====================\n")
ast = unit_return_sys()

# 单元测试1.0
# repeat 循环语句解析
print("\n====================单元测试1.0——repeat循环结构====================\n")
ast = unit_repeat_stmt()

# 单元测试1.0
# break, next 关键字
print("\n====================单元测试1.0——break, next 关键字===================\n")
ast = unit_breakandnext_stmt()

# 单元测试1.0
# c 函数声明
print("\n====================单元测试1.0—— c 函数声明===================\n")
ast = unit_c_sys()
print(ast)
