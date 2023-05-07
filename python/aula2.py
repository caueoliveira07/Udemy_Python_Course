# Métodos para quebra de linha:
# \r\n -> CRLF (É o padrão no Windows)
# \n -> LF (É o padrão no Mac/Linux)

print(12, 34, 1011, sep="-", end='##\n')
print(56, 78, sep='-', end='\n##')
print(56, 78, sep='-')