from pathlib import Path

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

# Expand directory
print(f'{f} absolute:',f.absolute())

# Get the home directory
print('Home directory is:', Path.home())

# Create a directory if it does not exist
new_dir = Path('a/b/c/d')
if not new_dir.is_dir(): new_dir.mkdir(parents=True, exist_ok=True)
# Create the file if it does not exist
new_file = 'new_file.txt'
if not Path(new_dir, new_file).exists(): Path(new_dir, new_file).touch()