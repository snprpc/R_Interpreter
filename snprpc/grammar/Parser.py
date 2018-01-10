from snprpc.grammar.Result import Result

# 基类Parser
# Parser 的子类将提供它们自己的 call 方法的实现
# 每个操作符提供了调用不同组合子的快捷方法

class Parser:
    def __call__(self, tokens, pos):
        return None

    def __add__(self, other):
        # 用于连接两个或多个数组
        return Concat(self, other)

    def __mul__(self, other):
        #
        return Exp(self, other)

    def __or__(self, other):
        return Alternate(self, other)

    def __xor__(self, func):
        return Process(self, func)


class Concat(Parser):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __call__(self, tokens, pos):
        # print("=====Concat Call In=====")
        left_result = self.left(tokens, pos)

        if left_result:
            right_result = self.right(tokens, left_result.pos)

            if right_result:
                combined_value = (left_result.value, right_result.value)
                # print("=====Concat Call Result=====")
                # print("left_result\t,\t", left_result)
                # print("right_result,\t", right_result)
                # print("\033[1;34m[+]\033[0m comb_result\t\t\t\t", combined_value)
                return Result(combined_value, right_result.pos)

            return None


class Exp(Parser):
    def __init__(self, parser, separator):
        self.parser = parser
        self.separator = separator

    def __call__(self, tokens, pos):
        # print("=====Exp Call In=====")
        result = self.parser(tokens, pos)

        def process_next(parsed):
            (sepfunc, right) = parsed
            return sepfunc(result.value, right)

        next_parser = self.separator + self.parser ^ process_next
        next_result = result
        while next_result:
            next_result = next_parser(tokens, result.pos)
            if next_result:
                result = next_result
                # print("\033[1;32m[>]\033[0m Exp Call Result\t\t\t ", result)
        return result

# Alternate类
# 它也需要两个参数：左解析器和右解析器
# 它先调用左解析器，如果解析成功了，刚返回相应的结果
# 如果不成功，则调用右解析器并返回它的结果。
class Alternate(Parser):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __call__(self, tokens, pos):
        # print("=====Alt Call In=====")
        left_result = self.left(tokens, pos)
        if left_result:
            # print("=====Alt Call Result=====")
            # print("left_result\t", left_result)
            return left_result
        else:

            right_result = self.right(tokens, pos)
            # print("=====Alt Call Result=====")
            # print("right_result\t", right_result)
            return right_result

# Process 类
# 用来处理结果的值
# 它的输入是一个解析器和一个函数
# 当解析器被成功调用时，Process 会将它的结果传给作为输入的函数作为参数
# 并用该函数返回的结果取代原本的值作为返回的结果。
class Process(Parser):
    def __init__(self, parser, func):
        self.parser = parser
        self.func = func

    def __call__(self, tokens, pos):
        # print("=====Process Call In=====")
        result = self.parser(tokens, pos)
        if result:
            # print("=====Process Call Result====")
            # print("result\t", result)
            result.value = self.func(result.value)
            return result



