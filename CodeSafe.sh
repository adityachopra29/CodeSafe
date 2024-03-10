#!/bin/bash

echo "Enter filename or folder:"
read filename_or_folder


if [ -f "$filename_or_folder" ]; then
   
    filename="$filename_or_folder"
    
    
    extension="${filename##*.}"
    
    if [ "$extension" == "c" ]; then
        # here list the python files that are finding vulnerabilities in C file
        python3 main.py "$filename"
        python3 unin.py "$filename"
    elif [ "$extension" == "py" ]; then
        # here list the python files that are finding vulnerabilities in python file
         echo "Python file"
    else
        echo "$filename is neither a C nor a Python file."
    fi

elif [ -d "$filename_or_folder" ]; then
   
    folder="$filename_or_folder"
    for file in "$folder"/*; do
        if [ -f "$file" ]; then
           
            extension="${file##*.}"
            
            if [ "$extension" == "c" ]; then
                # here list the python files that are finding vulnerabilities in C file
                echo "Vulnerabilities in $file"
                python3 main.py "$file"
                python3 unin.py "$file"
            elif [ "$extension" == "py" ]; then
                # here list the python files that are finding vulnerabilities in python file
                echo "Vulnerabilities in $file"
            else
                echo "$file is neither a C nor a Python file."
            fi
        fi
    done

else
    echo "$filename_or_folder is neither a file nor a folder."
fi
