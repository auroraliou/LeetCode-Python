## Advanced Solution

## Advanced Solution

### Idea

Create a variable `count` to calculate occurrences of the current result.
When any non-result numbers appear, `count` minus 1.
Since res must be a majority element.

### Code
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

### Idea
Create a hashmap to store how many times a number has appeared.
The answer will be the number with greatest value.

### Code

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
