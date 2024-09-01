from ..interfaces import ICliente
from ..validacion import es_fecha_valida, es_nombre_apellido_valido, es_num_pasaporte_valido, es_origen_valido


class Cliente(ICliente):
    @property
    def nombres_apellidos(self) -> str:
        return self.__nombres_apellidos

    @nombres_apellidos.setter
    def nombres_apellidos(self, nombres_apellidos: str):
        if es_nombre_apellido_valido(nombres_apellidos):
            self.__nombres_apellidos = nombres_apellidos
        else:
            raise ValueError("Error en el tipo de dato")

    @property
    def numero_pasaporte(self) -> int:
        return self.__numero_pasaporte

    @numero_pasaporte.setter
    def numero_pasaporte(self, numero_cliente: int):
        if es_num_pasaporte_valido(numero_cliente):
            self.__numero_pasaporte = numero_cliente
        else:
            raise ValueError("Pasaporte inválido")

    @property
    def fecha_expedicion_pasaporte(self) -> str:
        return self.__fecha_expedicion_pasaporte

    @fecha_expedicion_pasaporte.setter
    def fecha_expedicion_pasaporte(self, fecha_cliente: str):
        if es_fecha_valida(fecha_cliente):
            self.__fecha_expedicion_pasaporte = fecha_cliente
        else:
            raise ValueError("La fecha es invalida")

    @property
    def fecha_certificado_vacuna(self) -> str:
        return self.__fecha_certificado_vacuna
    
    @fecha_certificado_vacuna.setter
    def fecha_certificado_vacuna(self, fecha_cliente):
        if es_fecha_valida(fecha_cliente):
            self.__fecha_certificado_vacuna = fecha_cliente
        else:
            raise ValueError("La fecha es invalida")

    @property
    def fecha_declaracion_impuesto(self) -> str:
        return self.__fecha_declaracion_impuesto
    
    @fecha_declaracion_impuesto.setter
    def fecha_declaracion_impuesto(self, fecha_cliente):
        if es_fecha_valida(fecha_cliente):
            self.__fecha_declaracion_impuesto = fecha_cliente
        else:
            raise ValueError("La fecha es invalida")

    @property
    def origen_pasaporte(self) -> str:
        return self.__origen_pasaporte
    
    @origen_pasaporte.setter
    def origen_pasaporte(self, origen_cliente: str):
        if es_origen_valido(origen_cliente):
            self.__origen_pasaporte = origen_cliente
        else:
            raise ValueError("Origen invalido")

    @staticmethod
    def crear_nuevo_cliente(nombres_apellidos: str, num_pasaporte: int, fex_pasaporte: str, fc_vacuna: str, fd_impuesto: str, org_pasaporte: str):
        nuevo_cliente = Cliente()
        nuevo_cliente.nombres_apellidos = nombres_apellidos
        nuevo_cliente.numero_pasaporte = num_pasaporte
        nuevo_cliente.fecha_expedicion_pasaporte = fex_pasaporte
        nuevo_cliente.fecha_certificado_vacuna = fc_vacuna
        nuevo_cliente.fecha_declaracion_impuesto = fd_impuesto
        nuevo_cliente.origen_pasaporte = org_pasaporte
        return nuevo_cliente
