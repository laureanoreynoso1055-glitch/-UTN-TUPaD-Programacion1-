#1) crear una lista con las notas de 10 estudiantes.
 #.mostrar la lista completa 
 #. Calcular y mostrar el promedio .
 #. Indicaar la nota mas alta y la mas baja.


listas_notas =[2,9,8,7,6,7,5,4,9,10]
print ("Listas de notas: ", listas_notas)
sumatoria = 0
for notas in listas_notas:
    sumatoria = sumatoria + notas
    promedio =  sumatoria / len(listas_notas)
    print (notas)
print ("El promedio es:", promedio)
nota_mayor = max(listas_notas)
nota_menor = min(listas_notas)
print ("La nota mas alta es:", nota_mayor)
print ("La nota mas baja es:",nota_menor )


#2)
"""Pedir al usuario que cargue 5 productos de una lista.
    Mostrar la lista ordenada alfabeticamente.Investigue el uso del metodo sort().
     Preguntar al usuario que producto desea eliminar y actualizar la lista.
    remove = eliminar un elemento de la lista
    slicing = actualizar la """
productos = []
for prod in range(5):
    prod = input(f"Ingrese el nombre del producto: ")
    productos.append(prod)
    lista_ordenada = sorted(productos)
print("Lista de productos: ", productos)
print("Lista de productos ordenada: ", lista_ordenada)
prod = input ("Que producto desea eliminar: ")
lista_ordenada.remove(prod)
lista_ordenada = lista_ordenada[::]
print("Lista de productos actualizada: ", lista_ordenada)



"""3) Generar una lista con 15 números enteros al azar entre 1 y 100."""
lista_de_numeros = []
lista_numeros_par = []
lista_numeros_impar = []
import random 
for n in range(1,16):
    numero_aleatorio = random.randint(1,100)
    lista_de_numeros.append(numero_aleatorio)  
    if numero_aleatorio % 2 == 0 :
        lista_numeros_par.append(numero_aleatorio)
    elif numero_aleatorio % 2 != 0 :
         lista_numeros_impar.append(numero_aleatorio)
print (f"La lista de números generada es",lista_de_numeros)
print (f"La lista de  número par es",lista_numeros_par)
print (f"La lista de  número impar es",lista_numeros_impar)


#4) Dada una lista con valores repetidos:
# Crear una nueva lista sin elementos repetidos.
# Mostrar el resultado.
lista_numeros_repetidos = [1,3,5,3,7,1,9,5,3]
lista_sinrepetir = []
for numeros in lista_numeros_repetidos:
    if numeros not in lista_sinrepetir:
        lista_sinrepetir.append(numeros)
print ("La lista es",lista_numeros_repetidos)
print ("La lista de números sin repetir es",lista_sinrepetir)


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
  # Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
  # Mostrar la lista actuaizada.
lista_nombres = ["Lauro", "Sofia", "Federico", "Valentina", "Matias", "Camila", "Agustin", "Lucia"]
print (f"Lista de estudiantes presentes en clase: {lista_nombres}")
pregunta = input("¿Desea agregar un nuevo estudiante o quitar uno existente? (agregar/quitar):")
if pregunta == "agregar":
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ").upper
    lista_nombres.append(nuevo_estudiante)
    print (f"Lista actualizada de estudiantes: {lista_nombres}")
elif pregunta == "quitar":
    estudiante_a_quitar = input("Ingrese el nombre del estudiante a quitar: ").lower
    if estudiante_a_quitar in lista_nombres:
        lista_nombres.remove(estudiante_a_quitar)
        print (f"Lista actualizada de estudiantes: {lista_nombres}")
    else:
        print(f"El estudiante no se encuentra en la lista.")

#6) 
numero = [32, 10, 9, 5, 12, 14, 22]
lista_numero_rotados = numero [-1:] + numero[:-1]
print (f"El número aleatorio generado es: {numero}") 
print (f" La lista de números rotados es: ", lista_numero_rotados)

#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana. 
# Calcular el promedio de las mínimas y el de las máximas. 
#• Mostrar en qué día se registró la mayor amplitud térmica. 
lista = [[12,13,14,15,14,16,19],   #0 = [[0],[1],[2],[3],[4],[5],[6]]
         [23,34,32,30,28,27,25]]   #1 = [[0],[1],[2],[3],[4],[5],[6]]
                                    # #lista= 0 , 1 
