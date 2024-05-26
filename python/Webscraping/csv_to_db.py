import pandas as pd
import sqlite3


def csv_to_db(nombrecsv, tienda):
    # Conectar a la base de datos SQLite (se crea si no existe)
    conexion = sqlite3.connect("scraper.db")

    # Modelos de tarjetas gráficas NVIDIA de la serie 1000 a la serie 4000
    nvidia_models = [
        # Serie 4000
        "RTX 4090",
        "RTX 4080",
        "RTX 4070 Ti",
        "RTX 4070Ti",
        "RTX 4070",
        "RTX 4060 Ti",
        "RTX 4060Ti",
        "RTX 4060",
        "RTX 4050",
        # Serie 3000
        "RTX 3090 Ti",
        "RTX 3090Ti",
        "RTX 3090",
        "RTX 3080 Ti",
        "RTX 3080Ti",
        "RTX 3080",
        "RTX 3070 Ti",
        "RTX 3070Ti",
        "RTX 3070",
        "RTX 3060 Ti",
        "RTX 3060Ti",
        "RTX 3060",
        "RTX 3050",
        # Serie 2000
        "RTX 2090 Ti",
        "RTX 2090Ti",
        "RTX 2080 Ti",
        "RTX 2080Ti",
        "RTX 2080 Super",
        "RTX 2080Super",
        "RTX 2070 Super",
        "RTX 2070Super",
        "RTX 2060Super",
        "RTX 2060 Super",
        "RTX 2070",
        "RTX 2060",
        "RTX 2060 Max-Q",
        "RTX 2060Max-Q",
        "RTX 2050",
        # Serie 1600
        "GTX 1660 Ti",
        "GTX 1660Ti",
        "GTX 1060 Super",
        "GTX 1060Super",
        "GTX 1650 Super",
        "GTX 1650Super",
        "GTX 1650",
        # Serie 1000
        "GTX 1080 Ti",
        "GTX 1080Ti",
        "GTX 1070 Ti",
        "GTX 1070Ti",
        "GTX 1080",
        "GTX 1070",
        "GTX 1060",
        "GTX 1060 6GB",
        "GTX 10606GB",
        "GTX 1060 3GB",
        "GTX 10603GB",
        "GTX 1050 Ti",
        "GTX 1050Ti",
        "GTX 1050",
        "GTX 1030",
    ]

    # Modelos de tarjetas gráficas AMD de la serie RX 500 a la
    # serie RX 7000 (excluyendo versiones móviles)
    amd_models = [
        # RX 7000
        "RX 7900 XTX",
        "RX 7900XTX",
        "RX 7900",
        "RX 7800 XT",
        "RX 7800XT",
        "RX 7800",
        "RX 7700 XT",
        "RX 7700XT",
        "RX 7700",
        "RX 7600 XT",
        "RX 7600XT",
        "RX 7600",
        "RX 7500 XT",
        "RX 7500XT",
        "RX 7400",
        # RX 6000
        "RX 6950 XT",
        "RX 6900 XT",
        "RX 6900XT",
        "RX 6900",
        "RX 6800 XT",
        "RX 6800XT",
        "RX 6800",
        "RX 6700 XT",
        "RX 6700XT",
        "RX 6750 XT",
        "RX 6750XT",
        "RX 6700",
        "RX 6650 XT",
        "RX 6600 XT",
        "RX 6600XT",
        "RX 6600",
        "RX 6500 XT",
        "RX 6500XT",
        "RX 6400",
        # RX 5000
        "RX 5700 XT",
        "RX 5700XT",
        "RX 5700",
        "RX 5600 XT",
        "RX 5600XT",
        "RX 5600",
        "RX 5500 XT",
        "RX 5500XT",
        "RX 5500",
        "RX 5300 XT",
        "RX 5300XT",
        "RX 5300",
        # Rx 500
        "RX 590",
        "RX 580",
        "RX 570",
        "RX 560",
        "RX 550",
    ]

    # Leer el archivo CSV
    data = pd.read_csv(nombrecsv, delimiter=";")

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Crear la tabla si no existe
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS graficas (
                        nombre TEXT PRIMARY KEY,
                        precio REAL,
                        modelo TEXT,
                        tienda TEXT,
                        categoria TEXT)"""
    )

    # Insertar/update la información en la base de datos
    for index, row in data.iterrows():
        for n_model in nvidia_models:
            if n_model in row["Product"]:
                nombre = row["Product"]
                precio = row["Price"]

                cursor.execute(
                    "SELECT COUNT(*) FROM graficas WHERE nombre = ?", (nombre,)
                )
                if cursor.fetchone()[0]:
                    cursor.execute(
                        "UPDATE graficas SET precio = ? WHERE nombre = ?",
                        (precio, nombre),
                    )
                    break
                else:
                    cursor.execute(
                        "INSERT INTO graficas (nombre, precio, modelo, tienda, categoria) VALUES (?, ?, ?, ?, ?)",
                        (nombre, precio, n_model, tienda, "Nvidia"),
                    )
                    break

        for a_model in amd_models:
            if a_model in row["Product"]:
                nombre = row["Product"]
                precio = row["Price"]
                cursor.execute(
                    "SELECT COUNT(*) FROM graficas WHERE nombre = ?", (nombre,)
                )
                if cursor.fetchone()[0]:
                    cursor.execute(
                        "UPDATE graficas SET precio = ? WHERE nombre = ?",
                        (precio, nombre),
                    )
                else:
                    cursor.execute(
                        "INSERT INTO graficas (nombre, precio, modelo, tienda, categoria) VALUES (?, ?, ?, ?, ?)",
                        (nombre, precio, a_model, tienda, "AMD"),
                    )
                break

    # Confirmar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión y el cursor
    cursor.close()
    conexion.close()

# Llamadas a la función
csv_to_db("pccomponentes.csv", "pccomponentes")
csv_to_db("coolmod.csv", "coolmod")
csv_to_db("neobyte.csv", "neobyte")
