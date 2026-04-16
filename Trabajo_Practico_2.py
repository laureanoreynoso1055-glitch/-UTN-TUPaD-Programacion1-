#consigna_1 un programa que solicite la edad al usuario y determine si es mayor o menor de edad.
edad = int(input("ingrese su edad:"))
if edad >=18 and edad <100:
   print(f"Eres mayor de edad")
elif edad <=0:
   print(f"numero invalido")
elif edad >100:
   print(f"numero invalido")
else :
   print(f"Eres menor de edad") 
   

#consigna_2 un programa que solicite su nota al usuario y determine si aprobo o desaprobo la materia.
nota = float(input("Ingrese su nota: "))
if nota >= 6 and nota <= 10:
    print("Aprobaste la materia")
else:
    print("Desaprobaste la materia")    

#Consigna_3
modulopar = int(input("Ingrese un número entero para saber si es par o impar: "))
if modulopar % 2 == 0:
    print(f"el numero {modulopar} es par")
elif modulopar % 2 != 0:
    print(f"el numero {modulopar} es impar")
   

#Consigna_4
niño = int(input("ingrese su edad : "))
if niño <= 12:
    print("Usted es un niño")
else:
    print("Usted no es un niño")
adolescente = int(input("ingrese su edad : "))
if adolescente >= 12 and adolescente <= 18:
    print("Usted es un adolescente")
else:
    print("Usted no es un adolescente")
adulto = int(input("ingrese su edad : "))
if adulto >= 18 and adulto  <= 30:
    print("Usted es un adulto joven") 
else:
    print("Usted no es un adulto joven")  
mayor = int(input("ingrese su edad : "))
if mayor >= 30:
    print("Usted es un adulto")
else:
    print("Usted no es un adulto")

#Consigna_5
numero = input("Ingrese una cotraseña entre 8 y 14 caracteres: ")
if len(numero) >= 8 and len(numero) <= 14:
    print("Contraseña válida")  
else:
    print("Contraseña inválida, intente nuevamente")

#consigna_6
#Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
#mediana es mayor que la moda. 
# Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
#la mediana es menor que la moda. 
#Sin sesgo: cuando la media, la mediana y la moda son iguales. 
import random   
from statistics import mode, median, mean 
numero_aleatorio = [random.randint(1, 100) for i in range (50)]
print(numero_aleatorio) 
print(f"la media es: {mean(numero_aleatorio)}")
print(f"la mediana es: {median(numero_aleatorio)}") 
print(f"la moda es: {mode(numero_aleatorio)}")

if  (mean(numero_aleatorio) > median(numero_aleatorio) > mode(numero_aleatorio)):
    print("sesgopositivo") 
elif (mean(numero_aleatorio) < median(numero_aleatorio) < mode(numero_aleatorio)):
    print("sesgonegativo")
elif (mean (numero_aleatorio) == median(numero_aleatorio) == mode(numero_aleatorio)):
    print("sinsesgo")
    #Consigna_7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla.
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
    print (frase)
else:
    print(frase)

    #Consigna_8
 #Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas. 
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para primera letra mayúscula: "))
if opcion == 1:
    print(nombre.upper())   
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
# Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
#Periodo del año 
#Desde el 21 de diciembre hasta el 20 de 
#marzo (incluidos) 
#Estación en el 
#hemisferio norte 
#Invierno 
#Estación en el 
#hemisferio sur 
#Desde el 21 de marzo hasta el 20 de junio 
#(incluidos) 
#Desde el 21 de junio hasta el 20 de 
#septiembre (incluidos) 
#Desde el 21 de septiembre hasta el 20 de 
#diciembre (incluidos) 
#Primavera 
#Verano 
#Otoño 
#Verano 
#Otoño 
#Invierno 
#Primavera 
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano. 
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes != 6 or dia <= 20)):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 9 or dia <= 20)):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes <= 12 and (mes != 12 or dia <= 20)):
        print("Otoño")
elif hemisferio == "S":
    if (mes == 3 and dia >= 21) or (mes <= 6 and (mes != 6 or dia <= 20)):
        print("Verano")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 9 or dia <= 20)):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes <= 12 and (mes != 12 or dia <= 20)):
        print("Primavera")
    elif (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)):
        print("Otoño")
else:
    print("Hemisferio inválido")

