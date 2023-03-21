import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'scripts' directory to the system path
sys.path.append(os.path.join(current_dir, '..'))
import unittest
from unittest import TestCase, mock
import json
from unittest.mock import patch, mock_open
from index import Main
from Database import DB
from io import StringIO


class TestMain(unittest.TestCase): 
    @patch('builtins.input', return_value='3') 
    def test_query_database(self, mock_input):
        # Mock the database object and call the queryDatabase function
        db = DB()
        result = db.queryDatabase('Zach')
        
        # Check that the result is correct
        expected_result = (955, 'Zach', 'Shilling', 'zshillingnf@linkedin.com', '8889573076', 'Yabox', 'Active', 'Green')
        self.assertEqual(result, expected_result)
        if result == expected_result:
            print('Ok!')
            print('Result of the DB query')
            print(f'Result {result}, Expected Result Defined in test {expected_result}')
        
if __name__ == '__main__':
    unittest.main()