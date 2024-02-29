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
        if root == None:
            return True
        queue = collections.deque([root])
        n = 1 #number of nodes of current level
        level = nbOfChildren = 0
        prev = None
        while len(queue) > 0:
            node = queue.popleft()
            n -= 1
            if self.isEven(level) and self.isEven(node.val): return False
            if self.isOdd(level) and self.isOdd(node.val): return False
            if prev != None:
                if self.isEven(level):
                    if not (prev < node.val): return False
                else:
                    if not (prev > node.val): return False
            if node.left != None:
                queue.append(node.left)
                nbOfChildren += 1
            if node.right != None:
                queue.append(node.right)
                nbOfChildren += 1
            if n == 0: # new level
                n = nbOfChildren
                nbOfChildren = 0
                level += 1
                prev = None
            else:
                prev = node.val                
        return True
    
''''''''''''''''''''''''''''''''''''''''''''''''''