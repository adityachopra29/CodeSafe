from pickle import FALSE, TRUE
import re
from enum import Enum, auto

# collectively these 3 are called Temp
current_variables = {}
current_pointers = {}
current_functions = {}


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

# for list in data_type_list:
#     list = [s.replace(' ', '_') for s in list]
#     Data_type = Enum("Data_type", {data_type: auto() for data_type in list})
#     print(Data_type)

# for types in Data_type:
#     print(types)
# 
# class Ptr:
#     data_type=None
#     name=None
#     value=None

# class Var:
#     data_type=None
#     name=None
#     value=None

# class Funct:
#     pass

def remove_last_word(s):
    words = s.split()
    if len(words) > 0:
        # Remove the last word
        del words[-1]
    # Join the remaining words back together
    new_s = ' '.join(words)
    
    return new_s

# Not considering pointers to functions
# Not capable of handling loops
# check if that isTemp is not already defined
#this thing will fuck on repetition (ie in functions)
# in functions definitions, the variables defined in input wont be detected
def check_for_type_written(line):
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
    # remove_last_word(s)
    # s.replace(' ', '_')
    return [isTemp, i]

def detect_variables_pointers_functions(line):
    [isTemp, type_length] = check_for_type_written(line)
    line = line.strip()
    words = re.split(" ", line)
    s = None
    
    if isTemp:
        temp = words[type_length]
        # print(temp)
        # we will check here if the temp is already defined or not 
        #  also if us hi time pe kuch value assign kardi hai ya nahi
        if temp.endswith(';'):
            # Remove the semicolon from the end
            temp = temp[:-1]
        if '(' in temp:
            # it is a function
            temp = temp.split("(")[0]
            if temp in current_functions:
                # update the value
                print("some fuck has happened1")
                pass
            else:
                current_functions[temp] = None
                s = {"Funct":temp}
        elif temp.startswith('*'):
            temp = temp[1:]
            # it is pointer'
            if temp in current_pointers:
                # update the value
                print("some fuck has happened2")
                pass
            else:
                current_pointers[temp] = False
                s = {"Ptr":temp}
        else:
            # it is a variable
            if temp in current_variables:
                # print(temp)
                # update the value
                print("some fuck has happened3")
                pass
            else:
                current_variables[temp] = None
                s = {"Var":temp}
        return s

def pointer_value_update(line):
    line = line.strip()
    words = re.split(" ", line)
    if len(words) >= 3:
        if words[0] in current_pointers and words[1] == '=' and words[2] != 'NULL':
            current_pointers[words[0]] = True
        elif words[0] in current_pointers and words[1] == '=' and words[2] == "NULL":
            current_pointers[words[0]] = False
    return 0

def detect_pointer_deref(line, temp_in_line):
    line = line.strip()
    # simple dereferencing
    for pointer_name in current_pointers.keys():
        pattern = r".*\*"+pointer_name+".*"
        sample = re.findall(pattern, line)
        print("sup bitch", sample)
        if sample and temp_in_line != {"Ptr":pointer_name}:
            print("we here")
            # means that pointer was not initialised in this line so dereferenced
            if current_pointers[pointer_name] == False:
                print("Null pointer dereference error")
                return 0
    return 0
    

def main():
    file = open('./test.c', 'r')
    lines = file.readlines()
    for line in lines:
        temp_in_line = detect_variables_pointers_functions(line)
        pointer_value_update(line)
        detect_pointer_deref(line, temp_in_line)

    print("current vars", current_variables)
    print("pointers", current_pointers)
    print("functions", current_functions)


if __name__ == "__main__":
    main()
