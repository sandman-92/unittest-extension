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


    def test_assertequal(self):

        test_run = TestCaseExtension(test_objects=[1,1], use_method='assertEqual')
        result = TestResultExtension()

        test_run.run(result)

        self.assertEqual(1, len(result.successes))

    def test_failure(self):

        test_run = TestCaseExtension(test_objects=[1,0], use_method='assertEqual')
        result = TestResultExtension()

        test_run.run(result)

        self.assertEqual(1, len(result.failures))

    def test_result_print(self):

        instructions = [
            {"test_objects":[1,1], "use_method":'assertEqual'},
            {"use_method":'NULL'},
        ]
        result = TestResultExtension()
        for instruction in instructions:

            test = TestCaseExtension(**instruction)
            test.run(result)

        res = result.__str__()
        expected_result = ("\n"
                           "number of successes: 1\n"
                           "number of failures: 0\n"
                           "number of errors: 0\n"
                           "number of nulls: 1\n"
                           "number of skipped: 0\n"
                           "number of expectedFailures: 0\n"
                           "number of unexpectedSuccesses: 0\n")

        self.assertEqual(res, expected_result)

    def test_result_error(self):

        test = TestCaseExtension(test_objects=[], use_method='assertEqual')
        result = TestResultExtension()

        test.run(result)
        expected_result = ("\n"
                           "number of successes: 0\n"
                           "number of failures: 0\n"
                           "number of errors: 1\n"
                           "number of nulls: 0\n"
                           "number of skipped: 0\n"
                           "number of expectedFailures: 0\n"
                           "number of unexpectedSuccesses: 0\n")
        self.assertEqual(expected_result, result.__str__())

    def test_no_method_warning(self):
        """
        this tests a user warning is raised if no method is provided
        :return:
        """
        test = TestCaseExtension(test_objects=[1,1])
        result = TestResultExtension()
        test.run(result)

        warning = result.errors[0][1]
        self.assertIn('UserWarning', warning)

    def test_too_many_kwargs(self):
        """

        :return:
        """

        test = TestCaseExtension(test_objects=[1,1], use_method='assertEqual', useless_kwarg='nothing', msg='this should go in')
        result = TestResultExtension()
        test.run(result)

        self.assertEqual(1, len(result.successes))
        ### run this pipeline
