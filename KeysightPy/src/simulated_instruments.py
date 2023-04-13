import simpy
import random

class SimulatedTemperatureLogger:
    def __init__(self, sample_rate, num_channels):
        self.sample_rate = sample_rate
        self.num_channels = num_channels
        self.current_time = 0
        self.data = [[] for _ in range(num_channels)]
        self.env = simpy.Environment()
        self.env.process(self.generate_data())

    def connect(self):
        pass

    def disconnect(self):
        pass

    def configure_measurement(self, measurement_type, *args, **kwargs):
        pass

    def perform_measurement(self, measurement_type, *args, **kwargs):
        # Simulate data acquisition by returning random data
        duration = kwargs.get('duration', 1.0)
        num_samples = int(duration * self.sample_rate)
        for i in range(num_samples):
            for ch in range(self.num_channels):
                self.data[ch].append(random.uniform(18, 22))
        self.current_time += duration
        return [self.data[ch][-num_samples:] for ch in range(self.num_channels)]

    def generate_data(self):
        # Continuously generate random data at a fixed sample rate
        while True:
            for ch in range(self.num_channels):
                self.data[ch].append(random.uniform(18, 22))
            self.current_time += 1.0 / self.sample_rate
            yield self.env.timeout(1.0 / self.sample_rate)
