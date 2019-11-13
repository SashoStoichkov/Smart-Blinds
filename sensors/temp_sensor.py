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

        self.humidity, self.pressure, self.temperature_celsius = self.read_all()
        self.temperature_fahrenheit = (self.temperature_celsius * 1.8) + 32

        self.celsius_degree_symbol = u"\u2103"
        self.fahrenheit_degree_symbol = u"\u2109"

        self.config(text="Current temperature: " + str(round(self.temperature_celsius, 1)) + " " + self.celsius_degree_symbol + " / " + str(round(self.temperature_fahrenheit, 1)) + " " + self.fahrenheit_degree_symbol)

        self.after(1000, self.update_temperature)

    def read_all(self):
        bme280_data = bme280.sample(self.bus, self.address)
        return bme280_data.humidity, bme280_data.pressure, bme280_data.temperature

    def update_temperature(self):
        new_humidity, new_pressure, new_temperature = self.read_all()

        if new_temperature != self.temperature_celsius:
            self.humidity = new_humidity
            self.pressure = new_pressure

            self.temperature_celsius = new_temperature
            self.temperature_fahrenheit = (self.temperature_celsius * 1.8) + 32

            self.config(text="Current temperature: " + str(round(self.temperature_celsius, 1)) + " " + self.celsius_degree_symbol + " / " + str(round(self.temperature_fahrenheit, 1)) + " " + self.fahrenheit_degree_symbol)

        self.after(1000, self.update_temperature)