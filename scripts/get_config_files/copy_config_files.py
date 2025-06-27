import os

import paramiko

# Set the key file and remote machine information
PRIVATE_KEY = ""
REMOTE_USER = ""
REMOTE_HOST = ""  # Replace with your actual remote host IP
LOCAL_BASE_DIR = "/home/wsl2/projects/OLDCC/ansible/configuration_files"

# File containing the list of files
FILES_LIST = "configuration_files"

# Establish an SSH connection
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(REMOTE_HOST, username=REMOTE_USER, key_filename=PRIVATE_KEY)

# Loop over files listed in the configuration_files file
with open(FILES_LIST, "r") as file_list:
    for file in file_list:
        file = file.strip()
        file_name = os.path.basename(file)

        # Use SSH for copying files
        print(f"Executing command: sudo cat '{file}'")
        try:
            stdin, stdout, stderr = client.exec_command(f"sudo cat '{file}'")
            output = stdout.read().decode("utf-8")

            # Check the exit status of the command
            if stdout.channel.recv_exit_status() == 0:
                # Successful command execution, save the output
                relative_path = os.path.dirname(file)
                local_path = LOCAL_BASE_DIR + relative_path
                if not os.path.exists(local_path):
                    os.makedirs(local_path)

                with open(local_path + f"/{file_name}", "w") as local_file:
                    local_file.write(output)
            else:
                # Command failed, record it
                with open("/home/wsl2/projects/OLDCC/ansible/configuration_files/failed_copy_records.txt", "a") as failed_records:
                    failed_records.write(f"Failed to copy file: {file}\n")
        except Exception as e:
            # Handle exceptions (e.g., SSH connection issues)
            with open("/home/wsl2/projects/OLDCC/ansible/configuration_files/failed_copy_records.txt", "a") as failed_records:
                failed_records.write(f"Failed to copy file: {file}. Error: {str(e)}\n")

# Close the SSH connection
client.close()
