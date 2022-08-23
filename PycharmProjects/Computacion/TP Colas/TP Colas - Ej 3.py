class Carta:
    def __init__(self, palo, valor):
        self.palo = str(palo)
        self.valor = int(valor)



    def get_palo(self):
        return self.palo

    def get_valor(self):
        return self.valor

class PilaDeCartas:
    def __init__(self):
        self.pila = []

    def crear_carta(self):
        palo = str(input("Ingrese el palo de la carta a apilar: "))
        palo.lower()
        valor = int(input("Ingrese el valor de la carta a apilar: "))
        carta = Carta(palo, valor)
        return carta

    def apilar(self, carta_a_apilar):
        if self.pila == []:
            self.pila.append(carta_a_apilar)
        else:
            ultima_carta = self.pila[len(self.pila) - 1]
            if carta_a_apilar.valor == (ultima_carta.valor - 1) and carta_a_apilar.palo != ultima_carta.palo:
                self.pila.append(carta_a_apilar)
            elif carta_a_apilar.palo == ultima_carta.palo:
                print("No se puede apilar porque el palo de las dos cartas son iguales")
            elif carta_a_apilar.valor != (ultima_carta.valor - 1):
                print("No se puede apilar porque el valor de la carta no es inmediatamente inferior al de"
                    "la ultima carta en la pila")

    def __str__(self):
        print("Cartas en la pila:")
        for i in range(len(self.pila)):
            carta = self.pila[i]
            print(f'Valor: {carta.valor}, Palo: {carta.palo}')

pila = PilaDeCartas()
print("Juego de cartas")
while True:
    print("Opcion 1: Ingresar una nueva carta a la pila")
    print("Opcion 2: Ver pila de cartas")
    print("Opcion 0: Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        carta_creada = pila.crear_carta()
        pila.apilar(carta_creada)
    elif opcion == 2:
        print("Cartas en la pila:")
        for i in range(len(pila.pila)):
            carta = pila.pila[i]
            print(f'Valor: {carta.valor}, Palo: {carta.palo}')
    elif opcion == 0:
        break

