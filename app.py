from ttkbootstrap.constants import *
import ttkbootstrap as ttk
import pyglet
from tkinter import filedialog








def bulid():
    pass







def browse_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("GODOT files", "*.pck, *.exe")])
    # Do something with the file_path, e.g., display it in an Entry widget
    browse_file_Entry.delete(0, "end")
    browse_file_Entry.insert(0, file_path)







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



gameTitle_label = ttk.Label(window, text="Game Title", font=font1)
gameTitle_label.place(x=11, y=32)
gametitle_Entry = ttk.Entry(window, font=(font1, 16))
gametitle_Entry.place(x=11,y=60)




browse_file_label = ttk.Label(window, text="Choose Game File", font=font1)
browse_file_label.place(x=11, y=119)
browse_file_Entry = ttk.Entry(window, font=(font1, 16), width=30)
browse_file_Entry.place(x=11,y=147)
browse_file_btn = ttk.Button(window, text="Browse",style="success.Outline.TButton", command=browse_file)
browse_file_btn.place(x=11,y=190)



# runtime_label = ttk.Label(window, text="Runtime", font=font1)
# runtime_label.place(x=11, y=119)
# runtime_combobox = ttk.Combobox(window,values=runtimes, font=(font1, 14))
# runtime_combobox.place(x=11,y=147)



bulid_button = ttk.Button(window, text="Bulid", bootstyle=SUCCESS, style="success.Outline.TButton", width=8)
bulid_button.place(x=480,y=351)

if __name__ == "__main__":
    window.mainloop()