#funcion 
def factorial(n):
    resultado =1 
    # bucle desde 1 hasta n
    for i in range (1, n+1) : 
        #multiplicar el acumulado por i
        resultado = resultado * i
    #devolver el resultado final 

    return resultado 
print (factorial (6))