#colocamos los dos primeros numeros de la serie
a, b = 0, 1
print("serie de fibonacci entre 0 y 50: ")
while a <= 50:
    print(a,end = " ")
    a,b = b , a + b