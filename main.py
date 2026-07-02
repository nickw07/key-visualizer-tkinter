
import tkinter as tk
import keyboard

from ui.main_menu import main_menu

from overlays.space_status import space_status_overlay
from overlays.up_status import up_status_overlay

current_stop_overlay = None
root = tk.Tk()


def destroy_root_ui():
    for widget in root.winfo_children():
        widget.destroy()


def confirm(selection):
    global current_stop_overlay

    destroy_root_ui()

    if selection == "up":
        current_stop_overlay = up_status_overlay(root)
    elif selection == "space":
        current_stop_overlay = space_status_overlay(root)


def return_to_menu():
    global current_stop_overlay

    if current_stop_overlay:
        current_stop_overlay()  # calling the stored function
        current_stop_overlay = None

        # reset window
        root.overrideredirect(False)
        root.attributes("-topmost", False)
        root.attributes("-transparentcolor", "")

        root.geometry("")  # standard size

        main_menu(root, confirm)


def exit_program():
    global current_stop_overlay

    # cleanly close overlay
    if current_stop_overlay is not None:
        current_stop_overlay()
        current_stop_overlay = None

    keyboard.unhook_all()

    # close tkinter
    root.destroy()


if __name__ == '__main__':
    main_menu(root, confirm)

    keyboard.add_hotkey("ctrl+shift+o", return_to_menu)
    keyboard.add_hotkey("ctrl+shift+m", exit_program)

    root.mainloop()
