# 1. CREAR Clase
class Vehiculo:
    
    # 2. CREAR 
    # 3. CREAR 
    def __init__(self, modelo: str, color: str, motor: str, numero_puertas: int, capacidad_pasajeros: int, tipo_combustible: str):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    # 4. CREAR Métodos
    def arranque(self, llave_correcta: bool):
        if llave_correcta:
            return f"El vehículo {self.modelo} ha encendido su motor {self.motor}."
        return "Llave incorrecta. No se puede arrancar."

    def apagado(self):
        return f"Motor del vehículo {self.modelo} apagado correctamente."

    def aceleracion_y_frenado(self, velocidad_objetivo: int):
        return f"Acelerando hasta {velocidad_objetivo} km/h y aplicando frenado controlado."

    def sistema_de_direccion(self, direccion: str):
        return f"Girando el sistema de dirección hacia la {direccion}."

    def climatizacion(self, temperatura_deseada: int):
        return f"Aire acondicionado programado a {temperatura_deseada}°C."

    # 7. Retornos 
    def tipo_de_seguridad(self, activar_airbags: bool):
        estado = "Activos y Listos" if activar_airbags else "Desactivados"
        return f"Sistema de seguridad del {self.modelo}: Airbags -> {estado}."

    def luces(self, tipo_luces: str):
        return f"Luces tipo '{tipo_luces}' encendidas para el combustible {self.tipo_combustible}."

    def sistema_de_ventanas(self, posicion: str):
        return f"Ventanas del vehículo posicionadas en: {posicion}."

    def sistema_de_espejo(self, angulo: int):
        return f"Espejos retrovisores ajustados a un ángulo de {angulo}°."
