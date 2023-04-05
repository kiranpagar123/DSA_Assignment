class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]

# example usage
stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(1)
print("Minimum element in the stack:", stack.get_min()) # prints '1'
stack.pop()
stack.pop()
print("Minimum element in the stack:", stack.get_min()) # prints '2'
