from tkinter import *
from tkinter.ttk import *

def MainWindow():
    main_window = Tk()
    main_window.title("Smart Blinds")
    # main_window.geometry('800x480')
    main_window.attributes("-fullscreen", True)

    main_window_label = Label(main_window, text="Welcome to Smart Blinds")
    main_window_label.pack()

    auto_window_button = Button(main_window, text="Auto", command=AutoWindow)
    auto_window_button.pack()

    manual_window_button = Button(main_window, text="Manual", command=ManualWindow)
    manual_window_button.pack()

    main_window.bind("<Escape>", quit)
    
    main_window.mainloop()

def AutoWindow():
    print("Entering Automatic mode!")

    auto_window = Tk()
    auto_window.title("Smart Blinds")
    # auto_window.geometry('800x480')
    auto_window.attributes("-fullscreen", True)

    back_to_main_button = Button(auto_window, text="Back to Main", command=auto_window.destroy)
    back_to_main_button.pack()

def ManualWindow():
    print("Entering Manual mode!")

    manual_window = Tk()
    manual_window.title("Smart Blinds")
    # manual_window.geometry('800x480')
    manual_window.attributes("-fullscreen", True)

    up_button = Button(manual_window, text="^")
    up_button.pack()

    down_button = Button(manual_window, text="V")
    down_button.pack()

    clockwise_rotation_button = Button(manual_window, text="+")
    clockwise_rotation_button.pack()

    anticlockwise_rotation_button = Button(manual_window, text="-")
    anticlockwise_rotation_button.pack()

    other_options_button = Button(manual_window, text="More options", command=MoreMaualWindow)
    other_options_button.pack()

    back_to_main_button = Button(manual_window, text="Back to Main", command=manual_window.destroy)
    back_to_main_button.pack()

def MoreMaualWindow():
    print("Entering More Manual mode!")

    more_manual_window = Tk()
    more_manual_window.title("Smart Blinds")
    # more_manual_window.geometry('800x480')
    more_manual_window.attributes("-fullscreen", True)

    back_to_manual_button = Button(more_manual_window, text="Back to Manual", command=more_manual_window.destroy)
    back_to_manual_button.pack()

if __name__ == "__main__":
    MainWindow()