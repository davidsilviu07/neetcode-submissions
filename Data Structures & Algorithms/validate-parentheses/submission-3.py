class Solution:
    def isValid(self, s: str) -> bool:
        stiva = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stiva.append(c)
            elif stiva:
                if (c == ')' and stiva[-1] == '(') or (c == ']' and stiva[-1] == '[') or (c == '}' and stiva[-1] == '{'):
                    stiva.pop()
                else:
                    return False
            else:
                return False
        return not stiva