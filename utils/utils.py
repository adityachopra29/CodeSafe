import re


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

def remove_last_word(s):
    words = s.split()
    if len(words) > 0:
        # Remove the last word
        del words[-1]
    # Join the remaining words back together
    new_s = ' '.join(words)
    
    return new_s

# Not considering pointers of functions(call stack)
# Not capable of handling loops
# check if that isTemp is not already defined
#this thing will fuck on repetition (ie in functions)
# in functions definitions, the variables defined in input wont be detected
def check_for_type_written(line, data_type_list):
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

def detect_variables_pointers_functions(line, current_functions, current_pointers, current_variables):
    [isTemp, type_length] = check_for_type_written(line, data_type_list)
    line = line.strip()
    words = re.split(" ", line)
    s = None
    
    if isTemp:
        temp = words[type_length]
        # print(temp)
        initialized=False
        # we will check here if the temp is already defined or not 
        #  also if us hi time pe kuch value assign kardi hai ya nahi
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
                s = {"Funct":temp}
        elif temp.startswith('*'):
            temp = temp[1:]
            # it is pointer'
            if temp in current_pointers:
                print("Already defined pointer being reinitialized")
                pass
            else:
                if words[type_length + 1] == '=':
                    print(words[type_length + 2].replace(";", ""))
                    if not any(words[type_length + 2].replace(";", "") == tmp for tmp in ["NULL", "0"]):
                        initialized = True
                current_pointers[temp] = initialized
                s = {"Ptr":temp}
        else:
            # it is a variable
            if temp in current_variables:
                print("Already defined variable being reinitialized")
                pass
            else:
                if words[type_length + 1] == '=':
                    print(words[type_length + 2].replace(";", ""))
                    if not any(words[type_length + 2].replace(";", "") == tmp for tmp in ["NULL", "0"]):
                        initialized = True
                current_variables[temp] = initialized
                s = {"Var":temp}
        return s