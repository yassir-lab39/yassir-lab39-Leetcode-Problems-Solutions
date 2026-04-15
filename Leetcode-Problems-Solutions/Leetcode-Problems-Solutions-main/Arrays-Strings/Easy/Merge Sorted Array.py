class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        L = []
        while i < m and j < n :  
            if nums1[i] < nums2[j] :
                L = L + [nums1[i]]
                i += 1
            elif nums1[i] >= nums2[j] :
                L = L + [nums2[j]]   
                j += 1
        if i == m :
            nums1[0:i+j] = L 
            nums1[i+j:] = nums2[j:]
        if j == n :
            nums1[i+j:] = nums1[i:m]  
            nums1[0:i+j] = L         
 
