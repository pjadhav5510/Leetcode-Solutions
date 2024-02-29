class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = Counter(nums)

        for word, count in x.items():
            if count == 1:
                return word
        