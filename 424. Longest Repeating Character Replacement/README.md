# [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)


## Solution using hashmap and sliding window

**Time Complexity:** $O(n)$

### Pseudocode
```
Create a hashmap to store the occurences of each letter.

Traverse though the sliding window.
Update the hashmap

Check if the current window if valid
    if it's invalid, adjest the sliding window from left.
    if it is valid, update the res.
```


```
count.get(s[r], 0)
```
Return the the value of count[s[r]], if the character doesn't exist in our hashmap, just return 0. 

```
max(count.values())
```
Return the max value in count


### AC CODE
```
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {} ## the occurences of each letter in the sliding window.
        res = 0
        l = 0

        for r in range(len(s)):
            ## Update the occurrences of the current letter.
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)  

            ## Check if the window if valid.
            ## If not valid, adjest ptr l.
            if (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res



```
