
# ? Función de menu
def desplegarNombre():
    print("Nombre del alumno: magdiel")
    input("Presione una tecla para continuar...")

def desplegarCarnet():
    print("Carnet del alumno: 201801449")
    input("Presione una tecla para continuar...")


def desplegarNombreCarnet():
    print("Nombre del alumno: magdiel")
    print("Carnet del alumno: 201801449")
    input("Presione una tecla para continuar...")

def salir():
    print("Gracias por utilizar el programa")
    input("Presione una tecla para continuar...")

def menu():
    print("=========================================")
    print("| LENGUAJES FORMALES Y DE  PROGRAMACIÓN |")
    print("|             SECCIÓN B+                |")
    print("=========================================")
    print("| 1. Desplegar Nombre                   |")
    print("| 2. Desplegar Carnet                   |")
    print("| 3. Desplegar Nombre y Carnet          |")
    print("| 4. Salir                              |")
    print("=========================================")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        desplegarNombre()
        menu()
    elif  opcion == 2:
        desplegarCarnet()
        menu()
    elif opcion == 3:
        desplegarNombreCarnet()
        menu()
    elif opcion == 4:
        salir()
    else:
        print("Opción no válida")
        menu()



menu()
    