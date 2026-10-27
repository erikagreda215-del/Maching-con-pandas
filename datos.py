from pathlib import Path  

import pandas as pd 

CARPETA = Path(__file__).parent / "datos" 
ENTRADA = CARPETA / "entrada"
SALIDA = CARPETA / "salida" 

NOTAS = ["nota1", "nota2", "nota3",]

def leer_csv(nombre: str, columnas: list[str]) -> pd.DataFrame:
    """Lee un archivo CSV y verifica su existencia, contenido y columnas."""
    ruta = ENTRADA / nombre

    if not ruta.exists():
        raise ValueError(f"El archivo {ruta} no existe.")

    tabla = pd.read_csv(ruta, sep=";", dtype=str, encoding="utf-8")
    if tabla.empty:
        raise ValueError(f"El archivo {ruta} esta vacio.")

    if list(tabla.columns) != columnas:
        raise ValueError(f"El archivo {ruta} no tiene las columnas esperadas: {columnas}")
          

    return tabla

def preparar_datos():
    alumnos = leer_csv("alumnos.csv" , ["id_alumno" , "nombre"])
    notas = leer_csv("notas.csv" , ["id_alumno"] + NOTAS)

    alumnos = alumnos 