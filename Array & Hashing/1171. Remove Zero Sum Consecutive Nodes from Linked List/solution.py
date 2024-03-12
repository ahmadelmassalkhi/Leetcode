# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

''' My First Solution '''
class Solution(object):

    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = {}
        total = i = 0
        while head:
            if head.val == 0:
                i += 1
                head = head.next
                continue

            d[i] = head.val
            total += head.val
            if total == 0:
                for a in range(i, -1, -1):
                    if a in d:
                        del d[a]
            else:
                subTotal = d[i]
                for k in range(i-1, -1, -1):
                    if k not in d:
                        continue
                    subTotal += d[k]
                    if subTotal == 0:
                        for m in range(k, i+1):
                            if m in d:
                                total -= d[m]
                                del d[m]
                        break
            i += 1
            head = head.next

        # convert to list
        newHead = tail = None
        for j in range(i):
            if j not in d:
                continue
            newNode = ListNode(d[j], None)
            if newHead == None:
                newHead = newNode
            else:
                tail.next = newNode
            tail = newNode

        return newHead

        