from .funciones import entrada_receptor
from .validacion import (
    es_nombre_apellido_valido,
    es_num_pasaporte_valido,
    es_fecha_valida,
    es_fecha_pasada,
    es_origen_valido,
)
from .modelos.cliente import Cliente

# --------------------------------------------------
# PREPARAR FUNCION PARA RECIBIR ENTRADAS VALIDADAS
# --------------------------------------------------
TOKEN_CANCELACION = "x"
recibir_entrada = entrada_receptor(TOKEN_CANCELACION)


# ------------------------------------
# REGISTRO CLIENTE
# -------------------------------------
def registro_cliente(servicio_clientes):
    print(
        f"\nINCLUIR CLIENTE - inserte los datos requeridos (o ingrese '{TOKEN_CANCELACION}' para cancelar)\n"
    )

    nombres_apellidos = recibir_entrada(
        "Nombre del cliente",
        "Los nombres y apellidos deben ocupar entre 10 y 60 caracteres",
        es_nombre_apellido_valido,
    )
    if not nombres_apellidos:
        return False

    numero_pasaporte = recibir_entrada(
        "Numero de pasaporte",
        "El número de pasaporte debe ser de 10 digitos decimales",
        es_num_pasaporte_valido,
    )
    if not numero_pasaporte:
        return False
    if servicio_clientes.cliente_existe(numero_pasaporte):
        print(f"\nEl número de pasaporte {numero_pasaporte} ya está registrado")
        return False

    fecha_exp_pasaporte = recibir_entrada(
        "Fecha de expedicion del pasaporte (m/d/A)",
        "La fecha está en formato inválido",
        es_fecha_valida,
    )
    if not fecha_exp_pasaporte:
        return False
    if es_fecha_pasada(fecha_exp_pasaporte):
        print("\nLa fecha de expiracion del pasaporte ha superado el límite")
        return False

    fecha_cer_vacuna = recibir_entrada(
        "Fecha del certificado de vacunacion (m/d/A)",
        "La fecha está en formato inválido",
        es_fecha_valida,
    )
    if not fecha_cer_vacuna:
        return False

    fecha_dec_impuestos = recibir_entrada(
        "Fecha de la declaracion de impuestos (m/d/A)",
        "La fecha está en formato inválido",
        es_fecha_valida,
    )
    if not fecha_dec_impuestos:
        return False

    origen_pasaporte = recibir_entrada(
        "Origen de pasaporte (V o E)",
        "Orígen de pasaporte desconocido",
        es_origen_valido,
    )
    if not origen_pasaporte:
        return False

    nuevo_cliente = Cliente.crear_nuevo_cliente(
        nombres_apellidos,
        int(numero_pasaporte),
        fecha_exp_pasaporte,
        fecha_cer_vacuna,
        fecha_dec_impuestos,
        origen_pasaporte,
    )
    error = servicio_clientes.incluir(nuevo_cliente)
    print("\n" + error if error else "\n¡Cliente registrado exitosamente!")
    input("\npresiona ENTER para continuar")
    return True


# --------------------------------------------
# MODIFICAR CLIENTE
# --------------------------------------------
def modificacion_cliente(servicio_clientes):
    print(
        f"\nMODIFICAR CLIENTE - inserte los datos requeridos (o ingrese '{TOKEN_CANCELACION}' para cancelar)\n"
    )

    numero_pasaporte = recibir_entrada(
        "Número de pasaporte del cliente",
        "El número de pasaporte debe ser de 10 digitos decimales",
        es_num_pasaporte_valido,
    )
    if not numero_pasaporte:
        return False

    if not servicio_clientes.cliente_existe(numero_pasaporte):
        print(f"\nEl número de pasaporte {numero_pasaporte} no está registrado")
        return False

    nombres_apellidos = recibir_entrada(
        "Nombre del cliente",
        "Los nombres y apellidos deben ocupar entre 10 y 60 caracteres",
        es_nombre_apellido_valido,
    )
    if not nombres_apellidos:
        return False

    fecha_exp_pasaporte = recibir_entrada(
        "Fecha de expedicion del pasaporte (m/d/A)",
        "La fecha está en formato inválido",
        es_fecha_valida,
    )
    if not fecha_exp_pasaporte:
        return False
    if es_fecha_pasada(fecha_exp_pasaporte):
        print("La fecha de expiracion del pasaporte ha superado el límite")
        return False

    fecha_cer_vacuna = recibir_entrada(
        "Fecha del certificado de vacunacion (m/d/A)",
        "La fecha está en formato inválido",
        es_fecha_valida,
    )
    if not fecha_cer_vacuna:
        return False

    fecha_dec_impuestos = recibir_entrada(
        "Fecha de la declaracion de impuestos (m/d/A)",
        "La fecha está en formato inválido",
        es_fecha_valida,
    )
    if not fecha_dec_impuestos:
        return False

    origen_pasaporte = recibir_entrada(
        "Origen de pasaporte (V o E)",
        "Orígen de pasaporte desconocido",
        es_origen_valido,
    )
    if not origen_pasaporte:
        return False

    error = servicio_clientes.modificar(
        {
            "numero_pasaporte": numero_pasaporte,
            "nombres_apellidos": nombres_apellidos,
            "fecha_exp_pasaporte": fecha_exp_pasaporte,
            "fecha_cer_vacuna": fecha_cer_vacuna,
            "fecha_dec_impuestos": fecha_dec_impuestos,
            "origen_pasaporte": origen_pasaporte,
        }
    )
    print("\n" + error if error else "\n¡Cliente modificado exitosamente!")
    input("\npresiona ENTER para continuar")
    return True


# --------------------------------------
# ELIMINAR CLIENTE
# --------------------------------------
def eliminar_cliente(servicio_clientes):
    print(
        f"\nELIMINAR CLIENTE - inserte los datos requeridos (o ingrese '{TOKEN_CANCELACION}' para cancelar)\n"
    )
    numero_pasaporte = recibir_entrada(
        "Número de pasaporte del cliente",
        "El número de pasaporte debe ser de 10 digitos decimales",
        es_num_pasaporte_valido,
    )
    if not numero_pasaporte:
        return False

    error = servicio_clientes.eliminar(numero_pasaporte)
    if error:
        print(error)
        return False
    print("\n¡Cliente eliminado exitosamente!")
    input("\npresiona ENTER para continuar")
    return True
