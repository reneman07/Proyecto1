from django.http import HttpResponse
import datetime
from django.template import Template, Context
import pyodbc

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(reqeust): #Primera vista

    p1 = Persona("Rene Alejandro", "Mansilla")
    #nombre = "Rene"
    #apellido = "Mansilla" 
    ahora = datetime.datetime.now()

    doc_externo = open("C:/Users/Rene Mansilla/OneDrive - Boston Agrex/Documents/PythonTests/ProyectosDjango/Proyecto1/Proyecto1/plantillas/plantilla1.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona":p1.nombre, "apellido_persona": p1.apellido, "momento_actual":ahora})
    documento = plt.render(ctx)

    

    return HttpResponse(documento)

def despedida (reqeust):

    return HttpResponse("Adios amigos!")

def dameFecha(request):

    fecha_actual = datetime.datetime.now()
    documento = """<html>
        <body>
            <h1>
                Fecha y hora actuales %s
            </h1>
            </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edadActual, anio):

    #edadActual = 18
    periodo = anio - 2023
    edadFutura = edadActual + periodo
    documento = """<html>
    <body>
        <h2>
            en el año %s tendras %s años
        </h2>
    </body>
    </html>""" %(anio, edadFutura)

    return HttpResponse(documento)

def data(request):
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
            documento = documento + row[2] + "<br><hr>"
    except Exception as ex:
            Except = ex
    finally:
            connection.close()

    documento = """<html>
    <body>
        %s
    </body>
    </html>""" % documento
    

    return HttpResponse(documento)
