def find_first_non_repeated_char(s):
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    for c in s:
        if char_count[c] == 1:
            return c
    return None

# example usage
s = "abbccddeeff"
non_repeated_char = find_first_non_repeated_char(s)
if non_repeated_char is None:
    print("There is no non-repeated character in the string.")
else:
    print("The first non-repeated character is:", non_repeated_char)
