class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        a = True
        nb = 0
        for c in path :
            if c == '/' :
                if nb == 2 and len(stack) > 1 :
                    stack.pop()
                    while stack[-1] != '/' :
                        stack.pop()
                elif nb > 2 :
                    stack.append('.'*nb)
                    stack.append('/')
                nb = 0
                if a :
                    stack.append(c)
                    a = False
            elif c == '.' :
                if stack[-1] not in {'/'} :
                    stack.append('.')
                else : 
                    nb += 1
            else :
                if nb != 0 :
                    stack.append('.'*nb)
                    nb = 0
                stack.append(c)
                a = True

        if nb == 2 and len(stack) > 1 :
            stack.pop()
            while stack[-1] != '/' :
                stack.pop()
            stack.pop()
        elif nb > 2 :
            stack.append('.'*nb)
        if stack == [] :
            return "/"
        if len(stack) > 1 and ( path[-1] == '/' or stack[-1] == '/' ) :
            return "".join(stack[:len(stack)-1])
        return "".join(stack)


        
