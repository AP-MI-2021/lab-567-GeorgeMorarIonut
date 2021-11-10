from Domain.carte import toString, getId, getTitlu, getGen, getPret, getReducere
from Logic.CRUD import adaugaCarte, stergeCarte, modificaCarte, getById
from Logic.functionalitati import reducereClient, modificareGenDupaTitluDat, pretMinimPerGen, ordonareDupaPret, \
    titluriDistinctePerGen


def printMenu():
    print("1. Adauga carte")
    print("2. Sterge carte")
    print("3. Modifica carte")
    print("4. Reducere pret carte in functie de reducerea de client")
    print("5. Modifica genul cartii daca are un titlu dat")
    print("6. Determina pretul minim pentru fiecare gen")
    print("7. Ordoneaza crescator cartile in functie de pret")
    print("8. Afiseaza numarul de titluri distincte pentru fiecare gen")
    print("u. Undo")
    print("r. Redo")
    print("a. Afiseaza carti")
    print("x. Iesire")


def uiAdaugaCarte(lista, undoOperations, redoOperations):
    try:
        id = input("Dati id: ")
        titlu = input("Dati titlu: ")
        gen = input("Dati gen: ")
        pret = float(input("Dati pretul: "))
        reducere = input("Dati reducere: ")

        rezultat = adaugaCarte(id, titlu, gen, pret, reducere, lista)
        undoOperations.append([
            lambda: stergeCarte(id, rezultat),
            lambda: adaugaCarte(id, titlu, gen, pret, reducere, lista)
            ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def uiStergeCarte(lista, undoOperations, redoOperations):
    try:
        id = input("Dati id-ul cartii care va fi stearsa: ")

        rezultat = stergeCarte(id, lista)
        prajituraSters = getById(id, lista)
        undoOperations.append([
            lambda: adaugaCarte(
            getId(prajituraSters),
            getTitlu(prajituraSters),
            getGen(prajituraSters),
            getPret(prajituraSters),
            getReducere(prajituraSters),
            rezultat
            ),
            lambda: stergeCarte(id, lista)])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print(ve, "Eroare: Id-ul nu exista!")
        return lista


def uiModificaCarte(lista, undoOperations, redoOperations):
    try:
        id = input("Dati id-ul cartii de modificat: ")
        titlu = input("Dati noul titlu al cartii: ")
        gen = input("Dati noul gen al cartii: ")
        pret = float(input("Dati noul pret al cartii: "))
        reducere = input("Dati noua reducere a cartii: ")

        rezultat = modificaCarte(id, titlu, gen, pret, reducere, lista)
        prajituraInainteDeMod = getById(id, lista)
        undoOperations.append([lambda: modificaCarte(
            getId(prajituraInainteDeMod),
            getTitlu(prajituraInainteDeMod),
            getGen(prajituraInainteDeMod),
            getPret(prajituraInainteDeMod),
            getReducere(prajituraInainteDeMod),
            rezultat
        ),
                               lambda: modificaCarte(id, titlu, gen, pret, reducere, lista)])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def returnList(lista):
    return lista


def uiReducereClient(lista, undoOperations, redoOperations):
    rezultat = reducereClient(lista)
    undoOperations.append([
        lambda: returnList(lista),
        lambda: reducereClient(lista)
    ])
    redoOperations.clear()
    return rezultat


def uiModificaDupaPret(lista, undoOperations, redoOperations):
    titlulDat = input("Titlul dat: ")
    genulNou = input("Dati genul nou pe care vreti sa-l aiba cartea: ")

    rezultat = modificareGenDupaTitluDat(titlulDat, genulNou, lista)
    undoOperations.append([
        lambda: returnList(lista),
        lambda: modificareGenDupaTitluDat(titlulDat, genulNou, lista)
    ])
    redoOperations.clear()
    return rezultat


def uiDeterminaPretMinimPerGen(lista):
    rezultat = pretMinimPerGen(lista)
    for gen in rezultat:
        print(f'Pretul minim pentru genul {gen} este {rezultat[gen]}')


def uiOrdonareDupaPret(lista):
    rezultat = ordonareDupaPret(lista)
    for carte in rezultat:
        print(toString(carte))


def uiTitluriDistinctePerGen(lista):
    rezultat = titluriDistinctePerGen(lista)
    for gen in rezultat:
        print(f'Numarul de titluri distincte din genul {gen} este {rezultat[gen]}')


def runMenu(lista):
    undoOperations = []
    redoOperations = []

    while True:
        printMenu()
        optiune = input("Dati optiune: ")

        if optiune == "1":
            lista = uiAdaugaCarte(lista, undoOperations, redoOperations)
        elif optiune == "2":
            lista = uiStergeCarte(lista, undoOperations, redoOperations)
        elif optiune == "3":
            lista = uiModificaCarte(lista, undoOperations, redoOperations)
        elif optiune == "4":
            lista = uiReducereClient(lista, undoOperations, redoOperations)
        elif optiune == "5":
            lista = uiModificaDupaPret(lista, undoOperations, redoOperations)
        elif optiune == "6":
            uiDeterminaPretMinimPerGen(lista)
        elif optiune == "7":
            uiOrdonareDupaPret(lista)
        elif optiune == "8":
            uiTitluriDistinctePerGen(lista)
        elif optiune == "u":
            if len(undoOperations) > 0:
                operations = undoOperations.pop()
                redoOperations.append(operations)
                lista = operations[0]()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoOperations) > 0:
                operations = redoOperations.pop()
                undoOperations.append(operations)
                lista = operations[1]()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Selectati alta optiune!")
