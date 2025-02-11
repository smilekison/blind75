class Solution:
    def merge(intervals: list[list[int]]) -> list[list[int]]:  # Method to merge overlapping intervals
        intervals.sort(key=lambda i: i[0])  # Sort intervals based on the start value
        output = [intervals[0]]  # Initialize the output list with the first interval

        for start, end in intervals[1:]:  # Iterate through the remaining intervals
            lastEnd = output[-1][1]  # Get the end value of the last interval in the output list
            if start <= lastEnd:  # If the current interval overlaps with the last interval in the output
                output[-1][1] = max(lastEnd, end)  # Merge the intervals by updating the end value
            else:
                output.append([start, end])  # If no overlap, add the current interval to the output list
        
        return output  # Return the merged intervals

    print(merge([[2, 3], [3, 6], [8, 10], [15, 18]]))  # Test the function with an example


'''
Summary

    DSA Used: Sorting, Greedy Algorithm.

    Time Complexity: O(n log n).

    Space Complexity: O(n).

'''