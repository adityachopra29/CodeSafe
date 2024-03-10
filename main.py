
from importlib.metadata import PathDistribution
import sys
from traceback import print_tb
from pointers.null_pointer_deref import detect_pointer_deref
from pointers.utils import pointer_value_update
from utils.utils import detect_variables_pointers_functions
from variables.signed_unsigned_conv import integer_update_value

# collectively these 3 are called Temp
#all of type {name_of_temp, its_value}
current_variables = {} 
current_pointers = {}
current_functions = {}
current_signed_integers = {}
current_unsigned_integers = {}

def main():
    filename = sys.argv[1]
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        for (index, line) in enumerate(lines):
            # temp_in_line = of format ("<Temp type>", temp_name, data_type)
            temp_in_line = detect_variables_pointers_functions(line, current_functions, current_pointers, current_variables, current_signed_integers, current_unsigned_integers)

            pointer_value_update(line, current_pointers)
            integer_update_value(line, index+1, current_signed_integers, current_unsigned_integers)
            detect_pointer_deref(line, index+1, temp_in_line, current_pointers)

    # print("current vars", current_variables)
    # print("pointers", current_pointers)
    # print("functions", current_functions)
    # print("signed int", current_signed_integers)
    # print("unsigned int", current_unsigned_integers)

    except FileNotFoundError:
        print("File not found. Please enter a valid location to file")


if __name__ == "__main__":
    main()
