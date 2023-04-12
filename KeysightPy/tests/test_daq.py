### This file should contain test functions for the data acquisition functionality implemented in src/keysight_daq.py.
# You can use a testing framework like pytest or unittest to write and run your tests.

import pytest
from src.keysight_daq import KeysightDevice

def test_connection():
    resource_name = 'TCPIP0::192.168.0.100::inst0::INSTR'  # Replace with the appropriate resource name for your device
    daq = KeysightDevice(resource_name)
    daq.connect()

    # Test that the device is connected
    assert daq.device is not None

    # Disconnect the device
    daq.disconnect()

# Add more test functions to test other aspects of the data acquisition functionality.
