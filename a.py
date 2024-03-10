import re

# Variable representing the ending sequence
var = r"b;"

# Regular expression pattern
pattern = r".*= .*(\*"+var+"|\(\*"+var+"\)"

# Example strings
strings = [
    "= test *b;",
    "= hello world *b;",
    "= axxx *b;",
    "= test (*b);",
    "= hello world (*b);",
    "= axxx (*b);",
    "= test b;",
    "= hello world b;",
    "= axxx b;"
]

# Check if strings match the pattern
for s in strings:
    if re.match(pattern, s):
        print(f"'{s}' matches the pattern")
    else:
        print(f"'{s}' does not match the pattern")