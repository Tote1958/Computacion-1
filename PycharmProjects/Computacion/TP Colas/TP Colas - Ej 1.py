class TorreDeControl:
    def __init__(self):
        self.ready_to_fly = []
        self.ready_to_land = []

    def fly_push(self):
        element = input("Ingrese el elemento a ingresar en la cola de despegue: ")
        self.ready_to_fly.append(element)

    def land_push(self):
        element = input("Ingrese el elemento a ingresar en la cola de aterrizaje: ")
        self.ready_to_land.append(element)

    def accion(self):
        if not self.land_is_empty():
            self.land_pop()
            print("Aterriza un avion")
            print(f'Quedan {self.land_size()} aviones para aterrizar')
            print(f'Quedan {self.fly_size()} aviones para despegar')
        elif not self.fly_is_empty():
            self.fly_pop()
            print("Despega un avion")
            print(f'Quedan {self.land_size()} aviones para aterrizar')
            print(f'Quedan {self.fly_size()} aviones para despegar')

    def reconocimiento(self, landing, to_fly):
        if landing is not "vacio":
            self.ready_to_land.append(landing)
        elif to_fly is not "vacio":
            self.ready_to_land.append(to_fly)

    def land_pop(self):
        try:
            return self.ready_to_land.pop(0)
        except IndexError:
            raise ValueError("La cola esta vacia")

    def fly_pop(self):
        try:
            return self.ready_to_fly.pop(0)
        except IndexError:
            raise ValueError("La cola esta vacia")

    def land_size(self):
        return len(self.ready_to_land)

    def fly_size(self):
        return len(self.ready_to_fly)

    def land_is_empty(self):
        return self.ready_to_land == []

    def fly_is_empty(self):
        return self.ready_to_fly == []

    def __str__(self):
        print(f'Hay {self.ready_to_land} aviones para aterrizar')
        print(f'Hay {self.ready_to_fly} aviones para despegar')


airport = TorreDeControl()

