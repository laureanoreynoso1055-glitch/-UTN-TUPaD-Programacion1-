 ###“Caja del Kiosco”###
#OBJETIVO:Simular una compra con validaciones y cálculo de total. 
#Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
while True:
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    nombre_cliente = " ".join(nombre_cliente.split())
    if  nombre_cliente.isalpha():
        print("El nombre debe contener solo letras. Por favor, ingrese un nombre válido.")
    elif not nombre_cliente:
        print("El nombre no puede estar vacío. Por favor, ingrese un nombre válido.")
    else:
        nombre_cliente = nombre_cliente.title() # titulizar el nombre para una mejor presentación
        break

#Pedir cantidad de productos a comprar (número entero positivo, validar con 
#.isdigit() en while).
while True:
    cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")
    if not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
        print("La cantidad debe ser un número entero positivo. Por favor, ingrese una cantidad válida.")
    else:
        cantidad_productos = int(cantidad_productos)
        break 
#Por cada producto (usar for): 
#o Pedir precio (entero, validar .isdigit()). 
#o Pedir si tiene descuento S/N (validar con while, aceptar s o n en 
#cualquier mayuscula/minuscula). 
#o Si tiene descuento: aplicar 10% al precio de ese producto.
total = 0
total_sin_descuento = 0
ahorro_total = 0

for i in range(cantidad_productos):
    #ingreso de precio con validación   
    while True:
        precio = input(f"Ingrese el precio del producto {i+1}: ")
        if not precio.isdigit() or int(precio) <= 0:
            print("El precio debe ser un número entero positivo. Por favor, ingrese un precio válido.")
        else:
            precio = int(precio)
            break
    total_sin_descuento += precio #acumulador para total sin descuentos
    while True:
        descuento = input(f"¿El producto {i+1} tiene descuento? (S/N): ").strip().upper()
        if descuento not in ['S', 'N']:
            print("Por favor, ingrese 'S' para sí o 'N' para no.")
        else:
            break
    if descuento == 'S':
        ahorro = precio * 0.1 #calculo del ahorro por descuento para cada producto
        precio *= 0.9  # Aplicar 10% de descuento
        ahorro_total += ahorro #acumulador para total ahorrado
    else:
        print(f"El precio del producto {i+1}es: ${precio:.2f}")   
    total += precio #acumulador total final
    promedio = total / cantidad_productos #calculo del promedio por producto
#Al finalizar la compra, mostrar el total a pagar.
print("\nResumen de la compra: ")
print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")
print(f"Total sin descuentos: ${total_sin_descuento:.2f}")
print(f"Total con descuentos aplicados: ${total:.2f}")
print(f"Total ahorrado por descuentos: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${float(promedio):.2f}")
print(f"El total a pagar por {nombre_cliente} es: ${total:.2f}")

print("/////////////////////////////////////////////")

