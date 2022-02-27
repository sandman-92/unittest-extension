import unittest

class TestResultExtension(unittest.TestResult):
    """
    This class extends the unittest results class such that it now saves successful test cases.
    The null test has also been added, for scenarios where it is useful to see the testcase but not perform any pass/fail
    methods on them.
    """

    def __init__(self, stream=None, descriptions=None, verbosity=None):

        self.successes = []
        self.nulls = []
        super(TestResultExtension, self).__init__(stream=stream,
                                descriptions=descriptions, verbosity=verbosity)
    def addSuccess(self, test, *args):

        if hasattr(test, '__null__'):
            #test is a null test
            self.addNull((test, *args))
        else:
            self.successes.append((test, *args))

    def addNull(self, test, *args):

        self.nulls.append((test, *args))