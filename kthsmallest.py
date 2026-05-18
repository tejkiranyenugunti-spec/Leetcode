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
# I used a stack to store the nodes in the current path. I used a while loop to traverse the tree.
#I went through the left subtree, then I popped the latest node from the stack to check for the smallest value.
