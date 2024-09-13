# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

''''''''''''''''''''''''''''''''''''''''''''''''''''''

class Solution(object):

    def __init__(self):
        self.copyNodeOf = {}


    def copyList(self, head):
        if not head: return None

        # copy list (values & nexts)
        newNode = Node(head.val)
        newNode.next = self.copyList(head.next)

        # cache copied nodes
        self.copyNodeOf[head] = newNode
        return newNode


    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        copy = self.copyList(head)
        while head:
            if head.random:
                self.copyNodeOf[head].random = self.copyNodeOf[head.random]
            head = head.next
        return copy
    
''''''''''''''''''''''''''''''''''''''''''''''''''''''