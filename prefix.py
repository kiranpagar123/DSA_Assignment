def prefix_to_infix(prefix):
    stack = []
    operators = set(["+", "-", "*", "/", "^"])
    prefix = prefix[::-1]
    for char in prefix:
        if char in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            expr = "(" + op1 + char + op2 + ")"
            stack.append(expr)
        else:
            stack.append(char)
    return stack.pop()

# example usage
prefix = "*+AB-CD"
infix = prefix_to_infix(prefix)
print(infix) # prints '((A+B)*(C-D))'
