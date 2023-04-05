def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1s1 = s1 + s1
    if s2 in s1s1:
        return True
    else:
        return False

# example usage
s1 = "abcd"
s2 = "cdab"
print(is_rotation(s1, s2)) # prints True
