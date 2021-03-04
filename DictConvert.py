import unittest


class DictConvert:
    """ this class is handling and converting the dict. """
    def __init__(self):
        self.l: list = []

    def set_list(self, input_list) -> None:
        """
        set up the value of list for testing.
        :param input_list:
        :return:
        """
        self.l = input_list

    def parse_dict(self, d: dict) -> list:
        """
        parse the dict to list.
        :param d:
        :return:
        """
        if isinstance(d, dict):
            for k, v in d.items():
                self.l.append(k)
                self.parse_dict(v)
        else:
            self.l.append(d)
        return self.l

    def gen_reversed_dict(self) -> dict:
        """
        reverse the list and generate the dict.
        :return:
        """
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
        """
        the whole process from input_value to output_value.
        :param kwargs:
        :return:
        """
        self.parse_dict(kwargs)
        res = self.gen_reversed_dict()
        return res


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
    print(f'final result: {final_result}')

