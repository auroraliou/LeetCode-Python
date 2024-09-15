class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        binary = binary[2:]
        ans = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                ans += 1
            # print(binary[i])
        
        return ans
