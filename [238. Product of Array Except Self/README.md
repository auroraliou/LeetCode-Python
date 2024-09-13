# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)


[Ref](https://www.youtube.com/watch?v=bNvIQI2wAjk&t=409s)

## Explanation
Use the idea of prefix and postfix to solve the problem.


## AC Code

```
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
      
```

```
res = [1] * (len(nums))
```
if len(nums) = 4, create [1, 1, 1, 1]

![IMG_1137](https://hackmd.io/_uploads/r16_iU-T0.jpg)
