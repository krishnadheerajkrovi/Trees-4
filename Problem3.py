'''
1. Identify the root node for which p &q are children or one of p/q is a root.
2. We begin by checking if root is one of both the nodes, in that case return root.
3. Else we check the left and right children for p and q. 
4. If both children are found to be p and q, we return this root node as LCA; either p or q found in any child, we return that child. 

TC: O(n)
SC: O(h) 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return None
        
        if root == p or root==q:
            return root
        
        l=self.lowestCommonAncestor(root.left,p,q)
        r=self.lowestCommonAncestor(root.right,p,q)

        if l and r:
            return root
        else:
            return l or r

