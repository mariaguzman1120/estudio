import os

from io import open


if __name__ == '__main__':
    path = os.path.join('..', 'data', 'visitas.txt')
    fichero = open(path, 'r', encoding='utf-8')
    texto = fichero.read()
    fichero.close()

    if not texto:
        texto = 0
    else:
        texto = int(texto)

    argumento = input('ingrese argumento: ')

    if argumento == 'inc':
        texto += 1
    elif argumento == 'dec':
        texto -= 1
    else:
        print(texto)

    fichero = open(path, 'w')
    fichero.write(str(texto))
    fichero.close()
