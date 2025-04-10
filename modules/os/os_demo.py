import os
from datetime import datetime

print(dir(os), end='\n\n') # print out all of the methods

# Print out current working directory
print(os.getcwd(), end='\n\n')

# Change directory
os.chdir('/home/wsl2/linux/')
print(os.getcwd(), end='\n\n')

# List files
print(os.listdir(), end='\n\n')

# Create a new folder in the Desktop directory
os.chdir('/home/wsl2/Desktop/')
try:                                            # If folder already exists then we get a FileExistsError
    os.mkdir('OS-Demo-2')                       # This will create the directory. Not recursive, use makedirs().
except:
    pass

# You can also check if the Directory exists or not before proceeding
if not os.path.isdir('Dir-1/Sub-Dir-1/OS-Demo-2'): os.makedirs('Dir-1/Sub-Dir-1/OS-Demo-2')    # You can create intermediatory directories (subdirs)
print(os.listdir(), end='\n\n')

# Delete folders
os.rmdir('OS-Demo-2')                       # Removes the directory
os.removedirs('Dir-1/Sub-Dir-1/OS-Demo-2')  # Delete directories recursively
print(os.listdir(), end='\n\n')

# Rename a file or folder
os.rename('test.txt', 'demo.txt')  # Pass the original file name and then the new file name.
print(os.listdir(), end='\n\n')
os.rename('demo.txt', 'test.txt')  # Rename it back

# Look at information about the files
print(os.stat('test.txt'))
# Can access specific properties
print(os.stat('test.txt').st_size)
# Get last modification time
print(os.stat('test.txt').st_mtime)
# Get datetime in human readable format
mod_time = os.stat('test.txt').st_mtime
print(datetime.fromtimestamp(mod_time), end='\n\n')

# View the entire directory tree using os.walk()
for dirpath, dirnames, filenames in os.walk('/home/wsl2/tmp/'):  # Yields a tuple of the (directory path, directories in the path, files within that path)
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

# Access the home environment variable os.environ
print(os.environ.get('HOME'))
# Use the environment variable to create file
# Create a path using os.path
file_path = os.path.join(os.environ.get('HOME'), 'test_file_os.txt')
print(file_path)

# Get the basename of a file. Doesn't matter if it exists or not.
print(os.path.basename('/tmp/test_basename.txt'))
# Get the directory name
print(os.path.dirname('/tmp/path_to/test_basename.txt'))
# Get them both
print(os.path.split('/tmp/path_to/test_basename.txt'), end='\n\n') # Returns a tuple of the directory name and then the filename

# Check if a file exists
print(os.path.exists('/tmp/path_to/test_basename.txt'))  # False
print(os.path.exists('/home/wsl2/.bashrc'))              # True

# Check if it is a directory
print(os.path.isdir('/home/wsl2'))
# Check if it is a file
print(os.path.isfile('/home/wsl2/.bashrc'), end='\n\n')

# Split the file root and extension
print(os.path.splitext('/home/wsl2/keys/us-east-1.ansible.pub'))