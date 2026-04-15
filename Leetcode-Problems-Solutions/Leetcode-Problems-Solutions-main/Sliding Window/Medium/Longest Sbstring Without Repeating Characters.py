class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "" :
            return 0
        j = 0
        nb = 1
        left, right = 0, 1
        while left < len(s) and right < len(s) :
            for i in range(left,right) :
                if s[i] != s[right] :
                    j += 1
                else :
                    j = 0
            if nb < j+1 :
                nb = j+1
            right += 1
            left = right-j-1
            j = 0
        return nb
