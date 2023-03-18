from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Reading the data from the csv
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Function of generating random word to pass into buttons

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    # print(len(df))
    current_card = random.choice(to_learn)
    # print(new_card)
    # print(type(new_card))
    # print(new_word)
    canvas.itemconfigure(title, text="French", fill="black")
    canvas.itemconfigure(word, text=current_card['French'], fill="black")
    canvas.itemconfig(main_image, image=front_image)
    flip_timer = window.after(3000, card_flip)


def is_known():
    to_learn.remove(current_card)
    # print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# function flipping the card

def card_flip():
    canvas.itemconfig(main_image, image=back_image)
    canvas.itemconfigure(title, text="English", fill="white")
    canvas.itemconfigure(word, text=current_card['English'], fill="white")


# Creating the UI

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, card_flip)

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
main_image = canvas.create_image(400, 263, image=front_image)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=1, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

back_image = PhotoImage(file="images/card_back.png")

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=1, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=2, row=1)

next_card()

window.mainloop()
