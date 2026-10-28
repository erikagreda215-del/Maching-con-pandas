from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

CARPETA = Path(__file__).parent / "datos"
ENTRADA = CARPETA / "entrada"
SALIDA = CARPETA / "salida"

NOTAS = ["nota1", "nota2", "nota3"]
COLUMNAS_INFORME = ["id_alumno", "nombre"] + NOTAS + ["total", "media"]


def leer_csv(nombre: str, columnas: list[str]) -> pd.DataFrame:
    """Lee un archivo CSV y verifica su existencia, contenido y columnas."""
    ruta = ENTRADA / nombre

    if not ruta.exists():
        raise ValueError(f"Revisa {nombre}: el archivo no existe.")

    try:
        tabla = pd.read_csv(ruta, sep=";", dtype=str, encoding="utf-8")
    except pd.errors.EmptyDataError:
        raise ValueError(f"Revisa {nombre}: el archivo está vacío.")

    if tabla.empty:
        raise ValueError(f"Revisa {nombre}: el archivo está vacío.")

    if list(tabla.columns) != columnas:
        raise ValueError(f"Revisa {nombre}: columnas esperadas {columnas}")

    return tabla

def preparar_datos() -> pd.DataFrame:
    """Lee, limpia, cruza y calcula. Devuelve el informe."""
    alumnos = leer_csv("alumnos.csv", ["id_alumno", "nombre"])
    notas = leer_csv("notas.csv", ["id_alumno"] + NOTAS)

    # Limpiar
    filas_antes = len(alumnos)
    alumnos = alumnos.drop_duplicates(subset="id_alumno")
    print("Duplicados eliminados:", filas_antes - len(alumnos))

    if notas["id_alumno"].duplicated().any():
        raise ValueError("Revisa notas.csv: hay alumnos duplicados.")

    for columna in NOTAS:
        notas[columna] = pd.to_numeric(notas[columna], errors="coerce")
        fuera_rango = (notas[columna] < 0) | (notas[columna] > 10)
        notas.loc[fuera_rango, columna] = None

    sin_notas = sorted(set(alumnos["id_alumno"]) - set(notas["id_alumno"]))
    print("Alumnos sin notas:", ", ".join(sin_notas) or "ninguno")
    sin_alumno = sorted(set(notas["id_alumno"]) - set(alumnos["id_alumno"]))
    print("Notas sin alumno:", ", ".join(sin_alumno) or "ninguno")