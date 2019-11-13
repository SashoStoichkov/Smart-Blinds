import Tkinter as tk

from sensors.temp_sensor import TempSensor
from sensors.light_sensor import LightSensor

def AutoWindow():
    print("Entering Automatic mode!")

    auto_window = tk.Tk()
    auto_window.title("Smart Blinds")

    auto_window.attributes("-fullscreen", True)
    auto_window.configure(background="green")

    back_to_main_button = tk.Button(auto_window, height=5, width=20, text="Back to Main", font=("Comic Sans MS", 20, "bold"), command=auto_window.destroy, bg="red")
    back_to_main_button.pack(side="bottom", expand="yes")

    light_sensor_frame = tk.Frame(auto_window)
    light_sensor_frame.pack(side="bottom", expand="yes")

    light_intensity_sensor = LightSensor(light_sensor_frame)
    light_intensity_sensor.pack()
    light_intensity_sensor.config(font=("Arial", 15), bg="green")

    temp_sensor_frame = tk.Frame(auto_window)
    temp_sensor_frame.pack(side="bottom", expand="yes")

    temperature_sensor = TempSensor(temp_sensor_frame)
    temperature_sensor.pack()
    temperature_sensor.config(font=("Arial", 15), bg="green")