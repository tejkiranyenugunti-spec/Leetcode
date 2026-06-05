class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    left_same = is_same_tree(p.left, q.left)
    right_same = is_same_tree(p.right, q.right)

    return left_same and right_same


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(is_same_tree(p, q))

# I used  binary tree traversal to compare the values of the nodes in both trees. I checked if both nodes are None, if one of them is None, and if their values are different. If all checks pass, I recursively compared the left and right subtrees.