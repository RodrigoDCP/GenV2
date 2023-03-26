import itertools
import random
from datetime import datetime, timedelta
import sys
import os
from colorama import init
from termcolor import colored
import time

# Inicializar colorama
init()

# Cambiar el color del texto de nuevo y esperar un segundo
print(colored('Cargando....', 'yellow'))
time.sleep(1)
os.system('clear')
print(colored("""
  ____                 ____  
 / ___| ___ _ ____   _|___ \ 
| |  _ / _ \ '_ \ \ / / __) |
| |_| |  __/ | | \ V / / __/ 
 \____|\___|_| |_|\_/ |_____|
 			by Cañas
 				version - 1.2
""", "green"))
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
    print(colored("------------------------------------------", 'magenta'))
    print(colored("Cargando....", 'yellow'))
    time.sleep(2)
    print(colored("Las combinaciones se han guardado en combinations.txt", 'yellow'))
    time.sleep(3)
    os.system('clear')


def generate_passwords():
    words = []
    while True:
        word = input("Introduce las palabras, al finalizar escribe 'done': ")
        if word == 'done':
            break
        words.append(word)
        print(colored("------------------------------------------", 'cyan'))
	
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

def menu():
    while True:
        print(colored('''------------------------------------------''', 'blue'))
        print(colored("[1]", 'yellow'), "Generar contraseñas")
        print(colored("[2]", 'yellow'), "Generar identidades")
        print(colored("[3]", 'yellow'), "Limpiar consola")
        print(colored("[4]", 'yellow'), "salir")
        print(colored("------------------------------------------", 'blue'))
        opcion = input("Selecciona una opción: ")
        os.system('clear')

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
            print(colored("Opción no válida....", 'red'))
            time.sleep(1)
            os.system('clear')


if __name__ == '__main__':
    menu()
