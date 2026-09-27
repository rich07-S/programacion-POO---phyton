from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, modelo: str, color: str, motor: str, numero_puertas: int, capacidad_pasajeros: int, tipo_combustible: str, capacidad_carga_toneladas: float):
        
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.capacidad_carga_toneladas = capacidad_carga_toneladas
