# [66. Plus One](https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150)



```
## 999 + 1 = 1000
## 889 + 1 = 890
## 899 + 1 = 900
## 887 + 1 = 888
```


## Tip
```digits = digits[::-1]``` 
Reverse digits.


## CODE
```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry, i = 1, 0

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else: 
                    digits[i] += 1
                    carry = 0
            else: 
                digits.append(1)
                carry = 0
            i += 1
        return digits[::-1]
```
