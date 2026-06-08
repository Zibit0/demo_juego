# Libreria
import random as rand
# Funciones
def adivinar_numero(numero_usuario, apuesta_usuario):
    # Pedirle un número al usuario
    dinero = 0
    intentos = 3
    while intentos >= 0:
        dinero = 0  
        # Generar un número al azar
        numero_cpu = rand.randint(0,101)
        # Comparar input del usuario con el número generado
        if numero_usuario == numero_cpu:
            ganancias = apuesta_usuario * 2
            break
        # Si está incorrecto:
        # Decirle al usuario si está cerca o lejos del número
        elif numero_usuario < numero_cpu:
            print("El número correcto está más arriba")
            ganancias = 0
            intentos -= 1
            print(f"INTENTOS RESTANTES... {intentos} \n")
            pass
        else:
            ganancias = 0
            intentos -= 1
            print("El número correcto está más abajo")
            print(f"INTENTOS RESTANTES... {intentos} \n")
        print("Gracias por jugar...")
        return ganancias 
        
def blackJack(mazo=[], mazoDescarte=[]):
    # Determinar si el mazo es >= 10
    # Mientras el mazo sea mayor a diez se puede jugar
    # Cuando el mazo disminuya de diez hacer un shuffle
    # 
    pass