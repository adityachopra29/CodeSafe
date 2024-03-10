import re
import sys
def pointer_value_update(line, current_pointers):
    line = line.strip()
    words = re.split(" ", line)
    if len(words) >= 3:
        if words[0] in current_pointers and words[1] == '=' and words[2] != 'NULL':
            current_pointers[words[0]] = True
        elif words[0] in current_pointers and words[1] == '=' and words[2] == "NULL":
            current_pointers[words[0]] = False
    return 0


