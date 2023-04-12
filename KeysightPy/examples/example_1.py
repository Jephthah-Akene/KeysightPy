<<<<<<< HEAD
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


=======
### These files should contain example scripts demonstrating how to use the project for specific tasks or with different
# types of Keysight DAQ devices. The examples should be well-commented to help users understand how to modify them for 
# their own needs.
>>>>>>> 92976d4be0337bb4c4a27b9b3aabfd6cfd4e94be
