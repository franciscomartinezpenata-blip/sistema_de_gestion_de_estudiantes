
lista_de_estudiantes=[]
def registro_de_estudiantes():
    print ("ingrese los datos")
    ID=int (input ("ingrese el numero indentificador "))
    nombre=input ("nombre del nuevo estudiante ")
    edad= int(input("ingrese la edad del nuevo estuante "))
    estado=input("estudiante es activo o inactivo ")
    base_de_datos={"ID":ID, "nombre":nombre, "edad":edad, "estado":estado}
    lista_de_estudiantes.append (base_de_datos)
    return lista_de_estudiantes
