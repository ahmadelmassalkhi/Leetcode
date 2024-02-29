# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

''''''''''''''''''''''''''''''''''''''''''''''''''

import collections

class Solution(object):

    def isOdd(self, number):
        return number % 2
    def isEven(self, number):
        return not self.isOdd(number)
    
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        if self.isEven(root.val): return False
        
        previous = None
        queue = collections.deque([[root, True]]) # [node, isEvenLevel]
        while len(queue) > 0:
            node, isEvenLevel = queue.popleft()
            if isEvenLevel:
                if not self.isOdd(node.val): return False
                if previous and previous[1] and not (previous[0].val < node.val): return False
                if node.left: queue.append([node.left, False])
                if node.right: queue.append([node.right, False])
            else: # odd level
                if not self.isEven(node.val): return False
                if previous and not previous[1] and not (previous[0].val > node.val): return False
                if node.left: queue.append([node.left, True])
                if node.right: queue.append([node.right, True])
            previous = [node, isEvenLevel]
        return True

        
    
''''''''''''''''''''''''''''''''''''''''''''''''''