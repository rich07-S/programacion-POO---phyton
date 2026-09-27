from botella import Botella

class BotellaPlastica(Botella):
    def __init__(self, capacidad: str, forma: str, diseño: str, tapa: str, grabados: bool, es_reciclable: bool):
        
        super().__init__("Plástico", capacidad, forma, diseño, tapa, grabados)
        self.es_reciclable = es_reciclable
