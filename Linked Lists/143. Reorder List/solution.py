# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverse(self, head):
        if not head or not head.next:
            return head
        newHead = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return newHead

    def weaveLists(self, list1, list2, list1Turn):
        if not list1 or list1==list2:
            return list2
        if not list2:
            return list1

        if list1Turn:
            list1.next = self.weaveLists(list1.next, list2, False)
            return list1
        else:
            list2.next = self.weaveLists(list1, list2.next, True)
            return list2

        

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = fast = prev = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = self.reverse(slow.next)
        slow.next = None # slow is tail of left list

        return self.weaveLists(head, head2, True)

        
