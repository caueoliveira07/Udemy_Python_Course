"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')

    resposta = input('[i]nserir [a]pagar [l]istar: ')[0].lower()
    
    if resposta == 'i':
        os.system('cls')
        valor = input('Valor: ')
        if valor not in lista:
            lista.append(valor)
        else:
            print('Esse valor já está na lista.')
    elif resposta == 'a':
        os.system('cls')
        indice = input('Escoha o índice para apagar: ')
        try:
            del lista[int(indice)]
        except:
            print('Não foi possível apagar esse índice. ')
    elif resposta == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar.')
        else:
            for i, v in enumerate(lista):
                print(i, v)
    else:
        print('Por favor, digite [i]nserir, [a]pagar ou [l]istar.')

# Resolução do professor
# import os

# lista = []
# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar: ')

#     if opcao == 'i':
#         os.system('cls')
#         valor = input('Valor: ')
#         lista.append(valor)
#     elif opcao == 'a':
#         indice_str = input('Escolha o índice para apagar: ')

#         try:
#             indice = int(indice_str)
#             del lista[indice]
#         except TypeError:
#             print('Por favor digite um número inteiro (int).')
#         except IndexError:
#             print('Índice não existe na lista.')
#         except Exception:
#             print('Erro desconhecido.')
#     elif opcao == 'l':
#         os.system('cls')

#         if len(lista) == 0:
#             print('Nada para listar')
        
#         for i, valor in enumerate(lista):
#             print(i, valor)
#     else:
#         print('Por favor, escolha i, a ou l.')