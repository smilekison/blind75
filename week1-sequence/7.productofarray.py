class Solution:
    def productExceptSelf(nums: list[int]) -> list[int]:
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *=postfix
            postfix *= nums[i]

        return res

    print(productExceptSelf([-1,1,0,-3,3]))