# -*- coding: utf-8 -*-
# ==============================
 # Descripcion:          Framework de lectura de archivo csv
# Autor:                 Jaime Soriano
# Argumentos de entrada: tipo de procesamiento (A/M), tipo delimitador
#                        ejemplo:C:\Users\jaime.soriano\Documents\PythonCodes\ProyectoGlobant\SH\star.ps1 a "," C:\Users\jaime.soriano\Documents\PythonCodes\ProyectoGlobant\FILES\datos.csv si
# Cambia politica de ejecucion en power shell: Set-ExecutionPolicy Unrestricted -Scope Process
# ==============================

## Imports
import sys 
from datetime import datetime 
import os 
import generate_log_csv_ingestor
import help_csv_ingestor
import logging_csv_ingestor

## Variables globales
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log_filename = f'log_{now.replace(":", "-").replace(" ", "_")}.log'

## =================================================== ##
## Funciones Auxiliares
def show_parameters(delimiter, path_name_file, headboard):                         # mensaje multilinial con f que indica que se trata de un formato de cadena de f-strings 
    msg_sp=f'''
    -------------------------------------
    |Los parámetros obtenidos son:      |
    -------------------------------------                            
    Tipo de delimitador:        {delimiter}
    Path y nombre de archivo:   {path_name_file}
    Cabecera:                   {headboard}

    '''
    print(msg_sp)

def read_csv(path_name_file, delimiter, headboard):
    num_columnas = 0
    print("")
    msg_rcsv='''
    -------------------------------------
    |Se realiza proceso de carga CSV!   |
    -------------------------------------
    '''
    print(msg_rcsv)
    with open(path_name_file, 'r') as archivo:
        primera_linea = archivo.readline().strip()                                  # Leer la primera línea del archivo CSV
        num_columnas = primera_linea.count(delimiter) + 1

        if headboard == "NO":
            lst_column_name = [f"col{i+1}" for i in range(num_columnas)]
            print("   ",lst_column_name)

        archivo.seek(0)                                                              # Reiniciar el puntero de lectura del archivo al inicio
        line_count=0                                                                 # 
        for linea in archivo:                                                        # Iterar sobre cada línea del archivo CSV
            if line_count <=4:
                linea = linea.strip()                                                # Eliminar el carácter de nueva línea al final de la línea
                campos = linea.split(delimiter)                                      # Dividir la línea en campos utilizando una coma como delimitador
                print("   ",campos)                                                  # Imprimir los campos de cada línea
            line_count +=1
    print("")

def welcome():
    msg_wpcc='''
-----------------------------------------------------------------------------------------------------------------
|                                       Bienvenido al proceso de carga CSV!                                     |
-----------------------------------------------------------------------------------------------------------------
    '''
    print(msg_wpcc)
    generate_log_csv_ingestor.create_log("Inicio sesión ", log_filename)

def farewell():
    msg_fpcc='''
    -------------------------------
    |Fin del proceso de carga CSV!|
    -------------------------------
    '''
    print(msg_fpcc)
    generate_log_csv_ingestor.create_log("Fin sesión ", log_filename)

def get_parameters():
        delimiter = sys.argv[1]
        path_name_file = sys.argv[2]
        headboard = sys.argv[3].upper()
        return delimiter, path_name_file, headboard

def interactive_mode():
    msg_im='''
    ------------------------------------------
    |Se inicia Modo interactivo de carga CSV |
    ------------------------------------------
    '''
    while True:
        print(msg_im)
        delimiter = input("Tipo de delimitador: ")
        path_name_file = input("Path y nombre de archivo: ")
        headboard = input("Cabecera (SI/NO): ").upper()
        show_parameters(delimiter, path_name_file, headboard)
        flag_im = ""
        while flag_im not in ["S", "N"]:
            flag_im = input("Los parámetros de entrada están correctos? [S|N]?:").upper()

        if flag_im == "S":
            with open(path_name_file, 'r') as archivo:
                read_csv(path_name_file, delimiter, headboard)
            break                                                                       # sale del bucle while si parámetro es s
    generate_log_csv_ingestor.create_log(f"Carga por modo interactivo con los parametros Delimitador {delimiter}  Ruta/Archivo {path_name_file} Cabecera {headboard}", log_filename)
    return delimiter, path_name_file, headboard

    
def main():
    welcome()
    if '--help' in sys.argv or '-h' in sys.argv:
        help_csv_ingestor.main()
        return                                                                                    # Verificar el modo de ejecución
    if len(sys.argv) == 4:                                                              # Modo por parámetros
        get_parameters()
        delimiter, path_name_file, headboard = get_parameters()
        show_parameters( delimiter, path_name_file, headboard)
        read_csv(path_name_file, delimiter, headboard)
        generate_log_csv_ingestor.create_log(f"Carga por parametros Delimitador {delimiter}  Ruta/Archivo {path_name_file} Cabecera {headboard}", log_filename)
    else:                                                                               # Modo interactivo
        delimiter, path_name_file, headboard = interactive_mode()
        show_parameters( delimiter, path_name_file, headboard)
        read_csv(path_name_file, delimiter, headboard)
    farewell()

if __name__ == "__main__":
    main()