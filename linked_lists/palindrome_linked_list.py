# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool

        Given a singly linked list, determine if it is a palindrome.

        Algorithm:
        1. Reverse first half of linked list
        2. Create fast and slow pointers, fast moves 2 steps while slow moves 1 step
        3. Compare first half and second half of linked list and see if it is a palindrome
        4. Stop when reversed linked list pointer equal to None
        """

        # variable to store reversed linked list
        rev = None
        
        # slow and fast pointers start at head
        slow = fast = head

        # while fast and fast. next is not None
        while fast and fast.next:
            # move fast pointer
            fast = fast.next.next

            # move slow pointer and reverse first half of linked list
            rev, rev.next, slow = slow, rev, slow.next

        # fast is at the end, move slow one step further for comparison(cross middle one)
        if fast:
            slow = slow.next

         # compare the reversed first half with the second half
        while rev is not None:
            if(rev.val == slow.val):
                slow = slow.next
                rev = rev.next
            else:
                return False

        return True
