def divide(numbers,div):
    newList = []
    for i in range(len(numbers)):
        if numbers[i] % div == 0:
            newList.append(numbers[i])
    return newList


nums = []
n = int(input("Ingrese la cantidad de numeros a ingresar: "))
num = 0
for i in range(n):
    num = int(input("Ingrese un numero: "))
    nums.append(num)
divNum = int(input("Ingrese en que numero dividir la lista: "))
print(divide(nums, divNum))
