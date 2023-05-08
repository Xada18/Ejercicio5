
class PlanAhorro:
    __codigo = ""
    __modelo = ""
    __version = ""
    __valor = 0.0
    __cuota = 0.0
    __cuotas = 0
    __cuotas_necesarias = 0

    def __init__(self, codigo, modelo, version, valor, cuotas, necesarias):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = float(valor)
        self.__cuotas = int(cuotas)
        self.__cuotas_necesarias = int(necesarias)

        self.__cuota = float(valor)/int(cuotas) + float(valor) * 0.10

    def getCodigo(self):
        return self.__codigo
    
    def getModelo(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__version

    def getValor(self):
        return self.__valor

    def getCuotas(self):
        return self.__cuotas
    
    def getCuotasNecesarias(self):
        return self.__cuotas_necesarias
    
    def getCuota(self):
        return self.__cuota

    def actualizarPrecio(self, nuevo):
        self.__valor = float(nuevo)
        self.__cuota = self.__valor/self.__cuotas + self.__valor * 0.10

    def mostrarMontoNecesario(self):
        return self.__cuotas_necesarias * self.__cuota
    
    def modificarCuotasNecesarias(self, cantidad):
        self.__cuotas_necesarias = int(cantidad)
        