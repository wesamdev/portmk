import shutil
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
import pyglet
from tkinter import filedialog
import os
import godotpck





def build():
    global game_path, map_path  # Assuming game_path and map_path are global variables

    if game_path is not None and map_path is not None:
        file_name = os.path.basename(game_path)
        file_name = file_name[:-4]
        file_name_ = file_name.replace(" ", "").lower()

        _, file_extension = os.path.splitext(game_path)

        # Create a directory using the file name

        check = create_directory(file_name)
                # Create a subfolder named 'data' in the destination folder
        destination_folder_ = os.path.join(os.getcwd(), file_name)
        data_folder_path = os.path.join(destination_folder_, file_name_)
        os.mkdir(data_folder_path)

        if check:
            if file_extension.lower() == '.exe':
                # Copy the file to the destination folder
                destination_folder = os.path.join(os.getcwd(), f"{file_name}\\{file_name_}")
                shutil.copy(game_path, destination_folder)

                # Construct the paths for the source and destination files
                source_file = os.path.join(destination_folder, file_name + '.exe')
                destination_file = os.path.join(destination_folder, file_name + '.pck')

                # Rename the copied file to have a ".pck" extension
                os.rename(source_file, destination_file)
                game_path = destination_file
            else:
                # Copy the file to the destination folder
                destination_folder = os.path.join(os.getcwd(), f"{file_name}\\{file_name_}")
                shutil.copy(game_path, destination_folder)

            print(f"File copied and renamed to '{destination_folder}'")

            # Get Godot version information
            godot_ver, _ = godotpck.get_godot_info(game_path)
            frt_ver = get_version_frt(godot_ver)
            # Read the content of the script.txt file and replace placeholders
            with open("script.txt", "r") as script:
                sh_script = script.read().replace("Z", frt_ver).replace("`", file_name_).replace("+", file_name)
            with open("template.port.json", "r") as port_json:
                port_json = port_json.read().replace("`", frt_ver).replace("j", file_name_).replace("+", file_name)

            # Create a new file named 'godot_script.sh' in the destination folder
            script_file_path = os.path.join(destination_folder_, f'{file_name}.sh')
            with open(script_file_path, 'w') as script_file:
                script_file.write(sh_script)

            port_json_file_path = os.path.join(destination_folder, f'{file_name}.port.json')
            with open(port_json_file_path, 'w') as port_json_file:
                port_json_file.write(port_json)

            # Copy the .gptk file to the 'data' subfolder and rename it to 'godot.gptk'
            shutil.copy(map_path, os.path.join(data_folder_path, 'godot.gptk'))

            print(f"Script file and data copied to '{destination_folder}'")



def get_version_frt(godot_version):
    # Check if the godot_version contains the major version "4.0"
    if "4.0" in godot_version:
        return "4.0.4"
    if "4.1" in godot_version:
        return "4.1.3"

    if "3.5" in godot_version:
        return "3.5.2"
    if "3.4" in godot_version:
        return "3.4.5"

    if "3.3" in godot_version:
        return "3.3.4"
    if "3.2" in godot_version:
        return "3.2.3"

    if "3.0" in godot_version:
        return "3.0.6"
    if "2.1" in godot_version:
        return "2.1.6"

    # Handle cases where the version string doesn't match the specific case above
    return f"Invalid version format or not found in the mapping: {godot_version}"


def create_directory(directory_path):
    try:
        # Create target directory
        os.mkdir(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
        return True
    except FileExistsError:
        print(f"Directory '{directory_path}' already exists.")
        return False




def browse_file():
    global game_path
    game_path = filedialog.askopenfilename(title="Select a file", filetypes=[("GODOT files", "*.pck, *.exe")])
    # Do something with the file_path, e.g., display it in an Entry widget
    browse_file_Entry.delete(0, "end")
    browse_file_Entry.insert(0, game_path)
    game_path = browse_file_Entry.get()




def browse_file_gptk():
    global map_path
    map_path = filedialog.askopenfilename(title="Select a file", filetypes=[("gptokeyb files", "*.gptk")])
    # Do something with the file_path, e.g., display it in an Entry widget
    browse_file_gptk_Entry.delete(0, "end")
    browse_file_gptk_Entry.insert(0, map_path)
    map_path = browse_file_gptk_Entry.get()


# def browse_file_json():
#     global json_path
#     json_path = filedialog.askopenfilename(title="Select a file", filetypes=[("PortMatser Json files", "*.port.json")])
#     # Do something with the file_path, e.g., display it in an Entry widget
#     browse_file_gptk_Entry.delete(0, "end")
#     browse_file_gptk_Entry.insert(0, json_path)
#     json_path = browse_file_gptk_Entry.get()


# Setup Window
window = ttk.Window(themename="darkly")
window.geometry("600x400")
window.resizable(False, False)
window.title("PORTMK  Made by wesamdev   v0.1 alpha")


#Setup Fonts
pyglet.font.add_file("fonts/Poppins-Bold.ttf")
font1 = ttk.font.Font(family="Poppins", size=12, weight="bold")
font2= ttk.font.Font(family="Poppins", size=12, weight="normal")

#runtimes
runtimes=  [
    "GODOT 4.1.3",
    "GODOT 4.0.4",
    "GODOT 4.1.3",
    "GODOT 3.5.2",
    "GODOT 3.4.5",
    "GODOT 3.3.4",
    "GODOT 3.2.3",
    "GODOT 3.0.6",
    "GODOT 2.1.6",

]

#setup styles
style1 = ttk.Style()
style1.configure("success.Outline.TButton", font=(font1, 14))



# PortJson_label = ttk.Label(window, text="Select Game json", font=font1)
# PortJson_label.pack(pady=5)
# PortJson_Entry =ttk.Entry(window, font=(font1, 16), width=30)
# PortJson_Entry.pack(pady=3)
# PortJson_file_btn = ttk.Button(window, text="Browse",style="success.Outline.TButton", command=browse_file_json)
# PortJson_file_btn.pack(pady=3)



browse_file_label = ttk.Label(window, text="Choose Game File", font=font1)
browse_file_label.pack(pady=5)
browse_file_Entry = ttk.Entry(window, font=(font1, 16), width=30)
browse_file_Entry.pack(pady=3)
browse_file_btn = ttk.Button(window, text="Browse",style="success.Outline.TButton", command=browse_file)
browse_file_btn.pack(pady=3)



browse_file_gptk_label = ttk.Label(window, text="Choose key Mapping File", font=font1)
browse_file_gptk_label.pack(pady=5)
browse_file_gptk_Entry = ttk.Entry(window, font=(font1, 16), width=30)
browse_file_gptk_Entry.pack(pady=3)
browse_file_gptk_btn = ttk.Button(window, text="Browse",style="success.Outline.TButton", command=browse_file_gptk)
browse_file_gptk_btn.pack(pady=3)

# runtime_label = ttk.Label(window, text="Runtime", font=font1)
# runtime_label.place(x=11, y=119)
# runtime_combobox = ttk.Combobox(window,values=runtimes, font=(font1, 14))
# runtime_combobox.place(x=11,y=147)



bulid_button = ttk.Button(window, text="Bulid", bootstyle=SUCCESS, style="success.Outline.TButton", width=8, command=build)
bulid_button.place(x=480,y=351)

if __name__ == "__main__":
    window.mainloop()