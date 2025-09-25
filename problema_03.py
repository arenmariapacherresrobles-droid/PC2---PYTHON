def numeros_divisibles_multiplos (limite_inferior, limite_superior):
   if limite_superior > limite_inferior:
      
    resultado =[]

    for n in range(limite_inferior, limite_superior +1):
         if n % 7 == 0 and n % 5 == 0 :
              resultado.append(n)
              
    return resultado
   
   raise ValueError('el limite inferior debe ser menor al mimite superior.')

