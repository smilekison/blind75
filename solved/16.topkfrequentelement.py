import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count the frequency of each element using a hash map
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Use a min-heap to store the top k frequent elements
        heap = []
        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif count > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))
        
        # Step 3: Return the elements in the heap
        return [num for count, num in heap]


# https://leetcode.com/problems/top-k-frequent-elements/solutions/3246298/347-time-91-58-solution-with-step-by-step-explanation