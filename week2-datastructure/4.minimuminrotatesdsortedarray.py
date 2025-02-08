class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
                
        return nums[left]
    

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/5149850/fastest-100-easiest-shortest-binary-search-multiple-langs