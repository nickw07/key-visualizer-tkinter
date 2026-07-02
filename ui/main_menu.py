
import tkinter as tk
from tkinter import ttk


def main_menu(root: tk.Tk, confirm_callback):

    root.geometry("+50+50")  # root will be placed here always
    root.title("Button status display")
    root.resizable(False, False)

    button_option_var = tk.StringVar(value="up")

    def confirm():
        confirm_callback(button_option_var.get())

    heading_label = ttk.Label(root,
                              text="Button status display",
                              font=("Arial", 15))
    heading_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

    button_selection_label = ttk.Label(root,
                                       text="Select button:",
                                       font=("Arial", 13))
    button_selection_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

    rb1 = ttk.Radiobutton(root,
                          text="Up Arrow key",
                          variable=button_option_var,
                          value="up")
    rb1.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)

    rb2 = ttk.Radiobutton(root,
                          text="Space bar",
                          variable=button_option_var,
                          value="space")
    rb2.grid(row=1, column=2, sticky=tk.EW, padx=5, pady=5)

    hotkey_frame = ttk.LabelFrame(root,
                                  text="Options")
    hotkey_frame.grid(row=2, column=0, columnspan=3, sticky=tk.EW, padx=5, pady=5)

    description_label1 = ttk.Label(hotkey_frame,
                                   text="Return to menu:",
                                   font=("Arial", 11))
    description_label1.grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)

    info_text_label1 = ttk.Label(hotkey_frame,
                                 text="Ctrl+Shift+o",
                                 font=("Arial", 11))
    info_text_label1.grid(row=0, column=1, sticky=tk.W, padx=3)

    description_label2 = ttk.Label(hotkey_frame,
                                   text="Exit program:",
                                   font=("Arial", 11))
    description_label2.grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)

    info_text_label2 = ttk.Label(hotkey_frame,
                                 text="Ctrl+Shift+m",
                                 font=("Arial", 11))
    info_text_label2.grid(row=1, column=1, sticky=tk.W, padx=3)

    separator = ttk.Separator(root)
    separator.grid(row=3, column=0, columnspan=3, sticky=tk.EW, pady=3)

    confirm_button = ttk.Button(root,
                                text="Confirm",
                                command=confirm)
    confirm_button.grid(row=4, column=0, columnspan=3, sticky=tk.EW, padx=5, pady=5)
