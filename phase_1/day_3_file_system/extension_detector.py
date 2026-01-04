"""
This script loops through files in a given folder
and file name and extension of each file.
"""
from pathlib import Path

def extension_detector():
    current_dir = Path.cwd()
    print("Current working directory:")
    print(current_dir)

    for item in current_dir.iterdir():
        if item.is_file():
            print(f"File name: {item.name}, Extension: {item.suffix} ")

if __name__ == "__main__":
    extension_detector()
