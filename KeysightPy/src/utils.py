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
