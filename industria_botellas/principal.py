from botella_plastica import BotellaPlastica
from botella_vidrio import BotellaVidrio

def main():
    print("EJECUCIÓN ORDENADA IND_BOTELLAS")

    # 5. CREAR objeto
    botella_pet = BotellaPlastica("500ml", "Cilíndrica", "Ergonómico", "Rosca", False, True)
    botella_premium = BotellaVidrio("1 Litro", "Cuadrada", "Tallado Premium", "Corcho", True, "Verde")

    # 6. llamar Métodos
    print("Pruebas Botella de Plástico")
    resultado_contenido = botella_pet.contener_liquidos("Gaseosa")
    print(resultado_contenido)
    
    resultado_termico = botella_pet.compatibilidad_con_bebidas_calientes_frias(85)
    print(resultado_termico)

    print("Pruebas Botella de Vidrio")
    resultado_vertido = botella_premium.facilitar_el_vertido(45)
    print(resultado_vertido)
    
    resultado_reutilizar = botella_premium.reutilizacion(12)
    print(resultado_reutilizar)

if __name__ == "__main__":
    main()
