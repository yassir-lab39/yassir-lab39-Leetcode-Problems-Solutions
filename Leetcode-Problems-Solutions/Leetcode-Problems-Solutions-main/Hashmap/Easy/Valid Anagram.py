class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        D = dict()
        if len(s) != len(t) :
            return False
        for c in s :
            if c not in D :
                D[c] = 1
            else :
                D[c] += 1
        for c in t :
            if c in D :
                D[c] -= 1
        for c in s :
            if D[c] != 0 :
                return False
        return True
