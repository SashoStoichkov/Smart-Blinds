import bme280
import smbus2

import Tkinter as tk


class TempSensor(tk.Label):
    def __init__(self, parent=None, port=1, address=0x76):
        self.port = port
        self.address = address
        self.bus = smbus2.SMBus(self.port)

        bme280.load_calibration_params(self.bus, self.address)

        tk.Label.__init__(self, parent)

        self.humidity, self.pressure, self.temp_celsius = self.read_all()
        self.temp_fahrenheit = (self.temp_celsius * 1.8) + 32

        celsius_symbol = u"\u2103"
        fahrenheit_symbol = u"\u2109"

        str_temp_c = str(round(self.temp_celsius, 1))
        str_temp_f = str(round(self.temp_fahrenheit, 1))

        text = "Current temperature: " + str_temp_c + " " + celsius_symbol
        text += " / " + str_temp_f + " " + fahrenheit_symbol

        self.config(text=text)

        self.after(1000, self.update_temperature)

    def read_all(self):
        data = bme280.sample(self.bus, self.address)
        return data.humidity, data.pressure, data.temperature

    def update_temperature(self):
        new_humidity, new_pressure, new_temperature = self.read_all()

        if new_temperature != self.temp_celsius:
            self.humidity = new_humidity
            self.pressure = new_pressure

            self.temp_celsius = new_temperature
            self.temp_fahrenheit = (self.temp_celsius * 1.8) + 32

            celsius_symbol = u"\u2103"
            fahrenheit_symbol = u"\u2109"

            str_temp_c = str(round(self.temp_celsius, 1))
            str_temp_f = str(round(self.temp_fahrenheit, 1))

            text = "Current temperature: " + str_temp_c + " " + celsius_symbol
            text += " / " + str_temp_f + " " + fahrenheit_symbol

            self.config(text=text)

        self.after(1000, self.update_temperature)
