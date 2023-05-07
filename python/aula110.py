# nos caminhos de sys.path

import aula110_m
from aula110_m import soma, variavel_modulo

print('Este módulo se chama', __name__)
print(aula110_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula110_m.soma(2, 3))