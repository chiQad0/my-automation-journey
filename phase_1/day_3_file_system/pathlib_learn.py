from pathlib import Path

current_directory = Path.cwd()
print(current_directory)

file = Path("instruction.md")

file.rename(Path("instruction.md") / file.name)