"""Creates a random search term from a list of files in the "files" directory."""

import random
from pathlib import Path


def random_terms():
    """
    Randomizes search terms from files in the "files" directory.

    Returns:
        list: A list of random search terms.

    """
    file_path = Path("files")
    search_term = []
    print("Randomizing search terms...")
    files = list(Path.iterdir(file_path))
    select_file_number = random.choice(range(2, len(files) + 1))
    random_files = random.sample(files, select_file_number)
    for file in sorted(random_files):
        with Path(file).open("r") as f:
            items = f.read().splitlines()
        search_term.append(random.choice(items))

    return search_term


search = input("Enter search term: ")
if search == "random":
    search_term = random_terms()
    print(" ".join(search_term))
else:
    print("Searching for: " + search)
