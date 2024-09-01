from app.servicios import ServicioClientes
from app.validacion import (
    es_fecha_valida,
    es_nombre_apellido_valido,
    es_num_pasaporte_valido,
    es_origen_valido,
    es_fecha_pasada,
)
from app.modelos.cliente import Cliente


def imprimir_reporte():
    d_clientes_v = "Clientes con pasaporte venezolano (V):"
    num_clientes_V = f"{len(servicio_clientes.obtener_clientes_por_origen_v())}"

    d_clientes_e = "Clientes con pasaporte extranjero (E):"
    num_clientes_E = f"{len(servicio_clientes.obtener_clientes_por_origen_e())}"

    d_clientes_di = "Clientes con declaracion de impuesto vencida:"
    num_clientes_di_vencida = (
        f"{len(servicio_clientes.obtener_por_declaracion_impuestos_vencida())}"
    )

    d_clientes_vigentes = "Clientes con recaudos vigentes:"
    num_clientes_vigentes = (
        f"{len(servicio_clientes.obtener_clientes_recaudos_validos())}"
    )

    print("\nREPORTE CLIENTES\n")
    print(f"Total clientes: {servicio_clientes.total_clientes()}")
    print("{} {} {}".format(d_clientes_v, 20 * "-", num_clientes_V))
    print("{} {} {}".format(d_clientes_e, 20 * "-", num_clientes_E))
    print("{} {} {}".format(d_clientes_di, 13 * "-", num_clientes_di_vencida))
    print("{} {} {}".format(d_clientes_vigentes, 27 * "-", num_clientes_vigentes))
    input("\npresiona ENTER para continuar")


def imprimir_menu_opciones():
    print("\nMenu de opciones\n")
    print("1. Incluir")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Reporte")
    print("5. Salir")


def entrada_receptor(token_cancelacion: str):
    def recibir_entrada(msg: str, err: str, validacion_fn=None):
        while True:
            entrada = input(f"{msg} : ")
            if entrada == token_cancelacion:
                return False
            if validacion_fn and not validacion_fn(entrada):
                print("\n" + err + "\n")
            else:
                return entrada

    return recibir_entrada


servicio_clientes = ServicioClientes()
token_cancelacion = "x"
recibir_entrada = entrada_receptor(token_cancelacion)
programa_activo = True

def registro_cliente():
    print(f"\nINCLUIR CLIENTE - inserte los datos requeridos (o ingrese '{token_cancelacion}' para cancelar)\n")

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


def modificacion_cliente():
    print(f"\nMODIFICAR CLIENTE - inserte los datos requeridos (o ingrese '{token_cancelacion}' para cancelar)\n")

    numero_pasaporte = recibir_entrada(
        "Número de pasaporte del cliente",
        "El número de pasaporte debe ser de 10 digitos decimales",
        es_num_pasaporte_valido,
    )
    if not numero_pasaporte:
        return False

    if not servicio_clientes.cliente_existe(numero_pasaporte):
        print(f"\nEl número de pasaporte {numero_pasaporte} no está registrado")
        input("\npresiona ENTER para continuar")
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
        input("Presiona ENTER para continuar")
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

    error = servicio_clientes.modificar({
        "numero_pasaporte": numero_pasaporte,
        "nombres_apellidos": nombres_apellidos,
        "fecha_exp_pasaporte": fecha_exp_pasaporte,
        "fecha_cer_vacuna": fecha_cer_vacuna,
        "fecha_dec_impuestos": fecha_dec_impuestos,
        "origen_pasaporte": origen_pasaporte
    })
    print("\n" + error if error else "\n¡Cliente modificado exitosamente!")
    input("\npresiona ENTER para continuar")
    return True





print(
    """
****************************
SISTEMA VENTA - AGENCIA JDBI
****************************
"""
)
while programa_activo:
    imprimir_menu_opciones()
    opcion_usuario = input("\n-> ")

    match opcion_usuario:
        case "5":
            programa_activo = False
        case "1":
            if not registro_cliente():
                input("\npresiona ENTER para continuar")
                continue

        case "2":
            if not modificacion_cliente():
                input("\npresiona ENTER para continuar")
                continue

        case "3":
            print(
                f"\nELIMINAR CLIENTE - inserte los datos requeridos (o ingrese '{token_cancelacion}' para cancelar)\n"
            )

            numero_pasaporte = recibir_entrada(
                "Número de pasaporte del cliente",
                "El número de pasaporte debe ser de 10 digitos decimales",
                es_num_pasaporte_valido,
            )
            if not numero_pasaporte:
                continue

            error = servicio_clientes.eliminar(numero_pasaporte)
            print("\n" + error if error else "\n¡Cliente eliminado exitosamente!")
            input("\npresiona ENTER para continuar")

        case "4":
            imprimir_reporte()
