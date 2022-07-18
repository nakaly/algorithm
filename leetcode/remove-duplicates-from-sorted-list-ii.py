
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        result_head = None
        current_head = head
        prev = None
        while current_head is not None:
            if prev != current_head.val:
                prev = current_head.val
                if result_head is None:
                    result = ListNode(current_head.val)
                    result_head = result
                else:
                    result_head.next = ListNode(current_head.val)
                    result_head = result_head.next
            current_head = current_head.next
        return result

if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(2)
    root.next.next.next = ListNode(4)
    result = Solution().deleteDuplicates(root)

    print(result.val)
    print(result.next.val)
    print(result.next.next.val)