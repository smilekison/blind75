class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        newValue = {}

        for i, v in enumerate(nums):
            compliment = target - v
            if compliment in newValue:
                return [newValue[compliment], i]
            newValue[v] = i
        
        return [newValue[i], i]
    
    print(twoSum([2,7,11,15], 26))