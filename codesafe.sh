#!/bin/bash

echo "Enter filename or folder:"
read filename_or_folder


if [ -f "$filename_or_folder" ]; then
   
    filename="$filename_or_folder"
  
    
    if [ "${filename: -2}" == ".c" ]; then
        # here list the python files that are finding vulnerabilities in C file
        python3 main.py "$filename"
        python3 unin.py "$filename"
    elif [  "${filename: -3}" == ".py" ]; then
        # here list the python files that are finding vulnerabilities in python file
         echo "Python file"
    else
        echo "$filename is neither a C nor a Python file."
    fi

elif [ -d "$filename_or_folder" ]; then
   
    folder="$filename_or_folder"
    for file in "$folder"/*; do
        if [ -f "$file" ]; then
           
           
            
            if [ "${file: -2}" == ".c" ]; then
                # here list the python files that are finding vulnerabilities in C file
                echo "Vulnerabilities in $file"
                python3 main.py "$file"
                python3 unin.py "$file"
                echo "------------------------------"
            elif [ "${file: -3}" == ".py" ]; then
                # here list the python files that are finding vulnerabilities in python file
                echo "Vulnerabilities in $file"
            else
                echo "$file is neither a C nor a Python file."
            fi
        fi
    done

else
    echo "$filename_or_folder path doesn't exist."
fi