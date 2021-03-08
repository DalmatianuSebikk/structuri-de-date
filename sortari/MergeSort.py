
# lista = []

# n = int(input())
# input_strings = input("Numerele tale:")

# input_strings = input_strings.split()

# for i in range(len(input_strings)):
#     lista.append(int(input_strings[i]))

# mergeSort -> Sortarea prin interclasare
# tot impartim vectorul in 2 pana cand 

def merge(listaPar, st, mijloc, dr):
    n1 = mijloc - st + 1
    n2 = dr - mijloc

    Stanga = [0] * (n1)
    Dreapta = [0] * (n2)

    for i in range(0, n1):
        Stanga[i] = listaPar[st + i]
    
    for j in range(0, n2):
        Dreapta[j] = listaPar[mijloc + j + 1]

    # interclasarea

    i = 0
    j = 0
    k = st

    while i < n1 and j < n2:
        if Stanga[i] <= Dreapta[j]:
            listaPar[k] = Stanga[i]
            i += 1
        else:
            listaPar[k] = Dreapta[j]
            j += 1
        k += 1
    
    while i < n1:
        listaPar[k] = Stanga[i]
        i += 1
        k += 1
    
    while j < n2:
        listaPar[k] = Dreapta[j]
        j += 1
        k += 1

def mergeSort(listaPar, st, dr):
    if st < dr:
        mijloc = (st + dr) // 2
        mergeSort(listaPar, st, mijloc)
        mergeSort(listaPar, mijloc + 1, dr)
        merge(listaPar, st, mijloc, dr)
    return listaPar

# print(mergeSort(lista, 0, len(lista) - 1))

