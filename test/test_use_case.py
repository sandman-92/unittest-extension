import unittest

from source.testcase_extension import TestCaseExtension
from source.result_extension import TestResultExtension


class TestUseCase(unittest.TestCase):


    def test_run(self):
        """
        tests the null test works
        :return:
        """

        test_run = TestCaseExtension(use_method='NULL')
        result = TestResultExtension()

        #for test in test_run:
        test_run.run(result)

        if len(result.nulls) == 1: pass
        else: raise AssertionError

    def test_assertequal(self):

        test_run = TestCaseExtension(test_objects=[1,1], use_method='assertEqual')
        result = TestResultExtension()

        test_run.run(result)

        if len(result.successes) == 1:

            pass

        else:

            test, exc = result.errors[0]
            raise AssertionError(exc)

    def test_failure(self):

        test_run = TestCaseExtension(test_objects=[1,0], use_method='assertEqual')
        result = TestResultExtension()

        test_run.run(result)

        if len(result.failures) == 1:
            pass
        else:
            raise AssertionError("this test should have failed")

    def test_result_print(self):

        instructions = [
            {"test_objects":[1,1], "use_method":'assertEqual'},
            {"use_method":'NULL'},
        ]
        result = TestResultExtension()
        for instruction in instructions:

            test = TestCaseExtension(**instruction)
            test.run(result)

        print(result)

if __name__ == "__main__":
    unittest.main()