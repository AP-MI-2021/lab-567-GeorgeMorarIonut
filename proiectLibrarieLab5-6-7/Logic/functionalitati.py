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


def pretMinimPerGen(lista):
    """
    Determina cartea cu cel mai mic pret din fiecare gen.
    :param lista: o lista de dictionare
    :return: un dictionar
    """
    rezultat = {}
    for carte in lista:
        gen = getGen(carte)
        pret = getPret(carte)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:
            rezultat[gen] = pret
    return rezultat


def ordonareDupaPret(lista):
    """
    Ordoneaza o lista crescator dupa pret.
    :param lista: o lista de dictionare
    :return: o lista de dictionare
    """
    return sorted(lista, key=lambda carte: getPret(carte), reverse=False)


def titluriDistinctePerGen(lista):
    """
    Determina numarul de titluri distincte perntru fiecare gen.
    :param lista: o lista de dictionare
    :return: numarul de titluri distincte pentru fiecare gen
    """
    rezultat1 = {}
    rezultat2 = {}
    for carte in lista:
        gen = getGen(carte)
        titlu = getTitlu(carte)
        if gen in rezultat1:
            if titlu not in rezultat2[gen]:
                rezultat1[gen] += 1
                titluriconcatenate = rezultat2[gen] + titlu
                rezultat2[gen] = titluriconcatenate
        else:
            rezultat1[gen] = 1
            rezultat2[gen] = titlu
    return rezultat1
