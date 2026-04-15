class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nb = 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[nb] :
                nb += 1
                i += 1
            else :
                i -= (nb-1)
                nb = 0
            if nb == len(needle) :
                return i-nb
        return -1
