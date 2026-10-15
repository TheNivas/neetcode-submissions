# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None
        else:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            next1 = l1.next if l1 else None
            next2 = l2.next if l2 else None
            sum = v1 + v2 + carry
            carry = sum // 10

            return ListNode(
                sum % 10,
                self.addTwoNumbers(next1, next2, carry)
            )

        