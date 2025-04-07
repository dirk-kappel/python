from pathlib import Path

# Print out current working directory
cwd = Path.cwd()
print(cwd)

# Iterate over all files/directories
for q in Path().iterdir():
    print(q)

# Create a path
my_dir = Path("a")
my_file = Path("file_1.txt")
print(my_dir)
print(my_file)

# Create a newfile in the directory
newfile = my_dir / "newfile.txt"
print(newfile)

# Get the file extension
print(my_file.suffix)
# Get the filename
print(my_file.stem)

p = Path('/etc')

# Check if it is a directory
print(f'{p} exists?:', p.exists())
print(f'{p} is directory?:', p.is_dir())

# Check if it exists
n = Path('/non_existent')
print(f'{n} exists?:', n.exists())
print(f'{n} is directory?:', n.is_dir())

# Check file
f = Path('file_1.txt')
print(f'{f} exists?:', f.exists())
print(f'{f} is directory?:', f.is_dir())

# Get the absolute path
print(f'{f} absolute:',f.absolute())
# Use the resolve to get absolute path - same result.
print(f.resolve())
# Get absolute path to this python script
print(Path(__file__).resolve())
# Retrieve the parent directory
print(Path(__file__).resolve().parent)

# Get the home directory
print('Home directory is:', Path.home())

# Search files and folders using glob method - only searches the Path directory and not the subdirectories
for p in Path.home().glob("*.pem"):
    print(p)
# To search recursively us rglob. (glob is case sensitive by default)
for p in Path.home().rglob("*.pem", case_sensitive=False):
    print(p)

# To open a file
pem_path = Path.home() / "keys" / "Effectual2.pem"
with pem_path.open() as f:
    print(f.read())

# Create a directory if it does not exist
new_dir = Path('a/b/c/d')
if not new_dir.is_dir(): new_dir.mkdir(parents=True, exist_ok=True)
# Create the file if it does not exist
new_file = 'new_file.txt'
if not Path(new_dir, new_file).exists(): Path(new_dir, new_file).touch()

# Create a directory and subdirectories
new_p = Path("TempDir/Subdir")
new_p.mkdir(parents=True, exist_ok=True)

# Create a new file
f1 = Path("TempFile.txt")
f1.touch()

# Rename a file
f1.rename("NewName.txt")

# Remove a file
f1 = Path("NewName.txt") # Need to reset the path since the file was renamed after the variable was set
f1.unlink() # Deletes the file.