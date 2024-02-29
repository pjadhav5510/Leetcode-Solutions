class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        kk = ''.join(map(str, nums))

        ll = kk.split('0')
        max_len = 0
        for i in ll:
            if len(i) > max_len:
                max_len = len(i)
        return(max_len)