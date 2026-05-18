# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1

            if k == 0:
                return root.val

            root = root.right

obj = Solution()



print("\nFinal Answer:", obj.kthSmallest(root, 1))

# 230. Kth Smallest Element in a BST - LC230
# I used stack to store the nodes in the current path. I used while loop to traverse the tree.
# I go through the left sub tree then i ussed to pop the latest node  frrom the stack fot checking the smallest value.
