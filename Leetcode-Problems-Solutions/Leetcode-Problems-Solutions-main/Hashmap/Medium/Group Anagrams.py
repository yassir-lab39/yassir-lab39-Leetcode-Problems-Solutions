class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        L = []
        for i in range(n) :
            D = dict()
            for c in strs[i] :
                if c in D :
                    D[c] += 1
                else :
                    D[c] = 1
            L.append(D)
        res = []
        index_checked = []
        i = 0
        while i < n :
            if i not in index_checked :
                res.append([strs[i]])
                index_checked.append(i)
                for j in range(i+1,n) :
                    if L[j] == L[i] :
                        res[-1].append(strs[j])
                        index_checked.append(j)
            i += 1
        return res
