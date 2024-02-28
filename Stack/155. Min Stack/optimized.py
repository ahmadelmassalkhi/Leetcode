

# doesn't do unnecessary pushes incase of new element is not a new min
# => must handle pop() differently

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]: # if its equal to the min, push it to minStack
            self.minStack.append(val)                     # to avoid popping condition which, we have duplicate mins in stack, 
                                                          # and only one copy of it in minStack, thus we pop the only copy and cause incorrect behaivor

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.minStack[-1]:
                self.minStack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.minStack:
            return self.minStack[-1]