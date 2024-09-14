# [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)


## Solution Using Heap

### Time Complexity 
Time complexity: $O(n + klog(n))$
Making a heap takes $O(n)$
Poping an element from heap takes $log(n)$


## Solution Using Quick Select

### Time Complexity 
Average case: $O(n)$
Worst case: $O(n^2)$

### Explanation

In an ascending sorted array, the $k$th largest element is in the index $len(nums) - k$.
E.g., in a size 6 sorted list, the 2th largest is in list[4]

```
Set the rightmost element as pivot.
Use p as the pointer to indicate where to place nums less than pivot.
for i in range(l, r):
    if nums[i] <= pivot:
        swap nums[i] and nums[p]
        p increament 1
    After traverse the entire list, swap pivot and nums[p]
    So now, the left side of p is less than pivot,
    the right side of p is greater than pivot.
    
    
    if p > k:
        sort the left side again (kth largest is now in the left side of p)
    elif p < k:
        sort the right side (kth largest is now in the right side of p)
    else:
        kth largest num is at pos p
        
    Call quickSelect() in main function


```


### Time Limit Exceeded
```
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            ## p is a pointer indicate the index 
            ## to store the nums less than or equal to pivot.
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]

            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else:       return nums[p]

        return quickSelect(0, len(nums) - 1) 
```



## AC CODE
```
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(l: int, r: int) -> int:
            if l == r:
                return nums[l]
            i, j = l - 1, r + 1
            x = nums[(l + r) >> 1]
            while i < j:
                while 1:
                    i += 1
                    if nums[i] >= x:
                        break
                while 1:
                    j -= 1
                    if nums[j] <= x:
                        break
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            if j < k:
                return quick_sort(j + 1, r)
            return quick_sort(l, j)

        n = len(nums)
        k = n - k
        return quick_sort(0, n - 1)
```

