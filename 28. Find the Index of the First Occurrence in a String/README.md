# [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150)



## Pseudocode
```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i + j] !+ needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
```

```
for i in range(len(haystack) + 1 - len(needle))
```

Take `haystack = "leetcode"`, `needle = "leeto"` for example, if `i = 4` and `j = 0`,
it is impossible that the remaining string contains needle, since the length is not enough.


### Time Complexity: $O(m·n)$
Dominated by the nested for-loop


## AC CODE
```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

```
