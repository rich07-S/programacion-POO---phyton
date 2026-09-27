from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, modelo: str, color: str, motor: str, numero_puertas: int, capacidad_pasajeros: int, tipo_combustible: str, es_descapotable: bool):
        
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.es_descapotable = es_descapotable
