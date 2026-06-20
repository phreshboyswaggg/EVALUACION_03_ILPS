from datos.datos_app import compras, cursos, ventas

def ejercicio_1():
    try:
        compras = []
        total = 0
        seguir = "si"

        while seguir == "si":
            producto = input("Ingrese el nombre del producto: ")
            precio = int(input("Ingrese el precio: "))
            compras.append({"producto": producto,"precio": precio})
            seguir = input("Desea agregar otra compra?: ").lower()

        for compra in compras:
            total += compra["precio"]
        print(f"Su total es: ${total}")

        if len(compras) >0:
            print(f"El promedio es: ${total/len(compras)}")
    except ValueError:
        print("Dato incorrecto, ingrese un dato valido")

def ejercicio_2():
    try:
        seguir="si"
        while seguir=="si":
            curso=input("Escriba el nombre del curso: ")
            cantidad=int(input("Ingrese la cantidad de inscritos en el curso: "))
            cursos[curso]=cantidad
            seguir=input("Desea ingresar otro curso?: ").lower()
        mayor=""
        cantidad_mayor=0
        for curso in cursos:
            if cursos[curso] > cantidad_mayor:
                cantidad_mayor=cursos[curso]
                mayor=curso
        print (f"El curso con mas inscritos es {mayor} con {cantidad_mayor} inscritos")
    except ValueError:
        print("Dato incorrecto, ingrese un dato valido")

def ejercicio_3():
    try:
        seguir="si"
        while seguir=="si":
            venta=int(input("Ingrese las ventas del mes: "))
            ventas.append(venta)
            seguir=input("Desea ingresar otra venta?: ").lower()
        mayor=ventas[0]
        menor=ventas[0]
        suma=0
        for venta in ventas:
            suma += venta
            if venta > mayor:
                mayor=venta
            if venta < menor:
                menor=venta
        print(f"La venta maxima fue de: {mayor}$")
        print(f"La venta minima fue de: {menor}$")
        print(f"El promedio de ventas es: {suma/len(ventas)}$")
    except ValueError:
        print("Dato incorrecto, ingrese un dato valido")
