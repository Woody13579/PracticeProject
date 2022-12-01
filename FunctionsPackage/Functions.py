# Functions

import pyodbc
import requests
import textwrap 

 
# From : https://www.quora.com/How-can-I-execute-already-created-SQL-scripts-in-Python
 
entries = os.listdir('C:\\Users\\Michael\\Desktop\\SQL Files')
print(entries)

for filenames in entries:
    print(filenames) 
 
 
def create_query_string(sql_full_path): 
    with open(sql_full_path, 'r') as f_in: 
        lines = f_in.read() 
 
    # remove any common leading whitespace from every line     
    query_string = textwrap.dedent("""{}""".format(lines)) 
 
    return query_string 
 
 
def main(): 
    cnxn = pyodbc.connect('Driver={SQL Server};' 
                          'Server=placeholder;' 
                          'Database=placeholder;' 
                          'Trusted_Connection=yes;') 
 
    # declare a database cursor object
    cursor = cnxn.cursor() 
 
    query_string = create_query_string(r'path_to_sql') 
 
    # execute the SQL query string (returns the cursor object itself) 
    cursor.execute(query_string) 
 
    '''
    # return the next row in the query 
    row = cursor.fetchone() 
    if row: 
        print(row) 
    '''
 
    cursor.close() 
    cnxn.close() 
 
 
if __name__ == '__main__': 
    main() 


