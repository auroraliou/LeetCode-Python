class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        if n == 1:
            return True

        while n not in visit:
            visit.add(n)
            n = self.sumOfSqr(n)

            if n == 1:
                return True
                 
        return False

    def sumOfSqr(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n //= 10
        return output
