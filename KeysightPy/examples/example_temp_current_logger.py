import sys
print(sys.path)

from KeysightPy.src.simulated_temp_current_logger import SimulatedTempCurrentLogger


logger = SimulatedTempCurrentLogger(sample_rate=10, num_channels=3)


logger.start_logging()

# Log for 10 seconds
for i in range(100):
    temperature, resistance, current = logger.get_latest_data()
    print(f"Temperature: {temperature:.2f} °C, Resistance: {resistance:.2f} Ω, Current: {current:.2f} A")

logger.stop_logging()
