# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)


## Cubic Solution

```
for (i = 0 ... n-1)
    for (j = i .... n-1 )
        for (k = i ....j)
        compute sum 
```

## Quadratic Solution
```
for (i = 0 .... n-1)
    for (j = i ..... n-1)
        curSum += num[j]
```

Do we have to compute every subarray starting at the every single value of the array?

## Linear Solution

Everytime we get a negative prefix, remove it.

### Code
```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
```
