# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)


Time Complexity: $O(n)$


## AC CODE

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        return result
```


https://www.w3schools.com/python/python_sets.asp
Look at **The set() Constructor**



:::spoiler ```while s[r] in charSet:```  why use ```while``` instead of ```if```?
use ```while``` so that we can remove all repeating chars.
if we use ```if```, only one repeating char can be removed.
