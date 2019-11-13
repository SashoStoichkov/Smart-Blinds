import Tkinter as tk

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