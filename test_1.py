# Evaulate the performance of problem_1.py
import unittest
from unittest.mock import patch
import io
import sys
import problem_1

class TestBillCalculator(unittest.TestCase):

    @patch('builtins.input', side_effect=['25.50', '18'])
    def test_standard_case(self, mock_input):
        """Test with $25.50 and 18% tip"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        problem_1.calculate_bill()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("4.59", output, "Tip amount calculation is incorrect.")
        self.assertIn("30.09", output, "Total bill calculation is incorrect.")

    @patch('builtins.input', side_effect=['100', '20'])
    def test_round_numbers(self, mock_input):
        """Test with $100 and 20% tip"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        problem_1.calculate_bill()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("20.0", output)
        self.assertIn("120.0", output)

if __name__ == '__main__':
    unittest.main()
