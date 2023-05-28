# pyling
# pyflakes
# Auto PEP8
import unittest
import main


class TestMain(unittest.TestCase):
    '''Testing Exercise'''
    def test_input(self):
        answer=5
        guess=5
        result=main.run_guess(answer,guess)
        self.assertTrue(result)
    def test_input_wrong_guess(self):
        result=main.run_guess(5,0)
        self.assertFalse(result)

    def test_input_contions(self):
        result = main.run_guess(5, 12)
        self.assertFalse(result)

    '''testing theory'''
    # def setUp(self):
    #     print('about to test a function')
    # def test_do(self):
    #     '''result test'''
    #     test_param = 10
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 15)
    #
    # def test_do2(self):
    #     test_param = 'adfasda'
    #     result = main.do_stuff(test_param)
    #     self.assertIsInstance(result, ValueError)
    #
    # def test_do3(self):
    #     test_param = None
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 'please enter number')
    #
    # def test_do4(self):
    #     test_param = ''
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 'please enter number')
    #
    # def test_do5(self):
    #     test_param = 0
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
