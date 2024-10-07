"""

Crea un programa que convierta entre diferentes unidades de medida, estas son: metros
a pies, Kilogramos a libras, cm3 a onzas y Celsius a Fahrenheit. El programa debe permitir
al usuario seleccionar la conversión deseada e introducir el valor a convertir. 
Finalmente proporcionar el valor convertido y guardar el historial de conversiones en un archivo de texto. 
(4.5pts)


"""
from datetime import datetime
import json 

def calcular_conversiones(eleccion):
    resultado = 0
    try:
        cantidad = float(input("Ingresa cantidad a convertir: "))
        if eleccion == 1:
            resultado = cantidad * 3.28084
        elif eleccion == 2:
            resultado = cantidad * 2.20462
        elif eleccion == 3:
            resultado = cantidad * 0.033814
        else :
            resultado = ((cantidad * 9 )/5) + 32
    except ValueError:
        print("Debes Ingresar solo numeros...")    
        
    
        
    return resultado,cantidad

def agregar_conversiones_historial(historial,resultado,cantidad,opciones,eleccion):
    fecha_actual = datetime.now().date()
    conversion = {
        "Conversion": opciones[eleccion-1],
        "Cantidad": cantidad ,
        "Resultado": resultado,
        "Fecha" : fecha_actual.strftime("%Y-%m-%d")
    }
    historial.append(conversion)
    return historial

def guardar_historial(archivo,historial):
    json_historial = json.dumps(historial)
    
    try:
        with open(archivo,"w") as file:
            file.write(json_historial)
        print(f"El historial a sido guardado en {archivo}.")
    except IOError:
        print(f"Error al guardar historial en {archivo}.")

def cargar_historial(archivo):
    historial = []
    try:
        with open(archivo,"r") as file:
            json_historial = file.read()
            historial = json.loads(json_historial)
            print(f"El inventario a sido cargado desde {archivo}")
    except IOError:
        print(f"Error al intentar cargar el archivo desde {archivo}")
        
    return historial
        

def principal():
    archivo = "historial_conversiones.txt"
    historial = cargar_historial(archivo)
    condicion = True
    while condicion:

        opciones = ("metros -> pies","Kilogramos -> libras","cm3 -> onzas","Celsius -> Fahrenheit")
        print("Bienvenido a mi conversor")
        print("1.Hacer Conversiones\n2.Salir")
        resultado = 0
        eleccion = int(input("Ingresa tu eleccion: "))
        
        if eleccion == 1:
            print("1.metros -> pies\n2.Kilogramos -> libras\n3.cm3 -> onzas\n4.Celsius -> Fahrenheit\n")
            eleccion_conversion = int(input("Ingresa tu eleccion: "))
        
            if eleccion_conversion not in range(1,5):
                print("Eleccion invalida, intenta de nuevo.")
                continue
            
            resultado,cantidad = calcular_conversiones(eleccion_conversion)
            print(f"{opciones[eleccion_conversion-1]} = {resultado}")
            historial = agregar_conversiones_historial(historial,resultado,cantidad,opciones,eleccion_conversion)
            
        elif eleccion == 2:
            guardar_historial(archivo, historial)
            print("Saliendo del Programa...")
            condicion = False
        else:
            print("Eleccion invalida, intenta de nuevo.")
            
principal()