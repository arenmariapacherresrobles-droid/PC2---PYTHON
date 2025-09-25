print("números perfectos menores que 1000: ")
for n in range(2,1000):
    suma_divisores = 0 
    for d in range(1,n):
        if n% d == 0:
            suma_divisores +=d
    if suma_divisores ==n:
        print(n)
