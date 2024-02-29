class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=[]
        b=[]
        for i,num in enumerate(nums):
            print("num: "+str(num))
            if num == 0:
                a.append(num)
            else:
                b.append(num)
        print("nums: "+ str(b) + " a: "+str(a))
        nums.clear()
        for x in b:
            nums.append(x)
        for x in a:
            nums.append(x)