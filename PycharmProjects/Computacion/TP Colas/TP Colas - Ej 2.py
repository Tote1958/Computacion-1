class ColaDePacientes:
    def __init__(self):
        self.cola = []

    def nuevo_paciente(self, paciente):
        self.cola.append(paciente)
        return f'El paciente {paciente}, fue agregado a la cola'

    def proximo_paciente(self):
        paciente = self.cola[0]
        self.cola.pop(0)
        return f'El primer paciente de la cola es {paciente}'

    def get_size(self):
        return len(self.cola)

    def get_cola(self):
        return self.cola

consultorio = ColaDePacientes()
print("Consultorio")
while True:
    print("Opcion 1: Ingresar un nuevo usuario")
    print("Opcion 2: Indicar que el consultorio se libero")
    print("Opcion 3: Ver cola")
    print("Opcion 0: Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        paciente_a_ingresar = str(input("Ingrese el nombre del paciente: "))
        consultorio.nuevo_paciente(paciente_a_ingresar)
    elif opcion == 2:
        if consultorio.get_size() != 0:
            print(consultorio.proximo_paciente())
        else:
            print("No hay pacientes en la cola")
    elif opcion == 3:
        print(consultorio.get_cola())
    elif opcion == 0:
        break