promedio = 0
dias = ["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]

print( "La temperatura máxima es:",lista[1])
print("La temperatura minima es:",lista[0] )

for i in range (len ( lista [1])):
    total = sum (lista[1])
    dia_de_mayortemperatura = max (lista[1])
    dia_de_mayortemperatura = (lista[1]).index(dia_de_mayortemperatura)
promedio_1 = total // (i) # promedio 33,16

for i in range (len(lista [0])):
    total = sum (lista[0])
    dia_de_menortemperatura = min (lista[0])
    dia_de_menortemperatura = (lista[0]).index(dia_de_menortemperatura)
promedio_2 = total // (i) #promedio 17,16
print("El promedio de las temperaturas minimas  es:",promedio_2,"y el promedio de las temperaturas máxima  es:",promedio_1)
print("El día de mayor amplitud térmica fue el :",dias[1]) 

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 

notas =   [ [5,9,8],  #juan
            [3,10,7], #pedro
            [7,7,7],  # federico
            [3,7,8],  #constancia
            [2,1,3]]  # valeria

promedio_1 = 0
promedio_2 = 0
suma = 0
nota = 0
nombres = [["juan"],
           ["pedro"],
           ["federico"],
           ["constancia"],
           ["valeria"]]
materias = ("lengua", "matematicas", "física")

for n in notas:
    suma = sum (n)
    # print (float(suma))
for i in range (len (notas)):
    promedio_estudiantes = sum (notas [i]) / len (notas[i])
    print (f"El promedio de {nombres[i]} es: {promedio_estudiantes}")
for j in range (len (notas[0])):
    suma_materia = 0
    for i in range (len (notas)):
        suma_materia += notas [i][j]
    promedio_materia= suma_materia / len (notas)

    print (f"El promedio de la materia {materias[j]} es: {promedio_materia}")  

#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
##• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" u "O". 
##• Mostrar el tablero después de cada jugada. 
tablero = [["-","-","-",],  # fila 0 [["o","1","2"],
           ["-","-","-",],  # fila 1  ["o","1","2"],
           ["-","-","-"]]  # fila 2   ["o","1","2"]]
turnos = 0
while turnos < 9 :
    for fila in tablero:
        for elem in fila:
            print (elem, end= " ")
        print ()
    jugador = input ("Ingrese X u O para jugar: ").upper() 
    fila_jugador = int(input("Elige la fila entre( 0 y 2) :"))
    columna_jugador = int(input( "Elige una columna entre (0 y 2): "))
    if (tablero [fila_jugador][columna_jugador]) == "-":
        (tablero [fila_jugador][columna_jugador]) = jugador
    else: 
        print("Lugar ocupado") 
    turnos += 1

    for fila in tablero :
        if (fila [0] == fila[1] == fila[2]  and ( fila [0] != "-")):
            for fila in tablero:
                for elem in fila:
                    print (elem, end= " ")
                print ()
            print(f"jugador {jugador} GANO!!")     
            turnos = 9
            break
    for i in range(3):
        if (tablero[0][i] == tablero[1][i] == tablero[2][i]) and (tablero[0][i] != "-"):
            for fila in tablero:
                for elem in fila:
                    print(elem, end= " ")
                print ()
            print (f"El jugador {jugador} GANO!! ")
            turnos = 9
            break
    
        if(tablero [0][0] == tablero [1][1] == tablero [2][2]) and (tablero [0][0] != "-"):
            for fila in tablero:
                for elem in fila:
                    print(elem, end= " ")
                print ()    
            print (f"El jugador {jugador} GANO!! ")
            turnos = 9
            break
    for fila in tablero:
        if (tablero [0][2] == tablero [1][1] == tablero [2][0]) and (tablero [0][2] != "-" ):
            for fila in tablero:
                for elem in fila:
                    print(elem, end= " ")
                print ()   
            print (f"El jugador {jugador} GANO!! ")
            turnos = 9
            break
    if (turnos == 10):
        for fila in tablero:
            for elem in fila:
                print(elem, end= " ")
                print ()   
        print ("EMPATE =)")     

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana. 

productos = [[12,32,4,2,21,3,10], #0  #papa  1     [ [o,1,2,3,4,5,6,7]   #84
             [3,5,23,56,32,34,12],#1  #ceboll  3     [o,1,2,3,4,5,6,7]   #165
             [5,3,2,6,7,8,33],    #2  #zapallo 6    [o,1,2,3,4,5,6,7]    #64
             [4,5,3,8,4,12,15]]   #3  #camote  6    [o,1,2,3,4,5,6,7] ]  #51
#productos [0][1]
nombre_productos = ["papa", "cebolla", "zapallo", "camote"] 
dia_ventas = ["domingo", "lunes", "martes","miercoles","jueves","viernes", "sabado"]
suma = 0
mas_vendido = 0
for prod in productos:                
    suma = sum(prod)                             #suma de elementos: 84 / 165 /64
    if (suma > mas_vendido):       # 84 & 0, 165 & 32, 51&33 
        mas_vendido = suma          # 84 # 165 #64 #51
        indice_mas_vendido = productos.index(prod)  # 1 # 3
    print (f"EL total de productos vendido es :",suma)# 84  # 165 #64 #51
    venta_mayor = max (prod) #32 #56 #33 #15
    dia_de_mayor_venta = prod.index(venta_mayor)    #32 #56 #33 #15
    print(f"El día de mayores ventas totales fue:{dia_ventas[dia_de_mayor_venta]}") # 1 # 3 #6 #6
print (f"El producto mas vendido de la semana fue {nombre_productos[indice_mas_vendido]} con  {mas_vendido} ventas.")