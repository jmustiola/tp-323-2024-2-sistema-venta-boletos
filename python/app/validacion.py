import re
from datetime import datetime as dt
from .constantes import *


def es_fecha_pasada(fecha_string: str) -> bool:
    dt_format = "%m/%d/%Y"
    fecha = dt.strptime(fecha_string, dt_format)
    today = dt.today()
    return fecha < today

def es_fecha_valida(fecha_string: str) -> bool:
    PATTERN = r"(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01])\/(1|2)\d{3}$"
    return isinstance(fecha_string, str) and re.match(PATTERN, fecha_string)


def es_num_pasaporte_valido(num_pasaporte: str | int) -> bool:
    if isinstance(num_pasaporte, str) and not num_pasaporte.isdecimal():
        return False
    return MINB_NUM_PASAPORTE <= int(num_pasaporte).bit_length() <= MAXB_NUM_PASAPORTE


def es_origen_valido(origen_char: str) -> bool:
    return origen_char in (OrigenPasaporte)


def es_nombre_apellido_valido(na_string: str) -> bool:
    return (
        isinstance(na_string, str)
        and MIN_LEN_NOMBRE_APELLIDO <= len(na_string) <= MAX_LEN_NOMBRE_APELLIDO
    )
