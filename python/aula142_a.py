# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Alice", 25)

dados = vars(pessoa)

with open('aula142.json', 'w') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)



# Resolução do professor
# CAMINHO_ARQUIVO = 'aula142.json'


# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade


# p1 = Pessoa('João', 33)
# p2 = Pessoa('Helena', 21)
# p3 = Pessoa('Joana', 11)
# bd = [vars(p1), p2.__dict__, vars(p3)]


# def fazer_dump():
#     with open(CAMINHO_ARQUIVO, 'w') as arquivo:
#         print('FAZENDO DUMP')
#         json.dump(bd, arquivo, ensure_ascii=False, indent=2)


# if __name__ == '__main__':
#     print('ELE É O __main__')
#     fazer_dump()