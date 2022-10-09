"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    1) Make list of nodes
    2) Recursive
    """

    # Using lists
    def addTwoNumbersList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        over = 0
        while True:
            if l1 is None and l2 is None and over == 0:
                break

            val_1 = 0 if l1 is None else l1.val
            val_2 = 0 if l2 is None else l2.val

            l1 = ListNode() if l1 is None else l1
            l2 = ListNode() if l2 is None else l2

            sum_nodes_val = val_1 + val_2 + over
            over = sum_nodes_val // 10

            if sum_nodes_val > 9:
                sum_nodes_val %= 10

            nodes.append(ListNode(val=sum_nodes_val))
            l1 = l1.next
            l2 = l2.next

        for node_idx in range(1, len(nodes)):
            nodes[node_idx - 1].next = nodes[node_idx]

        if len(nodes) != 0:
            return nodes[0]

        return ListNode()

    # Recursive
    def addTwoNumbersRec(self, l1: Optional[ListNode], l2: Optional[ListNode], over: int = 0) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        val1 = 0 if l1 is None else l1.val
        val2 = 0 if l2 is None else l2.val
        l1 = ListNode() if l1 is None else l1
        l2 = ListNode() if l2 is None else l2

        value = val1 + val2 + over
        next_over = value // 10

        if value > 9:
            value %= 10

        if next_over != 0:
            if l1.next is None:
                l1.next = ListNode()
            if l2.next is None:
                l2.next = ListNode()

        curr_res = ListNode(value)
        curr_res.next = self.addTwoNumbersRec(l1.next, l2.next, over=next_over)

        return curr_res
