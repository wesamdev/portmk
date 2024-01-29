import os
import platform
def is_platform_windows():
    if platform.system() == "Windows":
        return True
    else:
        return False

if is_platform_windows():
    with open(os.getcwd()+"\\version.txt") as txt:
        version = txt.read()
else:
    with open(os.getcwd()+"/version.txt") as txt:
        version = txt.read()