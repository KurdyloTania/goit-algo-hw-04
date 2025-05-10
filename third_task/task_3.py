import sys
from pathlib import Path
from colorama import Fore


if len(sys.argv) == 1:
    print("Error: No path provided!!!")
    sys.exit(1)

input_path = sys.argv[1]
parent_folder_path = Path(input_path)


if not parent_folder_path.exists():
    print(f"Error: Path '{input_path}' does not exist!!!")
    sys.exit(1)


def parse_folder(path, level=0):
    indent = "  " * level
    try:
        for element in path.iterdir():
            if element.is_dir():
                print(Fore.BLUE + f"{indent}{Fore.BLUE + element.name}/")
                parse_folder(element, level + 1)
            elif element.is_file():
                print(Fore.GREEN + f"{indent} {element.name}")
    except FileNotFoundError:
        print(f"{indent}Error: Path {path} not found!!!")

parse_folder(parent_folder_path)
