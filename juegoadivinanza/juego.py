import random

numero_secreto = random.randint(0, 100)
cantidad_intentos = 0
cantidad_maxima_intentos = 6
adivinado = False

print("¡Bienvenido al juego de adivinanza!")
print("Tengo un número entre 0 y 100. Adivina cuál es.")

while not adivinado:
    
    if cantidad_intentos >= cantidad_maxima_intentos:
        print("Has agotado tus intentos. El número era:", numero_secreto)
        break

    intento = int(input("Ingresa tu intento: "))
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! Has adivinado el número.")
        adivinado = True

    cantidad_intentos += 1