from operator import truediv
import re
from tkinter.messagebox import RETRY


data_type_creators = ["struct", "#define", "enum", "typedef"]

data_type_name_single = {"int", "char",
                         "float", "double", "signed", "unsigned"}
data_type_name_double = {"long double", "long int", "short int",
                         "unsigned int", "signed int", "signed char", "unsigned char", "long long"}
data_type_name_triple = {"unsigned long int",
                         "unsigned short int", "long long int"}
data_type_name_quadruple = {"unsigned long long int"}

data_type_list = [data_type_name_single, data_type_name_double,
                  data_type_name_triple, data_type_name_quadruple]

signed_integer_types = ["int", "float", "double", "signed", "long double", "long int", "short int", "signed int", "long long", "long long int"]
unsigned_integer_types = ["unsigned", "unsigned int", "unsigned long int", "unsigned short int", "unsigned long long int"]

integer_data_types = signed_integer_types + unsigned_integer_types

def remove_last_word(s):
    words = s.split()
    if len(words) > 0:
        # Remove the last word
        del words[-1]
    # Join the remaining words back together
    new_s = ' '.join(words)
    
    return new_s


def clean(s):
    return re.sub(r'[^a-zA-Z0-9\-]', '', s)
# Not considering pointers of functions(call stack)
# Not capable of handling loops
# check if that isTemp is not already defined
#this thing will fuck on repetition (ie in functions)
# in functions definitions, the variables defined in input wont be detected

# returns [bool, data_type_name]
def check_for_type_written(line, data_type_list=data_type_list):
    print(line)
    line = line.strip()
    words = re.split(" ", line)

    isTemp = False
    flag = True
    i = 0
    s = ''
    while flag and i < len(data_type_list):
        if i == 0:
            s += words[i]
        else:
            s += ' ' + words[i]
        if s in data_type_list[i]:
            i += 1
            isTemp = True
        else:
            flag = False
    s  = remove_last_word(s)
    s= s.rstrip()
    # s.replace(' ', '_')
    return [isTemp, s]

# returns tuple ("<Temp type>", temp_name, data_type) when it is being written for the first time. else returns 0
def detect_variables_pointers_functions(line, current_functions, current_pointers, current_variables, current_signed_ints, current_unsigned_ints):
    [isTemp, data_type] = check_for_type_written(line)
    line = line.strip()
    words = re.split(" ", line)
    s = None
    x = data_type.split(" ")
    data_type_length = len(x)

    unsigned_flag = False
    signed_flag = False
    if data_type in signed_integer_types: signed_flag = True
    elif data_type in unsigned_integer_types: unsigned_flag = True
    
    if isTemp:
        temp = words[data_type_length]
        # print(temp)
        initialized=False
        # we will check here if the temp is already defined or not 
        if temp.endswith(';'):
            # Remove the semicolon from the end
            temp = temp[:-1]
            initialized = False

        if '(' in temp:
            # it is a function
            temp = temp.split("(")[0]
            if temp in current_functions:
                print("Already defined function being reinitialized")
                pass
            else:
                current_functions[temp] = None
                s = ("Funct", temp, data_type)

        elif temp.startswith('*'):
            temp = temp[1:]
            # it is pointer'
            if temp in current_pointers:
                print("Already defined pointer being reinitialized")
                pass
            else:
                if len(words) >= data_type_length+3: 
                    if words[data_type_length + 1] == '=':
                        if not any(words[data_type_length + 2].replace(";", "") == tmp for tmp in ["NULL", "0"]):
                            initialized = True
                else : initialized = False
                current_pointers[temp] = initialized
                s = ("Ptr", temp, data_type)

        else:
            # it is a variable
            if temp in current_variables:
                print("Already defined variable being reinitialized")
                pass
            else:
                if len(words) >= data_type_length+3:
                    if words[data_type_length + 1] == '=':
                        allotted_value = words[data_type_length + 2].replace(";", "")
                        if data_type in signed_integer_types:
                            current_signed_ints[temp] = True
                            signed_flag = True
                            # print("new int")

                        elif data_type in unsigned_integer_types:
                            current_unsigned_ints[temp] = True
                            unsigned_flag = True
                            # print("new int")

                        if  any(allotted_value == tmp for tmp in ["NULL", "0"]):
                            allotted_value = None
                            
                else:
                    allotted_value = None
                    if unsigned_flag: 
                        # print("new int")
                        current_unsigned_ints[temp] = False
                    elif signed_flag: 
                        # print("new int")
                        current_signed_ints[temp] = False
                current_variables[temp] = allotted_value
                s = ("Var", temp, data_type)
        return s
    else: return False