#!/usr/bin/env python3

import pandas as pd
import mysql.connector

#read the csv 
csv_file = "./JPW_Registration - Sheet1.csv"  
df = pd.read_csv(csv_file, sep=',')          # CSV is comma-separated
df.columns = df.columns.str.strip()

#connect to the database 
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="StuShop"
)

cursor = conn.cursor()

#create the insert query
insert_query = """
INSERT INTO orders 
(first_name, last_name, listing_id, size, qty, paid)
VALUES (%s, %s, %s, %s, %s, %s)
"""

#loop through dataframe and get the values for the db
for index, row in df.iterrows():
    first_name = row['FirstName'] if pd.notna(row['FirstName']) else 'no name'
    last_name = row['LastName'] if pd.notna(row['LastName']) else 'no name'
    listing_id = int(row['ListingID'])
    size = row['Size'] if pd.notna(row['Size']) else 'none'
    qty = int(row['qty'])
    paid = float(row['Paid'])
    
    cursor.execute(insert_query, (first_name, last_name, listing_id, size, qty, paid))

#commit and close 
conn.commit()
cursor.close()
conn.close()

print("CSV data inserted successfully!")
