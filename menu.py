from opciones import registro_de_estudiantes
def menu_de_opciones():
   
    print("1.registrar un nuevo estudiante")
    print("2.consultar lista de estudiantes")
    print("3.buscar estudiante con id o nombre")
    print("4.actualizar informacion de un estudiante")
    print("5.eliminar estudiantes")
   
    opcion=int(input("escoja la opcion que desea realizar"))
    while opcion==1:
        registro_de_estudiantes()