# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def mult(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

total = mult(5,5,2)
print(total)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def parouimpar(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par.'
    return f'O número {numero} é ímpar.'

print(parouimpar(328))



# Resolução do professor
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicação = multiplicar(10, 2, 3, 4, 5)
print(multiplicação)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)