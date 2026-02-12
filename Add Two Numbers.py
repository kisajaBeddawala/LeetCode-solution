# Add Two Numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1 = l1
        head2 = l2
        remain = 0
        prev = None  # to keep track of the last node in the result list

        # work with both lists until one of them runs out
        while head1 and head2:
            tot = head1.val + head2.val
            if tot >= 10:
                if remain == 0:
                    head1.val = tot - 10
                else:
                    tot += remain
                    head1.val = tot - 10
                remain = 1
            else:
                tot += remain
                if tot >= 10:
                    head1.val = tot - 10
                else:
                    head1.val = tot
                    remain = 0

            prev = head1
            head1 = head1.next
            head2 = head2.next

        # if head1 still has nodes left, continue adding the carry
        while head1:
            tot = head1.val + remain
            if tot >= 10:
                head1.val = tot - 10
                remain = 1
            else:
                head1.val = tot
                remain = 0
                break

            prev = head1
            head1 = head1.next

        # if head2 still has nodes left, attach it to the result and continue adding the carry
        if head2:
            prev.next = head2
            head1 = head2  # continue with head2 as the remaining list so we don't want to create new nodes for head2

            # after that we can use previous loop to add the carry to the remaining nodes of head2
            while head1:
                tot = head1.val + remain
                if tot >= 10:
                    head1.val = tot - 10
                    remain = 1
                else:
                    head1.val = tot
                    remain = 0
                    break

                prev = head1
                head1 = head1.next

        # if there is still a carry left after processing both lists, we need to add a new node with value 1    
        if remain == 1:
            prev.next = ListNode(1)

        return l1 # not return head1 because we need to return root of the result list which is l1
            