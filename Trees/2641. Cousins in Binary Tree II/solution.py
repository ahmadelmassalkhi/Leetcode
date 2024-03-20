from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root: return None

        queue = deque([(root, 0)])  # Store node and its parent sum
        d = {root: TreeNode()}  # Map original nodes to their corresponding result nodes

        nbOfChildren = n = 0
        prev_sum = current_sum = 0
        while queue:
            node, local_sum = queue.popleft()
            d[node].val = prev_sum - local_sum
            n -= 1

            # get current local sum (sum of child nodes)
            s = 0 
            if node.left: s += node.left.val
            if node.right: s += node.right.val
            current_sum += s

            # add child nodes if exist
            if node.left:
                queue.append((node.left, s))
                d[node].left = d[node.left] = TreeNode()
                nbOfChildren += 1
            if node.right:
                queue.append((node.right, s))
                d[node].right = d[node.right] = TreeNode()
                nbOfChildren += 1

            # end of current level
            if n <= 0:
                n = nbOfChildren
                nbOfChildren = 0

                prev_sum = current_sum
                current_sum = 0
        return d[root]
