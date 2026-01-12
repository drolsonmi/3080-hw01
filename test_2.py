# Evaulate the performance of problem_2.py
import unittest
from unittest.mock import patch
import io
import sys
import problem_2

class TestGreenhouseMonitor(unittest.TestCase):

    @patch('builtins.input', side_effect=['35', '20', '5', '20'])
    def test_temperature_logic(self, mock_input):
        """Test with high, stable, and low temperatures"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        problem_2.monitor_greenhouse()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().upper() # Case insensitive check
        
        # Check warnings
        self.assertIn("CRITICAL HEAT", output)
        self.assertIn("CRITICAL COLD", output)
        self.assertIn("STABLE", output)
        
        # Check Average: (35 + 20 + 5 + 20) / 4 = 20.0
        self.assertIn("20.0", output)

if __name__ == '__main__':
    unittest.main()
