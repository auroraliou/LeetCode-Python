class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
       
        n = len(s) - 1
        last = s[n]
        while last == '':
            last = s[n]
            
            n -= 1
        
        return len(last)
        
