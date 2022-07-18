
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorderTraversalRec(root, result)
        return result


    def preorderTraversalRec(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        result.append(root.val)
        self.preorderTraversalRec(root.left, result)
        self.preorderTraversalRec(root.right, result)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().preorderTraversal(root))