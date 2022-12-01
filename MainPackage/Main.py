# Main

import pyodbc
import requests
import os
from FunctionsPackage.Functions import *
#from FunctionsPackage.Functions import *


x = getSQLFiles('C:\\Users\\Michael\\Desktop\\SQL Files')
print(x)

for script in x:
    query = sqlQuery(script)
    print(query)
    print('Execute')