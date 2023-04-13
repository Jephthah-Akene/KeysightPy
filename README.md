# KeysightPy


KeysightPy is a Python library designed to simplify data acquisition with Keysight DAQ devices using PyVISA and Python. It provides an easy-to-use interface for communicating with and configuring Keysight Technologies data acquisition (DAQ) devices, acquiring data, and processing the acquired data. The library also offers simulation capabilities to help users familiarize themselves with Keysight DAQs and their functionalities before using physical hardware.

For questions or feature requests, please contact **Jephthah Akene** at 0xtachi@gmail.com. As an independent researcher, I built this project purely for the joy of creating something both enjoyable and practical. If you love to tinker and build innovative control systems, feel free to email me!

## Table of Contents
- Installation
- Usage
- Examples
- Simulation
- Testing
- Customization
- File Structure
- Dependencies

## Installation
To install KeysightPy, follow these steps:

- Ensure you have Python 3.6 or higher and Git installed on your system.
- Clone the repository:
`git clone https://github.com/username/KeysightPy.git`

- Change to the project directory:
`cd KeysightPy`

- Create a virtual environment and activate it:
`python3 -m venv venv`
`source venv/bin/activate`

- Install the required packages:
`pip install -r requirements.txt`

## Usage

Refer to the User Guide for step-by-step instructions on setting up and using KeysightPy for data acquisition with Keysight DAQ devices. The guide covers topics such as connecting to your DAQ device, configuring it for specific tasks, acquiring data, saving and loading data, and customizing the project for your specific requirements.

## Examples

The examples folder contains example scripts demonstrating how to use KeysightPy for various data acquisition tasks:

- example_1.py: Single-point data acquisition example.
- example_2.py: Continuous data acquisition example.
- example_temp_current_logger.py: A simulation of a temperature and current logger.

## Simulation

KeysightPy includes a simulation for simulating and logging temperature and current data. It was created to help users familiarize themselves with Keysight DAQs before using physical hardware.

## Objective

The main objective of the simulation is to simulate and log temperature and current data. KeysightPy is designed to help users become more familiar with Keysight DAQs and their functionalities, and to provide a way to experiment and develop code without the need for physical hardware.

## File Structure

To access the simulators, find the following files:

- `src/simulated_daq.py`: A module for simulating a DAQ (data acquisition) device, which reads and logs temperature and current data.
- `src/simulated_temp_current_logger.py`: A module that provides an interface for logging temperature and current data.
- `examples/example_temp_current_logger.py`: A sample script that demonstrates how to use the SimulatedTempCurrentLogger class to log and plot temperature and current data.

## Examples and Simulations

KeysightPy includes an example script example_temp_current_logger.py that demonstrates how to use the SimulatedTempCurrentLogger class to log and plot temperature and current data. The script uses the matplotlib package to plot the data.

## Getting Started

To use KeysightPy, clone the repository and install the required packages from the requirements.txt file. Then, you can run the example script example_temp_current_logger.py to see how to use the SimulatedTempCurrentLogger class to log and plot temperature and current data.

## Testing

To run the tests provided in the tests folder, execute the following command in the project directory:
`pytest tests/`

This will run the test suites included in the tests folder using the pytest testing framework.

## Customization

KeysightPy can be customized to meet specific requirements by modifying the source code in the src folder, creating custom scripts in the examples folder, and adding utility functions in the src/utils.py file. Refer to the User Guide for more information on customizing the project.

## File Structure

The repository is organized as follows:

- `KeysightPy`: Main project folder containing the LICENSE, data folder, env folder, and requirements.txt file.
- `docs`: Contains troubleshooting.md and user_guide.md files.
- `examples`: Contains example_1.py, example_2.py, and example_temp_current_logger.py files.
- `src`: Contains keysight_daq.py, simulated_daq.py, simulated_daq_core.py, simulated_instruments.py, and utils.py files.
- `tests`: Contains integration_test.py, test_daq.py, test_simulated_daq.py, and test_utils.py files.
- `README.md`: This file.
- `create_keysightpy_structure.py`: A script that generates the file structure for the project.

## Dependencies

The following packages are required to run KeysightPy and are listed in the requirements.txt file:

- yvisa
- pyvisa-py
- pytest
- numpy
- pandas
- matplotlib (optional, for running the example_temp_current_logger.py script)

To install these packages, run:
`pip install -r requirements.txt`

For more information on the packages, refer to their respective documentation:

- PyVISA
- PyVISA-py
- pytest
- NumPy
- pandas
- matplotlib

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

