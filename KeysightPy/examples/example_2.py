import os
import time
from src.keysight_daq import KeysightDevice
from src.utils import save_data_to_file

# Replace with the appropriate resource name for your device
resource_name = 'TCPIP0::192.168.0.100::inst0::INSTR'

# Initialize the KeysightDevice instance
daq = KeysightDevice(resource_name)
daq.connect()

# TODO: Configure your DAQ device for continuous data acquisition
# Consult your device's documentation for the appropriate command set and functionality

# Acquire data from the DAQ device continuously for a specified duration
duration = 10  # in seconds
start_time = time.time()
data = []

while time.time() - start_time < duration:
    # Replace this with the actual data acquisition function from your DAQ device
    current_data = []  # Acquire data
    data.extend(current_data)
    time.sleep(1)  # Adjust the sleep duration according to the desired data acquisition rate

# Save the acquired data to a file
save_data_to_file(data, os.path.join('data', 'continuous_data.txt'))

# Disconnect the DAQ device
daq.disconnect()

print("Continuous data acquisition completed and data saved to 'data/continuous_data.txt'")

