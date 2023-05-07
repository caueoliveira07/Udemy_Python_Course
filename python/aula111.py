import importlib

import aula111_m

print(aula111_m.variavel)

for i in range(10):
    importlib.reload(aula111_m)
    print(i)

print('Fim')