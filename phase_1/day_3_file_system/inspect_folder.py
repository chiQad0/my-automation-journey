"""
This script prints the current working directory.
It then inspects a specified folder to 
list all items in the directory and 
print whether each item is a file or folder
"""
from pathlib import Path

def inspect_folder():
    current_dir = Path.cwd()
    print("Current working directory: ")
    print(current_dir)
    print("-" * 30)

    for item in current_dir.iterdir():
        if item.is_file():
            print(f"{item.name} -> file. ({item.suffix})")
            
        elif item.is_dir():
            print(f"[DIR] {item.name} -> folder")

inspect_folder()
