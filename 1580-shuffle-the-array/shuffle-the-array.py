class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        j=0

        b=[]
        for i in range(int(len(nums)/2),len(nums)):
            b.append(nums[j])
            b.append(nums[i])
            j +=1
        return b