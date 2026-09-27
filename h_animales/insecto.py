from animal import Animal
class Insecto(Animal):
    def __init__(self, nombre: str, edad: int, hábitat: str, dieta: str, tamaño: str, color: str):
        super().__init__(nombre, edad, hábitat, dieta, tamaño, color)
