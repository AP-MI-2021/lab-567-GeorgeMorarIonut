from Domain.carte import getId, getTitlu, getGen, getPret, getReducere
from Logic.CRUD import adaugaCarte, getById, stergeCarte


def testAdaugaCarte():
    lista = []
    lista = adaugaCarte("1", "Messi", "sport", 10, "silver", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getTitlu(getById("1", lista)) == "Messi"
    assert getGen(getById("1", lista)) == "sport"
    assert getPret(getById("1", lista)) == 10
    assert getReducere(getById("1", lista)) == "silver"


def testStergeCarte():
    lista = []
    lista = adaugaCarte("1", "Messi", "sport", 10, "silver", lista)
    lista = adaugaCarte("2", "Retete", "mancare", 25, "gold", lista)

    lista = stergeCarte("1", lista)
    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    lista = stergeCarte("3", lista)
    assert len(lista) == 1
    assert getById("2", lista) is not None

