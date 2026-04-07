# Problem: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/
# Difficulty: Medium
# Topic: Linked List

# Approach:
# Traverse both lists, add digits with carry, and create new linked list

# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy 
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            cur.next = ListNode(val)
            cur = cur.next 

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
