class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b,
            "*": lambda a,b: a * b,
            "/": lambda a,b: int(a/b) if (b != 0) else 0
        }

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[token](a,b))
            else:
                stack.append(int(token))

        return stack[0]    
        