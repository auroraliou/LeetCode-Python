## Advanced Solution

```
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res
```

## Hashmap Solution 

```
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = 0
        hashmap = {}
        bar = len(nums) // 2
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
                print(hashmap[nums[i]])
            else:
                hashmap[nums[i]] = 1
            if hashmap[nums[i]] > bar:
                return nums[i]
```
