class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict(int)  
        for num in nums:
            m[num] += 1
        return list(m.keys())[list(m.values()).index(max(m.values()))]