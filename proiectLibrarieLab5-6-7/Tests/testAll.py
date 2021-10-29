from Tests.testCRUD import testAdaugaCarte, testStergeCarte, testModificaCarte
from Tests.testDomain import testCarte
from Tests.testFunctionalitati import testReducereClient, testModificareGenDupaTitluDat, testPretMinimPerGen, \
    testOrdonareDupaPret, testTitluriDistinctePerGen


def runAllTests():
    testCarte()
    testAdaugaCarte()
    testStergeCarte()
    testReducereClient()
    testModificareGenDupaTitluDat()
    testModificaCarte()
    testPretMinimPerGen()
    testOrdonareDupaPret()
    testTitluriDistinctePerGen()
