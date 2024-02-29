class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        products = [1] * length
        print(products)
        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]
        print(products)

        right = nums[-1]
        for i in range(length-2, -1, -1):
            print('i',i)
            products[i] *= right
            right *= nums[i]
        
        return products