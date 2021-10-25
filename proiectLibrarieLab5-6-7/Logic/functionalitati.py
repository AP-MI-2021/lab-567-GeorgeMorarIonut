from Domain.carte import getReducere, creeazaVanzareCarte, getId, getTitlu, getGen, getPret


def reducereClient(lista):
    """
    Reduce pretul unei carti in functie de reducerea pe care o are.
    :param reducere: string
    :param lista:  o lista de carti
    :return: cartea dupa ce a fost modificat pretul in functie de reducere
    """
    listaNoua = []
    for carte in lista:
        if getReducere(carte) == "silver":
            carteNoua = creeazaVanzareCarte(
                getId(carte),
                getTitlu(carte),
                getGen(carte),
                getPret(carte) - (0.05 * getPret(carte)),
                getReducere(carte)
            )
            listaNoua.append(carteNoua)
        elif getReducere(carte) == "gold":
            carteNoua = creeazaVanzareCarte(
                getId(carte),
                getTitlu(carte),
                getGen(carte),
                getPret(carte) - (0.1 * getPret(carte)),
                getReducere(carte)
            )
            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua


def modificareGenDupaTitluDat(titluDat, genulNou, lista):
    """
    Modificarea genului unei carti daca titlu cartii este acelasi cu un titlu dat.
    :param titluDat: string
    :param lista: o lista de carti
    :return:
    """
    listaNoua = []
    for carte in lista:
        if getTitlu(carte) == titluDat:
            carteNoua = creeazaVanzareCarte(
                getId(carte),
                getTitlu(carte),
                getGen(carte).replace(getGen(carte), genulNou),
                getPret(carte),
                getReducere(carte)
            )
            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua