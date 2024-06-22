import os
import funciones_NicolasSanchez_FPY1101_011V as funcion
os.system("cls")
while True:
    opcion = str(input("Gestión de prestamo de libros.\n1)Registrar libro\n2)Prestar Libro\n3)Listar todos los libros\n4)Imprimir reporte de prestamos\n5)Salir\nOpción: "))
    try:
        opcionInt=int(opcion)
        if opcionInt == 1:
            funcion.registro()
        elif opcionInt == 2:
            funcion.prestamo()
        elif opcionInt == 3:
            funcion.listar()
        elif opcionInt == 4:
            funcion.reporte()
        elif opcionInt == 5:
            print("Programa Finalizado...\nDesarrollado por Nicolas Sanchez\nRut: 19.993.775-8")
            break
        else:
            print("Por favor, ingrese una opción válida (1-5)")
    except ValueError:
        print("Ha Ocurrido un Error. Intente De nuevo.")

