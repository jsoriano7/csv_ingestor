import sys 
from datetime import datetime 
import os


log_directory = r'C:\Users\jaime.soriano\Documents\PythonCodes\ProyectoGlobant\LOGS'    # Especificar la ruta del directorio donde quieres guardar el archivo de log

def create_log(executed_in, log_filename):
    if sys.platform == "win32":
        user_name = os.getenv('USERNAME')
    else:
        user_name = os.getenv('USER')

    script_path = sys.argv[0]
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')                                  # Obtener la fecha y hora actual
    log_entry = f"{now} - Usuario: {user_name} - Ejecuta programa: {script_path} Actividad realizada: {executed_in} \n" # Crear el mensaje de log


    # Definir la ruta completa del archivo de log
    #log_filename = f'log_{now.replace(":", "-").replace(" ", "_")}.log'
    log_filepath = os.path.join(log_directory, log_filename)

    # Escribir el mensaje en el archivo de log
    with open(log_filepath, 'a') as log_file:
        log_file.write(log_entry)

# Verificar si el directorio de log existe, si no, crearlo
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
 
