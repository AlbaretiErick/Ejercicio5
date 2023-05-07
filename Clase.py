class PlanAhorro:
    __codPlan = None
    __modelo = None
    __version = None
    __valor = None
    __cantCuotas = 60
    __cantCuotasPagas = 10
    def __init__ (self, codPlan, modelo, version, valor):
        self.__codPlan = codPlan
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
    def getCPLicitar (self):
        return self.__cantCuotasPagas
    def getCuotas (self):
        return self.__cantCuotas
    def getValor (self):
        return float (self.__valor)
    def modifCuotas (self, nuevo):
        self.__cantCuotasPagas = nuevo
    def modifValor (self, nuevoValor):
        self.__valor = nuevoValor
    def mostrar (self):
        print ('Codigo de Plan: {}\nModelo del vehículo: {}\nVersion del vehículo: {}'.format (self.__codPlan, self.__modelo, self.__version))