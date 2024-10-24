from enum import Enum

# Enum para definir caracteres de origen admisibles
class OrigenPasaporte(Enum):
    V = "V"
    E = "E"

# Minimo y maximo de cantidad de caracteres para nombres y apellidos
MIN_LEN_NOMBRE_APELLIDO = 10
MAX_LEN_NOMBRE_APELLIDO = 40

# Minimo y maximo para numero de pasaporte segun la longitud de una secuencia binaria
MAXB_NUM_PASAPORTE = 34
MINB_NUM_PASAPORTE = 31

