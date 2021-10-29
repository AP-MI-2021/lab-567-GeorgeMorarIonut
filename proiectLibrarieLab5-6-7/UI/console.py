from Domain.carte import toString
from Logic.CRUD import adaugaCarte, stergeCarte, modificaCarte
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
    print("a. Afiseaza carti")
    print("x. Iesire")


def uiAdaugaCarte(lista):
    try:
        id = input("Dati id: ")
        titlu = input("Dati titlu: ")
        gen = input("Dati gen: ")
        pret = float(input("Dati pretul: "))
        reducere = input("Dati reducere: ")

        return adaugaCarte(id, titlu, gen, pret, reducere, lista)
    except ValueError as ve:
        print(f'Error: {ve}')
        return lista


def uiStergeCarte(lista):
    try:
        id = input("Dati id-ul cartii care va fi stearsa: ")

        return stergeCarte(id, lista)
    except ValueError as ve:
        print("Eroare: Id-ul nu exista!")
        return lista


def uiModificaCarte(lista):
    try:
        id = input("Dati id-ul cartii de modificat: ")
        titlu = input("Dati noul titlu al cartii: ")
        gen = input("Dati noul gen al cartii: ")
        pret = float(input("Dati noul pret al cartii: "))
        reducere = input("Dati noua reducere a cartii: ")

        return modificaCarte(id, titlu, gen, pret, reducere, lista)
    except ValueError as ve:
        print(f'Error: {ve}')


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def uiReducereClient(lista):
    return reducereClient(lista)


def uiModificaDupaPret(lista):
    titlulDat = input("Titlul dat: ")
    genulNou = input("Dati genul nou pe care vreti sa-l aiba cartea: ")

    return modificareGenDupaTitluDat(titlulDat, genulNou, lista)


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
    while True:
        printMenu()
        optiune = input("Dati optiune: ")

        if optiune == "1":
            lista = uiAdaugaCarte(lista)
        elif optiune == "2":
            lista = uiStergeCarte(lista)
        elif optiune == "3":
            lista = uiModificaCarte(lista)
        elif optiune == "4":
            lista = uiReducereClient(lista)
        elif optiune == "5":
            lista = uiModificaDupaPret(lista)
        elif optiune == "6":
            uiDeterminaPretMinimPerGen(lista)
        elif optiune == "7":
            uiOrdonareDupaPret(lista)
        elif optiune == "8":
            uiTitluriDistinctePerGen(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Selectati alta optiune!")
