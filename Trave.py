class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node):
            if not node:
                return
            
            print(node.val)
            result.append(node.val)
            
            traverse(node.left)
            traverse(node.right)
            
        traverse(root)
        return result
    
    # I used a recursive approach to perform a preorder traversal of the binary tree. I defined a helper function traverse that takes a node as input. If the node is not None, I print its value and append it to the result list. Then, I recursively call traverse on the left and right children of the node. I return the result list containing the values in preorder traversal order.