import os

import paramiko

# Set the key file and remote machine information
PRIVATE_KEY = ""
REMOTE_USER = ""
REMOTE_HOST = ""  # Replace with your actual remote host IP
LOCAL_BASE_DIR = "/home/wsl2/projects/OLDCC/ansible/configuration_files"

# Establish an SSH connection
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(REMOTE_HOST, username=REMOTE_USER, key_filename=PRIVATE_KEY)

# Directory to copy files from
remote_directories = ["/etc/sudoers.d/", "/etc/rsyslog.d/"]

# Loop over each directory
for remote_directory in remote_directories:
    try:
        # Get the list of files in the remote directory
        command = f"sudo ls {remote_directory}"
        stdin, stdout, stderr = client.exec_command(command)
        files_list = stdout.read().decode("utf-8").split()

        # Loop over each file in the list
        for file_name in files_list:
            full_file_path = os.path.join(remote_directory, file_name)
            # Execute sudo cat on each file and capture the output
            command = f"sudo cat {full_file_path}"
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read()

            # Check the exit status of the command
            if stdout.channel.recv_exit_status() == 0:
                # Successful command execution, save the output
                if not os.path.exists(LOCAL_BASE_DIR + remote_directory):
                    os.makedirs(LOCAL_BASE_DIR + remote_directory)

                with open(LOCAL_BASE_DIR + remote_directory + file_name, "wb") as local_file:
                    local_file.write(output)
            else:
                # Command failed, record it
                with open("/home/wsl2/projects/OLDCC/ansible/configuration_files/failed_copy_records.txt", "a") as failed_records:
                    failed_records.write(f"Failed to copy file: {full_file_path}\n")
    except Exception as e:
        # Handle exceptions (e.g., SSH connection issues)
        with open("/home/wsl2/projects/OLDCC/ansible/configuration_files/failed_copy_records.txt", "a") as failed_records:
            failed_records.write(f"Failed to get file list from {remote_directory}. Error: {str(e)}\n")

# Close the SSH connection
client.close()
