from Domain.carte import toString
from Logic.CRUD import adaugaCarte, stergeCarte


def meniuHelp():
    print("In acest program introduceti comanda si id-ul cartii, titlul,"
          " genul, pretul si tipul de reducere (silver/gold/none), separate prin virgula, fara spatii si in ordinea mentionata. \n"
          "Comenzile disponibile sunt: add (pentru a adauga o carte noua in lista), delete (pentru a sterge o carte existenta din lista) \n"
          "si showall (pentru a vedea cartile pe care le-ati adaugat deja in lista.)")


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def runMenu2(lista):
    while True:
        option = input("Va rugam introduceti comanda: ")

        if option == "help":
            meniuHelp()
        else:
            cuvinte = option.split(";")
            if cuvinte[0] == "stop":
                break
            else:
                for elem in cuvinte:
                    command = elem.split(",")
                    if command[0] == "add":
                        try:
                            lista = adaugaCarte(command[1], command[2], command[3], command[4], command[5], lista)
                        except ValueError as ve:
                            print(f'Eroare: {ve}')
                    elif command[0] == "delete":
                        try:
                            lista = stergeCarte(command[1], lista)
                        except ValueError as ve:
                            print(f'Eroare: {ve}')
                    elif command[0] == "showall":
                        showAll(lista)
