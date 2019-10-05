import tkinter as tk

def MainWindow():
    main_window = tk.Tk()
    main_window.title("Smart Blinds")
    # main_window.geometry('800x480')
    main_window.attributes("-fullscreen", True)

    main_window_label = tk.Label(main_window, text="Welcome to Smart Blinds")
    main_window_label.config(font=("Comic Sans MS", 30))
    main_window_label.pack()

    auto_window_button = tk.Button(main_window, height=10, width=20, text="Auto", font=("Comic Sans MS", 20, "bold"), command=AutoWindow, bg="green")
    auto_window_button.pack(side="left", expand="yes")

    manual_window_button = tk.Button(main_window, height=10, width=20, text="Manual", font=("Comic Sans MS", 20, "bold"), command=ManualWindow, bg="red")
    manual_window_button.pack(side="right", expand="yes")

    manual_window_button = tk.Button(main_window, height=10, width=40, text="Settings", font=("Comic Sans MS", 15, "bold"), command=SettingsWindow, bg="blue")
    manual_window_button.pack(side="bottom", expand="yes")

    main_window.bind("<Escape>", quit)

    main_window.mainloop()

def AutoWindow():
    print("Entering Automatic mode!")

    celsius_degree_symbol = " \u2103"
    fahrenheit_degree_symbol = " \u2109"

    auto_window = tk.Tk()
    auto_window.title("Smart Blinds")
    # auto_window.geometry('800x480')
    auto_window.attributes("-fullscreen", True)
    auto_window.configure(background="green")

    back_to_main_button = tk.Button(auto_window, height=5, width=20, text="Back to Main", font=("Comic Sans MS", 20, "bold"), command=auto_window.destroy, bg="red")
    back_to_main_button.pack(side="bottom", expand="yes")

    light_intensity_label = tk.Label(auto_window, text="Current light intensity: " + "5" + " lx", bg="green")
    light_intensity_label.config(font=("Arial", 15))
    light_intensity_label.pack(side="bottom", expand="yes")

    temperature_label = tk.Label(auto_window, text="Current temperature: " + "5" + celsius_degree_symbol + " / " + "10" + fahrenheit_degree_symbol, bg="green")
    temperature_label.config(font=("Arial", 15))
    temperature_label.pack(side="bottom", expand="yes")

def ManualWindow():
    print("Entering Manual mode!")

    running = False

    def start_motor(event):
        global running
        running = True
        print("starting motor...")

    def stop_motor(event):
        global running
        print("stopping motor...")
        running = False

    manual_window = tk.Tk()
    manual_window.title("Smart Blinds")
    # manual_window.geometry('800x480')
    manual_window.attributes("-fullscreen", True)
    manual_window.configure(background="blue")

    left_frame = tk.Frame(manual_window)
    left_frame.configure(background="blue")
    left_frame.pack(side="left")

    man_l_buttons = {0: "^", 1: "+", 2: "v", 3: "-"}

    for i in range(4):
        frame = tk.Frame(left_frame, width=100, height=100)
        button = tk.Button(frame, height=5, width=10, text=man_l_buttons[i], font=("Arial", 20, "bold"), bg="green")

        button.bind('<ButtonPress-1>', start_motor)
        button.bind('<ButtonRelease-1>', stop_motor)

        frame.grid(row = i // 2, column = i % 2)
        button.grid(sticky="nesw")

    right_frame = tk.Frame(manual_window)
    right_frame.configure(background="blue")
    right_frame.pack(side="right")

    fully_open_button = tk.Button(right_frame, height=5, width=10, text="Fully open!", font=("Arial", 20, "bold"), bg="green")
    fully_open_button.grid(row=1, column=2)

    fully_close_button = tk.Button(right_frame, height=5, width=10, text="Fully close!", font=("Arial", 20, "bold"), bg="green")
    fully_close_button.grid(row=2, column=2)

    back_to_main_button = tk.Button(right_frame, height=10, width=10, text="Back to Main", font=("Arial", 20, "bold"), command=manual_window.destroy, bg="red")
    back_to_main_button.grid(row=1, column=3, rowspan=2)

def SettingsWindow():
    print("Entering Settings mode!")

    settings_window = tk.Tk()
    settings_window.title("Smart Blinds")
    # settings_window.geometry('800x480')
    settings_window.attributes("-fullscreen", True)

    back_to_main_button = tk.Button(settings_window, height=5, width=20, text="Back to Main", font=("Comic Sans MS", 20, "bold"), command=settings_window.destroy, bg="red")
    back_to_main_button.pack(side="bottom", expand="yes")

if __name__ == "__main__":
    MainWindow()