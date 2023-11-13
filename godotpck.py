import re
from subprocess import run, PIPE

def get_godot_info(pck_path):
    # Specify the path to the GodotPCKExplorer.UI.exe executable
    godot_pck_explorer_path = "\GodotPCKExplorer\GodotPCKExplorer.UI.exe"

    # Construct the command to get pack file info
    command = [godot_pck_explorer_path, '-i', pck_path]

    try:
        # Execute the command and capture output
        result = run(command, stdout=PIPE, stderr=PIPE)

        # Check if the command was successful
        if result.returncode == 0:
            # Decode the byte output to a string using UTF-16le encoding
            decoded_output = result.stdout.decode('utf-16le')

            print("Command output:")
            print(decoded_output)

            # Define a regular expression pattern
            pattern = r"Pack version (\d+). Godot version (\d+\.\d+\.\d+)"

            # Search for the pattern in the command output
            match = re.search(pattern, decoded_output)

            # Extract information
            if match:
                pack_version, godot_version = match.groups()
                print(f"Pack Version: {pack_version}")
                print(f"Godot Version: {godot_version}")
                return godot_version, pack_version
            else:
                print("Failed to retrieve information from the command output.")
        else:
            print(f"Error executing command: {result.stderr}")

    except Exception as e:
        print(f"An error occurred: {e}")


