from ejercicio import validar_nombre, validar_edad, validar_nota, agregar_estudiante, buscar_estudiante, eliminar_estuadiante, mostrar_estudiantes, actualizar_estado, menu, mostrar_opcion

estudiantes = []
mostrar_menu = True

while mostrar_menu:
    menu()
    opcion = mostrar_opcion()

    if opcion == 1:
        Agregar_producto()
    elif opcion == 2:
        buscar_producto()
    elif opcion == 3:
        eliminar_producto()
    elif opcion == 4:
        actualizar_disponibilidad()
    elif opcion == 5:
        mostrar_productos()
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto.")
        mostrar_menu = False