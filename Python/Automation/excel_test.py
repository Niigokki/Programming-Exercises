import sqlite3
import openpyxl

print("Hello, Excel!")
#workbook loaded
workbook = openpyxl.load_workbook('/mnt/c/Users/jks0039/Documents/assetdatasheetwip.xlsx')
print ("Active Sheet is " + workbook.active )
