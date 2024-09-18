# [268. Missing Number](https://leetcode.com/problems/missing-number/description/)


## Solution using loop
Time Complexity: $O(n)$
Space Complexity: $O(1)$
```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        m = max(nums)
        for i in range(l):
            if i in nums:
                continue
            else:
                return i
        return m + 1
        #print(l, m)
```

## Solution using sum
Time Complexity: $O(n)$
Space Complexity: $O(1)$
```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
```

## Solution using XOR
Time Complexity: $O(n)$
Space Complexity: $O(1)$
```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res
```
