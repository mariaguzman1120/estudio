# Johan Arbey Mejía Vargas cc: 1152195956
# María del mar Ipia Guzmán cc: 1214726595

import os

from io import open


if __name__ == '__main__':
    path = os.path.join('..', 'data', 'estudiantes.txt')
    fichero = open(path, 'r', encoding='utf-8')
    texto = fichero.readlines()
    fichero.close()

    personas = []
    for i in range(len(texto)):
        new = texto[i].replace('\n', '').split(';')
        dic = {
            'id': new[0],
            'nombre': new[1],
            'apellido': new[2],
            'nacimiento': new[3]}
        personas.append(dic)

    print(personas)

    for persona in personas:
        print(persona['nombre'])
        for campo in persona:
            print(f'{campo} = {persona[campo]}')
