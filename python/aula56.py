"""
Introdução ao desempacotamento + tuples (tuplas)
"""
# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes

# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)