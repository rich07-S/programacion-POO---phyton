from botella import Botella

class BotellaVidrio(Botella):
    def __init__(self, capacidad: str, forma: str, diseño: str, tapa: str, grabados: bool, color_vidrio: str):
        
        super().__init__("Vidrio", capacidad, forma, diseño, tapa, grabados)
        self.color_vidrio = color_vidrio
