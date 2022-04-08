
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
