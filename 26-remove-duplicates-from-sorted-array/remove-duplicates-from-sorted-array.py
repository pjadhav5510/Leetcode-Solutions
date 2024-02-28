class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i=0
        z=0
        b=[]
        c=0
        nums.sort()
        x = len(nums)

        if x != 1:
            while i < x:
                    if nums[z] == nums[i]:
                        print(z, i)
                        c += 1
                        print(c)
                    else:
                        c=0
                        b.append(nums[z])
                        z = i
                    i+=1
            b.append(nums[z])
        else:
            b.append(nums[i])
        nums[:] = b