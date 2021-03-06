from .testmethods_extension import TestMethods

class TestCaseExtension(TestMethods):
    """
    This class can dynamically create a TestCase using kwargs:
      - test_objects: expects a list of arguments to pass to the method
      - use_method: expects a string with the assertion method to use; eg assertEqual, customAssertion ect.
      - test_name: name of this test case
      - **kwargs: any other kwargs get passed to the test method
    """

    def __init__(self,  test_objects=[],
                        use_method="",
                        test_name=None,
                        unittest_expecting_failure=False,
                        unittest_skip = False,
                        unittest_skip_why = None,
                        **kwargs):

        self.__unittest_expecting_failure__ = unittest_expecting_failure
        self.__unittest_skip__ = unittest_skip
        self.__unittest_skip_why__ = unittest_skip_why
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
            msg = "use_method is empty or '{0}' is not defined in TestMethods or TestCase".format(self.use_method)
            raise UserWarning(msg)

        method_args = method.__code__.co_varnames
        pass_kwargs = {}

        for key, arg in self.kwargs.items():
            if key in method_args:

                # pass kwargs ensures that unittest.TestCase doesnt error when too many kwargs are given
                pass_kwargs[key]=arg

        try:

            self.method_returned = method(*self.test_objects, **pass_kwargs)

        except AssertionError as exc:
            #test has failed
            return self.fail(exc)

        except:
            #test has errored
            raise

        else:

            return self.method_returned

