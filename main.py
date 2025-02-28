import csv
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
word_dict = None


try:
    data = pandas.read_csv("Words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_list = data.to_dict(orient="records")

def after_countdown(engrish):
    global back_image

    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=engrish, fill="white")

def correct_answer():

    global data_list, word_dict

    if word_dict is not None:

        data_list.remove(word_dict)
        dl = pandas.DataFrame(data_list)
        dl.to_csv("Words_to_learn.csv", index=False)

        new_word()

def new_word():

    global data_list, word_dict, timer

    if timer is not None:
        window.after_cancel(timer)

    word_dict= random.choice(data_list)
    word_list = list(word_dict.values())
    french_word = word_list[0]
    english_word = word_list[1]

    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")

    timer = window.after(3000,after_countdown, english_word)

window = Tk()
window.title("Flashy")
window.config(height=850, width=850, bg=BACKGROUND_COLOR, pady=50, padx=50)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height = 526, bg = BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image = front_image)
title_text = canvas.create_text(400,150,text = "French", font = ("Ariel", 40, "italic"))
word_text = canvas.create_text(400,263,text = "Press a button", font = ("Ariel", 60, "bold"))
canvas.grid(column=0,row=0, columnspan = 2)

right_img = PhotoImage(file="images/right.png")
correct = Button(image=right_img,borderwidth=0, highlightthickness=0, command= correct_answer)
correct.grid(column = 0, row = 1)

wrong_img = PhotoImage(file = "images/wrong.png")
wrong = Button(image=wrong_img, borderwidth=0, highlightthickness=0, command=new_word)
wrong.grid(column = 1, row = 1)

new_word()

window.mainloop()