from .interfaces import IServicio
from .modelos.cliente import Cliente
from .db import SistemaVentasDB
from .constantes import OrigenPasaporte
from .validacion import es_fecha_pasada

class ServicioClientes(IServicio):
    servicio_clientes_db = SistemaVentasDB()

    def incluir(self, cliente: Cliente):
        cliente_existe = self.servicio_clientes_db.obtener_cliente_por_num_pasaporte(cliente.numero_pasaporte)
        if cliente_existe:
            return "Este cliente ya está registrado en la base de datos"
        self.servicio_clientes_db.registro_cliente(cl=cliente)

    def modificar(self, num_pasaporte, datos: dict):
        cliente_existe = self.servicio_clientes_db.obtener_cliente_por_num_pasaporte(num_pasaporte)
        if not cliente_existe:
            return "Este cliente no está registrado en la base de datos"
        self.servicio_clientes_db.modificacion_cliente(num_pasaporte, datos)

    def eliminar(self, num_pasaporte):
        cliente_existe = self.servicio_clientes_db.obtener_cliente_por_num_pasaporte(num_pasaporte)
        if not cliente_existe:
            return "Este cliente no esta registrado en la base de datos"
        self.servicio_clientes_db.eliminar_cliente(num_pasaporte)
    
    def obtener_clientes_por_origen_v(self):
        clientes = self.servicio_clientes_db.obtener_clientes_por_origen_pasaporte(OrigenPasaporte.V.value)
        return clientes
    
    def obtener_clientes_por_origen_e(self):
        clientes = self.servicio_clientes_db.obtener_clientes_por_origen_pasaporte(OrigenPasaporte.E.value)
        return clientes
    
    def obtener_por_declaracion_impuestos_vencida(self):
        clientes = self.servicio_clientes_db.obtener_clientes()
        clientes_di_vencida = filter(lambda cl: es_fecha_pasada(cl.fecha_declaracion_impuesto), clientes)
        return list(clientes_di_vencida)
    
    def cliente_existe(self, num_pasaporte) -> bool:
        cliente = self.servicio_clientes_db.obtener_cliente_por_num_pasaporte(num_pasaporte)
        return True if cliente else False
    
    def obtener_clientes_recaudos_validos(self):
        clientes = self.servicio_clientes_db.obtener_clientes()
        clientes_vencidos = []
        for cliente in clientes:
            if es_fecha_pasada(cliente.fecha_expedicion_pasaporte):
                continue
            elif es_fecha_pasada(cliente.fecha_declaracion_impuesto):
                continue
            elif es_fecha_pasada(cliente.fecha_certificado_vacuna):
                continue
            else:
                clientes_vencidos.append(cliente)
        return clientes_vencidos
    
    def total_clientes(self):
        return len(self.servicio_clientes_db.obtener_clientes())

