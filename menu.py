import itertools
import random
from datetime import datetime, timedelta
import sys
import os
print("""
  ____                 ____  
 / ___| ___ _ ____   _|___ \ 
| |  _ / _ \ '_ \ \ / / __) |
| |_| |  __/ | | \ V / / __/ 
 \____|\___|_| |_|\_/ |_____|
 			by The Coños
""")
def generate_combinations(words, n):
    # Generate all possible combinations
    combinations = list(itertools.permutations(words, n))
    # Shuffle the combinations list
    random.shuffle(combinations)
    return combinations


def generate_combinations_and_save(words, n):
    combinations = generate_combinations(words, n)
    with open('combinations.txt', 'w') as f:
        for combination in combinations:
            f.write("".join(combination) + "\n")
    print("Las combinaciones se han guardado en combinations.txt")


def generate_passwords():
    words = []
    while True:
        word = input("Introduce las palabras, al finalizar escribe 'done': ")
        if word == 'done':
            break
        words.append(word)

    n = int(input("Introduce la cantidad de columnas: "))

    generate_combinations_and_save(words, n)

from datetime import datetime, timedelta

def generate_identities():
    # Leer nombres y apellidos de archivos de texto
    with open("nombres.txt", "r") as f:
        nombres = f.read().splitlines()
    with open("apellidos.txt", "r") as f:
        apellidos = f.read().splitlines()

    # Generar 10 nombres aleatorios con edades y fechas de nacimiento
    for i in range(10):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        edad = random.randint(18, 60) # Generar edad aleatoria entre 18 y 60 años
        fecha_nacimiento = datetime.now() - timedelta(days=365*edad) # Calcular fecha de nacimiento
        print(nombre + " " + apellido)
        print("Edad:", edad)
        print("Fecha de nacimiento:", fecha_nacimiento.strftime("%d/%m/%Y"))
        print("")

"""
def generate_identities():
    # Leer nombres y apellidos de archivos de texto
    with open("nombres.txt", "r") as f:
        nombres = f.read().splitlines()
    with open("apellidos.txt", "r") as f:
        apellidos = f.read().splitlines()

    # Generar 10 nombres aleatorios
    for i in range(10):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        print(nombre + " " + apellido)
        print("")
"""

def menu():
    while True:
        print("[1] Generar contraseñas")
        print("[2] Generar identidades")
        print("[3] Limpiar consola")
        print("[4] salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            generate_passwords()
            menu()
        elif opcion == "2":
            generate_identities()
            menu()
        elif opcion == "3":
            os.system('clear')
        elif opcion == "4":
            sys.exit()
        
        else:
            print("Opción no válida")


if __name__ == '__main__':
    menu()
