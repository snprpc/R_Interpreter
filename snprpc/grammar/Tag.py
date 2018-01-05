import Parser

class Tag(Parser):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, tokens, pos):
        if pos &amp; lt; len(tokens) and tokens[pos][1] is self.tag:
            return Result(tokens[pos][0], pos+1)
        else:
            return None
