# -*- coding: utf-8 -*-
# ==============================
 # Descripcion:          Framework de lectura de archivo csv
# Autor:                 Jaime Soriano
# Argumentos de entrada: tipo de procesamiento (A/M), tipo delimitador
#                        ejemplo: C:\Users\jaime.soriano\Documents\PythonCodes\ProyectoGlobant\SH\star.ps1 a "," C:\Users\jaime.soriano\Documents\PythonCodes\ProyectoGlobant\FILES datos.csv si
# cambia politica de ejecucion en power shell: Set-ExecutionPolicy Unrestricted -Scope Process
# ==============================

## Imports
import sys

## Variables globales

if len(sys.argv) == 6:                                                                    # Verificar numero de parametros enviados 
    process_type = sys.argv[1].upper()
    delimiter = sys.argv[2]
    path_file = sys.argv[3]
    name_file = sys.argv[4]
    headboard = sys.argv[5].upper()
    path_name_file = path_file + "\\" + name_file
elif len(sys.argv) < 6:  
    print("No se proporcionaron todos los parámetros")
    exit()
else: 
    print("Se proporcionaron más parámetros de lo esperado")
    exit()

## Funciones Auxiliares

## Cuerpo del program
def main():
    instruction_for_use()
    get_parameters()
    read_csv()
    despedida()


def despedida():
    s='''
    (" ")
    ("-----------------------------")
    ("Fin del proceso de carga CSV!")
    (" ")
    '''
    print(s)# sacar comillas y parentecis
    

def get_parameters():
    print("------------------------------")
    print("|Los parámetros obtenidos son:| ")
    print("------------------------------")
    print("Proceso se ejecutará de manera automatica [A] / Manual [M]   :", process_type )
    print("Tipo de delimitador es                                       :", delimiter)
    print("Path archo                                                   :", path_file)
    print("Nombre archivo                                               :", name_file)
    print("Cabecera                                                     :", headboard)

def instruction_for_use():
    print("Intrucciones")


def read_csv():
    num_columnas = 0
    print("")
    with open(path_name_file, 'r') as archivo:
        primera_linea = archivo.readline().strip()  # Leer la primera línea del archivo CSV
        num_columnas = primera_linea.count(delimiter) + 1

        if headboard == "NO":
            nombres_columnas = [f"col{i+1}" for i in range(num_columnas)]
            print(nombres_columnas)

        archivo.seek(0)                                                         # Reiniciar el puntero de lectura del archivo al inicio
        for linea in archivo:                                                   # Iterar sobre cada línea del archivo CSV
            linea = linea.strip()                                               # Eliminar el carácter de nueva línea al final de la línea
            campos = linea.split(delimiter)                                     # Dividir la línea en campos utilizando una coma como delimitador
            print(campos)                                                       # Imprimir los campos de cada línea

    print("")


## Llamada a funcion Main
if __name__ == "__main__":
    main()

