# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

''''''''''''''''''''''''''''''''''''''''''

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = tail = None
        while len(lists) > 0:
            
            # find min head
            min_idx = -1
            for i,head in enumerate(lists):
                if head == None:
                    continue
                if min_idx == -1:
                    min_idx = i
                elif head.val < lists[min_idx].val:
                    min_idx = i

            # all lists are empty OR were traversed to the end
            if min_idx == -1:
                return result

            # append node
            if result == None:
                result = lists[min_idx]
            else:
                tail.next = lists[min_idx]
            tail = lists[min_idx]

            # move
            lists[min_idx] = lists[min_idx].next
            if lists[min_idx] == None:
                lists.pop(min_idx)
        return result
    
''''''''''''''''''''''''''''''''''''''''''
