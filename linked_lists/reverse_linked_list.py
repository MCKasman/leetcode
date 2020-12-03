# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Reverse a singly linked list.

        Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL or NULL<-1<-2<-3<-4<-5


        Algorithm
        1. Start from head to the end of list
        2. Make prev equal to None first
        3. Get the next node = head.next
        4. Link head.next = prev
        5. Make prev = head
        6. Make head move to the next node
        """
        prev = None

        while(head is not None):
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev
