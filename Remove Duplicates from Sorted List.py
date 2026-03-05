# Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = head
        ans = prev
        if head is None:
            return 
        if head.next:
            head = head.next

            while head:
                if head.val != prev.val:
                    new = ListNode(head.val)
                    prev.next = new
                    prev = prev.next
                else:
                    prev.next = None
                head = head.next

            return ans
        else:
            return head
        

        # optimized solution
        # if not head:
        #     return
        
        # curr = head
        # while curr and curr.next:
        #     if curr.val == curr.next.val:
        #         curr.next = curr.next.next
        #     else:
        #         curr = curr.next
        # return head