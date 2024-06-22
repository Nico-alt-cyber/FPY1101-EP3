libros =[]
autores=[]
anios=[]
skus=[]
titulos_prestados = []
usuario_prestamos = []
skus_prestados=[]
fecha = "22-06-2024"

def registro():
    try:
        print("Sistema de Registro de Libros\n"+"-"*40)
        libro = str(input("Ingrese el nombre del libro: "))
        while len(libro)<= 0 or libro == " "*len(libro):
            libro = str(input("Ingrese un nombre válido: "))
        autor = str(input("Ingrese nombre del autor: "))
        while len(autor)<= 0 or autor == " "*len(autor):
            autor = str(input("Ingrese un nombre válido: "))
        anio = str(input("Ingrese el año de publicación: "))
        while not anio.isdigit():
            anio = str(input("Ingrese un año de publicación válido (solo números): "))
        sku = str(input("Ingrese el codigo SKU del Libro: "))
        libros.append(libro)
        autores.append(autor)
        anios.append(anio)
        skus.append(sku.lower())
    except ValueError:
        print("Ha Ocurrido un error. Intente de nuevo.")

def prestamo():
    try:
        nombre = str(input("Ingrese nombre del usuario: "))
        while len(nombre)<= 0 or nombre == " "*len(nombre):
            nombre = str(input("Ingrese un nombre válido: "))
        sku = str(input("Ingrese el codigo SKU del Libro: "))
        if len(skus)>0:
            for i in range (len(skus)):
                if sku.lower() == skus[i]:   #Existe el libro
                    if sku.lower() != skus_prestados[i]:  # No ha sido prestado
                        skus_prestados.append(sku.lower())
                        titulos_prestados.append(libros[i])
                        usuario_prestamos.append(nombre)
                    else:
                        print("El libro ya ha sido prestado")
                        break
                else:
                    print("El libro no se encuentra en la lista de libros.")
        else:
            print("No Hay libros registrados.")
    except ValueError:
        print("Ha ocurrido un error. Intente de nuevo.")

def listar():
    try:
        print("Título\t\tAutor\t\tAño de Publicación\t\tSKU\n"+"-"*100)
        for i in range(len(libros)):
            print(libros[i] + " "*(16-len(libros[i]))+autores[i]+ " "*(16-len(autores[i]))+anios[i]+" "*(32-len(anios[i]))+skus[i])
    except ValueError:
        print("Ha ocurrido un error. Intente de nuevo.")
def reporte():
    with open('reporte.txt','w') as reporte:
        reporte.write("Usuario\t\t\t\t\t\t\tTítulo\t\t\t\t\t\t\tFecha del préstamo\n"+ "-"*120 + "\n")
        for i in range(len(titulos_prestados)):
            reporte.write(usuario_prestamos[i] + " "*(32-len(usuario_prestamos[i]))+titulos_prestados[i]+ " "*(32-len(titulos_prestados[i]))+fecha + "\n")





