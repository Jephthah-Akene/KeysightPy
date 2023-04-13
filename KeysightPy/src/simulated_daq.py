import simpy
import random
from .simulated_daq_core import SimulatedDAQ


class SimulatedTempCurrentLogger:
    def __init__(self, sample_rate, num_channels=3):
        # Initialize the simulated DAQ with the specified sample rate and number of channels
        self.sample_rate = sample_rate
        self.num_channels = num_channels
        self.current_time = 0
        self.data = [[] for _ in range(num_channels)]
        self.env = simpy.Environment()

        # Create a simulated DAQ instance with 3 channels (temperature, current, and resistance)
        self.daq = SimulatedDAQ(sample_rate, num_channels)

        # Start the data generation process
        self.env.process(self.generate_data())

    def start_logging(self):
        # Connect to the DAQ device
        self.daq.connect()

        # Configure the DAQ for temperature, current, and resistance measurements
        self.daq.configure_measurement('temperature')
        self.daq.configure_measurement('current')
        self.daq.configure_measurement('resistance')

        # Start the data generation process
        self.env.run()

        # Disconnect from the DAQ device
        self.daq.disconnect()

    def generate_data(self):
        # Continuously generate data from the DAQ
        while True:
            # Get the latest measurements from the DAQ
            data = self.daq.perform_measurement('temperature', 'current', 'resistance')

            # Add the measurements to the data buffer
            for ch in range(self.num_channels):
                self.data[ch].extend(data[ch])

            # Update the current time
            self.current_time += 1.0 / self.sample_rate

            # Wait for the next sample
            yield self.env.timeout(1.0 / self.sample_rate)
