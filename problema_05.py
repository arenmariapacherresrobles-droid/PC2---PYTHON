#creamos una lista vacia 
numeros = []
while True:
    respuesta = input("¿Desea ingresar un número? (si/no) : ").strip().lower()
    if respuesta == "si":
       n = int(input("ingrese el número: "))
       numeros.append(n)
    elif respuesta == "no":
        break
    else:
        print("respuesta no valida, escribe si o no")

#contamos pares e impares
pares = 0
impares = 0
for n in numeros : 
    if n % 2 ==0:
        pares += 1
    else:
        impares += 1

# mostramos resultados
print("números ingresados: ", numeros)
print("cantidad de números pares: ", pares)
print("cantidad de números impares: ", impares)
         