import os

def list_zip_files(directory):
    """
    Lists all .zip files in the specified directory.
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    # List all .zip files in the directory
    zip_files = [file for file in os.listdir(directory) if file.endswith('.zip')]
    
    return zip_files

# Directory where the script is located
current_directory = os.getcwd()

# Call the function and print the result
zip_files = list_zip_files(current_directory)
for zip_file in zip_files:
    print(zip_file)