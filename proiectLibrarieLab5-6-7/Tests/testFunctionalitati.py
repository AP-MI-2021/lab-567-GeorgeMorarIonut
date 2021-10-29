from Domain.carte import getPret, getGen, getId
from Logic.CRUD import adaugaCarte, getById
from Logic.functionalitati import reducereClient, modificareGenDupaTitluDat, pretMinimPerGen, ordonareDupaPret, \
    titluriDistinctePerGen


def testReducereClient():
    lista = []
    lista = adaugaCarte("1", "Jamie Oliver", "food", 100, "silver", lista)
    lista = adaugaCarte("2", "Atomic Habits", "self development", 100,  "none", lista)
    lista = reducereClient(lista)

    assert len(lista) == 2
    assert getPret(getById("1", lista)) == 95
    assert getPret(getById("2", lista)) == 100


def testModificareGenDupaTitluDat():
    lista = []
    lista = adaugaCarte("1", "De la idee la bani", "dezvoltare personala", 150, "gold", lista)
    lista = adaugaCarte("2", "Harry Potter", "SF", 70, "silver", lista)
    lista = modificareGenDupaTitluDat("De la idee la bani", "business", lista)

    assert len(lista) == 2
    assert getGen(getById("1", lista)) == "business"
    assert getGen(getById("2", lista)) == "SF"


def testPretMinimPerGen():
    lista = []

    lista = adaugaCarte("1", "Ford vs Ferrari", "sport", 150, "silver", lista)
    lista = adaugaCarte("2", "Secretele lui DaVinci", "istorie", 26, "none", lista)
    lista = adaugaCarte("3", "The Mamba Mentality", "sport", 230, "gold", lista)

    rezultat = pretMinimPerGen(lista)
    assert rezultat["sport"] == 150
    assert rezultat["istorie"] == 26


def testOrdonareDupaPret():
    lista = []

    lista = adaugaCarte("1", "Ford vs Ferrari", "sport", 150, "silver", lista)
    lista = adaugaCarte("2", "Secretele lui DaVinci", "istorie", 26, "none", lista)
    lista = adaugaCarte("3", "The Mamba Mentality", "sport", 230, "gold", lista)

    lista = ordonareDupaPret(lista)

    assert len(lista) == 3
    assert getId(lista[0]) == "2"
    assert getId(lista[1]) == "1"
    assert getId(lista[2]) == "3"


def testTitluriDistinctePerGen():
    lista = []

    lista = adaugaCarte("1", "Ford vs Ferrari", "sport", 150, "silver", lista)
    lista = adaugaCarte("2", "Secretele lui DaVinci", "istorie", 26, "none", lista)
    lista = adaugaCarte("3", "The Mamba Mentality", "sport", 230, "gold", lista)

    rezultat = titluriDistinctePerGen(lista)

    assert rezultat["sport"] == 2
    assert rezultat["istorie"] == 1
