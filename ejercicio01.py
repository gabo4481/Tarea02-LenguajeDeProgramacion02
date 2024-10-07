"""

Escribe un programa que implemente el clásico juego del ahorcado. El programa debe
seleccionar una palabra aleatoria de una lista predefinida de palabras guardadas en un
archivo de texto llamado palabras.txt, y permitir al usuario adivinar letras hasta
completar la palabra o agotar sus intentos.

"""
import random

def buscarPalabra():
    with open("palabras.txt","r") as file:
        palabras = file.readlines()
        numero_random = random.randint(0,len(palabras))
        palabra_random = palabras[numero_random].strip().lower()
        return palabra_random
    
def encontrar_letra():
    palabra_ganadora = buscarPalabra()
    numero_caracteres = len(palabra_ganadora)
    
    letras_ocultas = ["_"] * numero_caracteres
    intentos = 11
    
    letras_adivinadas = set()
    
    while intentos > 0 and "_" in letras_ocultas:
        print(f"Palabra: {' '.join(letras_ocultas)}, intentos: {intentos}")
        letra = input("Ingresa tu letra: ")
        letra.lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Ingresa una sola letra valida.")
            continue
        
        if letra in letras_adivinadas:
            print("Esta letra ya fue adivinada, intenta de nuevo.")
            continue
            
        letras_adivinadas.add(letra)
        
        if letra in palabra_ganadora:
            print(f"Felicidades la letra {letra} esta en la palabra.")
            for i,letra_palabra in enumerate(palabra_ganadora):
                if letra == letra_palabra:
                    letras_ocultas[i] = letra
        else:
            print(f"la letra {letra} no se encuentra en la palabra.")
        intentos -= 1
    if "_" not in letras_ocultas:
        print(f"Felicidades Ganaste el juego, la palabra era: {palabra_ganadora}")
    else:
        print(f"Perdiste el juego, la palabra era: {palabra_ganadora}")
        


condicion = True
while condicion:
    print("\nBienvenido a mi juego del ahorcado")
    print("\n1. Juegar Nuevo Juego\n2. Salir ")
    seleccion = int(input("Ingresa tu opcion: "))
    if seleccion == 1:  
        encontrar_letra()
    elif seleccion == 2:
        print("Saliendo del Programa")
        condicion = False
    else:
        print("Opcion invalida, vuelve a intentar.")
    
    
    
    
    



