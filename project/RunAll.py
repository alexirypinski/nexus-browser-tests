import unittest
import tests
import tests.RunTests
import tests.ProjectTests

def all_suite():
    suite = unittest.TestSuite()
    suite.addTest(tests.RunCreationTestCase("test_run_creation"))
    suite.addTest(tests.ProjectCreationTestCase("test_project_creation"))


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(all_suite())
