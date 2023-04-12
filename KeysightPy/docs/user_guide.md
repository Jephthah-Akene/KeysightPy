This file should contain a step-by-step guide for users to set up and use the project, including examples of common tasks and explanations of how to modify the source code for their specific requirements.

# KeysightPy User Guide

This user guide provides step-by-step instructions for setting up and using the KeysightPy project to acquire data from Keysight Technologies data acquisition (DAQ) devices using Python and PyVISA.

## Table of Contents
- [KeysightPy User Guide](#keysightpy-user-guide)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Connecting to Your DAQ Device](#connecting-to-your-daq-device)

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
