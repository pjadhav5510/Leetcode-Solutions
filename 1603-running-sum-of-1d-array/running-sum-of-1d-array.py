class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        j,i=0,0
        b=[]
        for i in range(len(nums)):
            if i==0:
                b.append(nums[i])
                print(i)
            else:
                b.append(nums[i] + b[j])
                print(nums[i],nums[j])
                j +=1
                
        return b
            