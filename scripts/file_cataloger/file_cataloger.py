"""Clean up the file names and write them to a CSV file."""

import csv
import re
import string
from pathlib import Path

# # ------------ Configuration ------------
INPUT_PATH = Path("/home/wsl2/python/clean_files/input")
OUTPUT_PATH = Path("/home/wsl2/python/clean_files/output")
FILE_TYPES = ["mp4"]


def write_names_to_csv(all_names, file_path):
    """
    Writes the cleaned file names to a CSV file.

    Args:
        all_names (list): A list of cleaned file names.
        file_path (Path): The path to the directory where the CSV file will be saved.

    Returns:
        None

    """
    with Path(file_path / "all_names.csv").open("w+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name"])
        for name in all_names:
            writer.writerow([name])


def get_all_files(input_directory, allowed_extensions):
    """
    Returns all files in the "input_directory" directory and any subfolders.

    Args:
        input_directory (Path): The path to the directory containing files.
        allowed_extensions (list): A list of allowed file extensions.

    Returns:
        list: Path objects, each representing a file.

    """
    return [
        file_path
        for file_path in input_directory.rglob("*")
        if file_path.is_file()
        and file_path.suffix.lower().lstrip(".") in allowed_extensions
    ]


def clean_filename(filename):
    """
    Clean a single filename by.

    1. Removing file extension
    2. Replacing underscores with spaces
    3. Removing digits and trailing periods
    4. Splitting on periods and capitalizing each part

    Args:
        filename (Path): The path to the file.

    Returns:
        list: Cleaned name parts.

    """
    # Remove extension and replace underscores
    name = filename.stem.replace("_", " ").strip()

    # Remove digits and trailing periods in one step
    name = re.sub(r"\d", "", name).rstrip(".")

    # Split on periods and clean each part
    parts = []
    for part in name.split("."):
        cleaned_part = part.strip()
        if cleaned_part:  # Only add non-empty parts
            parts.append(string.capwords(cleaned_part))

    return parts


def get_unique_clean_names(file_paths):
    """
    Extract and clean all unique name parts from file paths.

    Args:
        file_paths (list): A list of file paths.

    Returns:
        list: A sorted list of unique cleaned names.

    """
    all_names = set()

    for file_path in file_paths:
        cleaned_parts = clean_filename(file_path)
        all_names.update(cleaned_parts)

    return sorted(all_names)


def main():
    """Main execution function."""
    files = get_all_files(INPUT_PATH, FILE_TYPES)
    clean_names = get_unique_clean_names(files)
    write_names_to_csv(clean_names, OUTPUT_PATH)
    print(f"Processed {len(files)} files, found {len(clean_names)} unique clean names")


if __name__ == "__main__":
    main()
