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
