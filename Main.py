from Menu import Menu
if __name__ == '__main__':
    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Inscribir persona en un taller
              2 Consultar inscripcion de una persona
              3 Consultar inscriptos en un taller
              4 Registrar pago de una inscripción
              5 Crear un archivo de los inscriptos""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op)
        salir = op == 0