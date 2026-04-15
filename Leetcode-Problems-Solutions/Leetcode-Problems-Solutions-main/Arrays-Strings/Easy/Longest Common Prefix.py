class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        if s == "" :
            return s
        for i in range(1, len(strs)) :
            if strs[i] == "" :
                return ""
            if s[0] != strs[i][0] :
                return ""
            for j in range(0,len(s)) :
                if j >= len(strs[i]) or s[j] != strs[i][j]  :
                    s = s[:j]
                    break
        return s
