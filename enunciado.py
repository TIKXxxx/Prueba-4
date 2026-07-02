from operaciones import validar_nombre, validar_edad, validar_nota, agregar_estudiante, buscar_estudiante, eliminar_estuadiante, mostrar_estudiantes, actualizar_estado, menu, mostrar_opcion

estudiantes = []
mostrar_menu = True

while mostrar_menu:
    menu()
    opcion = mostrar_opcion()

    if opcion == 1:
        agregar_estudiante()
    elif opcion == 2:
        buscar_estudiante()
    elif opcion == 3:
        eliminar_estuadiante()
    elif opcion == 4:
        actualizar_estado()
    elif opcion == 5:
        mostrar_estudiantes()
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto.")
        mostrar_menu = False