import ui

from temp_sensor import read_all
from time import sleep

if __name__ == "__main__":
    ui.MainWindow()

    while True:
        print(temperature)
        sleep(1)
