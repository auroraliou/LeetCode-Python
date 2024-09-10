# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## Use a queue to store nodes in each level
        if not root:
            return None
        output = []
        q = deque([root])

        while q:
            level = []
            d = len(q)
            for i in range(d):
                ## Get the top node
                root = q.popleft()
                level.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            ## Finish traverse a level
            output.append(level)
        return output

        
