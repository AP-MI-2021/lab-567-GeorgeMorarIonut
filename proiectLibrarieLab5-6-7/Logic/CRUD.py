from Domain.carte import creeazaVanzareCarte, getId


def adaugaCarte(id, titlu, gen, pret, reducere, lista):
    """
    Adauga o carte intr-o lista.
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param reducere: string
    :param lista: lista de carti
    :return: o lista continand vechile carti si noua carte
    """
    carte = creeazaVanzareCarte(id, titlu, gen, pret, reducere)
    return lista + [carte]


def getById(id, lista):
    """
    da elementul dintr-o lista cu un id dat
    :param id: string
    :param lista: lista de carti
    :return: cartea cu id-ul dat sau None daca nu exista
    """
    for carte in lista:
        if getId(carte) == id:
            return carte
    return None


def stergeCarte(id, lista):
    """
    Sterge o carte dintr-o lista
    :param id:
    :param lista:
    :return: sterge cartea cu id-ul dat din lista de carti data
    """
    return [carte for carte in lista if getId(carte) != id]


def modificaCarte(id, titlu, gen, pret, reducere, lista):
    """
    Modifica datele unei carti din lista.
    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param reducere:
    :param lista: o lista de carti
    :return:
    """
    listaNoua = []
    for carte in lista:
        if getId(carte) == id:
            carteNoua = creeazaVanzareCarte(id, titlu, gen, pret, reducere)
            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua