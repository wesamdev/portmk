from ttkbootstrap.constants import *
import ttkbootstrap as ttk
import pyglet


# Setup Window
window = ttk.Window(themename="darkly")
window.geometry("600x400")
window.resizable(False, False)
window.title("PORTMK  Made by wesamdev")


#Setup Fonts
pyglet.font.add_file("fonts/Poppins-Bold.ttf")
font1 = ttk.font.Font(family="Poppins", size=12, weight="bold")


gameTitle_label = ttk.Label(window, text="Game Title", font=font1)
gameTitle_label.place(x=11, y=32)


if __name__ == "__main__":
    window.mainloop()