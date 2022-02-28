"""

"""
import unittest

class TestMethods(unittest.TestCase):
    """
    add custom assertion methods here

    expected structure is
    def <assertion method name>(object1, object2, ... **kwargs):
        do stuff
    """


    def __init__(self, methodName="runTest"):

        super(TestMethods, self).__init__(methodName=methodName)

    def NULL(self, *args, **kwargs):

        setattr(self, '__null__', True)