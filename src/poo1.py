class Coche():

    def __init__ (self):
            self.__largoChasis = 250
            self.__anchoChasis = 120
            self.__ruedas = 4
            self.__enmarcha = False

    def arrancar(self, arrancamos):

        self.__enmarcha = arrancamos

        if(self.__enmarcha):
             chequeo = self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif (self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
            #self.__enmarcha = False
        else:
            return "El coche esta detenido"

        #self.enmarcha = True

    def estado(self):

        print("el coche tiene ", self.__ruedas, " ruedas")
        print("el coche tiene un ancho de ", self.__anchoChasis)
        print("el coche tiene un largo de ", self.__largoChasis)

    def  __chequeo_interno(self):
         print("Realizando chequeo interno...")
         self.gasolina = "ok"
         self.aceite = "Mal"
         self.puertas = "cerradas"

         if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
              return True
         else:
              return False

miCoche = Coche()

#print("El largo del coche es: ", miCoche.largoChasis)
#print("el coche tiene ", miCoche.ruedas, " ruedas")
print(miCoche.arrancar(True))
miCoche.estado()

print("====================== A continuacion creamos el segundo objeto ======================")

miCoche2 = Coche()
#print("El largo del coche es: ", miCoche2.largoChasis)
#print("el coche tiene ", miCoche2.ruedas, " ruedas")
print(miCoche2.arrancar(False))
miCoche2.ruedas = 2
miCoche2.estado()