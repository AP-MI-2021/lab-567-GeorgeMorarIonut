from Domain.carte import toString
from Logic.CRUD import adaugaCarte, stergeCarte, modificaCarte
from Logic.functionalitati import reducereClient, modificareGenDupaTitluDat


def printMenu():
    print("1. Adauga carte")
    print("2. Sterge carte")
    print("3. Modifica carte")
    print("4. Reducere pret carte in functie de reducerea de client")
    print("5. Modifica genul cartii daca are un titlu dat")
    print("a. Afiseaza carti")
    print("x. Iesire")


def uiAdaugaCarte(lista):
    id = input("Dati id: ")
    titlu = input("Dati titlu: ")
    gen = input("Dati gen: ")
    pret = float(input("Dati pretul: "))
    reducere = input("Dati reducere: ")

    return adaugaCarte(id, titlu, gen, pret, reducere, lista)


def uiStergeCarte(lista):
    id = input("Dati id-ul cartii care va fi stearsa: ")

    return stergeCarte(id, lista)


def uiModificaCarte(lista):
    id = input("Dati id-ul cartii de modificat: ")
    titlu = input("Dati noul titlu al cartii: ")
    gen = input("Dati noul gen al cartii: ")
    pret = float(input("Dati noul pret al cartii: "))
    reducere = input("Dati noua reducere a cartii: ")

    return modificaCarte(id, titlu, gen, pret, reducere, lista)


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def uiReducereClient(lista):
    return reducereClient(lista)


def uiModificaDupaPret(lista):
    titlulDat = input("Titlul dat: ")
    genulNou = input("Dati genul nou pe care vreti sa-l aiba cartea: ")

    return modificareGenDupaTitluDat(titlulDat, genulNou, lista)


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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Selectati alta optiune!")
