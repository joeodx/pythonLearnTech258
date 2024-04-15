import os

# Directory
directory = "test_dir"

parent_directory = "C:/Users/Joe/Documents"

# Path
path = os.path.join(parent_directory, directory)

# Create Dir
os.mkdir(path)
print(path)
