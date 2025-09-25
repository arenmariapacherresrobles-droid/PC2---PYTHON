# creamos una lista vacia 
alumnos =[]
# número de alumnos a ingresar 
n = int(input("¿cuántos alumnos desea registrar? "))
for i in range(n):
    nombre = input(f"ingrese el nombre del alumno {i+1}: ")

    notas = []
    for j in range(3):
        nota = int(input(f"ingrese la nota {j+1} de {nombre}"))
        notas.append(nota)

#para cada alumno, pedimos el nomnre y 3 notas
#creamos un diccionario 

alumno ={"alumno": nombre, "notas": notas}
alumnos.append(alumno)

print("listado de alumnos: ")
for a in alumnos:
    print(f"alumno: {a['alumno']}, notas: {a['notas']}")