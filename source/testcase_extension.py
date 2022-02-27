from testmethods_extension import TestMethods

class TestCaseExtension(TestMethods):
    """

    """

    def __init__(self, test_objects=[], use_method=None, test_name=None, **kwargs):
        self.test_name = test_name
        self.test_objects = test_objects
        self.use_method=use_method
        self.kwargs=kwargs

        self.method_returned = None

        #initialise unittest.TestCase
        super(TestCaseExtension, self).__init__(methodName="extension_RunTest")

    def extension_RunTest(self):

        method = getattr(self, self.use_method, "NA")

        if method == "NA":
            msg = "{0} is not a method defined in TestMethods or unittest.TestCase"
            raise UserWarning(msg)

        try:

            self.method_returned = method(*self.test_objects, **self.kwargs)

        except AssertionError as exc:
            #test has failed
            return self.fail(exc)

        except:
            #test has errored
            raise
        else:

            return self.method_returned