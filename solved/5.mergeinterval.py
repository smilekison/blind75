class Solution:
    def merge(intervals: list[list[int]]) -> list[list[int]]:
        # print(sorted(intervals))

        intervals.sort(key= lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            # print(start, end)
            lastEnd = output[-1][1]
            # print(lastEnd)
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

    print(merge([ [2,3], [3,6],[8,10],[15,18]]))