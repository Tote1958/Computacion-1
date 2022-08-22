def opuesto(num):
    if num != 0:
        num = num - (num*2)
    else:
        num = 0
    return num
numDado = int(input("Ingrese un numero: "))
print("El numero opuesto al ingresado es:", opuesto(numDado))