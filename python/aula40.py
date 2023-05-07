"""
Iterando strings com while
"""
#       0123456789...
nome = 'Cauê Oliveira' # Iteráveis
#       ...9876543210
print(nome)
print(len(nome))
contador = 0
nome_modificado = ''
while contador < len(nome):
    nome_modificado += f'*{nome[contador]}'
    contador += 1
print(nome_modificado)

# Resolução do professor
# #       0123456789...
# nome = 'Cauê Oliveira' # Iteráveis
# #       ...9876543210

# indice = 0
# novo_nome = ''
# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)