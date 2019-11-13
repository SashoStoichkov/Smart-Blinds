import Tkinter as tk

def SettingsWindow():
    print("Entering Settings mode!")

    settings_window = tk.Tk()
    settings_window.title("Smart Blinds")

    settings_window.attributes("-fullscreen", True)

    back_to_main_button = tk.Button(settings_window, height=5, width=20, text="Back to Main", font=("Comic Sans MS", 20, "bold"), command=settings_window.destroy, bg="red")
    back_to_main_button.pack(side="bottom", expand="yes")
