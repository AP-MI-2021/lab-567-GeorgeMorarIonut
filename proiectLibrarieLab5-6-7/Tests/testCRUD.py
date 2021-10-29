from Domain.carte import getId, getTitlu, getGen, getPret, getReducere
from Logic.CRUD import adaugaCarte, getById, stergeCarte, modificaCarte


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



def testModificaCarte():
    lista = []
    lista = adaugaCarte("1", "Atomic Habits", "disciplina", 50, "none", lista)
    lista = adaugaCarte("2", "Liderii mananca ultimii", "business", 150, "gold", lista)

    lista = modificaCarte("2", "Liderii mananca ultimii", "self development", 100, "silver", lista)
    lista = modificaCarte("1", "Atomic Habits", "self development", 75, "silver", lista)

    assert len(lista) == 2
    assert getGen(getById("1", lista)) == "self development"
    assert getPret(getById("1", lista)) == 75
    assert getGen(getById("2", lista)) == "self development"
    assert getReducere(getById("2", lista)) == "silver"

