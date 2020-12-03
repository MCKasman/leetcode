# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing         together the nodes of the first two lists.

        Algorithm
        1. Create a new linked list that is empty
        2. Create pointers that iterate through the new linked list and other 2 linked lists
        3. Compare numbers in linked list, whichever is smaller is put into the new linked list first
        4. Update pointers
        """

        head = ListNode(0)
        ptr = head

        while True:
            if l1 is None and l2 is None:
                return

            elif l1 is None:
                ptr.next = l2
                break

            elif l2 is None:
                ptr.next = l1
                break

            else:
                if(l1.val < l2.val):
                    smaller_val = l1.val
                    l1 = l1.next
                else:
                    smaller_val = l2.val
                    l2 = l2.next

            new_node = ListNode(smaller_val)
            ptr.next = new_node
            ptr = ptr.next

        return head.next
