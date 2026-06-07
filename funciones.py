# Libreria
import random as rand
# Funciones
def adivinar_numero(numero_usuario, apuesta_usuario):
    intentos = 3
    while intentos >= 0:
        dinero = 0 
        # Pedirle un número al usuario
        # Generar un número al azar
        numero_cpu = rand.randint(0,101)
        # Comparar input del usuario con el número generado
        # Si está correcto:
        # Entregar dinero
        if numero_usuario == numero_cpu:
            ganancias = apuesta_usuario * 2
            break
        # Si está incorrecto:
        elif numero_usuario < numero_cpu:
        # Decirle al usuario si está cerca o lejos del número
        # Mostrarle los intentos que quedan
            print("El número correcto está más arriba")
            intentos -= 1
            print(f"INTENTOS RESTANTES... {intentos} \n")
            ganancias = 0
        else:
            print("El número correcto está más abajo")
            intentos -= 1
            print(f"INTENTOS RESTANTES... {intentos} \n")
            ganancias = 0
    print("Gracias por jugar...")
    return ganancias 