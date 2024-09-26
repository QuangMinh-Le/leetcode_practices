# Definition for singly-linked list.
from typing import Optional


class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
class Solution:
   def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
      # Create a dummy node to handle cases where the head needs to be removed
      dummy = ListNode(0)
      dummy.next = head
      current = dummy
      # Traverse the list
      while current.next is not None:
          if current.next.val == val:
              # Remove the node by skipping it
              current.next = current.next.next
          else:
              # Move to the next node
              current = current.next
      # Return the updated list starting from the real head
      return dummy.next