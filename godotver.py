import os
import subprocess
import shutil
import re
import parser_godotver


def extract_version_info(pck_path,game_name):
    version_info = {}

    # Create a temporary directory for extraction
    temp_dir = "temp_extraction"
    os.makedirs(temp_dir, exist_ok=True)

    # Copy the original .pck file to a temporary location
    temp_pck_path = os.path.join(temp_dir, 'temp_file.7z')
    shutil.copy(pck_path, temp_pck_path)

    # Extract contents using 7z command
    extract_with_7z(temp_pck_path, temp_dir)

    # Check if .rsrc folder exists
    rsrc_path = os.path.join(temp_dir, '.rsrc')
    if not os.path.exists(rsrc_path):
        print("The PCK file does not contain the expected .rsrc folder.")
        cleanup_temp_files(temp_pck_path, temp_dir)
        return None

    # Read version.txt from .rsrc folder
    version_txt_path = os.path.join(rsrc_path, 'version.txt')  
    if not os.path.exists(version_txt_path):
        print("The PCK file does not contain the expected version.txt file.")
        cleanup_temp_files(temp_pck_path, temp_dir)
        return None
    
    foldergame = str(game_name).replace(" ","_")
    os.makedirs(foldergame, exist_ok=True)
    s = os.path.join(foldergame, 'pck.txt')
    shutil.copy(version_txt_path, s)

    # Clean up temporary files
    cleanup_temp_files(temp_pck_path, temp_dir)


    godot_ver, game_name_ = parser_godotver.parse(foldergame)
    print(godot_ver,"\n",game_name_)



def extract_with_7z(archive_path, destination_path):
    command = f"7z x {archive_path} -o{destination_path}"
    subprocess.run(command, shell=True)

def cleanup_temp_files(temp_pck_path, temp_dir):
    # Delete the temporary directory
    shutil.rmtree(temp_dir, ignore_errors=True)

# # Example Usage:
# pck_path = "y.pck"
# extract_version_info(pck_path,"hi ff ff")
