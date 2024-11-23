# file_organizer.py

import os
import shutil

def organize_files(directory):
    """
    Organizes files in the given directory by their extensions.

    Parameters:
    directory (str): Path to the folder containing files to organize.

    Returns:
    None
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return
    
    # Iterate through files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Skip folders, only organize files
        if os.path.isfile(filepath):
            # Extract the file extension
            ext = os.path.splitext(filename)[1][1:]
            if not ext:  
                ext = 'others'
            
            # Create a folder for the extension if it doesn't exist
            folder = os.path.join(directory, ext)
            os.makedirs(folder, exist_ok=True)
            
            # Move the file to the appropriate folder
            shutil.move(filepath, folder)
    
    print("Files organized successfully!")
    

if __name__ == "__main__":
    # Prompt user for a directory path
    folder_path = input("Enter the path to the folder to organize: ").strip()
    organize_files(folder_path)
