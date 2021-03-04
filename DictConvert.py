import unittest


class DictConvert:
    """ this class is handling and converting the dict. """
    def __init__(self):
        self.l: list = []

    def set_list(self, input_list) -> None:
        """ set up the value of list for testing. """
        self.l = input_list

    def parse_dict(self, d: dict) -> list:
        if isinstance(d, dict):
            for k, v in d.items():
                self.l.append(k)
                self.parse_dict(v)
        else:
            self.l.append(d[0])
        return self.l

    def gen_reversed_dict(self) -> dict:
        """ revserse the list and generate the dict. """
        d: dict = {}
        try:
            n = len(self.l)
            for i in range(n):
                if i == 0:
                    d[self.l[i+1]] = self.l[i]
                elif i < n-1:
                    temp = {}
                    temp[self.l[i+1]] = d
                    d = temp
        except Exception as e:
            raise e
        return d

    def whole_process(self, **kwargs) -> dict:
        self.parse_dict(kwargs)
        res = self.gen_reversed_dict()
        return res


class DictConvertTest(unittest.TestCase):
    """ unit test for the class of DictConvert. """
    def test_parse_dict(self):
        input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}
        l = []
        dc = DictConvert()

        self.assertEqual(
            dc.parse_dict(input_value), 
            ['hired', 'be', 'to', 'deserve', 'I']) # successful.

        self.assertEqual(
            dc.parse_dict(input_value), 
            ['be', 'to', 'deserve', 'I']) # error.
    
    def test_gen_reversed_dict(self):
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
        input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}
        l = []
        dc = DictConvert()

        self.assertEqual(
            dc.whole_process(**input_value),
            {'I': {'deserve': {'to': {'be': 'hired'}}}}) # successful.


if __name__ == '__main__':

    # Input:
    input_value = {
        'hired': {
            'be': {
                'to': {
                    'deserve': 'I'
                }
            }
        }
    }

    # # Output:
    # output_value = {
    #   'I': {
    #     'deserve': {
    #       'to': {
    #          'be': 'hired'
    #       }
    #     }
    #   }
    # }

    # for quiz.
    dc = DictConvert()
    final_result = dc.whole_process(**input_value)
    print('final res', final_result)

    # for testing.
    # run 3 tests, including 4 successful cases and 2 error cases. 
    unittest.main()
