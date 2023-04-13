import unittest
import numpy as np
from src.simulated_daq import SimulatedDAQ

class TestSimulatedDAQ(unittest.TestCase):
    def test_simulated_daq(self):
        # Create a SimulatedDAQ instance with sample rate of 100 Hz and 2 channels
        daq = SimulatedDAQ(100, 2)

        # Perform a measurement for 0.1 seconds and check the data
        data = daq.perform_measurement('voltage', duration=0.1)
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 10)
        self.assertEqual(len(data[1]), 10)

        # Check if the generated data has the correct shape and type
        data_array = np.array(data)
        self.assertEqual(data_array.shape, (2, 10))
        self.assertEqual(data_array.dtype, float)

# This block of code is necessary for running the tests when the script is executed
if __name__ == '__main__':
    unittest.main()
