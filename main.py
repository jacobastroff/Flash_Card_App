BACKGROUND_COLOR = "#B1DDC6"
import pandas
import random
from tkinter import *
try:
    with open('data/words_to_learn.csv', mode='r') as data_file:
        data = pandas.read_csv(data_file)

except FileNotFoundError:
    with open('data/words_to_learn.csv', mode="w") as data_file:
        data = pandas.read_csv('data/hebrew-words.csv')
except pandas.errors.EmptyDataError:
    with open('data/words_to_learn.csv', mode="w") as data_file:
        data = pandas.read_csv('data/hebrew-words.csv')
to_learn = data.to_dict(orient="records")
print(len(to_learn))
current_card_info = None
def generate_new_word_english():
    global current_card_info
    canvas.itemconfig(card, image = card_back_img)
    canvas.itemconfig(language_text,  text="English", fill="white")
    canvas.itemconfig(word_text, fill="white")
    canvas.itemconfig(word_text, text=current_card_info["English"])
def generate_new_word_hebrew():
    global current_card_info, flip_timer
    screen.after_cancel(flip_timer)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(language_text, fill="black", text="Hebrew")
    canvas.itemconfig(word_text,fill="black")
    current_card_info = random.choice(to_learn)
    current_word_info_hebrew = current_card_info['Hebrew']
    canvas.itemconfig(word_text, text = current_word_info_hebrew)
    flip_timer = screen.after(3000, generate_new_word_english)
def memorized():
    generate_new_word_hebrew()
    global current_card_info, to_learn
    to_learn.remove(current_card_info)
    csv_content = pandas.DataFrame(to_learn)
    csv_content.to_csv('data/words_to_learn.csv')






screen = Tk()
screen.config(bg=BACKGROUND_COLOR, padx = 50, pady = 50)
screen.title('Flashcard App!')
flip_timer = screen.after(3000, generate_new_word_hebrew )
canvas = Canvas(width = 826, height = 550, bg=BACKGROUND_COLOR, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image((826/2,550/2), image=card_front_img)
canvas.grid(column = 1, row= 1, columnspan=2)
language_text = canvas.create_text(400,150, font=('Arial', 40, "italic"))
word_text = canvas.create_text(400,263, font=('Arial', 60, "bold"))
right_img = PhotoImage(file='images/right.png')
right_btn = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=memorized )
right_btn.grid(row= 2, column =1)
wrong_img = PhotoImage(file='images/wrong.png')
wrong_btn = Button(image = wrong_img,highlightthickness=0, highlightbackground=BACKGROUND_COLOR,command=generate_new_word_hebrew )
wrong_btn.grid(row= 2, column = 2)
# print(data)
generate_new_word_hebrew()



mainloop()