from Tests.testCRUD import testAdaugaCarte, testStergeCarte, testModificaCarte
from Tests.testDomain import testCarte
from Tests.testFunctionalitati import testReducereClient, testModificareGenDupaTitluDat, testPretMinimPerGen, \
    testOrdonareDupaPret, testTitluriDistinctePerGen
from Tests.testeUndoRedo import testUndoRedo


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
    testUndoRedo()
