from ctypes import pointer
import re


# temp_in_line = of format ("<Temp type>", temp_name, data_type)
def detect_pointer_deref(line, index ,temp_in_line, current_pointers):
    line = line.strip()
    # simple dereferencing
    for pointer_name in current_pointers.keys():
        pattern = r".*\*"+pointer_name+".*"
        sample = re.findall(pattern, line)
        # print("sup ", sample)
        if sample and temp_in_line[0] == "Ptr" and temp_in_line[1] == pointer_name:
            # means that pointer was not initialised in this line so dereferenced
            if current_pointers[pointer_name] == False:
                print("Null pointer dereference error at line", index)
                return 0
    return 0
    