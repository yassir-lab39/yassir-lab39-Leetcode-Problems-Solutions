class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        D = dict()
        j = 0
        word = ""
        for i in range(len(pattern)) :
            while j < len(s) and s[j] != ' ' :
                word += s[j]
                j += 1
            if pattern[i] in D :
                if D[pattern[i]] != word :
                    return False
            else :
                if word in D.values() :
                    return False
                D[pattern[i]] = word
            j += 1
            word = ""
        return (j == len(s)+1)
