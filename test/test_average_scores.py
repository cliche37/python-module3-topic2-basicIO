"""
Created by Syed Rehman on 6-12-2020 for Python CIS 189
Contact via email at smrehman@dmacc.edu
Description: This acts as a mock test for user input for the average() function
"""


import unittest
import unittest.mock as mock
from format_output import average_scores


class FunctionTestCase(unittest.TestCase):
    def test_average(self):

        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert average_scores.average() == 90


"""
if __name__ == '__main__':
    unittest.main()
"""
