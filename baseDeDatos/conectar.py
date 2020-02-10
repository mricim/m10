import psycopg2

# try:
#     # conn = psycopg2.connect("dbname='m1' user='postgres' host='localhost' password='jupiter'")
#     conn = psycopg2.connect("dbname='mydb' user='myuser' host='localhost' password='mypass'")
# except:
#     print("No és possible connectar a la Base de Dades")

# try:
#     conn = psycopg2.connect("dbname='mydb' user='myuser' host='localhost' password='mypass'")
#     cur = conn.cursor()
#     cur.execute("SELECT * from cliente where repcod>%s", (103,))
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
# except(Exception, psycopg2.DatabaseError) as error:
#     print(error)
# finally:
#     if conn is not None:
#         conn.close()

cur=None
try:
    conn = psycopg2.connect("dbname='EXAMENECM' user='odoo1' host='localhost' password='odoo1'")
    cur = conn.cursor()
    #Fin conecxion

    #1
    cur.execute("SELECT * from res_users where id>%s", (1,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    #2
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT PRIMARY KEY, Name VARCHAR(10))")
    cur.execute("INSERT INTO Cars (Id, Name) VALUES (1,'Pal')")
    cur.execute("INSERT INTO Cars (Id, Name) VALUES (2,'Pel')")
    cur.execute("INSERT INTO Cars (Id, Name) VALUES (3,'Pil')")
    cur.execute("INSERT INTO Cars (Id, Name) VALUES (4,'Pol')")
    cur.execute("INSERT INTO Cars (Id, Name) VALUES (5,'Pul')")

    #3
    cur.execute("SELECT id from Cars")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    id=int(input("Info del id a mostrar?"))
    cur.execute("SELECT * from Cars where id=%s", (id,))
    print(cur.fetchall())


    #4
    cur.execute("SELECT id from Cars")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    id = int(input("Info del id a modificar?"))
    name=input("Nuevo nombre (10)?")
    cur.execute("UPDATE Cars SET name=%s where id=%s", (name,id))

    #5 print de nuevo
    cur.execute("SELECT * from Cars where id=%s", (id,))
    print(cur.fetchall())
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()


