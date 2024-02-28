class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n = nums1 + nums2
        n.sort()
        if len(n)%2 == 0:
            return (n[int(len(n)/2) - 1] + n[int(len(n)/2)])/2
        else:
            return n[int(len(n)//2)]/1