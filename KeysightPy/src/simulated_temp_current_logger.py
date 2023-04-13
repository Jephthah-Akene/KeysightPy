import simpy
import numpy as np
from KeysightPy.src.simulated_daq import SimulatedDAQ


class SimulatedTempCurrentLogger:
    def __init__(self, sample_rate, num_channels=3):
        # Initialize the simulated temperature and current logger with the specified sample rate and number of channels
        self.sample_rate = sample_rate
        self.num_channels = num_channels
        self.daq = SimulatedDAQ(sample_rate, num_channels)
        self.env = self.daq.env
        self.current_time = 0

    def start_logging(self, duration=10):
        # Import the SimulatedDAQ class here, to avoid circular imports
        from KeysightPy.src.simulated_daq_core import SimulatedDAQ

        # Perform temperature and current measurements for the specified duration
        temperature_data = self.daq.perform_measurement('temperature', duration=duration)
        current_data = self.daq.perform_measurement('current', duration=duration)
        print(f"Temperature data: {temperature_data}")
        print(f"Current data: {current_data}")

    def stop_logging(self):
        try:
            for p in self.env.active_process.values():
                p.interrupt()
        except AttributeError:
            print("No active processes in the environment.")

    def generate_data(self):
        while True:
            # Simulate temperature measurement by adding random noise to a constant value
            temperature = 25 + np.random.normal(scale=0.1)

            # Simulate current measurement by generating random data
            current = np.random.normal(loc=0.5, scale=0.1, size=10)

            # Simulate resistance measurement by adding random noise to a constant value
            resistance = 100 + np.random.normal(scale=1.0)

            # Write the data to the simulated DAQ
            data = [temperature, resistance] + list(current)
            self.daq.write(data, self.current_time)

            # Increment the time
            self.current_time += 1.0 / self.sample_rate

            # Wait for the next data point
            yield self.env.timeout(1.0 / self.sample_rate)

    def get_latest_data(self):
        # Get the latest temperature, resistance, and current data from the simulated DAQ
        temperature = self.daq.data[0][-1]
        resistance = self.daq.data[1][-1]
        current = self.daq.data[2][-1]
        return temperature, resistance, current
