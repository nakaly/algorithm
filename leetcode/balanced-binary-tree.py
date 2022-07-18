from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        (resultHeight, isBalanced) = self.calcBalanced(root)
        return isBalanced


    def calcBalanced(self, root: Optional[TreeNode]):
        if root is None:
            return (0, True)
        leftHeight = 0
        leftResult = True
        # print("node", root.val)
        if not root.left is None:
            (leftHeight, leftResult) = self.calcBalanced(root.left)
            # print("node", root.val, ":leftHeight", leftHeight)
            # print("node", root.val, ":leftResult", leftResult)
        rightHeight = 0
        rightesult = True
        if not root.right is None:
            (rightHeight, rightesult) = self.calcBalanced(root.right)
            # print("node", root.val, ":rightHeight", rightHeight)
            # print("node", root.val, ":rightResult", rightesult)
        return (max(leftHeight, rightHeight)+1, abs(leftHeight-rightHeight) <= 1 and leftResult and rightesult)


if __name__ == '__main__':
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)

    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(22)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(33)
    # root.left.left.left = TreeNode(4)
    # root.left.left.right = TreeNode(44)
    root = None
    print(Solution().isBalanced(root))
