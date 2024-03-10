#for finding uninitialized variables and strcpy vulnerabilities

import re
uninitialized = set()
initialized = set()
variables = set()
data_type_name_single = {"int", "char", "float", "double", "signed", "unsigned", "long"}
vulnerable_lines=[]

def detect_uninitialized(line ):
    line = line.strip()
    words =  re.split(" ",line)
    
   
    for index, word in enumerate(words):
        if word in data_type_name_single:
            if '(' in words[index+1]:
                continue
            if ')' in words[index+1]:
                words[index+1]=words[index+1][:-1]
            if words[index+1].endswith(';'):
                words[index+1]=words[index+1][:-1]
            
            variables.add(words[index+1])   
        elif "=" in word:
            initialized.add(words[index-1])


def buffer_overflow_vulnerabilities(line,i):
    
    line = line.strip()
    words =  re.split(" ",line)
   
    for word in words:
        
        if word[0:7]=='strcpy(' :
            print("yes")
            vulnerable_lines.append((i,line))


def detect_pointer_deref():
    pass
     

def main():
    filename = input("Enter the file name you want to find vulnerabilities: ")

    if filename.endswith('.c'):

        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                i=0
                for line in lines:
                    i=i+1
                    detect_uninitialized(line)
                    buffer_overflow_vulnerabilities(line,i)

                for variable in variables:
                    if variable in data_type_name_single:
                        variable.remove(variable)
                    if variable not in initialized:
                        uninitialized.add(variable)
       
                print("uninitialized variables:", uninitialized)
                
                
            if vulnerable_lines:
                print("Potential strcpy vulnerabilities found:")
                for line_number, line_code in vulnerable_lines:
                    print(f"Line {line_number}: {line_code}")
            else:
                print("No potential strcpy vulnerabilities found.")

        except FileNotFoundError:
             print("File not found. Please enter a valid file name.")
    
    else:
        print("The entered file is not a c file")
   
if __name__=="__main__": 
    main() 
    
