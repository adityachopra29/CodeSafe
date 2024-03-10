import ast
import argparse
import os
import sys

class VulnerabilityChecker(ast.NodeVisitor):
    def __init__(self):
        self.vulnerabilities = []

    def visit_Str(self, node):
        # Check for potential SQL injection vulnerabilities
        if "'" in node.s or '"' in node.s:
            self.vulnerabilities.append({
                "type": "SQL Injection",
                "line": node.lineno,
                "message": "Potential SQL injection vulnerability detected"
            })

        self.generic_visit(node)

    def visit_Node(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == "subprocess":
            self.vulnerabilities.append({
                "type": "Command Injection",
                "line": node.lineno,
                "message": "Potential command injection vulnerability detected"
            })

        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in ['eval', 'exec']:
            self.vulnerabilities.append({
                "type": "Code Injection",
                "line": node.lineno,
                "message": f"Potential code injection vulnerability detected: {node.func.id}() function used with user-supplied input."
            })
        self.generic_visit(node)

def analyze_file(file_path):
    with open(file_path, "r") as file:
        code = file.read()

    try:
        tree = ast.parse(code)
    except SyntaxError:
        print(f"Invalid syntax in file: {file_path}. Unable to analyze code.")
        return []

    checker = VulnerabilityChecker()
    checker.visit(tree)

    return checker.vulnerabilities

def main():
    parser = argparse.ArgumentParser(description="Python Code Vulnerability Scanner")
    parser.add_argument("path", nargs='?', help="Path to the Python file or directory to scan")
    args = parser.parse_args()

    path = args.path

    if not path:
        # path = input("Enter the path to the Python file or directory to scan: ")
        path = sys.argv[1]

    if os.path.isfile(path):
        vulnerabilities = analyze_file(path)
        if vulnerabilities:
            print(f"Vulnerabilities detected in file: {path}")
            for vulnerability in vulnerabilities:
                print(f"  - {vulnerability['type']} at line {vulnerability['line']}: {vulnerability['message']}")
        else:
            print(f"No vulnerabilities detected in file: {path}")

    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    vulnerabilities = analyze_file(file_path)
                    if vulnerabilities:
                        print(f"Vulnerabilities detected in file: {file_path}")
                        for vulnerability in vulnerabilities:
                            print(f"  - {vulnerability['type']} at line {vulnerability['line']}: {vulnerability['message']}")
                    else:
                        print(f"No vulnerabilities detected in file: {file_path}")
    else:
        print("Invalid path.")

if __name__ == "__main__":
    main()