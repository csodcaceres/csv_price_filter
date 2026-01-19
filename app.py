import csv
from pathlib import Path

def leer_csv(ruta_archivo: str) -> list[dict]:
    """Lee un archivo CSV y devuelve una lista de diccionarios.

    Args:
        ruta_archivo (str): La ruta al archivo CSV.

    Returns:
        list[dict]: Una lista de diccionarios representando las filas del CSV.
    """
    datos = []
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for file in lector:
            datos.append(file)
        return datos
    
def filtrar_por_precio(datos: list[dict], precio_min: float) -> list[dict]:
    """Filtra los datos por un precio mínimo.
    Args:
        datos (list[dict]): La lista de diccionarios a filtrar.
        precio_mini (float): El precio mínimo para filtrar.

    Returns:
        list[dict]: La lista filtrada de diccionarios.
    """
    resultado = []
    for item in datos:
        if float(item.get('precio', 0)) >= precio_min:
            resultado.append(item)
    return resultado
    
def guardar_resultado(datos: list[dict], salida: str):
    """Guarda los datos en un archivo CSV.

    Args:
        datos (list[dict]): La lista de diccionarios a guardar.
        salida (str): La ruta del archivo de salida.
    """
    if not datos:
        print("No hay datos para guardar.")
        return
        
    claves = datos[0].keys()

    with open(salida, mode='w', encoding='utf-8') as f:
        escribir = csv.DictWriter(f, fieldnames=claves)
        escribir.writeheader()
        escribir.writerows(datos)

if __name__ == "__main__":
    ruta_entrada = 'productos.csv'
    ruta_salida = 'productos_filtrados.csv'

    datos_leidos = leer_csv(ruta_entrada)
    datos_filtrados = filtrar_por_precio(datos_leidos, 1000)
    guardar_resultado(datos_filtrados, ruta_salida)

    print("Proceso completado. Datos filtrados guardados en", ruta_salida)

