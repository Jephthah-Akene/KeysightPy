import unittest
import os
import numpy as np
from src.utils import save_data_to_file, load_data_from_file, moving_average

class TestUtils(unittest.TestCase):
    def test_save_and_load_data(self):
        # Define test data and a test file name
        test_data = [1.0, 2.0, 3.0, 4.0, 5.0]
        test_file = 'test_data.txt'
        
        # Save the test data to a file and then load it back
        save_data_to_file(test_data, test_file)
        loaded_data = load_data_from_file(test_file)
        
        # Remove the test file after loading the data
        os.remove(test_file)

        # Check if the loaded data is equal to the original test data
        self.assertEqual(test_data, loaded_data)

    def test_moving_average(self):
        # Define test data and the expected result after applying a moving average filter
        test_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        expected_result = np.array([1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 8.5])

        # Apply the moving average filter to the test data
        result = moving_average(test_data, 2)
        
        # Check if the result is equal to the expected result
        np.testing.assert_array_equal(result, expected_result)

        # Test if the moving_average function raises a ValueError for a negative window size
        with self.assertRaises(ValueError):
            moving_average(test_data, -1)

# This block of code is necessary for running the tests when the script is executed
if __name__ == '__main__':
    unittest.main()
