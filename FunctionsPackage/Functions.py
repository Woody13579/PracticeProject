# Functions

import pyodbc
import requests
import textwrap
import os

# From : https://www.quora.com/How-can-I-execute-already-created-SQL-scripts-in-Python
# Starts by grabbing the names of all files within the file location provided
def getSQLFiles(fileLocation):
    entries = os.listdir(fileLocation)
    SQLFilesList = [] 
    for filenames in entries:
        SQLFilesList.append(fileLocation + "\\" + filenames)
    return SQLFilesList
    # outputs a list so the function to execute the scripts needs to be able to accept a list


def sqlQuery(SQLFilePath): 
    with open(SQLFilePath, 'r') as f_in: 
        lines = f_in.read() 
 
    # remove any common leading whitespace from every line     
    query_string = textwrap.dedent("""{}""".format(lines)) 
 
    return query_string 


def executeScript(): 
    cnxn = pyodbc.connect('Driver={SQL Server};' 
                          'Server=placeholder;' 
                          'Database=placeholder;' 
                          'Trusted_Connection=yes;') 
 
    # declare a database cursor object
    cursor = cnxn.cursor() 
    query_string = sqlQuery(r'path_to_sql') 
 
    # execute the SQL query string (returns the cursor object itself) 
    cursor.execute(query_string) 
  
    # Closing cursor an connection
    cursor.close() 
    cnxn.close() 
 

