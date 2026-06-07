from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def mirror(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return (
                left.val == right.val and
                mirror(left.left, right.right) and
                mirror(left.right, right.left)
            )

        return mirror(root.left, root.right)
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(Solution().isSymmetric(root))

# I used recursive function to check if the left and right subtrees are mirror images of each other. I compared the values of the nodes and recursively checked the left and right children of both subtrees. If all checks pass, I returned the result. 