from abc import ABCMeta, abstractmethod


class ICliente(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def crear_nuevo_cliente(
        nombres_apellidos: str,
        num_pasaporte: int,
        fex_pasaporte: str,
        fc_vacuna: str,
        fd_impuesto: str,
        org_pasaporte: str,
    ): ...

    @property
    @abstractmethod
    def nombres_apellidos(self) -> str: ...

    @property
    @abstractmethod
    def numero_pasaporte(self) -> int: ...

    @property
    @abstractmethod
    def fecha_expedicion_pasaporte(self) -> str: ...

    @property
    @abstractmethod
    def fecha_certificado_vacuna(self) -> str: ...

    @property
    @abstractmethod
    def fecha_declaracion_impuesto(self) -> str: ...

    @property
    @abstractmethod
    def origen_pasaporte(self) -> str: ...


class IServicio(metaclass=ABCMeta):
    @abstractmethod
    def incluir(self, cliente): ...

    @abstractmethod
    def modificar(self, num_pasaporte, datos: dict): ...

    @abstractmethod
    def eliminar(self, num_pasaporte): ...
