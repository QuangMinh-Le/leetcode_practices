# Definition for singly-linked list.
from typing import Optional


class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
      
class Solution:
   def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      l1Val = []
      l2Val = []
      while l1:
         l1Val.append(l1.val)
         l1 = l1.next
      while l2:
         l2Val.append(l2.val)
         l2 = l2.next
      l1Val.reverse()
      l2Val.reverse()
      
      rev1 = "".join(str(num) for num in l1Val)
      rev2 = "".join(str(num) for num in l2Val)
      
      total_sum = int(rev1) + int(rev2)
      prev = None
      for digit in str(total_sum):
          node = ListNode(int(digit))
          node.next = prev
          prev = node
      return prev
         
         