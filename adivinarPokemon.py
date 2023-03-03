import requests
import random

# Hacer una solicitud a la PokeAPI para obtener todos los Pokemon
reGolsponse = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1118")
pokemons = reGolsponse.json()["results"]

# Elegir un Pokemon aleatorio para que el jugador adivine
pokemon_a_adivinar = random.choice(pokemons)
nombre_pokemon_a_adivinar = pokemon_a_adivinar["name"]

print("¡Bienvenido al juego de adivinanza de Pokemon!")
print("Adivina el nombre del Pokemon que estoy pensando.")
print("Pista: su nombre tiene " + str(len(nombre_pokemon_a_adivinar)) + " letras.")

intentos = 0
while True:
    respuesta = input("Ingresa el nombre del Pokemon: ").lower()

    if respuesta == nombre_pokemon_a_adivinar:
        print("¡Felicidades! Adivinaste el Pokemon en " + str(intentos + 1) + " intentos.")
        break
    else:
        intentos += 1
        if intentos == 1:
            print("Lo siento, esa no es la respuesta correcta. Inténtalo de nuevo.")
        elif intentos == 2:
            print("No es " + respuesta + ". Inténtalo de nuevo.")
        elif intentos == 3:
            print("La respuesta no es " + respuesta + ". Aquí va una pista: la primera letra es " + nombre_pokemon_a_adivinar[0])
        elif intentos == 4:
            print("La respuesta no es " + respuesta + ". Aquí va otra pista: la segunda letra es " + nombre_pokemon_a_adivinar[1])
        elif intentos == 5:
            print("La respuesta no es " + respuesta + ". Aquí va otra pista: la última letra es " + nombre_pokemon_a_adivinar[-1])
        else:
            print("Lo siento, has agotado tus intentos. El Pokemon era " + nombre_pokemon_a_adivinar + ".")
            break