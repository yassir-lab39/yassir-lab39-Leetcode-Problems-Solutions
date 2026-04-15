class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in {'}',')',']'} or len(s)/2 != len(s)//2 :
            return False
        stack = [s[0]]
        for c in s[1:] :
            if c == ')' :
                if stack == [] or stack[-1] != '(' :
                    return False
                stack.pop()
            elif c == ']' :
                if stack == [] or stack[-1] != '[' :
                    return False
                stack.pop()
            elif c == '}' :
                if stack == [] or stack[-1] != '{' :
                    return False
                stack.pop()
            else :
                stack.append(c)
        return (stack==[])
