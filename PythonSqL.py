import mysql.connector as mysql

con = mysql.connector.connect(host="localhost", port = "3306", user="root", password="", database="facturacion")
cursor = con.cursor()
selectquery = "select * from cliente"
cursor.execute(selectquery)
records = cursor.fetchall()
print("El numero de clientes es: ",cursor.rowcount)

for row in records:
    print("codigo del cliente",row[0])
    print("nit del cliente",row[1])
    print("Nombre del cliente",row[2])
    print("Telefono del cliente",row[3])
    print("Direccion del cliente",row[4])
    print()
cursor.close()
con.close()
