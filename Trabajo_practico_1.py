#consigna_1 crea un programa que imprima en pantalla "¡hola, mundo!"
print ("¡hola, mundo!")


#consigna_2 crea un programa que le pida al usuario su nombre e imprima en pantalla "Hola <nombre>"
nombre = input (f"ingrese su nombre: ")
print (f"Hola", nombre)


#consigna_3 crea un programa que le pida al usuario su nombre, apellido, lugar de residencia y edad e imprima en pantalla "Hola, me presento: <nombre> <apellido>, que vive en <lugar de residencia> y tiene <edad> años."
nombre = input (f"ingrese su nombre: ")
apellido = input (f"ingrese su apellido: ")
lugar_de_residencia = input (f"ingrese su lugar de recidencia: ")
edad = int (input("ingrese su edad: "))
print (f"soy {nombre} {apellido}, que vive en {lugar_de_residencia} y tengo {edad} años.")

#consigna_4 crea un programa que pida al usuario el radio de un círculo e imprima en pantalla su perimetro y área.
#¿calcula el radio del circulo?
diametro = float (input("ingrese el diametro del circulo: "))
radio = diametro / 2    
print (f"el radio del circulo es: {radio}")
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print (f"el area del circulo es: {area}")
print (f"el perimetro del circulo es: {perimetro}")

#consigna_5 crea un programa que pida al usuario una cantidad de segundos e imprima en pantalla a cuantas horas equivalen.
segundos = int (input("ingrese una cantidad de segundos: "))
horas = segundos / 3600
print (f"la cantidad de segundos ingresada equivale a: {horas} horas")

#consigna_6 crea un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de ese número.
numero = int (input("ingrese un numero para ver su tabla de multiplicar: "))
for i in range (1,11):
    resultado = numero * i
    print (f"{numero} x {i} = {resultado}")

#consigna_7 
numero1 = int (input("ingrese un numero entero distinto de cero: "))
numero2 = int (input("ingrese otro numero entero distinto de cero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print (f"la suma de {numero1} + {numero2} es: {suma}")
print (f"la resta de {numero1} - {numero2} es: {resta}")
print (f"la multiplicacion de {numero1} * {numero2} es: {multiplicacion}")
print (f"la division de {numero1} / {numero2} es: {division}")  

#consigna_8 
altura = float (input("ingrese su altura en metros: "))
peso = float (input("ingrese su peso en kilogramos: ")) 
imc = peso / (altura ** 2)
print (f"su indice de masa corporal es: {imc}") 

#consigna_9
temperatura_celsius = float (input("ingrese una temperatura en grados celsius:"))
temperatura_farenheit = (temperatura_celsius * 9/5) + 32 
print (f"la temperatura en grados farenheit es: {temperatura_farenheit}")

#consigna_10
numero1 = int (input("ingrese un numero entero:"))
numero2 = int (input("ingrese otro numero entero:"))
numero3 = int (input("ingrese un tercer numero entero:"))
promedio = (numero1 + numero2 + numero3) / 3
print (f"el promedio de los tres numeros ingresados es: {promedio}")

import random

numero_correcto = random.randint(1,100) 

numero_usuario = int(input("Adivina el número entre 1 y 100: ")) 

if numero_usuario == numero_correcto:
     
      print("¡Has adivinado el número!") 

elif numero_usuario < numero_correcto:

     print("Intenta con un número mayor.") 
else:   
     print("Intenta con un número menor.")

