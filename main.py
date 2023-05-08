from ClaseManejadorPlanes import ManejadorPlanes

if __name__ == '__main__':
    archivo = "planes.csv"
    ListaPlanes = ManejadorPlanes()
    ListaPlanes.carga(archivo)

    ban = True
    while ban:
        print("Menu")
        print("1 - Actualizar precio")
        print("2 - Planes con valor de cuota menor al valor ingresado")
        print("3 - Mostrar monto a pagar para licitar")
        print("4 - Modificar cantidad de cuotas necesarias para licitar")
        print("")
        op = input("Ingrese una opcion: ")

        if op == "0":
            ban = False
        elif op == "1":
            ListaPlanes.actualizarPrecios()
            
        elif op == "2":
            valor = input("Ingrese un valor: ")
            ListaPlanes.cuotasMenores(valor)

        elif op == "3":
            codigo = input("Ingrese codigo del plan: ")
            plan = ListaPlanes.buscarPlan(codigo)
            if plan == None:
                print("Plan no encontrado")
            else:
                monto = plan.mostrarMontoNecesario()
                print(F"Monto necesario para licitar el vehiculo: {monto: .2f}")
        
        elif op == "4":
            codigo = input("Ingrese codigo del plan: ")
            plan = ListaPlanes.buscarPlan(codigo)
            if plan == None:
                print("Plan no encontrado")
            else:
                cantidad = input("Ingrese la nueva cantidad de cuotas necesarias para licitar: ")
                plan.modificarCuotasNecesarias(cantidad)

        else:
            print("Opcion no valida")
        print("")
