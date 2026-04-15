class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        D = dict()
        for i in range(len(s)) :
            if s[i] in D :
                if D[s[i]] != t[i] :
                    return False
            else :
                D[s[i]] = t[i]
        S = []
        for c in D :
            if D[c] in S :
                return False
            S.append(D[c])
        return True
