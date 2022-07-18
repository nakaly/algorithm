
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        stack = []
        while current != None :
            stack.append(current.val)
            current = current.next
        resultRoot = None
        if len(stack) > 0:
            result = ListNode(stack.pop())
            resultRoot = result
        while len(stack) > 0:
            result.next = ListNode(stack.pop())
            result = result.next
        return resultRoot


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)

    result = Solution().reverseList(root)

    print(result.val)
    print(result.next.val)
    print(result.next.next.val)