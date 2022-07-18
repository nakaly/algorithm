from typing import Optional
import queue
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if node.val == val:
                return node
            if not node.left is None:
                q.put(node.left)
            if not node.right is None:
                q.put(node.right)
        return None




if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(22)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(33)
    # root.left.left.left = TreeNode(4)
    # root.left.left.right = TreeNode(44)
    print(Solution().searchBST(root, 2))

