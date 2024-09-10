class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## use binary search
        ## cut the list into two half (left and right)
        ## check if the target is greater than or less than or equal to
        ## the mid point
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            ## target is either in the left or non-exist
            if nums[mid] > target:
                ## update right pointer
                right = mid - 1       
            else:
                left = mid + 1
        return left
