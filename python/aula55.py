"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
indices = []
contador = 0

for nome in lista:
    indices.append(contador)
    contador += 1

for indice in indices:
    print(indice, lista[indice])

# Resolução do professor
# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('João')

# indices = range(len(lista))

# for indice in indices:
#     print(indice, lista[indice], type(lista[indice]))