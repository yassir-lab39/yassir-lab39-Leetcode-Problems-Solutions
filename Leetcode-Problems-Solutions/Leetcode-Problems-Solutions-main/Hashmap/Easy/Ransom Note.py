class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        D = dict()
        for c in magazine :
            if c in D :
                D[c] += 1
            else :
                D[c] = 1
        for c in ransomNote :
            if c not in D :
                return False
            D[c] -= 1    
            if D[c] < 0 :
                return False
        return True
