#consigna N°1
print ("Números del 0 al 100:")
for numeros in range (0,101):
     print (numeros)


#consigna N°2 

numero_ingresado = input("Para saber la cantidad de digitos de un número,Ingrese los números enteros: ")

cantidad_digitos = len(numero_ingresado)    
print("La cantidad de dígitos del número ingresado es:", cantidad_digitos)  

#consigna N°3 
numero_1 = input ("Ingrese el primer número entero: ")
numero_2 = input ("Ingrese el segundo número entero: ")
sumatoria = 0
for cont in range (int(numero_1)+1,int(numero_2)):
     sumatoria += cont
print ("La sumatoria de los números enteros es", sumatoria)

#consigna N°4
sumatoria = 0
for cont in range (1,numeros+1):
     print ("ingrese el número!",cont)
     print("Si desea finalizar el programa ingrese el número 0")
     numeros = int (input())
     sumatoria = sumatoria + numeros
     if numeros == 0:
          print ("La sumatoria de los números enteros es", sumatoria)
          break



#consigna N°5
aleatorio = 0
import random
aleatorio = random.randint(0,10)
sumatoria = 0
for cont in range (10):
     print ("Ingrese un número entre 0 y 9: ")
     numero = int (input())
     if numero == aleatorio:
          sumatoria = sumatoria + cont
          print ("¡Ganaste! La sumatoria de los intentos ingresados es", sumatoria+1)
          break
     else:
          print ("¡Perdiste!")
          print ("intentalo de nuevo, tu puedes ")


#consigna N°6
import random
aleatorio = random.randint(0,101,)
for numeros_pares in range (100,1,-2):   
          print (numeros_pares)

#consigna N°7
numeros = int (input ("Ingrese un número entero positivo: "))
sumatoria = 0
for cont in range (numeros+1):
      sumatoria += cont 
print ("La sumatoria de los números enteros es", sumatoria)

#consigna N°8
cont_1= 0
cont_2= 0
cont_3= 0
cont_4= 0
cantidad_numeros = 10
for cont in range (cantidad_numeros+1):
          print("Ingrese el número entero!",cont)
          numeros = int(input())
          if numeros % 2 == 0:
               cont_1 += 1
          elif numeros % 2 != 0:
               cont_2 += 1
          if numeros > 0:
               cont_3 += 1
          elif numeros < 0:
               cont_4 += 1

print("la cantidad de numeros pares es",cont_1)  
print("la cantidad de numeros impares es",cont_2)
print("la cantidad de numeros positivos es",cont_3)
print("la cantidad de numeros negativos es",cont_4) 

#consigna N°9
cantidad_de_numeros = 5
suamtoria = 0
for cont in range(1,cantidad_de_numeros+1):
     print ("Ingrese el número entero!",cont)
     num = int(input())  
     suamtoria += num
     print ()
print("La sumatoria de la variable es: ", suamtoria)
print ("La media de los númreos ingresados es: ", (suamtoria/cantidad_de_numeros,"cantida de numeros ingresados:",cont))


#consigna N°10
numero = input("Ingrese un número entero: ")
numero_invertido = numero[::-1]
print("///////////////////////////")
print("ok, el número ingresado es:", numero)
print("///////////////////////////")
print("El número invertido es:", numero_invertido)














 



























