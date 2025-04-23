# Conda Commands Reference

## Overview
Conda is a powerful package manager and environment management system. This reference document covers essential Conda commands for creating, managing, and working with environments.

## Environment Management

### Creating Environments

```bash
# Create a new environment
conda create -n myenv    # This will create the environment in a centralized location.
conda create --prefix ./myenv  # This will create the environment in a custom location.
 
# Create environment with specific Python version
conda create -n myenv python=3.9

# Create environment with specific packages
conda create -n myenv python=3.9 scikit-learn pandas numpy matplotlib

# Create environment from a YAML file
conda env create -f environment.yml
```

### Listing Environments

```bash
# List all conda environments
conda env list

# Alternative way to list environments
conda info --envs
```

### Activating/Deactivating Environments

```bash
# Activate an environment
conda activate myenv

# Activate an environment by path
conda activate ./envs/myenv

# Deactivate current environment
conda deactivate
```

### Removing Environments

```bash
# Remove an environment
conda remove --name myenv --all

# Alternative way to remove an environment
conda env remove -n myenv

# Remove by specifying the path
conda remove -p /path/to/env
```

## Package Management

### Installing Packages

```bash
# Install a package in the current environment
conda install package_name

# Install a specific version of a package
conda install package_name=1.2.3

# Install multiple packages
conda install package1 package2 package3

# Install a package from a specific channel
conda install -c conda-forge package_name
```

### Listing Packages

```bash
# List all packages in the current environment
conda list

# List packages in a specific environment (if not activated)
conda list -n myenv

# List packages in a specific environment by path
conda list -p /path/to/myenv
```

### Updating Packages

```bash
# Update a specific package
conda update package_name

# Update all packages in the current environment
conda update --all

# Update conda itself
conda update conda
```

### Searching for Packages

```bash
# Search for available versions of a package
conda search package_name

# Example: search for available Python versions
conda search python
```

### Removing Packages

```bash
# Remove a package from the current environment
conda remove package_name

# Remove multiple packages
conda remove package1 package2
```

## Environment Export/Import

```bash
# Export active environment to YAML file
conda env export > environment.yml

# Export environment without build specifications (more portable)
conda env export --from-history > environment.yml

# Export with specific platform (e.g., for cross-platform compatibility)
conda env export --no-builds > environment.yml

# Create environment from exported YAML file
conda env create -f environment.yml
```

## Channels Management

```bash
# Add a channel
conda config --add channels channel_name

# Remove a channel
conda config --remove channels channel_name

# List configured channels
conda config --show channels
```

## Conda Information and Help

```bash
# Get conda information
conda info

# Get help on a specific command
conda command --help

# Example: get help on the create command
conda create --help
```

## Cleaning Up

```bash
# Remove unused packages and caches
conda clean --all

# Just remove package tarballs
conda clean --packages

# Just remove index cache
conda clean --index-cache
```

## Advanced Usage

```bash
# Install packages without asking for confirmation
conda install --yes package_name

# Create environment with specific channel priority
conda create -n myenv -c conda-forge python=3.9

# Clone an existing environment
conda create --name new_env --clone existing_env
```

## Working with Pip in Conda Environments

When conda doesn't have a package you need, you can use pip inside a conda environment:

```bash
# First activate your conda environment
conda activate myenv

# Then install with pip
pip install package_name

# You can also include pip packages in environment.yml files
# Example environment.yml section:
# dependencies:
#   - python=3.9
#   - pandas
#   - pip:
#     - special-package
```

## Best Practices

1. Create dedicated environments for different projects
2. Always activate the environment before installing packages
3. Use environment files for reproducibility
4. Prefer conda packages over pip when available
5. Keep conda itself updated
6. Use conda-forge channel for packages not in the default channel


## Install jupyter notebook
`conda install jupyter`  This will allow you to use a jupyter notebook in the environment.