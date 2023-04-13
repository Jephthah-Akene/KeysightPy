import numpy as np

def save_data_to_file(data, file_path):
    """
    Save acquired data to a file.

    :param data: The data to be saved.
    :param file_path: The path to the file where the data should be saved.
    """
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def load_data_from_file(file_path):
    """
    Load data from a file.

    :param file_path: The path to the file containing the data.
    :return: A list of data points.
    """
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(float(line.strip()))
    return data

# Add more utility functions as needed for your project.

def moving_average(data, window_size):
    """
    Smooth the input data using a moving average filter.

    Args:
        data (list or numpy array): The input data to be smoothed.
        window_size (int): The size of the moving average window.

    Returns:
        numpy array: The smoothed data.
    """
    if window_size <= 0:
        raise ValueError("Window size must be greater than 0")

    return np.convolve(data, np.ones(window_size)/window_size, mode='same')