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
