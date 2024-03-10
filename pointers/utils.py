import re

# *ptr = 20; -> this type of updating still need to be checked
def pointer_value_update(line, current_pointers):
    line = line.strip()
    words = re.split(" ", line)
    if len(words) >= 3:
        third_word = ''.join(char for char in words[2] if char.isalnum())
        if words[0] in current_pointers and words[1] == '=' and third_word != 'NULL':
            current_pointers[words[0]] = True
        elif words[0] in current_pointers and words[1] == '=' and third_word == "NULL":
            current_pointers[words[0]] = False
    return 0