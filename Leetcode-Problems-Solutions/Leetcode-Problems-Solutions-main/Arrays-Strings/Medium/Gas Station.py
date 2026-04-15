class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        L = [a - b for a, b in zip(gas, cost)]
        if sum(L) < 0 :
            return -1
        i = 0
        while i < len(L) :
            index = (i+1) % len(L)
            fuel = L[i]
            while index != i and fuel > 0 :
                fuel += L[index]  
                index = (index+1) % len(L) 
            if index == i and fuel >= 0 :
                return index 
            if fuel <= 0 :
                i = index  
        return -1           
