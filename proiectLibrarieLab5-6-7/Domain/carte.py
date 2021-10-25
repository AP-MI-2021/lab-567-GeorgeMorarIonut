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
    return {
        "id": id,
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "reducere": reducere
    }


def getId(carte):
    """
    Ia id-ul unei carti.
    :param carte: dictionar ce retine o carte
    :return: id-ul cartii
    """
    return carte["id"]


def getTitlu(carte):
    """
    Ia titlul unei carti.
    :param carte: dictionar ce retine o carte
    :return: titlul cartii
    """
    return carte["titlu"]


def getGen(carte):
    """
    Ia genul unei carti.
    :param carte:  dictionar ce retine o carte
    :return:  genul cartii
    """
    return carte["gen"]


def getPret(carte):
    """
    Ia pretul unei carti.
    :param carte: dictionar ce retine o carte
    :return: pretul cartii
    """
    return carte["pret"]


def getReducere(carte):
    """
    Ia reducerea unei carti.
    :param carte: dictionar ce retine o carte
    :return: reducerea clientului
    """
    return carte["reducere"]


def toString(carte):
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, Reducere: {}".format(
        getId(carte),
        getTitlu(carte),
        getGen(carte),
        getPret(carte),
        getReducere(carte)
    )