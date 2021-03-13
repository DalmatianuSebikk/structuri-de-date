import sys

# lista = []

# n = int(input())
# input_strings = input("Numerele tale:")

# input_strings = input_strings.split()

# for i in range(len(input_strings)):
#     lista.append(int(input_strings[i]))

# Count Sort : Ai un array de frecventa, adaugi elementele in frecv, unde nu e 0 afisezi de cate ori apare in lista

def countSort(lista):
    sortat = []
    frecv = [0] * (max(lista) + 1)
    for element in lista:
        frecv[element] += 1
    
    for i in range(len(frecv)):
        if frecv[i] != 0:
            while frecv[i] != 0:
                sortat.append(i)
                frecv[i] -= 1
    return sortat



