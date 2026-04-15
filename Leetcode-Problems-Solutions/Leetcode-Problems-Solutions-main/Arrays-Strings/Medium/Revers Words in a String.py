class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = ""
        s2 = ""
        a = 0
        for i in range(len(s)-1,-1,-1) :
            if s[i] != " " :
                s1 = s[i] + s1
                a = 1
            if s[i] == " " and a == 1 :
                s2 = s2 + s1 + " "
                s1 = ""
                a = 0
            if i == 0 and s[0] != " " :
                s2 = s2 + s1
        if s2[-1] == " " :
            return s2[:len(s2)-1]
        return s2
