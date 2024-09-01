import sqlite3
import os
from pathlib import Path
from .modelos.cliente import Cliente


class SistemaVentasDB:
    def __init__(self) -> None:
        self.__conexion = sqlite3.connect(self.__obtener_path_db())
        self.__setup()

    def registro_cliente(self, cl: Cliente):
        cursor = self.__conexion.cursor()
        cursor.execute(SistemaVentasDBQueries.nuevo_cliente_creacion, (
            cl.nombres_apellidos,
            cl.numero_pasaporte,
            cl.fecha_expedicion_pasaporte,
            cl.fecha_certificado_vacuna,
            cl.fecha_declaracion_impuesto,
            cl.origen_pasaporte
        ))
        self.__conexion.commit()
        cursor.close()

    def modificacion_cliente(self, num_pasaporte: int, datos: dict):
        keys = ("nombres_apellidos", "fecha_expedicion_pasaporte", "fecha_certificado_vacuna", "fecha_declaracion_impuestos", "origen_pasaporte")
        datos_en_diccionario = list(filter(lambda x: x in keys, datos.keys()))
        valores_query = (datos_en_diccionario[key] for key in keys)
        if datos_en_diccionario:
            cursor = self.__conexion.cursor()
            cursor.execute(SistemaVentasDBQueries.cliente_actualizacion, (*valores_query, num_pasaporte,))
            self.__conexion.commit()
            cursor.close()
    
    def obtener_cliente_por_num_pasaporte(self, num_pasaporte: int):
        cursor = self.__conexion.cursor()
        cursor.execute(SistemaVentasDBQueries.cliente_obtener_por_num_pasaporte, (num_pasaporte,))
        data = cursor.fetchone()
        self.__conexion.commit()
        cursor.close()
        return Cliente.crear_nuevo_cliente(*data[1:]) if data else None
    
    def obtener_clientes_por_origen_pasaporte(self, origen: str):
        cursor = self.__conexion.cursor()
        cursor.execute(SistemaVentasDBQueries.clientes_obtener_por_origen, (origen,))
        data = cursor.fetchall()
        self.__conexion.commit()
        cursor.close()
        clientes = [Cliente.crear_nuevo_cliente(*cl[1:]) for cl in data]
        return clientes
    
    def obtener_clientes(self):
        cursor = self.__conexion.cursor()
        cursor.execute("SELECT * from clientes")
        data = cursor.fetchall()
        self.__conexion.commit()
        cursor.close()
        clientes = [Cliente.crear_nuevo_cliente(*cl[1:]) for cl in data]
        return clientes
    
    def eliminar_cliente(self, num_pasaporte):
        cursor = self.__conexion.cursor()
        cursor.execute("DELETE FROM clientes WHERE numero_pasaporte = ?", (num_pasaporte,))
        self.__conexion.commit()
        cursor.close()
    
    def __setup(self):
        cursor = self.__conexion.cursor()
        cursor.execute(SistemaVentasDBQueries.tabla_clientes_creacion)
        cursor.execute(SistemaVentasDBQueries.tabla_ventas_creacion)
        self.__conexion.commit()
        cursor.close()

    def __obtener_path_db(self) -> str:
        DB_ARCHIVO = "sistemaventasdb.db"
        DB_DIR = "sistema-ventas"
        home = Path.home()
        if DB_DIR not in os.listdir(home):
            db_dir_creacion = Path(home, DB_DIR)
            os.mkdir(db_dir_creacion)
        return Path(home, DB_DIR, DB_ARCHIVO)


class SistemaVentasDBQueries:
    tabla_clientes_creacion = """
CREATE TABLE IF NOT EXISTS clientes (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
nombres_apellidos TEXT NOT NULL, 
numero_pasaporte INT(10) NOT NULL, 
fecha_expedicion_pasaporte TEXT NOT NULL, 
fecha_certificado_vacuna TEXT NOT NULL, 
fecha_declaracion_impuestos TEXT NOT NULL, 
origen_pasaporte CHAR(1) NOT NULL)
"""

    tabla_ventas_creacion = """
CREATE TABLE IF NOT EXISTS ventas (
id INTEGER PRIMARY KEY AUTOINCREMENT,
cliente_id INTEGER,
CONSTRAINT fk_clientes
    FOREIGN KEY (cliente_id)
    REFERENCES clientes(id)
)
"""

    nuevo_cliente_creacion = """
INSERT INTO clientes (
nombres_apellidos, 
numero_pasaporte, 
fecha_expedicion_pasaporte, 
fecha_certificado_vacuna, 
fecha_declaracion_impuestos, 
origen_pasaporte)
VALUES (?,?,?,?,?,?)
"""

    cliente_actualizacion = """
UPDATE clientes SET 
    nombres_apellidos = ?,
    fecha_expedicion_pasaporte = ?,
    fecha_certificado_vacuna = ?,
    fecha_declaracion_impuestos = ?,
    origen_pasaporte = ?
WHERE numero_pasaporte = ?
"""

    cliente_obtener_por_num_pasaporte = """
SELECT * FROM clientes WHERE numero_pasaporte = ?
"""

    clientes_obtener_por_origen = """
SELECT * FROM clientes WHERE origen_pasaporte = ?
"""