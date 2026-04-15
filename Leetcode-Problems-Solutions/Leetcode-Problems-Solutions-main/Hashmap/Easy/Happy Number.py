class Solution:
    def isHappy(self, n: int) -> bool:
        s = 0
        D = set()
        while s != 1 :
            s = 0
            while n > 0 :
                s += (n % 10)**2
                n = n // 10
            if s in D :
                return False
            D.add(s)
            n = s
        return True
            
