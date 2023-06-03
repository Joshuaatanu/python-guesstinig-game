from tkinter import *
import random

ws = Tk()
ws.title("Guessing Game")  # title for the window
ws.geometry('600x400')  # size of the window
ws.config(bg='#e9ecef')  # background color of the window

ranNum = random.randint(0, 1000)  # generate a random number from 0 to 1000
chance = 10  # number of tries
var = IntVar()
disp = StringVar()


def check_guess():
    global ranNum
    global chance
   
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == ranNum:
            msg = f'You won! {ranNum} is correct'
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'{usr_ip} is greater. You have {chance} attempts left'
        elif usr_ip < ranNum:
            chance -= 1
            msg = f'{usr_ip} is smaller. You have {chance} attempts left'
    else:
        msg = f'You Lost! The number was {ranNum}'

    disp.set(msg)


Label(
    ws,
    text='Number Guessing Game',
    font=('san-serif', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg="#868e96"
).pack(pady=(10, 0))

Entry(
    ws,
    textvariable=var,
    font=('san-serif', 18)
).pack(pady=(10, 0))

Button(
    ws,
    text='Submit Guess',
    font=('san-serif', 18),
    command=check_guess
).pack()

Label(
    ws,
    textvariable=disp,
    bg="#e9ecef",
    font=('san-serif', 14),
).pack(pady=(20, 0))

ws.mainloop()
