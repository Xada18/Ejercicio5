from ClasePlanAhorro import PlanAhorro
import csv

class ManejadorPlanes:
    __planes = []

    def __init__(self):
        self.__planes = []

    def carga(self, file):
        archivo = open(file, "r")
        reader = csv.reader(archivo, delimiter = ";")

        for plan in reader:
            planAhorro = PlanAhorro(plan[0], plan[1], plan[2], plan[3], plan[4], plan[5])
            self.__planes.append(planAhorro)

    def buscarPlan(self, codigo):
        i = 0
        plan = None
        while plan == None and i < len(self.__planes):
            if codigo == self.__planes[i].getCodigo():
                plan = self.__planes[i]
            i += 1

        return plan 

    def actualizarPrecios(self):
        i = 0
        for i in range(len(self.__planes)):
            print(f"Codigo: {self.__planes[i].getCodigo()}")
            print(f"Vehiculo: {self.__planes[i].getModelo()} {self.__planes[i].getVersion()}")
            nuevoPrecio = input("Ingrese el nuevo precio del vehiculo: ")
            print("")
            self.__planes[i].actualizarPrecio(nuevoPrecio)

    def cuotasMenores(self, valor):
        ban = True
        for plan in self.__planes:
            cuota = plan.getCuota()
            if cuota < float(valor):
                print(f"Codigo: {plan.getCodigo()}")
                print(f"Vehiculo: {plan.getModelo()} {plan.getVersion()}")
                print("")
                ban = False

        if ban == True:
            print("No habia planes con valor de cuota menor que el valor ingresado")
            

    