import unittest
from mygo_quiz.DictConvert import DictConvert


class DictConvertTest(unittest.TestCase):
    """ unit test for the class of DictConvert. """
    def test_parse_dict(self):
        """
        testing for parse_dict.
        :return:
        """
        input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}
        l = []
        dc = DictConvert()

        self.assertEqual(
            dc.parse_dict(input_value),
            ['hired', 'be', 'to', 'deserve', 'I']) # successful.

        self.assertEqual(
            dc.parse_dict(input_value),
            ['to', 'deserve', 'I']) # error.

    def test_gen_reversed_dict(self):
        """
        testing for gen_reversed_dict.
        :return:
        """
        l = ['hired', 'be', 'to', 'deserve', 'I']
        l2 = ['1', '2', '3', '4', '5']

        dc = DictConvert()
        dc.set_list(l)

        dc2 = DictConvert()
        dc2.set_list(l2)

        self.assertEqual(
            dc.gen_reversed_dict(),
            {'I': {'deserve': {'to': {'be': 'hired'}}}}) # successful.

        self.assertEqual(
            dc2.gen_reversed_dict(),
            {'5': {'4': {'3': {'2': '1'}}}}) # successful.

        self.assertEqual(
            dc2.gen_reversed_dict(),
            {'1': {'2': {'3': {'2': '1'}}}}) # error

    def test_whole_process(self):
        """
        testing for whole_process.
        :return:
        """
        input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}
        l = []
        dc = DictConvert()

        self.assertEqual(
            dc.whole_process(**input_value),
            {'I': {'deserve': {'to': {'be': 'hired'}}}}) # successful.


if __name__ == '__main__':
    # for testing.
    # run 3 tests, including 4 successful cases and 2 error cases.
    unittest.main()
