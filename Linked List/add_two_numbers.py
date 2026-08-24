class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        dummy = ListNode(0)
        current = dummy

        carry = 0

        while p1 or p2 or carry:

            digit1 = p1.val if p1 else 0
            digit2 = p2.val if p2 else 0

            total = digit1 + digit2 + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if p1:
                p1 = p1.next

            if p2:
                p2 = p2.next

        return dummy.next