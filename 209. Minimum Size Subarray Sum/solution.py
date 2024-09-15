class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, sum = 0, 0
        result = float("inf")
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                result = min(result, r - l + 1)
                sum -= nums[l]
                l += 1
        return 0 if result == float("inf") else result
