import psycopg2

conn = psycopg2.connect("host=localhost dbname=salesapp_2 user=rodrigovalente")
cur = conn.cursor()
with open('SalesAllExportCustomerProducts2.csv', 'r') as f:
    next(f)  # Skip the header row.
    cur.copy_from(f, 'salesapp_customers', sep=';')

conn.commit()
