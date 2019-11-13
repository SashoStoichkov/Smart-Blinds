from python_tsl2591 import tsl2591

import Tkinter as tk


class LightSensor(tk.Label):
    def __init__(self, parent=None):
        self.tsl = tsl2591()

        tk.Label.__init__(self, parent)

        self.lux = self.read_data()

        self.config(text="Current light intensity: " + str(round(self.lux, 2)) + " Lux")

        self.after(1000, self.update_light)

    def read_data(self):
        full, ir = self.tsl.get_full_luminosity()
        return self.tsl.calculate_lux(full, ir)

    def update_light(self):
        new_lux = self.read_data()

        if new_lux != self.lux:
            self.lux = new_lux

            self.config(text="Current light intensity: " + str(round(self.lux, 2)) + " Lux")

        self.after(1000, self.update_light)
