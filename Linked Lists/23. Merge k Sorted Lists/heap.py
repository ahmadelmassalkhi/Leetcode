# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

''''''''''''''''''''''''''''''''''''''''''
''' Optimal Solution '''
        
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []

        for list in lists:
            while list != None:
                heapq.heappush(heap, (list.val, list))
                list = list.next

        if len(heap) == 0:
            return None
            
        head = prev = heapq.heappop(heap)[1]
        while heap:
            value,node = heapq.heappop(heap)
            prev.next = node
            prev = node
        prev.next = None # prevent loop (tail.next = None)

        return head
    
''''''''''''''''''''''''''''''''''''''''''
