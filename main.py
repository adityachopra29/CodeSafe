
from pointers.null_pointer_deref import detect_pointer_deref
from pointers.utils import pointer_value_update
from utils.utils import detect_variables_pointers_functions

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
current_variables = {}
current_pointers = {}
current_functions = {}

def main():
    file = open('./test.c', 'r')
    lines = file.readlines()
    for line in lines:
        temp_in_line = detect_variables_pointers_functions(line, current_functions, current_pointers, current_variables)
        pointer_value_update(line, current_pointers)
        detect_pointer_deref(line, temp_in_line, current_pointers)

    print("current vars", current_variables)
    print("pointers", current_pointers)
    print("functions", current_functions)


if __name__ == "__main__":
    main()
