import os
from src.keysight_daq import KeysightDevice
from src.utils import save_data_to_file

# Replace with the appropriate resource name for your device
resource_name = 'TCPIP0::192.168.0.100::inst0::INSTR'

# Initialize the KeysightDevice instance
daq = KeysightDevice(resource_name)
daq.connect()

# TODO: Configure your DAQ device for single-point data acquisition
# Consult your device's documentation for the appropriate command set and functionality

# Acquire data from the DAQ device
data = []  # Replace this with the actual data acquisition function from your DAQ device

# Save the acquired data to a file
save_data_to_file(data, os.path.join('data', 'single_point_data.txt'))

# Disconnect the DAQ device
daq.disconnect()

print("Single-point data acquisition completed and data saved to 'data/single_point_data.txt'")

