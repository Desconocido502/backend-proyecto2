# Importando el modulo de regex de python
import re

# cadena = 'regla7re#'
cadena = 'regularesca'

# *print(re.search('aprender', cadena))


'''
print(re.search(textoBuscar, cadena))
# *print(re.findall(textoBuscar, cadena))
listaLetrasUserName = []
listaLetrasUserName.extend(cadena)
print(len(listaLetrasUserName))

if re.search(textoBuscar, cadena) is not None:
    print('Nombre de usuario valido')
else:
    print('Nombre de usuario no valido')
'''


def validarUserName(cadena=''):
    textoBuscar = '[\w{8,}]+\W'
    if cadena == '':
        print('Cadena vacia')
        return None
    elif re.search(textoBuscar, cadena):
        print('Nombre de usuario valido')
        return True
    else:
        print('Nombre de usuario no valido')
        return False


validarUserName('')
validarUserName(cadena)
cadena = 'regla7re#'
validarUserName(cadena)
