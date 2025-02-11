class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:  # Method to find two indices whose values add up to the target
        arr = {}

        for i, v in enumerate(nums):
            comp = target -v
            if comp in arr:
                return [arr[comp], i]
            arr[v] = i
        return [arr[v], i]