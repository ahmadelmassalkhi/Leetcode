# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


''''''''''''''''''''''''''''''''''''''''''''''''''''''

class Solution(object):

    def __init__(self):
        self.cache = {}

    def createCopy(self, head):
        if head == None: return None
        self.cache[head] = Node(head.val)
        self.cache[head].next = self.createCopy(head.next)
        return self.cache[head]

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        copy = self.createCopy(head)
        while head:
            if head.random:
                self.cache[head].random = self.cache[head.random]
            head = head.next
        return copy

''''''''''''''''''''''''''''''''''''''''''''''''''''''