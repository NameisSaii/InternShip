#imports excel data into sqlite3 database
import sqlite3
import pandas as pd

con = sqlite3.connect('fangsearch.db')
wb = pd.read_excel('fangsearch.xlsx', sheet_name=None)

for sheet in wb:
    wb[sheet].to_sql(sheet, con, index=False)
con.commit()
con.close()