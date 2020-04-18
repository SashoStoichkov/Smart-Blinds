import Tkinter as tk


def SettingsWindow():
    print("Entering Settings mode!")

    settings_window = tk.Tk()
    settings_window.title("Smart Blinds")

    settings_window.attributes("-fullscreen", True)
    settings_window.configure(cursor="none")

    back_to_main_button = tk.Button(settings_window)

    back_to_main_button.config(height=5, width=20)
    back_to_main_button.config(text="Back to main!")
    back_to_main_button.config(font=("Comic Sans MS", 20, "bold"), bg="red")
    back_to_main_button.config(activebackground="red")
    back_to_main_button.config(command=settings_window.destroy)

    back_to_main_button.pack(side="bottom", expand="yes")
