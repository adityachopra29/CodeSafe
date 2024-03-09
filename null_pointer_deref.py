from distutils.command import clean
from pickle import FALSE, TRUE
import re
import tempfile


current_variables = set()
current_pointers = set()
current_functions = set()

data_type_creators = ["struct", "#define", "enum", "typedef"]

data_type_name_single = {"int", "char", "float", "double", "signed", "unsigned"}
data_type_name_double = {"long double", "long int", "short int", "unsigned int", "signed int", "signed char", "unsigned char", "long long"}
data_type_name_triple = {"unsigned long int", "unsigned short int", "long long int"}
data_type_name_quadruple = {"unsigned long long int"}

data_type_list = [data_type_name_single, data_type_name_double, data_type_name_triple, data_type_name_quadruple]


# Not considering pointers to functions
def detect_variables_pointers_function(line):
    line = line.strip()
    words = re.split(" ", line)
    flag = False
    allowed_list = [data_type_name_single]

    i = 0
    s = words[i]
    # current_word = [s]
    flag = False
    flag1=False
    if s in data_type_name_single:
        flag = True
        flag1=True
        temp = s
    i = i+ 1
    while flag and i<len(data_type_list):
        s = s + ' ' + words[i]
        if s in data_type_list[i]:
            i = i+ 1
        else :
            flag = False

    if flag1 : 
        print(i)
        temp = words[i]
        # print(temp)
        if temp.endswith(';'):
            #Remove the semicolon from the end
            temp = temp[:-1]
        if '(' in temp:
            # it is a function
            temp = temp.split("(")[0]
            current_functions.add(temp)
        elif temp.startswith('*'):
            # it is pointer'
            temp = temp[1:]
            current_pointers.add(temp)
        else:
            # it is a variable
            current_variables.add(temp)


def detect_pointer_deref():
    pass


def main():
    file = open('./test.c', 'r')
    lines = file.readlines()
    # print("yo")
    for line in lines:
        # words = re.split(" ", line)
        # print(words)
        detect_variables_pointers_function(line)

    print("current vars", current_variables)
    print("pointers", current_pointers)
    print("functions", current_functions)

if __name__=="__main__": 
    main() 