# 1. CREAR Clase
class Botella:
    
    # 2. CREAR Constructor 
    # 3. CREAR Atributos
    def __init__(self, material: str, capacidad: str, forma: str, diseño: str, tapa: str, grabados: bool):
        self.material = material
        self.capacidad = capacity = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados

    # 4. CREAR Métodos 
    def contener_liquidos(self, liquido: str):
        return f"La botella de {self.material} ahora contiene: {liquido}"

    def facilitar_el_vertido(self, angulo_inclinacion: int):
        return f"Vertiendo líquido eficientemente a un ángulo de {angulo_inclinacion}°"

    def cierre_hermetico(self, tipo_sellado: str):
        return f"Cierre hermético activado usando {tipo_sellado} en la tapa {self.tapa}"

    def transporte(self, destino: str):
        return f"Transportando lote de botellas con forma {self.forma} hacia {destino}"

    def manejo(self, tipo_agarre: str):
        return f"Manejo de la botella optimizado para agarre de tipo: {tipo_agarre}"

    # 7. Retornos 
    def compatibilidad_con_bebidas_calientes_frias(self, temperatura_celsius: int):
        if temperatura_celsius > 60 and self.material == "Plástico":
            return f"Alerta: {temperatura_celsius}°C no es compatible con {self.material}."
        return f"Compatibilidad exitosa para {temperatura_celsius}°C en material {self.material}."

    def reutilizacion(self, veces_reutilizada: int):
        limite = 20 if self.material == "Vidrio" else 3
        apto = veces_reutilizada <= limite
        return f"¿Apta para reutilizar {veces_reutilizada} veces?: {apto}"

    def transparencia(self, porcentaje_luz: int):
        return f"Transparencia del {self.material} permite el paso del {porcentaje_luz}% de luz"
