# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = list1
        r = list2
        dummy = ListNode(0)
        prev = dummy

        while l or r:
            if l and r:
                if l.val < r.val:
                    prev.next = l
                    prev = prev.next
                    l = l.next
                elif l.val >= r.val:
                    prev.next = r
                    prev = prev.next
                    r = r.next
            else:
                if not l:
                    prev.next = r
                elif not r:
                    prev.next = l
                break
        
        return dummy.next


#                 l
# 1 -> 2 -> 4 -> None

# r
# 6 -> 7 -> 8 -> None

#                     prev
# dummy -> 1  -> 2  ->  4


#           p     l
# 1 -> 2 -> 4 -> None

#           r
# 1 -> 3 -> 5 -> None

# 1 -> 1 -> 2 -> 3 -> 4 