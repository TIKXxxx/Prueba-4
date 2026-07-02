estudiantes = []
def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("====================================")

def mostrar_opcion():
    opcion = 0
    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input("Ingrese una opcion (1-6): "))
            if opcion < 1 or opcion > 6:
                print("Ingrese una opcion del 1 al 6.")
        except ValueError:
            print("Solo se admiten numeros.")
    return opcion

def validar_nombre(nombre_valido):
    return nombre_valido.strip() != ""

def validar_edad(edad_valida):
    return edad_valida > 0

def validar_nota(nota_valida):
    return 1.0 <= nota_valida <= 7.0

def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")

    try:
        edad = int(input("Ingrese la edad del estudiante: "))
        nota = float(input("Ingrese la nota del estudiante: "))
    except ValueError:
        print("Solo se amiten numeros")

    if not validar_nombre(nombre):
        print("El nombre no debe contener espacios ni estar vacio.")
    elif not validar_edad(edad):
        print("La edad debe ser un numero entero mayor que 0.")
    elif not validar_nota(nota):
        print("La nota debe ser un numero decimal entre 1 y 7.")
    else:
        nuevo_estudiante = {
            "nombre": nombre,
            "edad": edad,
            "nota": nota,
            "aprobado": False
        }
        estudiantes.append(nuevo_estudiante)
        print("Estudiantre agregado con exito!")

def buscar_estudiante(estudiantes, dato_busqueda):
    posicion = -1
    i = 0
    while i < len(estudiantes) and posicion == -1:
        if estudiantes[i]["nombre"] == dato_busqueda:
            posicion = i
        i += 1
    return posicion


def eliminar_estuadiante(estudiantes):
    dato_busqueda = input("Ingrese el estudiante que desea eliminar: ").strip()
    posicion = buscar_estudiante(estudiantes, dato_busqueda)

    if posicion != -1:
        estudiantes.pop(posicion)
        print("Estudiante eliminado de la lista con exito!")
    else:
        print(f"Estudiante {dato_busqueda} no se encuentra registrado.")

def actualizar_estado(estudiantes):
    for estudiante in estudiantes:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
        else:
            estudiante["aprobado"] = False

def mostrar_estudiantes(estudiantes):
    actualizar_estado(estudiantes)
    print("=== LISTA DE ESTUDIANTES ===")

    if len(estudiantes) == 0:
        print("No hay estudiantes agregados en la lista.")
    else:
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Edad: {estudiante['edad']}")
            print(f"Nota: {estudiante['nota']}")
            if estudiante["aprobado"]:
                print("Estado: aprobado")
            else:
                print("Estado: no aprobrado")
        print("********************************************")

estudiantes = []
mostrar_menu = True

while mostrar_menu:
    menu()
    opcion = mostrar_opcion()

    if opcion == 1:
        agregar_estudiante(estudiantes)
    elif opcion == 2:
        dato_busqueda = input("Ingrese el nombre del estudiante a buscar: ").strip().lower()
        posicion = buscar_estudiante(estudiantes, dato_busqueda)

        if posicion != -1:
            print(f"Estudiante encontrado en: {estudiantes[posicion]}.")
        else:
            print("No se a encontrado el estudiante.")
    elif opcion == 3:
        eliminar_estuadiante(estudiantes)
        if len(estudiantes) == 0:
            print("No hay estudiantes para eliminar.")
        else:
            print("Estudiante eliminado de la lista con exito!") 
    elif opcion == 4:
        actualizar_estado(estudiantes)
        if len(estudiantes) == 0:
            print("No hay estudiantes para actualizar estados.")
        else:
            print("Estados actualizados!") 
    elif opcion == 5:
        mostrar_estudiantes(estudiantes)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto.")
        mostrar_menu = False