
# lista = []

# n = int(input())
# input_strings = input("Numerele tale:")

# input_strings = input_strings.split()

# for i in range(len(input_strings)):
#     lista.append(int(input_strings[i]))

# quick sort -> algoritm divide et impera
# alegi un pivot si pui numerele mai mici decat pivotul in stanga si pe cele mai mari in dreapta
# spatiu extra nu este necesar

# functia partitie -> ia elementul pivot si il pune in pozitia corecta din lista

def partitie(listaP, st, dr):
    i = st - 1
    pivot = listaP[dr]

    # acum punem elementele mai mici decat pivot la stanga si alea mai mari la dreapta
    for j in range(st, dr):
        if listaP[j] <= pivot:
            i += 1
            listaP[i], listaP[j] = listaP[j], listaP[i]
    # replace la valoarea care este mai mare decat pivotul
    # stim ca valoarea este pe lista[i + 1], iar pivotul pe lista[dr]
    listaP[i + 1], listaP[dr] = listaP[dr], listaP[i + 1]

    return (i + 1) # returneaza indexul partitiei

def quickSort(listaP, st, dr):
    if st < dr:
        pi = partitie(listaP, st, dr)
        quickSort(listaP, st, pi - 1)
        quickSort(listaP, pi + 1, dr)


# quickSort(lista, 0, len(lista) - 1)
# print(lista)