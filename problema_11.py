texto = input ("escribe una frase: ")
#decidimos que queremos eliminar 
vocales = "aeiouAEIOU"
#recorremos cada letra y solo la agregamos si no es vocal
resultado = ""
for letra in texto:
    if letra not in vocales :
        resultado += letra 
print(resultado)