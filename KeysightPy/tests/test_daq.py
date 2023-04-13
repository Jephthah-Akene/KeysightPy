import unittest
from src.keysight_daq import KeysightDevice

class TestKeysightDevice(unittest.TestCase):
    def setUp(self):
        # Set up the KeysightDevice instance for testing
        self.daq = KeysightDevice('mock_device')

    def test_configure_measurement(self):
        # Test configuring an example measurement type
        self.daq.connect()
        self.daq.configure_measurement('example_measurement', 10, 'V', 'DC')
        self.assertEqual(self.daq.query('QUERY_FOR_EXAMPLE_MEASUREMENT_SETTINGS'), '10 V DC')
        self.daq.disconnect()

        # Test configuring an unsupported measurement type
        self.daq.connect()
        with self.assertRaises(ValueError):
            self.daq.configure_measurement('unsupported_measurement_type')
        self.daq.disconnect()

# This block of code is necessary for running the tests when the script is executed
if __name__ == '__main__':
    unittest.main()
