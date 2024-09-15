class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i, j = 0, 0
        while j < len(nums):
            if j < len(nums) - 1 and nums[j + 1] - nums[j] == 1:
                j = j + 1
            else:
                if i == j:
                    ans.append(str(nums[j]))
                    j = j + 1
                    i = j
                else:
                    ans.append(str(nums[i]) + "->" + str(nums[j]))
                    j = j + 1
                    i = j
        return ans
