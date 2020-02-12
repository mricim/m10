import psycopg2

try:
    conn = psycopg2.connect("dbname='EXAMENECM' user='odoo1' host='localhost' password='odoo1'")
    cur = conn.cursor()
    #Fin conecxion

    cur.execute("CREATE TABLE IF NOT EXISTS Cliente(Id INT PRIMARY KEY, Name VARCHAR(50), Telefon VARCHAR(50), Correu VARCHAR(50), Adreca VARCHAR(50), Ciutat VARCHAR(50))")
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()