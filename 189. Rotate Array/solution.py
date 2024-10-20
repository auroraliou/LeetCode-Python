class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        alt = []
        for i in range(len(nums)):
            j = (i + k) % len(nums)
            alt.insert(j,nums[i])

        for i in range(len(nums)):
            nums[i] = alt[i]
        
