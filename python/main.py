from app.servicios import ServicioClientes
from app.funciones import imprimir_menu_opciones
from app.reportes import imprimir_reporte
from app.clientes import registro_cliente, modificacion_cliente, eliminar_cliente

servicio_clientes = ServicioClientes()

print(
    """
****************************
CRM CLIENTES - AGENCIA JDBI
****************************
"""
)

programa_activo = True
while programa_activo:
    imprimir_menu_opciones()
    opcion_usuario = input("\n-> ")

    match opcion_usuario:
        case "5":
            programa_activo = False
        case "1":
            if not registro_cliente(servicio_clientes):
                input("\npresiona ENTER para continuar")
                continue

        case "2":
            if not modificacion_cliente(servicio_clientes):
                input("\npresiona ENTER para continuar")
                continue

        case "3":
            if not eliminar_cliente(servicio_clientes):
                input("\npresiona ENTER para continuar")
                continue

        case "4":
            origen_v = len(servicio_clientes.obtener_clientes_por_origen_v())
            origen_e = len(servicio_clientes.obtener_clientes_por_origen_e())
            impuestos_vencidos = len(
                servicio_clientes.obtener_por_declaracion_impuestos_vencida()
            )
            vigentes = len(servicio_clientes.obtener_clientes_recaudos_validos())
            imprimir_reporte(origen_v, origen_e, impuestos_vencidos, vigentes)
