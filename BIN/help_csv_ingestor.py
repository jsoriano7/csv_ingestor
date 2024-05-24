import argparse

def show_help():
    msg1 = '''    
    :::::::::::::::::::::::::::::::::::::::
    :Bienvenido a la ayuda de CSV Ingestor:
    :::::::::::::::::::::::::::::::::::::::
    '''
    print(msg1)

def main():
    show_help()
    
    parser = argparse.ArgumentParser(description='Este programa es un framework diseñado para facilitar la carga y procesamiento de archivos CSV.')
    parser.add_argument('-q', '--quit', action='store_true', help='Salir del programa ingesta')
    parser.add_argument('-o', '--otro', action='store_true', help='Mostrar otro mensaje')
    parser.add_argument('-p', '--parametros', action='store_true', help='Mostrar parámetros adicionales')

    parser.add_argument('path_name_file', type=str, help='Ruta y nombre del archivo CSV.')
    parser.add_argument('delimiter', type=str, help='Delimitador usado en el archivo CSV.')
    parser.add_argument('headboard', type=str, choices=['SI', 'NO'], help='Indicar si el archivo CSV tiene cabecera (SI/NO).')
    
    args = parser.parse_args()

    if args.quit:
        print('Salir del programa ingesta')

    if args.otro:
        print('Mostrar otro mensaje')

    if args.parametros:
        print('Mostrar parámetros adicionales')
    
if __name__ == "__main__":
    main()
