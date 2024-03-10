import re
from utils.utils import clean, data_type_list, integer_data_types, signed_integer_types, unsigned_integer_types, detect_variables_pointers_functions
from utils.utils import check_for_type_written

# also takes care of signed unsigned conv
# for line like -> t = -5;
def integer_update_value(line, current_signed_int, current_unsigned_int):
    line = line.strip()
    words = re.split(" ", line)
    if len(words) >= 3:
        # print("we are in")
        # print(current_unsigned_int)
        if words[0] in current_unsigned_int and words[1] == '=' :
            print(clean(words[2]))
            try : 
                value = int(clean(words[2]))
                if value < 0:
                    print("Signed to Unsigned Conversion Error at line .. ")
                
            except ValueError:
                print("Not")
            current_unsigned_int[words[0]] = True
        elif words[0] in current_unsigned_int and words[1] == '=' and words[2] == "NULL":
            current_unsigned_int[words[0]] = False
    return 0

        
    # it was simply being updated(ie of form -> x = 5;)