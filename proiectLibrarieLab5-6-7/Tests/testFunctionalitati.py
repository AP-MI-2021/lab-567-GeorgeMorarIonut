from Domain.carte import getPret, getGen
from Logic.CRUD import adaugaCarte, getById
from Logic.functionalitati import reducereClient, modificareGenDupaTitluDat


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

