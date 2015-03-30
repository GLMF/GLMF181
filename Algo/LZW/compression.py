def compresser(chaine, verbose=True):
    car = chaine[0]
    dico = {}
    dico[car] = str(ord(car))
    code = 256
    resultat = None

    for i in range(1, len(chaine)):
        suivant = chaine[i]
        if suivant not in dico:
            dico[suivant] = str(ord(suivant))
        concat = car + suivant
        if concat in dico:
            car = concat
        else:
            dico[concat] = str(code)
            code += 1
            if resultat is None:
                resultat = dico[car]
            else:
                resultat += ' ' + dico[car]
            car = suivant

    resultat += ' ' + dico[car]

    if verbose:
        for seq, code in dico.items():
            print('{:5s} => {:5s}'.format(seq, code))

    return resultat


def decompresser(chaine, verbose=True):
    code = 256
    dico = {}
    data = list(map(int, chaine.split(' ')))
    car = chr(data[0])
    result = car

    for i in range(1, len(data)):
        suivant = data[i]
        if suivant < 255:
            entree = chr(suivant)
        elif suivant in dico:
            entree = dico[suivant]
        elif suivant == code:
            entree = car + car[0]
        else:
            raise ValueError('Données mal compressées!')
        result += entree

        dico[code] = car + entree[0]
        code += 1

        car = entree

    if verbose:
        for code, seq in dico.items():
            print('{:5d} => {:5s}'.format(code, seq))

    return result


if __name__ == '__main__':
    c = compresser('titi itit titi')
    print(c)
    print(decompresser(c))
