from snprpc.grammar.ParserStruct import *
from snprpc.grammar.DataExp import *
# R语言 语法字典

def keyword(kw):
    # print("=====def keyword=====")
    return Reserved(kw, RESERVED)

# 定义符号类型
RESERVED = 'RESERVED'

INT = 'INTEGER'
VARABLE = 'VARIABLE'
STRING = 'STRING'
DOUBLE = 'DOUBLE'
BOOLEAN = 'BOOLEAN'
NUMERIC = 'NUMERIC'

# 定义数据类型

# 变量类型
var = Tag(VARABLE)
# 整型常量
num = Tag(INT) ^ (lambda i: int(i))
# 字符串类型常量
string = Tag(STRING) ^ (lambda s: str(s))
# 浮点数类型常量
double = Tag(DOUBLE) ^ (lambda d: double(d))
# 布尔数据类型常量
boolen = Tag(BOOLEAN) ^ (lambda b: boolen(b))
#
numeric = Tag(NUMERIC) ^ (lambda num: numeric(num))

