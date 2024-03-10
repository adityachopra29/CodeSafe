# CodeSafe
CodeSafe is a security analysis tool designed to identify vulnerabilities in C and Python source code files.

## Installation
To install CodeSafe, follow these steps: 

* Run the following commands:

```
git clone https://github.com/adityachopra29/CodeSafe.git   
cd CodeSafe
sh ./CodeSafe.sh
```

* The program will fire up.  
* Enter the path to your file or folder you want to analyze.

## Vulnerabilites detected
### For C
* Null pointer derefernce vulnerability
* Signed to unsigned integer conversion vulnerability
* Unintialized variables vulnerability

### For Python
* Code Injection
* Command Injection
* Sql injection


## Note
* The test code should be formatted in VS Code Formatter format.  
* Code cannot have loops and other functions except main (Call stack not able to maintain at present)