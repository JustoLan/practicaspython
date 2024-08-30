jugador1 = input("jugador 1 piedra papel o tijera?: ")
jugador2 = input("jugador 2 piedra papel o tijera?: ")

if jugador1 != "piedra" and jugador1 != "papel" and jugador1 != "tijera":
    print("Jugador 1, introduce una opción correcta")
    exit()
elif jugador2 != "piedra" and jugador2 != "papel" and jugador2 != "tijera":
    print("Jugador 2, introduce una opción correcta")
    exit()

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "tijera" and jugador2 == "papel") or (jugador1 == "papel" and jugador2 == "piedra"):
    print("Gana jugador 1")
else:
    print("Gana jugador 2")