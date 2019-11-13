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

    auto_window_button = tk.Button(main_window, height=10, width=10, text="Auto", font=("Comic Sans MS", 20, "bold"), command=AutoWindow, bg="green")
    auto_window_button.pack(side="left", expand="yes")

    manual_window_button = tk.Button(main_window, height=10, width=10, text="Manual", font=("Comic Sans MS", 20, "bold"), command=ManualWindow, bg="red")
    manual_window_button.pack(side="right", expand="yes")

    exit_window_button = tk.Button(main_window, height=10, width=20, text="Exit!", font=("Comic Sans MS", 15, "bold"), command=quit, bg="red")
    exit_window_button.pack(side="bottom", expand="yes")

    manual_window_button = tk.Button(main_window, height=10, width=20, text="Settings", font=("Comic Sans MS", 15, "bold"), command=SettingsWindow, bg="blue")
    manual_window_button.pack(side="bottom", expand="yes")

    main_window.bind("<Escape>", quit)

    main_window.mainloop()