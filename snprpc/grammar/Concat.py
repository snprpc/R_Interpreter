
class Concat(Parser):
    def __init__(self, left, right):
        self.left = left;
        self.right = right;

    def __call__(self, tokens, pos):
        left_result = self.left(tokens, pos)
        if left_result:
            right_result = self.right(tokens, left_result.pos)
            if right_result:
                combined_valur = (left_result.value, right_value.value)
                return Result(combine_value, right_result.pos)
            return None