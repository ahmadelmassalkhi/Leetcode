














class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = set(['+', '-','*','/'])
        stack = []

        for t in tokens:
            if t not in operations:
                stack.append(int(t))
                continue
            right, left = stack.pop(), stack.pop()
            if t=='+':
                stack.append(left+right)
            elif t=='-':
                stack.append(left-right)
            elif t=='*':
                stack.append(left*right)
            else:
                if left*right<0:
                    stack.append(-int(abs(left)//abs(right)))
                else:
                    stack.append(left//right)
        return stack.pop()
    
