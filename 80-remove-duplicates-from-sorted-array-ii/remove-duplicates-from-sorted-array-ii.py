class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i=0
        z=0
        b=[]
        c=0
        nums.sort()
        x = len(nums)

        if x > 1:
            while i < x:
                    if i==0:
                        b.append(nums[z])
                        i+=1
                    if nums[z] == nums[i]:
                        c += 1
                        if c==1:
                            b.append(nums[z])
                            print(b)
                    else:
                        c=0
                        z = i
                        b.append(nums[z])
                    i+=1
        else:
            b.append(nums[i])
        nums[:] = b