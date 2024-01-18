import shutil
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap as ttk
import pyglet
from tkinter import filedialog
import os
import godotpck





def build():
    global game_path, map_path, author  # Assuming game_path and map_path are global variables
    game_path = browse_file_Entry.get()
    map_path = browse_file_gptk_Entry.get()
    author = author_Entry.get()
    try:
        if game_path != '' and map_path != '' and author != '':
            if  os.path.isfile(game_path) is not True and os.path.isfile(map_path) is not True:
                Messagebox.show_error("FileNotFound, please verfiy the path", title="PORTMK - FileNotFound")
                return
            file_name = os.path.basename(game_path)
            file_name = file_name[:-4]
            file_name_ = file_name.replace(" ", "").lower()


            # Create a directory using the file name

            try:
                check = create_directory(file_name)
                        # Create a subfolder named 'data' in the destination folder
                destination_folder_ = os.path.join(os.getcwd(), file_name)
                data_folder_path = os.path.join(destination_folder_, file_name_)
                os.mkdir(data_folder_path)
            except FileExistsError:
                Messagebox.show_error("FileExists", title="PORTMK - FileExistsError")


            if check:
                # _, file_extension = os.path.splitext(game_path)
                file_extension = os.path.splitext(game_path)[1]
                author = author_Entry.get()
                if file_extension.lower() == '.x86_64':
                    # Copy the file to the destination folder
                    destination_folder = os.path.join(os.getcwd(), f"{file_name}\\{file_name_}")
                    shutil.copy(game_path, destination_folder)

                    # Construct the paths for the source and destination files
                    source_file = os.path.join(destination_folder, file_name + '.x86_64')
                    destination_file = os.path.join(destination_folder, file_name + '.pck')

                    # Rename the copied file to have a ".pck" extension
                    os.rename(source_file, destination_file)
                    game_path = destination_file
                    print(f"File copied and renamed to '{destination_folder}'")
                else:
                    #Copy the file to the destination folder
                    destination_folder = os.path.join(os.getcwd(), f"{file_name}\\{file_name_}")
                    shutil.copy(game_path, destination_folder)
                    print(f"File copied to '{destination_folder}'")
                


                # Get Godot version information
                if godotpck.get_godot_info(game_path) is not False:
                    godot_ver, _ = godotpck.get_godot_info(game_path)
                else:
                    Messagebox.show_error("please download .net6 desktop runtime", title="PORTMK - Error in godotpckExp (EXPerror)")
                    return
                frt_ver = get_version_frt(godot_ver)
                # check if the version is valid
                if frt_ver ==  False:
                    Messagebox.show_error("Invalid Godot version, portmk dose not support {0}".format(godot_ver), title="PORTMK - Invalid Godot version")
                    return
            # Read the content of the script.txt file and replace placeholders
                with open("script.txt", "r") as script:
                    sh_script = script.read().replace("{FRTVER}", frt_ver).replace("{NAME}", file_name_).replace("{NAME++}", file_name)
                with open("template.port.json", "r") as port_json:
                    port_json = port_json.read().replace("{FRTVER}", frt_ver).replace("{NAME}", file_name_).replace("{NAME++}", file_name.capitalize()).replace("{AUTHOR}", author)

                with open("LICENSE.FRT.txt", "r") as frt_LICENSE:
                    frt_LICENSE = frt_LICENSE.read()


                # Create a new file named 'godot_script.sh' in the destination folder
                script_file_path = os.path.join(destination_folder_, f'{file_name.capitalize()}.sh')
                with open(script_file_path, 'w') as script_file:
                    script_file.write(sh_script)

                port_json_file_path = os.path.join(destination_folder, f'{file_name}.port.json')
                with open(port_json_file_path, 'w') as port_json_file:
                    port_json_file.write(port_json)


                frt_LICENSE_path  = os.path.join(destination_folder, f'LICENSE.FRT.txt')
                with open(frt_LICENSE_path, 'w') as frt_LICENSE_path:
                    frt_LICENSE_path.write(frt_LICENSE)

                # Copy the .gptk file to the 'data' subfolder and rename it to 'godot.gptk'
                shutil.copy(map_path, os.path.join(data_folder_path, 'godot.gptk'))

                print(f"Script file and data copied to '{destination_folder}'")
                Messagebox.ok("Port Builded!", title="PORTMK")
        else:
            Messagebox.show_error("Please Fill All Fields ", title="PORTMK - Error")
            print("Please Fill All Fields")
    except Exception as e:
        print(e)


def get_version_frt(godot_version):
    
    #expermintally added
    # if "4.0" in godot_version:
    #     return "4.0.4"
    # if "4.1" in godot_version:
    #     return "4.1.3"

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
    
    #remove support for 2.1
    # if "2.1" in godot_version:
    #     return "2.1.6"

    # Handle cases where the version string doesn't match the specific case above
    return False


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
    game_path = filedialog.askopenfilename(title="Select a file", filetypes=[("GODOT files", "*.pck"), ("GODOT files", "*.x86_64")])
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



# Setup Window
window = ttk.Window(themename="darkly")
window.geometry("800x600")
window.resizable(False, False)
window.title("PORTMK  v0.2-dev")


#Setup Fonts
pyglet.font.add_file(os.getcwd()+"\\fonts\\Poppins-Bold.ttf")
font1 = ttk.font.Font(family="Poppins", size=12, weight="bold")
font2= ttk.font.Font(family="Poppins", size=12, weight="normal")


#setup styles
style1 = ttk.Style()
style1.configure("success.Outline.TButton", font=(font1, 14))
style2 = ttk.Style()
style2.configure("primairy.Outline.TButton", font=(font1, 14))


#logo label
logo_label = ttk.Label(window, text="PORTMK", font=(font1, 28, "bold"))
logo_label.pack(pady=3)



# browse file game
browse_file_label = ttk.Label(window, text="Choose Game File", font=font1)
browse_file_label.pack(pady=10)
browse_file_Entry = ttk.Entry(window, font=(font1, 16), width=30)
browse_file_Entry.pack(pady=3)
browse_file_btn = ttk.Button(window, text="Browse",style="success.Outline.TButton", command=browse_file)
browse_file_btn.pack(pady=3)


# browse file gptk
browse_file_gptk_label = ttk.Label(window, text="Choose key Mapping File", font=font1)
browse_file_gptk_label.pack(pady=8)
browse_file_gptk_Entry = ttk.Entry(window, font=(font1, 16), width=30)
browse_file_gptk_Entry.pack(pady=3)
browse_file_gptk_btn = ttk.Button(window, text="Browse",style="success.Outline.TButton", command=browse_file_gptk)
browse_file_gptk_btn.pack(pady=3)

# author
author_label = ttk.Label(window, text="Author", font=font1)
author_label.pack(pady=8)
author_Entry = ttk.Entry(window, font=(font1, 16), width=30)
author_Entry.pack(pady=3)

#bulid button
bulid_button = ttk.Button(window, text="Bulid", bootstyle=SUCCESS, style="primairy.Outline.TButton", width=8, command=build)
bulid_button.pack(pady=50)

#version text
version_label = ttk.Label(window, text="v0.2-dev", font=font1)
version_label.pack(pady=2)

if __name__ == "__main__":
    window.mainloop()