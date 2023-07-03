import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

with open('aula142.json', 'r') as arquivo:
    dados = json.load(arquivo)

pessoa = Pessoa(dados['nome'], dados['idade'])

print(vars(pessoa))



# Resolução do professor
# from aula127_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

# # fazer_dump()

# with open(CAMINHO_ARQUIVO, 'r') as arquivo:
#     pessoas = json.load(arquivo)
#     p1 = Pessoa(**pessoas[0])
#     p2 = Pessoa(**pessoas[1])
#     p3 = Pessoa(**pessoas[2])

#     print(p1.nome, p1.idade)
#     print(p2.nome, p2.idade)
#     print(p3.nome, p3.idade)