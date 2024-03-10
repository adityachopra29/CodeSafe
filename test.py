import psycopg2
import os

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="testdb", 
    user="your_username", 
    password="your_password", 
    host="localhost"
)

# Create a cursor object
cur = conn.cursor()

# Test for SQL Injection
username = input("Enter your username: ")

# This query is vulnerable to SQL injection
# Never concatenate input directly into SQL queries
# Instead, use parameterized queries or ORM frameworks
query = f"SELECT * FROM users WHERE username = '{username}'"

# Execute the query
cur.execute(query)

# Fetch all rows
rows = cur.fetchall()
print("Results for SQL Injection Test:")
for row in rows:
    print(row)

# Test for Command Injection
filename = input("Enter the filename: ")
# Vulnerable to command injection if not properly sanitized
os.system(f"cat {filename}")

# Test for Code Injection
code_to_execute = input("Enter Python code to execute: ")
# Vulnerable to code injection if not properly sanitized
exec(code_to_execute)

# Close the cursor and connection
cur.close()
conn.close()
