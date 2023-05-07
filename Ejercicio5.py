from Clase import PlanAhorro

def actualizarValores (listaPlanes):
    for plan in listaPlanes:
            plan.mostrar ()
            nuevoValor = float (input ('Ingrese nuevo valor del vehículo: '))
            plan.modifValor (nuevoValor)
            print ('\n')

def mostrarVehículos (listaPlanes):
    valorDeReferencia = float (input ('Ingrese el valor de referencia: '))
    print ('Se presenta una lista de los automoviles cuyo valor de cuota es menor al ingresado:')
    for plan in listaPlanes:
        valorCuota = (plan.getValor ()/plan.getCuotas ()) + plan.getValor () * 0.10
        if valorCuota < valorDeReferencia:
            plan.mostrar ()
            print ('\n')

def paraLicitar (listaPlanes):
    for plan in listaPlanes:
        valorCuota = (plan.getValor ()/plan.getCuotas ()) + plan.getValor () * 0.10
        print ('Para licitar el siguiente vehículo:')
        plan.mostrar ()
        print ('Debe tener pago un total de: ${:.2f}\n'.format(plan.getCPLicitar ()*valorCuota))

def modifCuotas (listaPlanes):
    nuevaCuotLicitar = int (input ('Ingrese la nueva cantidad de cuotas para licitar: '))
    for plan in listaPlanes:
        plan.modifCuotas (nuevaCuotLicitar)

if __name__ == '__main__':
    listaPlanes = []
    with open ('planes.csv', '+r') as archivo:
        for linea in archivo:
            listaVariable = []
            listaVariable = linea.split (';')
            listaPlanes.append (PlanAhorro (listaVariable[0], listaVariable[1], listaVariable[2], listaVariable[3]))
    print ('Seleccione una de las siguientes opciones:\na - Actualizar el valor del vehículo de cada plan.\nb - Mostrar vehículos cuyos valores son inferiores a uno especificado.\nc - Mostrar el monto que se debe haber pagado para licitar el vehículo\nd - Modificar la cantidad de cuotas que debe tener pagas para licitar.')
    opcion = input ('Opción: ')
    if opcion == 'a':
        actualizarValores (listaPlanes)
    elif opcion == 'b':
        mostrarVehículos (listaPlanes)
    elif opcion == 'c':
        paraLicitar (listaPlanes)
    elif opcion == 'd':
        modifCuotas (listaPlanes)
    else:
        print ('La opcion seleccionada no existe.')
    print ('Fin del programa...')