from collections import OrderedDict


def tableau_freq(chaine):
    tab = {}
    for car in chaine:
        tab[car] = (tab.get(car, (0,))[0] + 1, None, None)
    return OrderedDict(sorted(tab.items(), key=lambda t:t[1]))


def arbre_bin(chaine):
    T = tableau_freq(chaine)
    noeud = 1

    while len(T) != 1:
        N1 = T.popitem(last=False)
        N2 = T.popitem(last=False)
        N  = (N1[1][0] + N2[1][0], N1, N2)
        T['noeud_'+str(noeud)] = N
        noeud += 1
        T = OrderedDict(sorted(T.items(), key=lambda t: t[1][0]))

    return (T, noeud - 1)


def parcours(arbre_bin, codage, code='', verbose=False):
    if not arbre_bin[1][1] is None:
        parcours(arbre_bin[1][1], codage, code=code+'0')
    if not arbre_bin[0].startswith('noeud'):
        if verbose:
            print(arbre_bin[0], '=>', code)
        codage[arbre_bin[0]] = code
    if not arbre_bin[1][2] is None:
        parcours(arbre_bin[1][2], codage, code=code+'1')


def determine_code(arbre_bin, racine):
    codage = {}
    parcours(arbre_bin[racine][1], codage, code='0')
    parcours(arbre_bin[racine][2], codage, code='1')
    return codage


def compresser(chaine):
    A, num_racine = arbre_bin(chaine)
    codage = determine_code(A, 'noeud_' + str(num_racine))
    compresse = ''

    for car in chaine:
        compresse += codage[car]

    return compresse, {v: k for k, v in codage.items()}


def decompresser(chaine, codage):
    pos = 0
    courant = ''
    result = ''

    while pos < len(chaine):
        courant += chaine[pos]
        car = codage.get(courant, None)
        if not car is None:
            result += car
            courant = ''
        pos += 1

    return result


if __name__ == '__main__':
    c, codage = compresser('Moi je lis GNU/Linux Magazine')
    print(c)
    print(decompresser(c, codage))
