from tkinter import *
import random

ws = Tk()
ws.title("Guessing Game")  # title for the window
ws.geometry('600x400')  # size of the window
ws.config(bg='#e9ecef')  # background color of the window

ranNum = random.randint(0, 1000)  # generate a random number from 0 to 1000
chance = 10  # number of tries
var = StringVar()
disp = StringVar()
print(ranNum)



# Function to check the user's guess


def check_guess():
    global ranNum
    global chance

    usr_ip = var.get()

    if usr_ip.isdigit():  # Check if the input is a number
        usr_ip = int(usr_ip)

        if usr_ip < 0:
            msg = 'Number should be greater than or equal to 0.'
        elif usr_ip > 1000:
            msg = 'Number should be less than or equal to 1000.'
        elif chance > 0:
            if usr_ip == ranNum:
                msg = f'You won! {ranNum} is correct'
                # Disable end game button
                end_game_button.config(state=DISABLED)
                restart_button.pack()  # Display the restart button
                # Disable the submit button
                submit_button.config(state=DISABLED)
            elif usr_ip > ranNum:
                chance -= 1
                msg = f'{usr_ip} is greater. You have {chance} attempts left'
            elif usr_ip < ranNum:
                chance -= 1
                msg = f'{usr_ip} is smaller. You have {chance} attempts left'
        else:
            msg = f'You Lost! The number was {ranNum}'
            end_game_button.config(state=DISABLED)  # Disable end game button
            restart_button.pack()  # Display the restart button
            submit_button.config(state=DISABLED)  # Disable the submit button
    else:
        msg = 'Invalid input. Please enter a number.'

    disp.set(msg)
    tries_label.config(text=f'Tries Left: {chance}')  # Update the tries label

# Function to restart the game


def restart_game():
    global ranNum
    global chance
    ranNum = random.randint(0, 1000)  # Generate a new random number
    chance = 10  # Reset the number of tries
    disp.set('')  # Clear the message display
    var.set('')  # Clear the input field
    restart_button.pack_forget()  # Hide the restart button
    submit_button.config(state=NORMAL)  # Enable the submit button
    end_game_button.config(state=NORMAL)  # Enable the end game button
    tries_label.config(text=f'Tries Left: {chance}')  # Reset the tries label

# Function to end the game


def end_game():
    ws.destroy()  # Close the game window


Label(
    ws,
    text='Number Guessing Game',
    font=('san-serif', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg="#868e96"
).pack(pady=(10, 0))

tries_label = Label(
    ws,
    text=f'Tries Left: {chance}',
    font=('san-serif', 14),
    bg='#e9ecef',
    anchor=E
)
tries_label.pack(padx=10, pady=(10, 0), anchor=E)

Entry(
    ws,
    textvariable=var,
    font=('san-serif', 18)
).pack(pady=(10, 0))

submit_button = Button(
    ws,
    text='Submit Guess',
    font=('san-serif', 18),
    command=check_guess
)
submit_button.pack()

restart_button = Button(
    ws,
    text='Restart Game',
    font=('san-serif', 18),
    command=restart_game,
    state=NORMAL  # Initially disabled until the game ends
)

end_game_button = Button(
    ws,
    text='End Game',
    font=('san-serif', 18),
    command=end_game
)

Label(
    ws,
    textvariable=disp,
    bg="#e9ecef",
    font=('san-serif', 14),
).pack(pady=(20, 0))

end_game_button.pack(side=LEFT, padx=(0, 10))

ws.mainloop()
