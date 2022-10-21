


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        parent = None
        grandParent = None
        result = [0]
        def traverse(node, p, gP, r):
            if node is None:
                return
            if gP is not None and gP % 2 == 0:
                r[0] += node.val
            gP = p
            p = node.val
            traverse(node.left, p, gP, r)
            traverse(node.right, p, gP, r)

        traverse(root, parent, grandParent, result)
        return result


if __name__ == '__main__':
    root = TreeNode(
        6,
        TreeNode(
            7,
            TreeNode(
                2,
                TreeNode(9)
            ),
            TreeNode(
                7,
                TreeNode(1),
                TreeNode(4)
            )
        ),
        TreeNode(
            8,
            TreeNode(1),
            TreeNode(
                3,
                None,
                TreeNode(5)
            )
        )
    )

    print(Solution().sumEvenGrandparent(root))