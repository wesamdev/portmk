import re

# Example command output
command_output = """
[11/13/2023 16:38:13]   // Time format - MM/dd/yyyy HH:mm:ss
[11/13/2023 16:38:13]
[11/13/2023 16:38:13]   The console is displayed. The following logs will be duplicated into it!
[11/13/2023 16:38:13]   PCK Info started
[11/13/2023 16:38:13]   Input file: C:\\Users\\Wesam Almasruri\\Documents\\GitHub\\portmk\\y.pck
[11/13/2023 16:38:13]   [Progress] Open PCK: Opening: C:\\Users\\Wesam Almasruri\\Documents\\GitHub\\portmk\\y.pck
[11/13/2023 16:38:13]   [Progress] Open PCK: 0%
[11/13/2023 16:38:13]   [Progress] Open PCK: Version: 2.4.1.0, Flags: 0
[11/13/2023 16:38:13]   [Progress] Open PCK: File count: 716
[11/13/2023 16:38:13]   [Progress] Open PCK: Completed!
[11/13/2023 16:38:13]   [Progress] Open PCK: 100%
[11/13/2023 16:38:13]   Pack version 2. Godot version 4.1.0
[11/13/2023 16:38:13]-  Version string for this program: 2.4.1.0
[11/13/2023 16:38:13]-  File count: 716
"""

# Define a regular expression pattern
pattern = r"Pack version (\d+). Godot version (\d+\.\d+\.\d+)"

# Search for the pattern in the command output
match = re.search(pattern, command_output)

# Extract information
if match:
    pack_version, godot_version = match.groups()
    print(f"Pack Version: {pack_version}")
    print(f"Godot Version: {godot_version}")
else:
    print("Failed to retrieve information from the command output.")
