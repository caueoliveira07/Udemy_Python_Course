# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(l1, l2):
    contador = 0
    if l1 > l2:
        for item in l1:
            lista_final.append(())
            lista_final[contador] = (item, segunda_lista[contador])
            contador += 1
    else:
        for item in l2:
            lista_final.append(())
            lista_final[contador] = (item, primeira_lista[contador])
            contador += 1


primeira_lista = ['Salvador', 'Ubatuba', 'Belo Horizonte']
segunda_lista = ['BA', 'SP', 'MG', 'RJ']
lista_final = []
zipper(primeira_lista, segunda_lista)
print(lista_final)



# Resolução do professor
# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]
# from itertools import zip_longest

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(list(zip(l1, l2)))
# print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))