"""

"""
import unittest


class TestMethods(unittest.TestCase):
    """

    """


    def __init__(self, methodName="runTest"):

        super(TestMethods, self).__init__(methodName=methodName)

    def NULL_test(self, *args, **kwargs):

        setattr(self, '__null__', True)