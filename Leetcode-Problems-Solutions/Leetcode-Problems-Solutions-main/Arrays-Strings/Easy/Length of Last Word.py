class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s)-1
        while i >= 0 :
            if s[i] != ' ' :
                length += 1
            if s[i] == ' ' and length != 0 :
                i = 0
            i -= 1
        return length

