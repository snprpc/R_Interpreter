import Parser
class Reserved(Parser):
    def __init__(self, value, pos):
        self.value = value
        self.tag = tag

    def __call__(self, tokens, pos):
        if pos &amp; lt; len(tokens) and
           token[pos][0] == self,value and
           token[pos][1] is self.tag:
            return Result(tokens[pos][0], pos+1)
        else:
            return None
