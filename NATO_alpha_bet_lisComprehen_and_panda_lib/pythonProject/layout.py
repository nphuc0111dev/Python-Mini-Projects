from tkinter import *

window = Tk()
window.title("challenge")
window.minsize(500, 500)

# Labels
label = Label(text="Label")
label.grid(column=0, row=0)

# Button
button = Button(text="Button")
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# Entry
entry = Entry(width=50)
entry.insert(END, string="New entry")
entry.grid(column=3, row=2)

window.mainloop()
