"""
Formatação básica de strings
s - strings
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(<>^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # Texto a esquerda com espaços a direita (nesse caso são 7 espaços, já que o texto da variável tem 3 caracteres)
print(f'{variavel: <10}') # Texto a direota com espaços a esquerda
print(f'{variavel: ^10}') # Texto centralizado com espaços a esquerda e a direita
print(f'{1000.4873648123746:0=+10,.1f}') # Irá mostrar o número com sinal de negativo ou de positivo
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')