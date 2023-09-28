import pyodbc
documento = ""

try:
    connection = pyodbc.connect("Driver={SQL Server};Server=ba-dc01-vm\\agrex;UID=rene;PWD=BA-quan-6542;Database=AgrexProduction;")
    cursor = connection.cursor()
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    print(row)
    print("Conexion exitosa")
    cursor.execute("SELECT * FROM TRADERS")
    rows = cursor.fetchall()
    for row in rows:
        #print(row[2])
        documento = documento + row[2] + "<hr>"
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print(documento)
    print("Conexion finalizada")