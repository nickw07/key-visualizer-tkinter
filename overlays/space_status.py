
from tkinter import Canvas, Tk
import keyboard


WIDTH, HEIGHT = 170, 50


def space_status_overlay(root: Tk):
    global WIDTH, HEIGHT

    # overlay state management
    overlay_active = True
    after_id = None

    # create adjusted window
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.attributes("-transparentcolor", "black")

    # window size setup
    root.geometry(f"{WIDTH}x{HEIGHT}+{root.winfo_screenwidth()-WIDTH-20}+20")  # place in top right

    canvas = Canvas(root,
                    width=WIDTH,
                    height=HEIGHT,
                    bg="black",
                    highlightthickness=0)
    canvas.pack()

    # key design
    key_rect = canvas.create_rectangle(0, 50,  # rect top left position
                                       170, 0,  # rect bottom right position
                                       fill="#444444",
                                       outline="white",
                                       width=2)
    # bar design
    bar_line = canvas.create_line(40, 15,  # line start position
                                  130, 15,  # line end position
                                  fill="white",
                                  width=2)

    def update():
        nonlocal after_id

        if not overlay_active:
            return

        if keyboard.is_pressed("space"):
            canvas.itemconfig(key_rect, fill="#00ff88")  # fill green when hotkey is pressed
        else:
            canvas.itemconfig(key_rect, fill="#444444")  # fill grey when hotkey is not pressed

        after_id = root.after(16, update)

    def stop_overlay():
        nonlocal overlay_active, after_id
        overlay_active = False

        if after_id is not None:
            root.after_cancel(after_id)

        canvas.destroy()

    update()
    return stop_overlay
