# numarul de galeti = rotunjit(sqrt(numarul de elemente))
# galeata "apropiata" = ceil(valoare * numar_galeti / valMaxima)

import sys
import math

# lista = []

# n = int(input())
# input_strings = input("Numerele tale:")

# input_strings = input_strings.split()

# for i in range(len(input_strings)):
#     lista.append(int(input_strings[i]))

# # insertionSort pentru bucketSort
# """
#     -> imparti vectorul in doua
#     -> Iei primul element din vectorul nesortat si ii gasesti pozitia coresp in vectorul sortat
#     -> repeti pana vectorul nesortat este gol
# """

def insertionSort(listaPar):
    for i in range(1, len(listaPar)):
        key = listaPar[i]
        j = i - 1
        while j >= 0 and key < listaPar[j]:
            # parcurgem elementele din vectorul "sortat" si punem pe pozitia corespunzatoare
            listaPar[j + 1] = listaPar[j]
            j -= 1
        # daca nu se (mai) intampla ce am zis mai sus, atunci listaPar va fi elementul key
        listaPar[j + 1] = key

    return listaPar



# bucketSort
def bucketSort(lista):
    numarGaleti = round(math.sqrt(len(lista)))
    valMaxima = max(lista)
    vectorGaleti = []


    for galeata in range(numarGaleti):
        vectorGaleti.append([])
    
    for elem in lista:
        indexG = math.ceil(elem*numarGaleti/valMaxima)
        vectorGaleti[indexG - 1].append(elem)

    for i in range(numarGaleti):
        vectorGaleti[i] = insertionSort(vectorGaleti[i])
    
    k = 0
    for i in range(numarGaleti):
        for j in range(len(vectorGaleti[i])):
            lista[k] = vectorGaleti[i][j]
            k += 1
    
    return lista


