# Evaulate the performance of problem_3.py
# test_5.py
import unittest
from unittest.mock import patch
import io
import sys
import problem_3

class TestPostAnalyst(unittest.TestCase):

    @patch('builtins.input', side_effect=['Python coding is better than a flight'])
    def test_keyword_logic(self, mock_input):
        """Test if keywords are correctly categorized into the dictionary"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        problem_3.analyze_post()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        # Expected: tech: 2 (python, coding), travel: 1 (flight), health: 0
        # We look for the dictionary string in the output
        self.assertIn("'tech': 2", output)
        self.assertIn("'travel': 1", output)
        self.assertIn("'health': 0", output)

    @patch('builtins.input', side_effect=['GYM GYM python'])
    def test_case_insensitivity(self, mock_input):
        """Test if the program handles uppercase versions of keywords"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        problem_3.analyze_post()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        # Expected: health: 2 (gym, gym), tech: 1 (python)
        self.assertIn("'health': 2", output)
        self.assertIn("'tech': 1", output)

if __name__ == '__main__':
    unittest.main()
