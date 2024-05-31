import os  # Importing the os module to interact with the operating system

import shutil  # Importing the shutil module to perform high-level file operations

def create_subfolder_if_needed(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)  # Create the full path for the subfolder
    if not os.path.exists(subfolder_path):  # Check if the subfolder does not exist
        os.makedirs(subfolder_path)  # Create the subfolder if it does not exist
    return subfolder_path  # Always return the subfolder path

def clean_folder(folder_path):
    for filename in os.listdir(folder_path):  # Iterate over each file in the folder

        if os.path.isfile(os.path.join(folder_path, filename)):  # Check if the current item is a file
            file_extension = filename.split('.')[-1].lower()  # Get the file extension and convert it to lowercase
            if file_extension:  # Proceed if there is a file extension
                subfolder_name = f'{file_extension.upper()} Files'  # Create a subfolder name based on the file extension
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)  # Ensure the subfolder exists
                file_path = os.path.join(folder_path, filename)  # Create the full path to the file
                new_location = os.path.join(subfolder_path, filename)  # Create the new location path for the file
                
                if not os.path.exists(new_location):  # Check if the file does not already exist in the subfolder
                    shutil.move(file_path, new_location)  # Move the file to the new location
                    print(f'Moved: {filename} -> {subfolder_name}/')  # Print a message indicating the file was moved
                else:
                    print(f'Skipped: {filename} already exists in {subfolder_name}/')  # Print a message if the file already exists

if __name__ == "__main__":
    print("Desktop Cleaner Script")  # Print the script's name
    folder_path = r'C:\Users\USER\OneDrive\Documents'  # Set the folder path to clean (using a raw string to handle backslashes)
    if os.path.isdir(folder_path):  # Check if the folder path is a valid directory
        clean_folder(folder_path)  # Call the function to clean the folder
        print("Cleaning complete.")  # Print a message indicating the cleaning is complete
    else:
        print("Invalid folder path. Please ensure the path is correct and try again")  # Print an error message if the folder path is invalid