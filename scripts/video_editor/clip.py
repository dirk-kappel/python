"""Clips a video file using ffmpeg."""

import subprocess
import sys
from pathlib import Path

# Variables
output_directory = ""


def run_command(command):
    command = ["ls", "-l", "/"]  # Replace this with the command and its arguments
    print("Running command:", " ".join(command))
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=False)
    print("Output:", result.stdout)
    print("Return code:", result.returncode)


def format_time(input_value):
    """Convert input to a standardized format (HH:MM:SS)."""
    if ":" not in input_value:
        # Assuming input in the format "923"
        input_value = input_value.zfill(6)  # Zero-fill to ensure 6 digits
        input_value = f"{input_value[:2]}:{input_value[2:4]}:{input_value[4:]}"

    # Parse and format the time
    try:
        hours, minutes, seconds = map(int, input_value.split(":"))
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return formatted_time
    except ValueError:
        return "Invalid input format"


def format_filename(input_file_path):
    input_file_name = Path(input_file_path).stem
    file_extension = Path(input_file_path).suffix
    filename = input_file_name.split("_")
    for name in filename:
        if name.isdigit():
            filename.remove(name)
    filename = " ".join(filename).title().replace(".", " | ") + file_extension
    return filename


def check_and_rename_file(output_directory, output_file):
    while True:
        if Path(output_directory, output_file).is_file():
            output_file = Path(output_file).stem + "+" + Path(output_file).suffix
        else:
            return output_directory + output_file


# Input/Output filenames
input_file_path = input("Input file absolute path: ")
output_file = format_filename(input_file_path)
output_file = input(f"Output file (default: {output_file}): ") or output_file
output_file_path = check_and_rename_file(output_directory, output_file)

# Start and stop times
start_time = input("Start clip time: ")
end_time = input("End clip time: ")
if int(start_time) > int(end_time):
    print("Start time must be before end time")
    sys.exit()
start_time = format_time(start_time)
end_time = format_time(end_time)

command = (
    f"ffmpeg -i {input_file_path} -ss {start_time} -to {end_time} -c {output_file_path}"
)
run_command(command)
