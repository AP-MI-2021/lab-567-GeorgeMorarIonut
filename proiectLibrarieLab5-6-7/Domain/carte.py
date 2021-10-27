def creeazaVanzareCarte(id, titlu, gen, pret, reducere):
    """
    Creeaza un dictionar pentru vanzarea unei carti.
    :param id: numar intreg
    :param titluCarte: string
    :param genCarte: string
    :param pret: float
    :param tipReducere: string
    :return:
    """
    lista = []

    lista.append(id)
    lista.append(titlu)
    lista.append(gen)
    lista.append(pret)
    lista.append(reducere)

    return lista


def getId(lista):
    """
    Ia id-ul unei carti.
    :param carte: dictionar ce retine o carte
    :return: id-ul cartii
    """
    return lista[0]


def getTitlu(lista):
    """
    Ia titlul unei carti.
    :param lista: dictionar ce retine o carte
    :return: titlul cartii
    """
    return lista[1]


def getGen(lista):
    """
    Ia genul unei carti.
    :param lista:  dictionar ce retine o carte
    :return:  genul cartii
    """
    return lista[2]


def getPret(lista):
    """
    Ia pretul unei carti.
    :param lista: dictionar ce retine o carte
    :return: pretul cartii
    """
    return lista[3]


def getReducere(lista):
    """
    Ia reducerea unei carti.
    :param lista: dictionar ce retine o carte
    :return: reducerea clientului
    """
    return lista[4]


def toString(lista):
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, Reducere: {}".format(
        lista[0],
        lista[1],
        lista[2],
        lista[3],
        lista[4]
    )