
# [1. Two Sum](https://leetcode.com/problems/two-sum/description/)



# Two-pass Hash Table


```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
                
```

 <font color="#f5a142">List[int]</font>

```hashmap[nums[i]] = i```
ie.
nums = [3, 5, 6, 8]
hashmap[3] = 0
hashmap[5] = 1
hashmap[6] = 2
hashmap[8] = 3


```if complement in hashmap and hashmap[complement] != i:```
Check if the qualified number is itself.



# Brute Force


```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
```

* Time complexity: $O(n^2)$.
* Space complexity: $O(1)$.





```def twoSum(self, nums: List[int], target: int) -> List[int]:```

What are the proposes of ```nums: List[int]```, ```target: int``` and ```-> List[int]```

Original:
``` def twoSum(self, nums, target)```

Python has introduced type hinting, which mean we could hinting the type of variable, this was done by doing variable: type (or parameter: type), so for example target is a parameter, of type integer.

the arrow (->) allows us to type hint the return type, which is a list containing integers.

