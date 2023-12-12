from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
en_vi_words = {}

# Read data
try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv("data/english_words.csv")
    en_vi_words = original_data.to_dict(orient="records")
else:
    en_vi_words = data_frame.to_dict(orient="records")

# Window UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Flip card
def flip_card():
    canvas.itemconfig(card_title, text="Vietnamese", fill="white")
    canvas.itemconfig(card_word, text=current_card['Vietnamese'], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# Button click
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(en_vi_words)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card['English'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def is_know():
    en_vi_words.remove(current_card)
    data = pandas.DataFrame(en_vi_words)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


flip_timer = window.after(3000, func=flip_card)

# Init image
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
# Button
know_button = Button(image=right_img, highlightthickness=0, command=is_know)
know_button.grid(row=1, column=1)

unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()
