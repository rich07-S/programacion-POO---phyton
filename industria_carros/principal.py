from automovil import Automovil
from camion import Camion

def main():
    print("**GESTIÓN INDUSTRIA CARROS**")

    # 5. CREAR objeto 
    carro_deportivo = Automovil("BMW Z4", "Negro", "3.0L Turbo", 2, 2, "Gasolina", True)
    camion_carga = Camion("Chevrolet FVR", "Blanco", "7.8L Diesel", 2, 3, "Diesel", 12.0)

    # 6. llamar Métodos 
    print("--Pruebas con el Automóvil Deportivo--")
    print(carro_deportivo.arranque(True))
    print(carro_deportivo.climatizacion(21))
    print(carro_deportivo.tipo_de_seguridad(True))

    print("--Pruebas con el Camión de Carga--")
    print(camion_carga.arranque(True))
    print(camion_carga.aceleracion_y_frenado(60))
    print(camion_carga.luces("Altas de carretera"))

if __name__ == "__main__":
    main()
