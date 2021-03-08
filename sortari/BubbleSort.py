
# CITIRE CUM TREBUIE 
# lista = []
# n = int(input())
# input_strings = input("Numerele tale:")

# input_strings = input_strings.split()

# for i in range(len(input_strings)):
#     lista.append(int(input_strings[i]))

def bubbleSort(lista, n):
    # mergem prin toate elementele
    for i in range(n):
        # elementele de la n - i - 1 la final sunt puse deja in ordine
        for j in range(n - i - 1):
            # daca e mai mare, atunci dam swap
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# bubbleSort()
# print(lista)

