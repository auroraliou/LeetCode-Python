# [57. Insert Interval](https://leetcode.com/problems/insert-interval/)



```
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda i : i[0])
        ##print(intervals)

        output = [intervals[0]]

        for start, end in intervals[1: ]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])


        return output
        
```
