from Tests.testAll import runAllTests
from UI.console import runMenu
from UI.console2 import runMenu2


def main():

    runAllTests()
    while True:
        option = input("Selectati meniul pe care vreti sa-l utilizati (1 (Client menu) sau 2 (Command line menu)) sau stop pentru a inchide meniul: ")
        if option == "1":
            runMenu([])
        elif option == "2":
            runMenu2([])
        elif option == "stop":
            break

if __name__ == '__main__':
    main()