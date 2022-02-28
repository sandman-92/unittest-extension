from source.testmethods_extension import TestMethods

class TestCaseExtension(TestMethods):
    """
    This class can dynamically create a TestCase using kwargs:
      - test_objects: expects a list of arguments to pass to the method
      - use_method: expects a string with the assertion method to use; eg assertEqual, customAssertion ect.
      - test_name: name of this test case
      - **kwargs: any other kwargs get passed to the test method
    """

    def __init__(self, test_objects=[], use_method=None, test_name=None, **kwargs):
        self.test_name = test_name
        self.test_objects = test_objects
        self.use_method = use_method
        self.kwargs = kwargs

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