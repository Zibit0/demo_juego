# Libreria
import random as rand
# Funciones
def adivinar_numero(numero_usuario, apuesta_usuario):
    dinero = 0 
    # Pedirle un número al usuario
    # Generar un número al azar
    numero_cpu = rand.randint(0,101)
    # Comparar input del usuario con el número generado
    # Si está correcto:
    # Entregar dinero
    if numero_usuario == numero_cpu:
        ganancias = apuesta_usuario * 2
    # Si está incorrecto:
    elif numero_usuario < numero_cpu:
    # Decirle al usuario si está cerca o lejos del número

    # Mostrarle los intentos que quedan