# 1. CREAR Clase
class Animal:
    # 2. CREAR Constructor
    # 3. CREAR Atributos
    def __init__(self, nombre: str, edad: int, hábitat: str, dieta: str, tamaño: str, color: str):
        self.nombre = nombre
        self.edad = edad
        self.hábitat = hábitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    # 4. CREAR Métodos 
    def moverse(self, tipo_movimiento: str):
        return f"{self.nombre} se mueve por medio de: {tipo_movimiento}."

    def alimentarse(self, alimento: str):
        return f"{self.nombre} está comiendo {alimento}."

    # 7. Retornos
    def instintos(self, peligro: bool):
        reaccion = "Alerta/Ataque" if peligro else "Calma"
        return f"Instinto de {self.nombre}: {reaccion}."
