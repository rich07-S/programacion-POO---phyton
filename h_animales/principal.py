from mamifero import Mamifero
from reptil import Reptil
from pez import Pez
from insecto import Insecto
from ave import Ave

def main():
    print("SISTEMA COMPLETO REINO ANIMAL")

    # 5. CREAR objetos 
    caballo = Mamifero("Caballo", 4, "Pradera", "Herbívoro", "Grande", "Negro")
    cocodrilo = Reptil("Cocodrilo", 12, "Pantano", "Carnívoro", "Grande", "Verde Oscuro")
    pez_cirujano = Pez("Pez Cirujano", 1, "Arrecife", "Omnívoro", "Pequeño", "Azul")
    escarabajo = Insecto("Escarabajo", 1, "Bosque", "Herbívoros", "Pequeño", "Marrón")
    pato = Ave("Pato", 2, "Laguna", "Omnívoro", "Mediano", "Blanco y Café")

    # 6. llamar Métodos 
    print(caballo.moverse("Galope"))
    print(cocodrilo.instintos(True))
    print(pez_cirujano.moverse("Nado"))
    print(escarabajo.alimentarse("Hojas"))
    print(pato.moverse("Vuelo/Nado"))

if __name__ == "__main__":
    main()
