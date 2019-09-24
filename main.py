from tkinter import *
# from tkinter.ttk import *

window = Tk()
window.title("Smart Blinds")
window.geometry('800x480')
# window.attributes("-fullscreen", True)

height = 0

height_l = Label(window, text="Height: " + str(height))
height_l.grid(column=0, row=0)

def clicked(num):
    global height
    if (height + num <= 10 and height + num >= -10):
        height += num
        height_l.config(text="Height: " + str(height))
    else:
        pass

blinds_up = Button(window, text="+", command=lambda:clicked(1))
blinds_up.grid(column=1, row=0)

blinds_down = Button(window, text="-", command=lambda:clicked(-1))
blinds_down.grid(column=1, row=1)

window.bind("<Escape>", quit)

window.mainloop()