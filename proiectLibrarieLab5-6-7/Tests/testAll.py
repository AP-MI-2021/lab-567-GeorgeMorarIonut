from Tests.testCRUD import testAdaugaCarte, testStergeCarte, testModificaCarte
from Tests.testDomain import testCarte
from Tests.testFunctionalitati import testReducereClient, testModificareGenDupaTitluDat


def runAllTests():
    testCarte()
    testAdaugaCarte()
    testStergeCarte()
    testReducereClient()
    testModificareGenDupaTitluDat()
    testModificaCarte()
