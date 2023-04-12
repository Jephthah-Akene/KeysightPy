<<<<<<< HEAD
=======
This file should contain a step-by-step guide for users to set up and use the project, including examples of common tasks and explanations of how to modify the source code for their specific requirements.

>>>>>>> 92976d4be0337bb4c4a27b9b3aabfd6cfd4e94be
# KeysightPy User Guide

This user guide provides step-by-step instructions for setting up and using the KeysightPy project to acquire data from Keysight Technologies data acquisition (DAQ) devices using Python and PyVISA.

## Table of Contents
- [KeysightPy User Guide](#keysightpy-user-guide)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Connecting to Your DAQ Device](#connecting-to-your-daq-device)
<<<<<<< HEAD
  - [Configuring Your DAQ Device](#configuring-your-daq-device)
  - [Acquiring Data](#acquiring-data)
  - [Saving and Loading Data](#saving-and-loading-data)
  - [Customizing the Project](#customizing-the-project)
  - [Running Tests](#running-tests)
=======
>>>>>>> 92976d4be0337bb4c4a27b9b3aabfd6cfd4e94be

## Prerequisites

Before you start using the KeysightPy project, make sure you have the following installed on your system:

- Python 3.6 or higher
- Git

## Installation

Follow the installation instructions provided in the [README.md](../README.md) file to set up the KeysightPy project on your system.

## Connecting to Your DAQ Device

1. Locate the resource name of your DAQ device. The resource name typically has a format like `'TCPIP0::192.168.0.100::inst0::INSTR'` for a networked device, or `'USB0::0x1234::0x5678::INSTR'` for a USB device. Consult your device's documentation for information on how to find the resource name.

2. Open the `src/keysight_daq.py` file and locate the `example_usage` function. Replace the `resource_name` variable with the resource name of your DAQ device.

```python
resource_name = 'TCPIP0::192.168.0.100::inst0::INSTR'  # Replace with your device's resource name
<<<<<<< HEAD
```
Run the example_usage function to connect to your DAQ device. The KeysightDevice class will establish a connection using PyVISA.

## Configuring Your DAQ Device
Explain how to configure the DAQ device for specific data acquisition tasks using the provided methods in the KeysightDevice class. Include examples of common configurations.

## Acquiring Data
Explain how to acquire data from the DAQ device using the provided methods in the KeysightDevice class. Include examples of different types of data acquisition, such as single-point or continuous data acquisition.

## Saving and Loading Data
Explain how to save and load acquired data using the utility functions provided in the src/utils.py file. Include examples of saving data to a file and loading data from a file.

## Customizing the Project
Explain how users can customize the project for their specific requirements by modifying the source code in the src folder, creating custom scripts in the examples folder, and adding utility functions in the src/utils.py file.

## Running Tests
Explain how to run the tests provided in the tests folder using the pytest testing framework. Include instructions for installing the required dependencies and running the tests from the command line.
=======
>>>>>>> 92976d4be0337bb4c4a27b9b3aabfd6cfd4e94be
