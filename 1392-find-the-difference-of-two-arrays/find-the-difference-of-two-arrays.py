class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1 = set(nums1)
        nums2 = set(nums2)

        a = nums1- nums2
        b = nums2 - nums1  
        print(a) 
        print(b)
        x=[]
        x.append(list(a))
        x.append(list(b))
        return x