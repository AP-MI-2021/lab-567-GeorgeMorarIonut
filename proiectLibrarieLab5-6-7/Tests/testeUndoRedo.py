from Domain.carte import getId
from Logic.CRUD import adaugaCarte, stergeCarte, getById


def testUndoRedo():
    lista = []
    undoOperations = []
    redoOperations = []
    operations = []

    # prima adaugare
    lista = adaugaCarte("1", "Jamie Oliver", "food", 100, "silver", lista)
    undoOperations.append([
        lambda: stergeCarte("1", lista),
        lambda: adaugaCarte("1", "Jamie Oliver", "food", 100, "silver", lista)
    ])
    redoOperations.clear()


    # a doua adaugare
    lista = adaugaCarte("2", "Atomic Habits", "self development", 100, "none", lista)
    undoOperations.append([
        lambda: stergeCarte("2", lista),
        lambda: adaugaCarte("2", "Atomic Habits", "self development", 100, "none", lista)
    ])
    redoOperations.clear()


    # a treia adaugare
    lista = adaugaCarte("3", "Robin Hood", "sf", 45, "silver", lista)
    undoOperations.append([
        lambda: stergeCarte("3", lista),
        lambda: adaugaCarte("3", "Robin Hood", "sf", 45, "silver", lista)
    ])
    redoOperations.clear()
    assert len(lista) == 3


    # primul undo
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista)is not None
    assert getById("3", lista) is None


    # al doilea undo
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None


    # al treilea undo
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    assert len(lista) == 0
    assert getById("1", lista) is None

    # al patrulea undo
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    assert len(lista) == 0

    # a patra adaugare
    lista = adaugaCarte("1", "Jamie Oliver", "food", 100, "silver", lista)
    undoOperations.append([
        lambda: stergeCarte("1", lista),
        lambda: adaugaCarte("1", "Jamie Oliver", "food", 100, "silver", lista)
    ])
    redoOperations.clear()

    # a cincea adaugare
    lista = adaugaCarte("2", "Atomic Habits", "self development", 100, "none", lista)
    undoOperations.append([
        lambda: stergeCarte("2", lista),
        lambda: adaugaCarte("2", "Atomic Habits", "self development", 100, "none", lista)
    ])
    redoOperations.clear()

    # a sasea adaugare
    lista = adaugaCarte("3", "Robin Hood", "sf", 45, "silver", lista)
    undoOperations.append([
        lambda: stergeCarte("3", lista),
        lambda: adaugaCarte("3", "Robin Hood", "sf", 45, "silver", lista)
    ])
    redoOperations.clear()
    assert len(lista) == 3

    # primul redo
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        pass
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None


    # al cincelea si al saselea undo
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None


    # al doilea redo
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista)is None

    # al treilea redo
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        pass
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None


    # al saptelea si al optulea undo
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None


    # al patrulea redo
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is None


    # al cincelea redo
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        pass
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None


    # noualea si al zecelea undo
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None


    # a saptea adaugare
    lista = adaugaCarte("4", "Ford vs Ferrari", "masini", 150, "gold", lista)
    undoOperations.append([
        lambda: stergeCarte("4", lista),
        lambda: adaugaCarte("4", "Ford vs Ferrari", "masini", 150, "gold", lista)
    ])
    redoOperations.clear()
    assert len(lista) == 2


    # al saselea redo
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is not None


    # al unsprezecelea undo
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is None

    # al doisprezecelea undo
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        pass
    assert len(lista) == 0
    assert getById("1", lista) is None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is None


    # al saptelea si al optulea redo
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        pass
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is not None

    # al noualea redo
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is not None
