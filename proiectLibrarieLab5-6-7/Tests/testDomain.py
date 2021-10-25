from Domain.carte import creeazaVanzareCarte, getId, getTitlu, getGen, getPret, getReducere


def testCarte():
    carte = creeazaVanzareCarte("1", "Messi", "sport", 10, "silver")

    assert getId(carte) == "1"
    assert getTitlu(carte) == "Messi"
    assert getGen(carte) == "sport"
    assert getPret(carte) == 10
    assert getReducere(carte) == "silver"