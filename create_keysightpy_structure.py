import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path, content=""):
    with open(path, "w") as file:
        file.write(content)

# Project root directory
root_dir = "KeysightPy"

# Create directories
create_directory(root_dir)
create_directory(os.path.join(root_dir, "data"))
create_directory(os.path.join(root_dir, "docs"))
create_directory(os.path.join(root_dir, "examples"))
create_directory(os.path.join(root_dir, "src"))
create_directory(os.path.join(root_dir, "tests"))

# Create files
create_file(os.path.join(root_dir, "docs", "user_guide.md"))
create_file(os.path.join(root_dir, "docs", "troubleshooting.md"))
create_file(os.path.join(root_dir, "examples", "example_1.py"))
create_file(os.path.join(root_dir, "examples", "example_2.py"))
create_file(os.path.join(root_dir, "src", "__init__.py"))
create_file(os.path.join(root_dir, "src", "keysight_daq.py"))
create_file(os.path.join(root_dir, "src", "utils.py"))
create_file(os.path.join(root_dir, "tests", "test_daq.py"))
create_file(os.path.join(root_dir, ".gitignore"), "*.pyc\n__pycache__/\n*.pyo\n*.egg-info/\ndist/\nbuild/\nvenv/\n")
create_file(os.path.join(root_dir, "LICENSE"))
create_file(os.path.join(root_dir, "README.md"))
create_file(os.path.join(root_dir, "requirements.txt"), "pyvisa\npyvisa-py\n")

print("KeysightPy file structure created.")
