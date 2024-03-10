import re
uninitialized = set()
initialized = set()
variables = set()
data_type_name_single = {"int", "char", "float", "double", "signed", "unsigned", "long"}

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

def detect_pointer_deref():
    pass
     

def main():
    file = open('./test.c', 'r')
    lines = file.readlines()

    for line in lines:     
        detect_uninitialized(line )
          
    for variable in variables:
        if variable in data_type_name_single:
            variable.remove(variable)
        if variable not in initialized:
            uninitialized.add(variable)
       
            
        
    print("uninitialized used", uninitialized)
   
if __name__=="__main__": 
    main()