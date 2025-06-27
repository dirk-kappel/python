"""
Create a virtual environment.

Find where python is installed.
1. which python --> /usr/bin/python3

Create the virtual environment.
2. /usr/bin/python3 -m venv myVenvName
-m : module mode. Tells python to run a specified module as a script instead of a standalone script file.
venv : the module that creates the virtual environment.

Activate the virtual environment.
3. source myVenvName/bin/activate

Once activated, if you ech $PATH then the first path will be in the virtual environment.

Installing a package using pip will place it in the virtual environment directory.
e.g. $ pip install flask

4. Create a requirements.txt file to name all of the dependencies.
To install all of the requirements:
$ pip install -r requirements.txt

Name the version using:
flask==1.0.0          # Specific version.
requests>=1.1.2,<2.0  # Setting a range of acceptable versions.
"""
import sys

print(sys.path)

list(map(lambda x: print(x), sys.path)) # This uses map to print out each value of the list. No need to print the variable since the function already does it.


