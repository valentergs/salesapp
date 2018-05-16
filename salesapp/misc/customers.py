# import csv
# import psycopg2
#
# conn = psycopg2.connect("dbname=salesapp_2 user=rodrigovalente")
# cur = conn.cursor()
#
# #Enter here the CSV file containg the info to be added to the Database.
# with open('SalesAllExportCustomerProducts.csv', 'rt', encoding='latin1') as csvfile:
#     readCSV = csv.reader(x.replace('\0', '') for x in csvfile)
#
#     for row in readCSV:
#         #You need to combine the CSV file columns with the Database columns.
#         cur.execute('''INSERT INTO SalesApp_oxeacustomers
#         (soldToNumber, soldToName, shipToNumber, shipToName, shipToCity, shipToCountry, products, sellerNumber, sellerName, cmscNumber, cmscName)
#         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
#         ('default', row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
#
# conn.commit()
# cur.close()
# conn.close()


import psycopg2

conn = psycopg2.connect("host=localhost dbname=salesapp_2 user=rodrigovalente")
cur = conn.cursor()
with open('SalesAllExportCustomerProducts2.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'salesapp_customers', sep=';')

conn.commit()
