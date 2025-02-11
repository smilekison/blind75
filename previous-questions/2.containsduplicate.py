class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        # if len(nums) == len(set(nums)):
        #     return True
        # return False

        char_set = set()

        for v in nums:
            if v in char_set:
                return True
            char_set.add(v)
        return False