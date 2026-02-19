class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)


tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)


sol = Solution()
print(sol.isSameTree(tree1, tree2))
