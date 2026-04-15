class Solution:
    def romanToInt(self, s: str) -> int:
        S = 0
        if s[-1]=="I" :
            S+=1
        if s[-1]=="V" :
            S+=5
        if s[-1]=="X" :
            S+=10
        if s[-1]=="L" :
            S+=50
        if s[-1]=="C" :
            S+=100
        if s[-1]=="D" :
            S+=500
        if s[-1]=="M" :
            S+=1000
        if len(s) == 1 :
            return S    
        for i in range(len(s)-1) :
            if s[i]=="I" and ( s[i+1]=="V" or s[i+1]=="X" ) :
                S-=2
            if s[i]=="X" and ( s[i+1]=="L" or s[i+1]=="C" ) :
                S-=20
            if s[i]=="C" and ( s[i+1]=="D" or s[i+1]=="M" ) :
                S-=200
            if s[i]=="I":
                S+=1
            if s[i]=="V" :
                S+=5
            if s[i]=="X" :
                S+=10
            if s[i]=="L" :
                S+=50
            if s[i]=="C":
                S+=100
            if s[i]=="D" :
                S+=500
            if s[i]=="M" :
                S+=1000
        return S
