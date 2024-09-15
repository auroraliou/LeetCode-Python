class Solution:
    def isPalindrome(self, x: int) -> bool:

        s = str(x)
        
        ## When s is even
        # if len(s) % 2 == 0:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

        # ## When s is odd
        # elif len(s) % 2 == 1:
