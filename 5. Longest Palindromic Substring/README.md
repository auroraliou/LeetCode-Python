# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

# Pseudocode
1. Create an empty string to store the palindrome and a variable to store answer.
2. A For loop to scan over the string. Now, separate into ODD and EVEN cases.
Check the left and right side from the center.
 Remember to set the bound. 
If the left and right side are the same char, check if the new string is longer than the record.
 If so, update answer.
Update l and r.
3. Return answer substring.


# AC code
```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        subStr = ""
        subStrLen = 0

        for i in range(len(s)):
            ## odd length 
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > subStrLen:
                    subStr = s[l:r+1]
                    subStrLen = r - l + 1
                l -= 1
                r += 1

            ## even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > subStrLen:
                    subStr = s[l:r+1]
                    subStrLen = r - l + 1
                l -= 1
                r += 1
        return subStr

```

