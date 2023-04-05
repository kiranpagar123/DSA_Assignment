def reverse_stack(stack):
    if not stack:
        return stack
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)

def insert_at_bottom(stack, x):
    if not stack:
        stack.append(x)
        return
    temp = stack.pop()
    insert_at_bottom(stack, x)
    stack.append(temp)

# example usage
stack = [1, 2, 3, 4, 5]
print("Original stack:", stack)
reverse_stack(stack)
print("Reversed stack:", stack)
