import time

def busqueda_lineal(arr, element):
    for i in arr:
        if arr[i] == element:
            print("El elemento fue encontrado")
            return i
            break
def binary_search(arr, element):
    ord_arr = arr
    ord_arr.sort()
    index = len(ord_arr)//2
    counter = 0
    high = 0
    while True:
        counter = counter + 1
        if ord_arr[index] == element:
            print("El elemento fue encontrado")
            return counter
        elif ord_arr[index] > element:
            high = index - 1
            index = high//2
        else:
            low = index + 1
            index = (high + low)//2

list = []
for i in range(200):
    list.append(i)


inicio = time.time()
print(binary_search(list, int(20)))
time.sleep(1)
fin = time.time()
print(fin - inicio)
inicio = time.time()
print(busqueda_lineal(list, int(20)))
time.sleep(1)
fin = time.time()
print(fin - inicio)