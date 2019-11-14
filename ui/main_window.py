import Tkinter as tk

from auto_window import AutoWindow
from manual_window import ManualWindow
from settings_window import SettingsWindow


def MainWindow():
    main_window = tk.Tk()
    main_window.title("Smart Blinds")

    main_window.attributes("-fullscreen", True)

    main_window_label = tk.Label(main_window, text="Welcome to Smart Blinds")
    main_window_label.config(font=("Comic Sans MS", 30))
    main_window_label.pack()

    auto_window_button = tk.Button(main_window)

    auto_window_button.config(height=10, width=10)
    auto_window_button.config(text="Auto")
    auto_window_button.config(font=("Comic Sans MS", 20, "bold"), bg="green")
    auto_window_button.config(activebackground="green")
    auto_window_button.config(command=AutoWindow)

    auto_window_button.pack(side="left", expand="yes")

    manual_window_button = tk.Button(main_window)

    manual_window_button.config(height=10, width=10)
    manual_window_button.config(text="Manual")
    manual_window_button.config(font=("Comic Sans MS", 20, "bold"), bg="red")
    manual_window_button.config(activebackground="red")
    manual_window_button.config(command=ManualWindow)

    manual_window_button.pack(side="right", expand="yes")

    exit_window_button = tk.Button(main_window)

    exit_window_button.config(height=10, width=20)
    exit_window_button.config(text="Exit!")
    exit_window_button.config(font=("Comic Sans MS", 15, "bold"), bg="red")
    exit_window_button.config(activebackground="red")
    exit_window_button.config(command=quit)

    exit_window_button.pack(side="bottom", expand="yes")

    manual_window_button = tk.Button(main_window)

    manual_window_button.config(height=10, width=20)
    manual_window_button.config(text="Settings")
    manual_window_button.config(font=("Comic Sans MS", 15, "bold"), bg="blue")
    manual_window_button.config(activebackground="blue")
    manual_window_button.config(command=SettingsWindow)

    manual_window_button.pack(side="bottom", expand="yes")

    main_window.bind("<Escape>", quit)

    main_window.mainloop()
