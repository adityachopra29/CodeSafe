import re



def detect_pointer_deref(line, temp_in_line, current_pointers):
    line = line.strip()
    # simple dereferencing
    for pointer_name in current_pointers.keys():
        pattern = r".*\*"+pointer_name+".*"
        sample = re.findall(pattern, line)
        # print("sup ", sample)
        if sample and temp_in_line != {"Ptr":pointer_name}:
            # print("we here")
            # means that pointer was not initialised in this line so dereferenced
            if current_pointers[pointer_name] == False:
                print("Null pointer dereference error")
                return 0
    return 0
    