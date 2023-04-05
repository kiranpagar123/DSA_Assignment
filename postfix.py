def postfix_to_prefix(postfix):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for c in postfix:
        if c in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            expr = c + operand1 + operand2
            stack.append(expr)
        else:
            stack.append(c)
    return stack.pop()

# example usage
postfix = "ab*c+"
prefix = postfix_to_prefix(postfix)
print(prefix) # prints "+*abc"
