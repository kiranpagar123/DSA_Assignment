def is_balanced(s):
    stack = []
    open_brackets = set(["(", "[", "{"])
    close_brackets = set([")", "]", "}"])
    bracket_map = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack:
                return False
            if stack.pop() != bracket_map[char]:
                return False
    return not stack


code_snippet = "def foo():\n    print('hello world')\n}"
if is_balanced(code_snippet):
    print("All brackets are closed.")
else:
    print("Not all brackets are closed.")