#EJERCICIO 2 Acceso al campus y menu seguro.
USUARIO = "alumno"
CONTRASEÑA = "python123"
intentos = 3
for n in range(intentos):
    usuario_ingresado = input("Ingrese su usuario:")
    contraseña_ingresada = input("Ingrese su contraseña:")
    print (f"Intentos {n+1} de  {intentos}")
    if usuario_ingresado == USUARIO and contraseña_ingresada == CONTRASEÑA:
        print("Acceso concedido. Bienvenido al campus.")
        while True:
            print("Menu de opciones:"
                    "\n1. Ver estado de inscripción"
                    "\n2. Cambiar contraseña"
                    "\n3. Ver mensaje motivacional"
                    "\n4. Salir")
            opcion = input("Seleccione una opción (1-4): ")
            if opcion == "1":
                print("Tu estado de inscripción es: Inscripto")
            elif opcion == "2":
                nueva_contraseña = input("Ingrese su nueva contraseña de 6 caracteres: ")
                if len(nueva_contraseña) == 6:
                    CONTRASEÑA = nueva_contraseña
                    print("Contraseña actualizada exitosamente.")
                    print("Tu nueva contraseña es: ", CONTRASEÑA)
                else:
                    print("La contraseña debe tener 6 caracteres.")
            elif opcion == "3":
                print("¡LO QUE HACEMOS EN VIDA RESUENA EN LA ETERNIDAD!")
            elif opcion == "4":
                print("Gracias por visitar el campus. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        break
    else:
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
else:
    print("Has agotado tus intentos. Acceso bloqueado.")

print("/////////////////////////////////////////////")

#EJERCICIO 3 Sistema de turnos para una clínica.

nombre_operador = input ("Ingrese el nombre del operador: ").strip().title()
while not nombre_operador.replace(" ", "").isalpha():
    print("El nombre del operador debe contener solo letras. Por favor, ingrese un nombre válido.")
    nombre_operador = input("Ingrese el nombre del operador: ").strip().title()
  
print(f"Bienvenido {nombre_operador} al sistema de turnos.")

#variables para almacenar las reservas de cada día (sin usar listas)
reserva_lunes1 = ""
reserva_lunes2 = ""
reserva_lunes3 = ""
reserva_lunes4 = ""

reserva_martes1 = ""    
reserva_martes2 = ""
reserva_martes3 = ""

while True:
    print("\nMenú de opciones:")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione una opción (1-5): ").strip()

    if opcion == '1':
        
        dia = input("Seleccione el día para reservar el turno (1=Lunes, 2=Martes): ").strip()
        nombre_paciente = input("Ingrese el nombre del paciente: ").strip().title()
        
        if not nombre_paciente.replace(" ", "").isalpha():
            print("El nombre del paciente debe contener solo letras. Por favor, ingrese un nombre válido.")

        if dia == '1':
            if nombre_paciente == reserva_lunes1 or nombre_paciente == reserva_lunes2 or nombre_paciente == reserva_lunes3 or nombre_paciente == reserva_lunes4:
                print("El paciente ya tiene un turno reservado para ese día.")
            elif reserva_lunes1 == "":
                reserva_lunes1 = nombre_paciente
                print (f"Turno reservado para {nombre_paciente} el Lunes.")
            elif reserva_lunes2 == "":
                reserva_lunes2 = nombre_paciente
                print (f"Turno reservado para {nombre_paciente} el Lunes.")
            elif reserva_lunes3 == "":
                reserva_lunes3 = nombre_paciente
                print (f"Turno reservado para {nombre_paciente} el Lunes.")
            elif reserva_lunes4 == "":
                reserva_lunes4 = nombre_paciente
                print (f"Turno reservado para {nombre_paciente} el Lunes.")
            else:
                print("No hay cupo para ese día.")

        elif dia == '2':
            if nombre_paciente == reserva_martes1 or nombre_paciente == reserva_martes2 or nombre_paciente == reserva_martes3:
                print("Paciente ya registrado en Martes.")
            else:
                if reserva_martes1 == "":
                        reserva_martes1 = nombre_paciente 
                        print (f"Turno reservado para {nombre_paciente} el Martes.")  
                elif reserva_martes2 == "":
                        reserva_martes2 = nombre_paciente
                        print (f"Turno reservado para {nombre_paciente} el Martes.")
                elif reserva_martes3 == "":
                    reserva_martes3 = nombre_paciente
                    print (f"Turno reservado para {nombre_paciente} el Martes.")
                
                else:
                    print("No hay cupo para ese día.")
        else:
            print("Día no válido. Por favor, seleccione 1 para Lunes o 2 para Martes.")     





    
    elif opcion == '2':
        dia = input("Seleccione el dia para cancelar el turno  (1=Lunes, 2=Martes):").strip()
        nombre_paciente = input("Ingrese el nombre del paciente para cancelar el turno: ").strip().title()
        if not nombre_paciente.replace(" ", "").isalpha():
            print("El nombre del paciente debe contener solo letras. Por favor, ingrese un nombre válido.")
        
        if dia == "1":
            if nombre_paciente == reserva_lunes1:
                reserva_lunes1 = ""
            elif nombre_paciente == reserva_lunes2:
                reserva_lunes2 = ""
            elif nombre_paciente == reserva_lunes3:
                reserva_lunes3 = ""
            elif nombre_paciente == reserva_lunes4:
                reserva_lunes4 = ""
            else:
                print("No se encontró el turno.")
        elif dia == "2":
            if nombre_paciente == reserva_martes1:
                reserva_martes1 = ""
            elif nombre_paciente == reserva_martes2:
                reserva_martes2 = ""
            elif nombre_paciente == reserva_martes3:
                reserva_martes3 = ""
            else:
                print("No se encontró el turno.")


    elif opcion == '3':
        # Lógica para ver agenda del día
        dia = input("Seleccione día (1=Lunes, 2=Martes): ").strip().title()

        if dia == "1":
            print("\nAgenda Lunes:")
            print("1:", reserva_lunes1)
            print("2:", reserva_lunes2)
            print("3:", reserva_lunes3)
            print("4:", reserva_lunes4)

        elif dia == "2":
            print("\nAgenda Martes:")
            print("1:", reserva_martes1)
            print("2:", reserva_martes2)
            print("3:", reserva_martes3)


    elif opcion == "4":
        print("\n--- RESUMEN GENERAL ---")
        print("Lunes:")
        print(reserva_lunes1, reserva_lunes2, reserva_lunes3, reserva_lunes4)

        print("Martes:")
        print(reserva_martes1, reserva_martes2, reserva_martes3)
    
    elif opcion == '5':
            print("Cerrando el sistema. ¡Hasta luego!")
            break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.") 

print("/////////////////////////////////////////////")


# “Escape Room: La Bóveda”
# VARIABLES INICIALES
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

# VALIDACIÓN NOMBRE
nombre = input("Ingrese nombre del agente: ").strip().title()

while not nombre.isalpha():
    print("Nombre inválido. Solo letras.")
    nombre = input("Ingrese nombre del agente: ").strip().title()

print(f"\nAgente {nombre}, misión iniciada...\n")

# JUEGO
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # BLOQUEO POR ALARMA
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("🚨 La bóveda se bloqueó por la alarma. DERROTA.")
        break

    # ESTADO
    print("\n--- ESTADO ---")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVA' if alarma else 'INACTIVA'}")

    # MENÚ
    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione opción: ")

    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        print("Opción inválida.")
        opcion = input("Seleccione opción: ")

    # ---------------- FORZAR ----------------
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        # ANTI-SPAM
        if racha_forzar == 3:
            print("⚠️ Forzaste demasiadas veces seguidas. La cerradura se trabó.")
            alarma = True
            racha_forzar = 0
            continue

        # RIESGO DE ALARMA
        if energia < 40:
            numero = input("Riesgo de alarma! Elegí número (1-3): ")

            while not numero.isdigit() or numero not in ["1", "2", "3"]:
                print("Número inválido.")
                numero = input("Elegí número (1-3): ")

            if numero == "3":
                print("🚨 Activaste la alarma!")
                alarma = True
                continue

        # ABRIR CERRADURA
        if not alarma:
            cerraduras_abiertas += 1
            print("🔓 Abriste una cerradura!")

    # ---------------- HACKEAR ----------------
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        racha_forzar = 0  # corta racha

        print("Hackeando...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("💻 Hackeo exitoso! Se abrió una cerradura.")

    # ---------------- DESCANSAR ----------------
    elif opcion == "3":
        tiempo -= 1
        energia += 15
        racha_forzar = 0  # corta racha

        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10
            print("⚠️ Descansar con alarma activa consume energía extra.")

        print("😴 Recuperaste energía.")

# ---------------- RESULTADO FINAL ----------------
if cerraduras_abiertas == 3:
    print("\n🏆 VICTORIA! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("\n💀 DERROTA! Te quedaste sin recursos.")

print("////////////////////////////////////////////////////")

#“Escape Room:"La Arena del 
# Gladiador"  
    
print("--- BIENVENIDO A LA ARENA ---")

# ---------------- NOMBRE ----------------
nombre = input("Nombre del Gladiador: ").strip().title()

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ").strip().title()

# ---------------- VARIABLES ----------------
vida_jugador = 100        # int
vida_enemigo = 100        # int
pociones = 3              # int
danio_jugador = 15        # int
danio_enemigo = 12        # int
turno_jugador = True      # bool

print("\n=== INICIO DEL COMBATE ===")

# ---------------- COMBATE ----------------
while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    
    # -------- TURNO DEL JUGADOR --------
    if turno_jugador:
        print("\nElige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        # VALIDACIÓN
        while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        # -------- OPCIÓN 1 --------
        if opcion == "1":
            danio_final = danio_jugador

            if vida_enemigo < 20:
                danio_final = danio_jugador * 1.5  # float
                print("¡Golpe crítico!")

            vida_enemigo -= danio_final
            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

        # -------- OPCIÓN 2 --------
        elif opcion == "2":
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        # -------- OPCIÓN 3 --------
        elif opcion == "3":
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Recuperaste 30 HP")
            else:
                print("¡No quedan pociones!")

        # -------- TURNO ENEMIGO --------
        if vida_enemigo > 0:
            vida_jugador -= danio_enemigo
            print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

# ---------------- RESULTADO ----------------
print("\n=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f" ¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print(" ¡DERROTA. Has caído en combate.")
