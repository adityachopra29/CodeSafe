
from importlib.metadata import PathDistribution
from traceback import print_tb
from pointers.null_pointer_deref import detect_pointer_deref
from pointers.utils import pointer_value_update
from utils.utils import detect_variables_pointers_functions
from variables.signed_unsigned_conv import integer_update_value


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


# collectively these 3 are called Temp
#all of type {name_of_temp, its_value}
current_variables = {} 
current_pointers = {}
current_functions = {}
current_signed_integers = {}
current_unsigned_integers = {}

def main():
    file = open('./test.c', 'r')
    lines = file.readlines()
    for line in lines:
        # temp_in_line = of format ("<Temp type>", temp_name, data_type)
        # gives the first temp (in case of long long)
        temp_in_line = detect_variables_pointers_functions(line, current_functions, current_pointers, current_variables, current_signed_integers, current_unsigned_integers)
        pointer_value_update(line, current_pointers)
        detect_pointer_deref(line, temp_in_line, current_pointers)
        integer_update_value(line, current_signed_integers, current_unsigned_integers)

    print("current vars", current_variables)
    print("pointers", current_pointers)
    print("functions", current_functions)
    print("signed int", current_signed_integers)
    print("unsigned int", current_unsigned_integers)



if __name__ == "__main__":
    main()
