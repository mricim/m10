import psycopg2
try:
    #conn = psycopg2.connect("dbname='m1' user='postgres' host='localhost' password='jupiter'")
    conn = psycopg2.connect("dbname='m1' user='odoo1' host='localhost' password='odoo1'")
except:
    print("No és possible connectar a la Base de Dades")