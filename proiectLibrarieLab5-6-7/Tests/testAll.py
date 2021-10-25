from Tests.testCRUD import testAdaugaCarte, testStergeCarte
from Tests.testDomain import testCarte


def runAllTests():
    testCarte()
    testAdaugaCarte()
    testStergeCarte()
