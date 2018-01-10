from Leimport import *
# Result类
# 包括了一个值（作为 AST 的一部分)
# 以及一个位置信息（标记符流中 一下个标记符的索引）
class Result:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos

    def __repr__(self):
        return 'Result(%s, %d)' % (self.value, self.pos)

    def getHaooon(self, node):
        nodeList = []
        while isinstance(node, list):
            nodeList.insert(0, node[1])
            node = node[0]
        nodeList.insert(0, node)
        return nodeList

    def createAST(self, env):

        nodeList = self.value.createAST(env)
        # print("============", nodeList)
        newList = self.getHaooon(nodeList)
        return newList
