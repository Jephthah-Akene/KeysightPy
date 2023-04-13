import os
import time
from src.keysight_daq import KeysightDevice
from src.utils import save_data_to_file, moving_average

def main(self):
    # Define the resource name for the DAQ device
    resource_name = 'TCPIP0::192.168.0.100::inst0::INSTR'  # Replace with the appropriate resource name for your device

    # Create an instance of the KeysightDevice class and connect to the device
    daq = KeysightDevice(resource_name)
    daq.connect()

    # Configure the device for continuous data acquisition and set the acquisition time
    daq.configure_measurement("continuous")
    acquisition_time = 5  # seconds

    # Acquire data continuously for the specified acquisition time
    data = []
    start_time = time.time()
    while time.time() - start_time < acquisition_time:
        data.append(daq.perform_measurement("continuous"))

    # Disconnect from the device
    daq.disconnect()

    # Smooth the acquired data using a moving average filter
    smoothed_data = moving_average(data, 10)

    # Save the smoothed data to a file
    file_name = 'test_data.txt'
    save_data_to_file(smoothed_data, file_name)

    # Check if the file exists and remove it after the test
    self.assertTrue(os.path.isfile(file_name))
    os.remove(file_name)

if __name__ == '__main__':
    main()
