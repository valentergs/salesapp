# import csv
# import psycopg2

# conn = psycopg2.connect("dbname=salesapp_2 user=rodrigovalente")
# cur = conn.cursor()

# #Enter here the CSV file containg the info to be added to the Database.
# with open('SalesAllExportCustomerProducts_180525.csv', 'rt', encoding='latin1') as csvfile:
#     readCSV = csv.reader(x.replace('\0', '') for x in csvfile)

#     for row in readCSV:
#         #You need to combine the CSV file columns with the Database columns.
#         cur.execute('''COPY salesapp_sapbase
#         (soldToNumber, soldToName, shipToNumber, shipToName, shipToCity, shipToCountry, products, sellerNumber, sellerName, cmscNumber, cmscName)
#         FROM 'SalesAllExportCustomerProducts_180525.csv' DELIMITER ';' CSV''')
# conn.commit()
# cur.close()
# conn.close()

import psycopg2

conn = psycopg2.connect("host=localhost dbname=salesapp_2 user=rodrigovalente")
cur = conn.cursor()
with open('SalesAllExportCustomerProducts2.csv', 'r') as f:
    next(f)  # Skip the header row.
    cur.copy_from(f, 'SalesApp_sapbase', sep=';')

conn.commit()