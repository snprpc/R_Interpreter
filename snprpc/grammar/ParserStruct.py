from snprpc.grammar.Parser import Parser
from snprpc.grammar.Result import Result

# Reserved类
# 用来解析保留关键字及操作符
# 它将接受有特定值和标签的标记符
class Reserved(Parser):
    def __init__(self, value, tag):
        self.value = value
        self.tag = tag

    def __call__(self, tokens, pos):
        # print("=====Reserved Call In=====")
        # print(pos < len(tokens))
        # print(tokens[pos][0] == self.value)
        # print(tokens[pos][0])
        # print(self.value)
        # print(tokens[pos][1] == self.tag)
        if pos < len(tokens) and tokens[pos][0] == self.value and tokens[pos][1] == self.tag:
            # print("\033[1;32m[+]\033[0m Reserved Call Result\t", '\033[1;30;32m', tokens[pos][0], '\033[0m')
            return Result(tokens[pos][0], pos+1)
        else:
            return None

# Tag类
# 匹配有某一特殊标签的任意标记符
# 标记符的值可以是任意值
class Tag(Parser):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, tokens, pos):
        # print("=====Tag Call In=====")
        if pos < len(tokens) and tokens[pos][1] is self.tag:
            # print("=====Tag Call Result=====")
            # print("\033[1;32m[+]\033[0m Tag Call Result\t\t\t",'\033[1;30;32m', tokens[pos][0], '\t', tokens[pos][1], '\033[0m')
            return Result(tokens[pos][0], pos+1)
        else:
            return None

# Opt类
# 可用于解析可选的文本，例如 if 语句中的 else 子句
# 它需要一个语法分析器作为输入
# 如果该解析器调用成功，则正常返回它的结果
# 如果失败，仍返回一个成功的结果，但该结果的值为 None
class Opt(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, tokens, pos):
        # print("=====Opt Call In=====")
        result = self.parser(tokens, pos)
        if result:
            # print("=====Opt Call Result=====")
            # print("result , ", result)
            return result
        else:
            return Result(None, pos)

# Rep类
# 组合子将重复调用作为输入的解析器，直到失败为止
# 它可以用来生成某样事物的列表
# 如果解析器第一次调用就失败了， Rep 仍旧成功返回
# 此时它匹配的是一 个空的列表，并且不消耗标记符。
class Rep(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, tokens, pos):
        # print("=====Rep Call In=====")
        results = []
        result = self.parser(tokens, pos)
        while result:
            results.append(result.value)
            pos = result.pos
            result = self.parser(tokens, pos)
        # print("=====Rep Call Result=====")
        # print("result , ", result)
        return Result(results, pos)

# Phrase 类
# 接受一个单独的解析器作为输入
# 调用它并正常地返回它的结果
# 如果它的解析器没有消耗所有剩余的标记符，则 Phrase 调用失败。
class Phrase(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, tokens, pos):
        # print("=====Phr Call In=====")
        result = self.parser(tokens, pos)

        if result and result.pos == len(tokens):
            # print("=====Phr Call Result=====")
            # print("result , ", result)
            return result
        else:
            return None

# Lazy 类
# 接受一个函数作为参数
# 该函数接收零个参数并返回一个解析器
# 除非被调用了，否则 Lazy 本身不会调用这个函数来获取解析器
class Lazy(Parser):
    def __init__(self, parser_func):
        self.parser = None
        self.parser_func = parser_func

    def __call__(self, tokens, pos):
        # print("=====Lazy Call In=====")
        if not self.parser:
            self.parser = self.parser_func()
        # print("=====Lazy Call Result=====")
        result = self.parser(tokens, pos)
        # print("result , ", result)
        return result

