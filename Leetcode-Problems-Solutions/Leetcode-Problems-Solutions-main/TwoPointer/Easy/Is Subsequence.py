class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 :
            return True
        left_t, right_t = 0, len(t)-1
        left_s, right_s = 0, len(s)-1
        while left_t <= right_t :
            if t[left_t] == s[left_s] :
                left_s += 1
            if t[right_t] == s[right_s] and ( right_t != left_t or t[right_t] != s[left_s-1] ):
                right_s -= 1
            left_t += 1 
            right_t -= 1
            if left_s > right_s :
                return True 
        return False
