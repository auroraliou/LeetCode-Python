# [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## Iterative Solution

Time Complexity: $O(n)$
```
prev, curr = None, head

while curr: ## keep going until reach the end of the list
    ## Reverse the pointer
```

### AC CODE
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr ## the next interation's prev is curr
            curr = nxt ## shift curr 
        return prev
        
```


## Recursive Solution

Time Complexity: $O(n)$, since we are visiting each node only once.

### AC CODE
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
```
