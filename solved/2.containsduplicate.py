class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        
        newValue = set(nums)

        if len(nums) == len(newValue):
            return False
        return True

    print(containsDuplicate([1,2,3,4,1]))