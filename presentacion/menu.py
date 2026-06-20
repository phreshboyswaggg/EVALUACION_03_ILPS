from negocio.ejercicios import ejercicio_1, ejercicio_2, ejercicio_3

def mostrar_menu():
    while True:
        print()
        print("Bienvenido, seleccione el servicio que necesita")
        print("=====================")
        print("1: Registro de compras")
        print("2: Gestion de cursos")
        print("3: Estadísticas de ventas")
        print("0: Salir")
        try:
            op=int(input("Opcion: "))
            if op==1:
                ejercicio_1()
            elif op==2:
                ejercicio_2()
            elif op==3:
                ejercicio_3()
            elif op==0:
                print("Adios y que tenga un buen dia")
                break
            else:
                print("Opcion invalida, porfavor ingrese una de las opciones mostradas.")
        except ValueError:
            print("Opcion invalida, debe de ingresar un numero.")
