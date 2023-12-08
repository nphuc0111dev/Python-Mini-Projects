from tkinter import *


def miles_to_km():
    miles = float(entry1.get())
    km = round(miles * 1.609, 2)
    res_label.config(text=f"{km}")


window = Tk()
window.title("Mile to km Converter")
window.config(padx=20, pady=20)

# Labels
label1 = Label(text="Miles")
label2 = Label(text="is equal to")
label3 = Label(text="Km")
res_label = Label(text="0")

label1.grid(row=0, column=2)
label2.grid(row=1, column=0)
label3.grid(row=1, column=2)
res_label.grid(row=1, column=1)

# Entry
entry1 = Entry(width=7)
entry1.grid(row=0, column=1)

# Button
cal_button = Button(text="Calculate", command=miles_to_km)
cal_button.grid(row=2, column=1)

window.mainloop()
